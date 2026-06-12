#!/usr/bin/env python3

"""Module that includes functions to execute ADCP and SDAP commands"""

import logging
import json

import ucapi

import config
import driver
import media_player
import remote
import sensor
import selects
import adcp as ADCP
import enums

_LOG = logging.getLogger(__name__)



def projector_def(device_id:str = None):
    """Create the projector object. Use custom ports and password if they differ from the projectors default values
    
    :device_id: The id of the device in config.Devices. If empty the temp device id from config.Setup will be used e.g. during setup
    """

    if device_id is None:
        #Using temp device id for projector object definition during setup
        device_id = config.Setup.get(config.Setup.Keys.SETUP_TEMP_DEVICE_NAME)

    ip = config.Devices.get(device_id=device_id, key=config.DevicesKeys.IP)
    adcp_password = config.Devices.get(device_id=device_id, key=config.DevicesKeys.ADCP_PASSWORD)
    adcp_port = config.Devices.get(device_id=device_id, key=config.DevicesKeys.ADCP_PORT)
    adcp_timeout = config.Devices.get(device_id=device_id, key=config.DevicesKeys.ADCP_TIMEOUT)
    sdap_port = config.Devices.get(device_id=device_id, key=config.DevicesKeys.SDAP_PORT)

    attr = {config.DevicesKeys.IP: ip, config.DevicesKeys.ADCP_PORT: adcp_port, config.DevicesKeys.SDAP_PORT: sdap_port, \
            config.DevicesKeys.ADCP_PASSWORD: adcp_password, config.DevicesKeys.ADCP_TIMEOUT: adcp_timeout}

    # Only include attributes that are not None (non default values) when creating the projector object
    valid_attributes = {key: value for key, value in attr.items() if value is not None}

    return ADCP.Projector(**valid_attributes)



async def get_setting(device_id: str, setting: str, standby: bool = False):
    """Get the current adcp value of a specific setting from the projector and return it as a string without quotes that adcp normally includes.
    Some values get converted to match a valid entity state like power_status or get loaded from a json like light, temperature, warning and error messages
    """

    _LOG.debug(f"Get current value for setting \"{setting}\" for {device_id}")

    #enums.SelectTypes.POWER has no query option. Use enums.SensorTypes.POWER_STATUS instead
    if setting == enums.SelectTypes.POWER:
        setting = enums.SensorTypes.POWER_STATUS

    #enums.SelectTypes.PICTURE_POSITION_SAVE is an adcp exec command that doesn't support query or range. Use select instead
    if setting == enums.SelectTypes.PICTURE_POSITION_SAVE:
        setting = enums.SelectTypes.PICTURE_POSITION_SELECT

    adcp_setting_name = config.UC2ADCP.get(setting)

    try:
        setting_value = await projector_def(device_id).command(adcp_setting_name, ADCP.Parameters.QUERY)
    except (OSError, NameError):
        #3D status command is temporally unavailable or not supported means mode is 2D
        if setting == enums.SensorTypes.MODE_2D_3D:
            setting_value = "2d"
        #HDR Format command is temporally unavailable or not supported means range is SDR
        elif setting == enums.SensorVideoSignalTypes.DYNAMIC_RANGE:
            setting_value = "sdr"
        else:
            raise
    except Exception:
        raise

    #Needed as enums.SensorTypes.POWER_STATUS also reports interstates like standby that can't be used as a adcp select value
    # Return ucapi.media_player.States.STANDBY if standby=True which is used for media_player.update_attributes()
    if setting == enums.SensorTypes.POWER_STATUS \
        and setting_value in (ADCP.Responses.States.COOLING1, ADCP.Responses.States.COOLING2, ADCP.Responses.States.STANDBY):
        if standby:
            setting_value = ucapi.media_player.States.STANDBY
        else:
            setting_value = ADCP.Responses.States.OFF
    if setting == enums.SensorTypes.POWER_STATUS and setting_value in (ADCP.Responses.States.STARTUP):
        setting_value = ADCP.Responses.States.ON

    if setting in (enums.SensorSystemStatusTypes.WARNING, enums.SensorSystemStatusTypes.ERROR):
        try:
            msg_json = json.loads(setting_value)
            msgs = [str(item) for item in msg_json if item]
            if msgs:
                setting_value = ", ".join(msgs).replace("[", "").replace("]", "")
            else:
                _LOG.warning(f"No warning/error message data found in response: {setting_value}")
        except json.JSONDecodeError as e:
            _LOG.error(f"Failed to parse warning/error message response: {e}")
            _LOG.debug(f"Raw response: {setting_value}")

    if setting in (enums.SensorTypes.TEMPERATURE, enums.SensorTypes.LIGHT_TIMER):
        key = "intake_air" if setting == enums.SensorTypes.TEMPERATURE else "light_src"
        try:
            msg_json = json.loads(setting_value)
            item = next((item for item in msg_json if key in item), None)
            if item is not None:
                setting_value = str(item[key]) #Needed for string-based comparison in sensor.update_setting()
            else:
                _LOG.warning(f"No {key} data found in response: {setting_value}")
        except json.JSONDecodeError as e:
            _LOG.error(f"Failed to parse temperature response: {e}")
            _LOG.debug(f"Raw response: {setting_value}")

    setting_value = setting_value.replace('"', "")

    return setting_value



async def get_setting_options(device_id: str, setting: str):
    """Get the available options for a specific setting from the projector and return them as a list of strings. Used for select entities"""

    _LOG.debug(f"Get available options for setting \"{setting}\" for {device_id}")

    #Because enums.SelectTypes.POWER has no query option manually return possible options. enums.SelectTypes.POWER would return also return options that are query only
    if setting == enums.SelectTypes.POWER:
        options = [ADCP.Responses.States.ON.replace('"', ""), ADCP.Responses.States.OFF.replace('"', "")]
        return options

    # enums.SelectTypes.PICTURE_POSITION_SAVE is a exec command that doesn't support query or range. Use select instead
    if setting == enums.SelectTypes.PICTURE_POSITION_SAVE:
        setting = enums.SelectTypes.PICTURE_POSITION_SELECT


    adcp_setting_name = config.UC2ADCP.get(setting)

    try:
        options = await projector_def(device_id).command(adcp_setting_name, ADCP.Parameters.RANGE)
    except Exception:
        raise

    return options



async def send_cmd(device_id: str, cmd_name: str | dict, params = None):
    """Send a command to the projector and raise an exception if it fails"""

    projector_adcp = projector_def(device_id)

    # Select entity commands
    if isinstance(cmd_name, dict):
        try:
            command_adcp = {k: v for k, v in cmd_name.items() if k != "setting"} #Remove setting as it's not needed for ADCP, only for updating attributes
            await projector_adcp.command(command_adcp)
        except Exception:
            raise

    # Media player and remote commands
    else:

        #Parameter commands
        if cmd_name == ucapi.media_player.Commands.SELECT_SOURCE:
            source = params["source"]

            try:
                if source == enums.Sources.HDMI_1:
                    await projector_adcp.command(ADCP.Commands.Select.INPUT, ADCP.Values.Inputs.HDMI1)
                elif source == enums.Sources.HDMI_2:
                    await projector_adcp.command(ADCP.Commands.Select.INPUT, ADCP.Values.Inputs.HDMI2)
                else:
                    raise ValueError("Unknown source: " + source)
            except Exception:
                raise

        elif cmd_name in (ucapi.media_player.Commands.MUTE_TOGGLE, enums.SimpleCommands.PICTURE_MUTING_TOGGLE):
            try:
                mute_state = await get_setting(device_id, enums.SensorTypes.PICTURE_MUTING)
                if mute_state == ADCP.Values.States.OFF.replace('"', ""):
                    mute_state = False
                else:
                    mute_state = True
            except Exception:
                raise

            try:
                if mute_state is False:
                    await projector_adcp.command(ADCP.Commands.Select.MUTE, ADCP.Values.States.ON)
                elif mute_state is True:
                    await projector_adcp.command(ADCP.Commands.Select.MUTE, ADCP.Values.States.OFF)
            except Exception:
                raise

        elif cmd_name == enums.SimpleCommands.BLANKING_TOGGLE:
            try:
                blanking_state = await get_setting(device_id, enums.SensorTypes.BLANKING)
                if blanking_state == ADCP.Values.States.OFF.replace('"', ""):
                    blanking_state = False
                else:
                    blanking_state = True
            except Exception:
                raise

            try:
                if blanking_state is False:
                    await projector_adcp.command(ADCP.Commands.Select.BLANKING, ADCP.Values.States.ON)
                elif blanking_state is True:
                    await projector_adcp.command(ADCP.Commands.Select.BLANKING, ADCP.Values.States.OFF)
            except Exception:
                raise

        #Attribute update commands are handled here instead of update_attributes() as a failed command needs to be shown to the user
        #which doesn't happen if the command is executed in update_attributes()
        elif cmd_name in (enums.SimpleCommands.UPDATE_VIDEO_INFO, ucapi.media_player.Commands.PLAY_PAUSE):
            try:
                await sensor.update_video(device_id)
            except Exception:
                raise

        elif cmd_name == enums.SimpleCommands.UPDATE_HEALTH_STATUS:
            try:
                await sensor.update_setting(device_id, enums.SensorTypes.LIGHT_TIMER)
                await sensor.update_setting(device_id, enums.SensorTypes.TEMPERATURE)
                await sensor.update_system(device_id)
            except Exception:
                raise

        elif cmd_name == enums.SimpleCommands.UPDATE_ALL_SENSORS:
            try:
                await sensor.update_all_sensors(device_id)
            except Exception:
                raise

        elif cmd_name == enums.SimpleCommands.UPDATE_SELECT_OPTIONS:
            try:
                await selects.update_all_selects(device_id)
            except Exception:
                raise

        #Simple Commands
        else:
            try:
                adcp_cmd = config.UC2ADCP.get(cmd_name)
            except KeyError as k:
                if not any(cmd_name == item for item in ucapi.media_player.Commands):
                    _LOG.info(f"Could't find a matching entity or simple command. \"{cmd_name}\" could be a native ADCP command. Skipping conversion")
                    quote_linting = str.maketrans({
                        "‘": '"',  # left single quotation mark
                        "’": '"',  # right single quotation mark
                        "‚": '"',  # single low-9 quotation mark
                        "‛": '"',  # single high-reversed-9 quotation mark
                        "“": '"',  # left double quotation mark
                        "”": '"',  # right double quotation mark
                        "„": '"',  # double low-9 quotation mark
                        "‟": '"',  # double high-reversed-9 quotation mark
                        "‹": '"',  # single guillemet
                        "›": '"',
                        "«": '"',  # double guillemet
                        "»": '"',
                        "`": '"',
                        "´": '"'
                    })
                    cmd_name.translate(quote_linting)
                    try:
                        await projector_adcp.command(cmd_name)
                    except Exception:
                        raise
                else:
                    _LOG.error(f"Command \"{cmd_name}\" is not supported or implemented")
                    raise KeyError() from k
            except Exception as e:
                _LOG.error("Could not map UC command to ADCP command")
                raise Exception(e) from e
            else:
                _LOG.debug(f"Mapped UC command \"{cmd_name}\" to ADCP command \"{adcp_cmd}\"")
                try:
                    await projector_adcp.command(adcp_cmd)
                except Exception:
                    raise



async def update_attributes(device_id:str , cmd_name:str|dict, params:dict = None):
    """Update entity attributes if the command changes or could potentially change these attributes or values"""

    #If cmd_name is a dict it's coming from a select entity
    if isinstance(cmd_name, dict):
        setting = cmd_name["setting"]

        await selects.update_attributes(device_id=device_id, select_type=setting)
        await sensor.update_setting(device_id=device_id, setting=setting)

        match setting:
            case enums.SensorTypes.POWER_STATUS | enums.SelectTypes.POWER:
                await driver.asyncio.sleep(4)  # Wait 4 seconds for the projector to report the correct settings after power state change
                await media_player.update_attributes(device_id)
                await remote.update_attributes(device_id)
                await remote.update_attributes(device_id)
                await sensor.update_all_sensors(device_id)
                await selects.update_all_selects(device_id)
            case enums.SensorTypes.INPUT:
                await driver.asyncio.sleep(2)  # Wait 2 seconds for the projector to report the correct signal info after HDMI handshake
                await media_player.update_attributes(device_id)
                await sensor.update_all_sensors(device_id)
                await selects.update_all_selects(device_id)
            case enums.SensorTypes.PICTURE_MUTING:
                await media_player.update_attributes(device_id)
                await sensor.update_video(device_id)
            case enums.SensorTypes.HDR_STATUS | enums.SelectTypes.HDR_FORMAT | enums.SensorTypes.PICTURE_PRESET:
                await sensor.update_setting(device_id, enums.SensorTypes.GAMMA)
                await sensor.update_setting(device_id, enums.SensorTypes.COLOR_SPACE)
                await sensor.update_setting(device_id, enums.SensorTypes.CONTRAST_ENHANCER)
                await sensor.update_setting(device_id, enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING)
                await selects.update_attributes(device_id, enums.SensorTypes.GAMMA)
                await selects.update_attributes(device_id, enums.SensorTypes.COLOR_SPACE)
                await selects.update_attributes(device_id, enums.SensorTypes.CONTRAST_ENHANCER)
                await selects.update_attributes(device_id, enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING)
                await selects.update_attributes(device_id, enums.SensorTypes.LASER_BRIGHTNESS)
                await selects.update_attributes(device_id, enums.SensorTypes.IRIS_BRIGHTNESS)
            case enums.SelectTypes.PICTURE_POSITION_SAVE | enums.SelectTypes.PICTURE_POSITION_SELECT:
                await sensor.update_setting(device_id, enums.SensorTypes.PICTURE_POSITION)
                await selects.update_attributes(device_id, enums.SelectTypes.PICTURE_POSITION_SELECT)
                await selects.update_attributes(device_id, enums.SelectTypes.PICTURE_POSITION_SAVE)

        _LOG.info(f"Entity attributes updated for setting {setting}")

    #Command comes from a media player or remote entity
    else:

        simple_command = None

        match cmd_name:

            case ucapi.media_player.Commands.ON:

                await driver.asyncio.sleep(3)  # Wait 3 seconds for the projector to report the correct power state
                try:
                    await media_player.update_attributes(device_id)
                    await remote.update_attributes(device_id)
                    await sensor.update_all_sensors(device_id)
                    await selects.update_all_selects(device_id)
                except Exception:
                    raise

            case ucapi.media_player.Commands.OFF:

                await driver.asyncio.sleep(3)  # Wait 3 seconds for the projector to report the correct power state
                try:
                    await media_player.update_attributes(device_id)
                    await remote.update_attributes(device_id)
                    await sensor.update_all_sensors(device_id)
                    await selects.update_all_selects(device_id)
                except Exception:
                    raise

            case ucapi.media_player.Commands.TOGGLE:
                await driver.asyncio.sleep(3)  # Wait 3 seconds for the projector to report the correct power state and the user to confirm the shut down dialog

                try:
                    await media_player.update_attributes(device_id)
                    await remote.update_attributes(device_id)
                    await sensor.update_all_sensors(device_id)
                    await selects.update_all_selects(device_id)
                except Exception:
                    raise

            case \
                ucapi.media_player.Commands.MUTE | \
                ucapi.media_player.Commands.UNMUTE | \
                ucapi.media_player.Commands.MUTE_TOGGLE | \
                enums.SimpleCommands.PICTURE_MUTING_ON | \
                enums.SimpleCommands.PICTURE_MUTING_OFF | \
                enums.SimpleCommands.PICTURE_MUTING_TOGGLE:

                try:
                    await media_player.update_attributes(device_id)
                    await remote.update_attributes(device_id)
                    await sensor.update_setting(device_id, setting=enums.SensorTypes.PICTURE_MUTING)
                    await selects.update_attributes(device_id, select_type=enums.SelectTypes.PICTURE_MUTING)
                except Exception:
                    raise

            case \
                ucapi.media_player.Commands.SELECT_SOURCE | \
                enums.SimpleCommands.INPUT_HDMI1 | \
                enums.SimpleCommands.INPUT_HDMI2:

                await driver.asyncio.sleep(4)  # Wait 4 seconds for the projector to report the correct settings after power state change
                try:
                    await sensor.update_setting(device_id, setting=enums.SensorTypes.INPUT)
                    await selects.update_attributes(device_id, select_type=enums.SelectTypes.INPUT)
                except Exception:
                    raise

            case ucapi.remote.Commands.SEND_CMD | ucapi.remote.Commands.SEND_CMD_SEQUENCE:
                command = params.get("command")
                if command in (item.value for item in enums.SimpleCommands) or command in (item.value for item in ucapi.media_player.Commands):
                    simple_command = command
                else:
                    _LOG.debug(f"The command \"{command}\" is not a known command from this integration. It could be a native ADCP command. \
Updating all attributes of all entities to reflect potential changes from this command")
                    try:
                        await media_player.update_attributes(device_id)
                        await remote.update_attributes(device_id)
                        await sensor.update_all_sensors(device_id)
                        await selects.update_all_selects(device_id)
                    except Exception:
                        raise

            case _:
                #Simple command send by media player entity
                simple_command = cmd_name

        if simple_command:

            setting_name = ""

            match simple_command:

                case _ if simple_command.startswith("MODE_PIC"):
                    setting_name = enums.SensorTypes.PICTURE_PRESET
                case _ if simple_command.startswith("MODE_AR"):
                    setting_name = enums.SensorTypes.ASPECT
                case _ if simple_command.startswith("PIC_POSITION_SELECT"):
                    setting_name = enums.SensorTypes.PICTURE_POSITION
                case _ if simple_command.startswith("PIC_POSITION_SAVE"):
                    setting_name = enums.SelectTypes.PICTURE_POSITION_SAVE
                case _ if simple_command.startswith("MODE_HDR") and not simple_command.startswith("MODE_HDR_TONEMAP"):
                    setting_name = enums.SensorTypes.HDR_STATUS
                case _ if simple_command.startswith("MODE_HDR_TONEMAP"):
                    setting_name = enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING
                case _ if simple_command.startswith("MODE_LAMP"):
                    setting_name = enums.SensorTypes.LAMP_CONTROL
                case _ if simple_command.startswith("MODE_DYN_IRIS"):
                    setting_name = enums.SensorTypes.DYNAMIC_IRIS_CONTROL
                case _ if simple_command.startswith("MODE_DYN_LIGHT"):
                    setting_name = enums.SensorTypes.DYNAMIC_LIGHT_CONTROL
                case _ if simple_command.startswith("MODE_MOTION"):
                    setting_name = enums.SensorTypes.MOTIONFLOW
                case _ if simple_command.startswith("MODE_2D/3D"):
                    setting_name = enums.SensorTypes.MODE_2D_3D
                case _ if simple_command.startswith("MODE_3D"):
                    setting_name = enums.SensorTypes.FORMAT_3D
                case _ if simple_command.startswith("MODE_LAG"):
                    setting_name = enums.SensorTypes.INPUT_LAG_REDUCTION
                case _ if simple_command.startswith("MENU_POS"):
                    setting_name = enums.SensorTypes.MENU_POSITION
                case _ if simple_command.startswith("MODE_DYN_CONTR"):
                    setting_name = enums.SensorTypes.CONTRAST_ENHANCER
                case _ if simple_command.startswith("LASER_DIM"):
                    setting_name = enums.SensorTypes.LASER_BRIGHTNESS
                case _ if simple_command.startswith("IRIS_BRIGHTNESS"):
                    setting_name = enums.SensorTypes.IRIS_BRIGHTNESS
                case _ if simple_command.startswith("MUTING"):
                    setting_name = enums.SensorTypes.PICTURE_MUTING
                case _ if simple_command.startswith("BLANKING"):
                    setting_name = enums.SensorTypes.BLANKING
                case _:
                    _LOG.debug(f"Command \"{simple_command}\" has no associated entity attributes, sensors or select entities to update")
                    return

            if setting_name != "":
                try:
                    await sensor.update_setting(device_id, setting_name)
                    await selects.update_attributes(device_id, setting_name)
                    if setting_name in (enums.SensorTypes.HDR_STATUS, enums.SensorTypes.PICTURE_PRESET):
                        await sensor.update_setting(device_id, enums.SensorTypes.GAMMA)
                        await sensor.update_setting(device_id, enums.SensorTypes.COLOR_SPACE)
                        await sensor.update_setting(device_id, enums.SensorTypes.CONTRAST_ENHANCER)
                        await sensor.update_setting(device_id, enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING)
                        await sensor.update_setting(device_id, enums.SensorTypes.LASER_BRIGHTNESS)
                        await sensor.update_setting(device_id, enums.SensorTypes.IRIS_BRIGHTNESS)
                        await selects.update_attributes(device_id, enums.SensorTypes.GAMMA)
                        await selects.update_attributes(device_id, enums.SensorTypes.COLOR_SPACE)
                        await selects.update_attributes(device_id, enums.SensorTypes.CONTRAST_ENHANCER)
                        await selects.update_attributes(device_id, enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING)
                        await selects.update_attributes(device_id, enums.SensorTypes.LASER_BRIGHTNESS)
                        await selects.update_attributes(device_id, enums.SensorTypes.IRIS_BRIGHTNESS)
                except Exception:
                    raise

        _LOG.info(f"Entity attributes updated for command {cmd_name}")
