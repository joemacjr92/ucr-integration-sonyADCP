"""
This module contains the i18n (internationalization) related code for the Sony ADCP integration.
Some English strings are just defined to prettify them (e.g. add Title cases and remove underscores) and there is no need to actually translate them
"""

import logging
import adcp
import enums

_LOG = logging.getLogger(__name__)



class Strings:
    """Defines all translated strings"""

    class en_US:
        """Defines all English (en_US) translations. The key is based on an enum"""

        settings = {
            enums.Messages.REMOTE: "Remote",
            #Sensor+Selects
            enums.SensorTypes.INPUT: "Input",
            enums.SensorTypes.PICTURE_MUTING: "Video Muting",
            enums.SensorTypes.PICTURE_PRESET: "Picture Preset",
            enums.SensorTypes.ASPECT: "Aspect",
            enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING: "Dynamic HDR Tone Mapping",
            enums.SensorTypes.LAMP_CONTROL: "Lamp Control",
            enums.SensorTypes.DYNAMIC_IRIS_CONTROL: "Dynamic Iris Control",
            enums.SensorTypes.DYNAMIC_LIGHT_CONTROL: "Dynamic Light Control",
            enums.SensorTypes.MOTIONFLOW: "Motionflow",
            enums.SensorTypes.INPUT_LAG_REDUCTION: "Input Lag Reduction",
            enums.SensorTypes.MENU_POSITION: "Menu Position",
            enums.SensorTypes.COLOR_TEMPERATURE: "Color Temperature",
            enums.SensorTypes.COLOR_SPACE: "Color Space",
            enums.SensorTypes.GAMMA: "Gamma Correction",
            enums.SensorTypes.CONTRAST_ENHANCER: "Contrast Enhancer/Dynamic HDR Enhancer",
            enums.SensorTypes.MODE_2D_3D: "2D/3D Mode",
            #Sensor Only
            enums.SensorTypes.VIDEO_SIGNAL: "Video Signal",
            enums.SensorTypes.TEMPERATURE: "Temperature",
            enums.SensorTypes.LIGHT_TIMER: "Light Timer",
            enums.SensorTypes.SYSTEM_STATUS: "System Status",
            enums.SensorTypes.POWER_STATUS: "Power Status",
            enums.SensorTypes.PICTURE_POSITION: "Picture Position",
            enums.SensorTypes.HDR_STATUS: "HDR Status",
            enums.SensorTypes.FORMAT_3D: "3D Format",
            enums.SensorTypes.LASER_BRIGHTNESS: "Laser Brightness",
            enums.SensorTypes.IRIS_BRIGHTNESS: "Iris Brightness",
            #Select Only
            enums.SelectTypes.POWER: "Power State",
            enums.SelectTypes.PICTURE_POSITION_SELECT: "Picture Position Select",
            enums.SelectTypes.PICTURE_POSITION_SAVE: "Picture Position Save",
            enums.SelectTypes.HDR_FORMAT: "HDR Format",
        }

        messages = {
            #Integration Messages
            enums.Messages.TEMPORARILY_UNAVAILABLE: "Polling Temporarily Unavailable",
            enums.Messages.POLLING_ERROR: "Polling Error",
            enums.Messages.NO_SIGNAL: "No Signal",
            enums.Messages.VIDEO_MUTED: "Video Muted",
            enums.Messages.UNKNOWN: "Unknown",
            #Projector Warnings
            adcp.Responses.Warnings.LIGHT_SRC_LIFE: "Light-Source Error",
            adcp.Responses.Warnings.ALTITUDE: "High Altitude Warning",
            adcp.Responses.Warnings.TEMP: "Temperature Warning",
            adcp.Responses.Warnings.SIGNAL_FREQ: "Signal Frequency Warning",
            adcp.Responses.Warnings.SIGNAL_TYPE: "Signal Selection Warning",
            adcp.Responses.Warnings.NO: "No Warnings",
            #Projector Errors
            adcp.Responses.Errors.POWER: "Main Power Supply Error",
            adcp.Responses.Errors.POWER2: "DC Power Supply or NAND Error",
            adcp.Responses.Errors.SYSTEM3: "System Error 3 (MAIN_STARTUP)",
            adcp.Responses.Errors.SYSTEM4: "System Error 4 (WDT)",
            adcp.Responses.Errors.SYSTEM5: "System Error 5 (BE_STARTUP)",
            adcp.Responses.Errors.COVER: "Cover Error",
            adcp.Responses.Errors.LIGHT_SRC: "Light-source Error",
            adcp.Responses.Errors.LENS_COVER: "Top Cover Or Lens Shutter Error",
            adcp.Responses.Errors.SHOCK: "Drop Shock Error",
            adcp.Responses.Errors.NO_LENS: "Lens Not Attached Error",
            adcp.Responses.Errors.ANGLE: "Installation Angle Error",
            adcp.Responses.Errors.TEMP: "Temperature Error",
            adcp.Responses.Errors.FAN: "Fan Error",
            adcp.Responses.Errors.WHEEL: "Wheel Error",
            adcp.Responses.Errors.LUMINANCE: "Luminance Error",
            adcp.Responses.Errors.ASSY: "ASSY Error",
            adcp.Responses.Errors.BALLAST: "Ballast Updating Error",
            adcp.Responses.Errors.NO: "No Errors",
            }

        options = {
            # States
            adcp.Values.States.ON: "On",
            adcp.Values.States.OFF: "Off",
            adcp.Values.States.STANDBY: "Standby",
            adcp.Values.States.STARTUP: "Startup",
            adcp.Values.States.COOLING1: "Cooling 1",
            adcp.Values.States.COOLING2: "Cooling 2",
            # Inputs
            adcp.Values.Inputs.HDMI1: "HDMI 1",
            adcp.Values.Inputs.HDMI2: "HDMI 2",
            # Picture Modes
            adcp.Values.PictureModes.CINEMA_FILM1: "Cinema Film 1",
            adcp.Values.PictureModes.CINEMA_FILM2: "Cinema Film 2",
            adcp.Values.PictureModes.REFERENCE: "Reference",
            adcp.Values.PictureModes.TV: "TV",
            adcp.Values.PictureModes.PHOTO: "Photo",
            adcp.Values.PictureModes.BRIGHT_CINEMA: "Bright Cinema",
            adcp.Values.PictureModes.BRIGHT_TV: "Bright TV",
            adcp.Values.PictureModes.USER: "User",
            adcp.Values.PictureModes.USER1: "User 1",
            adcp.Values.PictureModes.USER2: "User 2",
            adcp.Values.PictureModes.USER3: "User 3",
            adcp.Values.PictureModes.GAME: "Game",
            # Picture Positions
            adcp.Values.PicturePositions.PP_1_85: "1.85:1",
            adcp.Values.PicturePositions.PP_2_35: "2.35:1",
            adcp.Values.PicturePositions.CUSTOM1: "Custom 1",
            adcp.Values.PicturePositions.CUSTOM2: "Custom 2",
            adcp.Values.PicturePositions.CUSTOM3: "Custom 3",
            adcp.Values.PicturePositions.CUSTOM4: "Custom 4",
            adcp.Values.PicturePositions.CUSTOM5: "Custom 5",
            # Aspect
            adcp.Values.Aspect.FULL1: "Full 1",
            adcp.Values.Aspect.FULL2: "Full 2",
            adcp.Values.Aspect.NORMAL: "Normal",
            adcp.Values.Aspect.STRETCH: "Stretch",
            adcp.Values.Aspect.V_STRETCH: "V-Stretch",
            adcp.Values.Aspect.SQUEEZE: "Squeeze",
            adcp.Values.Aspect.ZOOM_1_85: "Zoom 1.85:1",
            adcp.Values.Aspect.ZOOM_2_35: "Zoom 2.35:1",
            adcp.Values.Aspect.ASPECT_RATIO_SCALING: "Aspect Ratio Scaling",
            # Motionflow
            adcp.Values.Motionflow.SMOOTH_HIGH: "Smooth High",
            adcp.Values.Motionflow.SMOOTH_LOW: "Smooth Low",
            adcp.Values.Motionflow.IMPULSE: "Impulse",
            adcp.Values.Motionflow.COMBINATION: "Combination",
            adcp.Values.Motionflow.TRUE_CINEMA: "True Cinema",
            adcp.Values.Motionflow.OFF: "Off",
            # HDR
            adcp.Values.HDR.AUTO: "Auto",
            adcp.Values.HDR.OFF: "Off",
            adcp.Values.HDR.HLG: "HLG",
            adcp.Values.HDR.HDR10: "HDR10",
            adcp.Values.HDR.HDR_REF: "HDR Reference",
            # HDR Dynamic Tone Mapping
            adcp.Values.HDRDynToneMapping.MODE_1: "Mode 1",
            adcp.Values.HDRDynToneMapping.MODE_2: "Mode 2",
            adcp.Values.HDRDynToneMapping.MODE_3: "Mode 3",
            # Lamp Control
            adcp.Values.LampControl.LOW: "Low",
            adcp.Values.LampControl.HIGH: "High",
            # Light/Iris Control
            adcp.Values.LightControl.FULL: "Full",
            adcp.Values.LightControl.LIMITED: "Limited",
            adcp.Values.LightControl.OFF: "Aus",
            # 2D/3D Mode
            adcp.Values.Mode2D3D.MODE_AUTO: "Auto",
            adcp.Values.Mode2D3D.MODE_3D: "3D",
            adcp.Values.Mode2D3D.MODE_2D: "2D",
            # 3D Format
            adcp.Values.Mode3DFormat.SIMULATED: "Simulated 3D",
            adcp.Values.Mode3DFormat.SIDE_BY_SIDE: "Side by Side",
            adcp.Values.Mode3DFormat.OVER_UNDER: "Over Under",
            # Menu Position
            adcp.Values.MenuPosition.BOTTOM_LEFT: "Bottom Left",
            adcp.Values.MenuPosition.CENTER: "Center",
            # Contrast Enhancer
            adcp.Values.ContrastEnhancer.OFF: "Off",
            adcp.Values.ContrastEnhancer.LOW: "Low",
            adcp.Values.ContrastEnhancer.MID: "Mid",
            adcp.Values.ContrastEnhancer.HIGH: "High",
            # Color Space
            adcp.Values.ColorSpaces.BT709: "BT.709",
            adcp.Values.ColorSpaces.BT2020: "BT.2020",
            adcp.Values.ColorSpaces.ADOBE_RGB: "Adobe RGB",
            adcp.Values.ColorSpaces.COLOR_SPACE1: "Color Space 1",
            adcp.Values.ColorSpaces.COLOR_SPACE2: "Color Space 2",
            adcp.Values.ColorSpaces.COLOR_SPACE3: "Color Space 3",
            adcp.Values.ColorSpaces.CUSTOM: "Custom",
            adcp.Values.ColorSpaces.DCI: "DCI",
            # Color Temperature
            adcp.Values.ColorTemps.D93: "D93",
            adcp.Values.ColorTemps.D75: "D75",
            adcp.Values.ColorTemps.D65: "D65",
            adcp.Values.ColorTemps.D55: "D55",
            # Gamma
            adcp.Values.GammaValues.GAMMA_1_8: "1.8",
            adcp.Values.GammaValues.GAMMA_2_0: "2.0",
            adcp.Values.GammaValues.GAMMA_2_1: "2.1",
            adcp.Values.GammaValues.GAMMA_2_2: "2.2",
            adcp.Values.GammaValues.GAMMA_2_4: "2.4",
            adcp.Values.GammaValues.GAMMA_2_6: "2.6",
            adcp.Values.GammaValues.GAMMA_7: "Gamma 7",
            adcp.Values.GammaValues.GAMMA_8: "Gamma 8",
            adcp.Values.GammaValues.GAMMA_9: "Gamma 9",
            adcp.Values.GammaValues.GAMMA_10: "Gamma 10",
            adcp.Values.GammaValues.OFF: "Off",
            # Color Formats
            adcp.Responses.ColorFormats.RGB: "RGB",
            adcp.Responses.ColorFormats.YCBCR444: "YCbCr 4:4:4",
            adcp.Responses.ColorFormats.YCBCR422: "YCbCr 4:2:2",
            adcp.Responses.ColorFormats.YCBCR420: "YCbCr 4:2:0",
            # HDR Formats
            adcp.Responses.HDRFormats.HDR10: "HDR10",
            adcp.Responses.HDRFormats.HLG: "HLG",
            adcp.Responses.HDRFormats.HDR_REF: "HDR Reference",
        }

    class de_DE:
        """Defines all German (de_DE) translations. The key is based on an enum"""

        settings = {
            enums.Messages.REMOTE: "Fernbedienung",
            #Sensor+Selects
            enums.SensorTypes.INPUT: "Eingang",
            enums.SensorTypes.PICTURE_MUTING: "Video Ausschalten",
            enums.SensorTypes.PICTURE_PRESET: "Voreinstellung",
            enums.SensorTypes.ASPECT: "Seitenverhältnis",
            enums.SensorTypes.HDR_DYNAMIC_TONE_MAPPING: "HDR Tone-Mapping",
            enums.SensorTypes.LAMP_CONTROL: "Lampenregelung",
            enums.SensorTypes.DYNAMIC_IRIS_CONTROL: "Dynamikkontrolle Iris",
            enums.SensorTypes.DYNAMIC_LIGHT_CONTROL: "Dynamikkontrolle Laser",
            enums.SensorTypes.MOTIONFLOW: "Motionflow",
            enums.SensorTypes.INPUT_LAG_REDUCTION: "Reduzierte Eingangsverzögerung",
            enums.SensorTypes.MENU_POSITION: "Menüposition",
            enums.SensorTypes.COLOR_TEMPERATURE: "Farbtemperatur",
            enums.SensorTypes.COLOR_SPACE: "Farbraum",
            enums.SensorTypes.GAMMA: "Gammakorrektur",
            enums.SensorTypes.CONTRAST_ENHANCER: "Kontrastverstärker/Dynamischer HDR-Verstärker",
            enums.SensorTypes.MODE_2D_3D: "2D/3D Modus",
            #Sensor Only
            enums.SensorTypes.VIDEO_SIGNAL: "Videosignal",
            enums.SensorTypes.TEMPERATURE: "Temperatur",
            enums.SensorTypes.LIGHT_TIMER: "Lichttimer",
            enums.SensorTypes.SYSTEM_STATUS: "Systemstatus",
            enums.SensorTypes.POWER_STATUS: "Betriebsstatus",
            enums.SensorTypes.PICTURE_POSITION: "Bildposition",
            enums.SensorTypes.HDR_STATUS: "HDR-Status",
            enums.SensorTypes.FORMAT_3D: "3D-Format",
            enums.SensorTypes.LASER_BRIGHTNESS: "Laser-Helligkeit",
            enums.SensorTypes.IRIS_BRIGHTNESS: "Iris-Helligkeit",
            #Select Only
            enums.SelectTypes.POWER: "Betriebsstatus",
            enums.SelectTypes.PICTURE_POSITION_SELECT: "Bildposition Auswählen",
            enums.SelectTypes.PICTURE_POSITION_SAVE: "Bildposition Speichern",
            enums.SelectTypes.HDR_FORMAT: "HDR-Format",
        }

        messages = {
            #Integration Messages
            enums.Messages.TEMPORARILY_UNAVAILABLE: "Abfrage zurzeit nicht möglich",
            enums.Messages.POLLING_ERROR: "Abfragefehler",
            enums.Messages.NO_SIGNAL: "Kein Signal",
            enums.Messages.VIDEO_MUTED: "Video aus",
            enums.Messages.UNKNOWN: "Unbekannt",
            #Warnings
            adcp.Responses.Warnings.LIGHT_SRC_LIFE: "Lichtquellenfehler",
            adcp.Responses.Warnings.ALTITUDE: "Höhenwarnung",
            adcp.Responses.Warnings.TEMP: "Temperaturwarnung",
            adcp.Responses.Warnings.SIGNAL_FREQ: "Signalfrequenzwarnung",
            adcp.Responses.Warnings.SIGNAL_TYPE: "Signalauswahlwarnung",
            adcp.Responses.Warnings.NO: "Keine Warnungen",
            #Errors
            adcp.Responses.Errors.POWER: "Hauptstromversorgungsfehler",
            adcp.Responses.Errors.POWER2: "DC-Stromversorgungs- oder NAND-Fehler",
            adcp.Responses.Errors.SYSTEM3: "Systemfehler 3 (MAIN_STARTUP)",
            adcp.Responses.Errors.SYSTEM4: "Systemfehler 4 (WDT)",
            adcp.Responses.Errors.SYSTEM5: "Systemfehler 5 (BE_STARTUP)",
            adcp.Responses.Errors.COVER: "Abdeckungsfehler",
            adcp.Responses.Errors.LIGHT_SRC: "Lichtquellenfehler",
            adcp.Responses.Errors.LENS_COVER: "Top-Abdeckung oder Objektivblendenfehler",
            adcp.Responses.Errors.SHOCK: "Drop Shock Fehler",
            adcp.Responses.Errors.NO_LENS: "Objektiv nicht angebracht Fehler",
            adcp.Responses.Errors.ANGLE: "Installationswinkel Fehler",
            adcp.Responses.Errors.TEMP: "Temperaturfehler",
            adcp.Responses.Errors.FAN: "Lüfterfehler",
            adcp.Responses.Errors.WHEEL: "Radfehler",
            adcp.Responses.Errors.LUMINANCE: "Leuchtstärkenfehler",
            adcp.Responses.Errors.ASSY: "ASSY-Fehler",
            adcp.Responses.Errors.BALLAST: "Ballast Aktualisierungsfehler",
            adcp.Responses.Errors.NO: "Keine Fehler",
            }

        options = {
            # States
            adcp.Values.States.ON: "Ein",
            adcp.Values.States.OFF: "Aus",
            adcp.Values.States.STANDBY: "Standby",
            adcp.Values.States.STARTUP: "Start",
            adcp.Values.States.COOLING1: "Kühlung 1",
            adcp.Values.States.COOLING2: "Kühlung 2",
            # Inputs
            adcp.Values.Inputs.HDMI1: "HDMI 1",
            adcp.Values.Inputs.HDMI2: "HDMI 2",
            # Picture Modes
            adcp.Values.PictureModes.CINEMA_FILM1: "Kino Film 1",
            adcp.Values.PictureModes.CINEMA_FILM2: "Kino Film 2",
            adcp.Values.PictureModes.REFERENCE: "Referenz",
            adcp.Values.PictureModes.TV: "TV",
            adcp.Values.PictureModes.PHOTO: "Foto",
            adcp.Values.PictureModes.BRIGHT_CINEMA: "Kino hell",
            adcp.Values.PictureModes.BRIGHT_TV: "TV hell",
            adcp.Values.PictureModes.USER: "Benutzer",
            adcp.Values.PictureModes.USER1: "Benutzer 1",
            adcp.Values.PictureModes.USER2: "Benutzer 2",
            adcp.Values.PictureModes.USER3: "Benutzer 3",
            adcp.Values.PictureModes.GAME: "Spiel",
            # Picture Positions
            adcp.Values.PicturePositions.PP_1_85: "1.85:1",
            adcp.Values.PicturePositions.PP_2_35: "2.35:1",
            adcp.Values.PicturePositions.CUSTOM1: "Benutzerdefiniert 1",
            adcp.Values.PicturePositions.CUSTOM2: "Benutzerdefiniert 2",
            adcp.Values.PicturePositions.CUSTOM3: "Benutzerdefiniert 3",
            adcp.Values.PicturePositions.CUSTOM4: "Benutzerdefiniert 4",
            adcp.Values.PicturePositions.CUSTOM5: "Benutzerdefiniert 5",
            # Aspect
            adcp.Values.Aspect.FULL1: "Voll 1",
            adcp.Values.Aspect.FULL2: "Voll 2",
            adcp.Values.Aspect.NORMAL: "Normal",
            adcp.Values.Aspect.STRETCH: "Stecken",
            adcp.Values.Aspect.V_STRETCH: "V-Streckung",
            adcp.Values.Aspect.SQUEEZE: "Verkleinern",
            adcp.Values.Aspect.ZOOM_1_85: "Zoom 1.85:1",
            adcp.Values.Aspect.ZOOM_2_35: "Zoom 2.35:1",
            adcp.Values.Aspect.ASPECT_RATIO_SCALING: "Aspect Ratio Scaling",
            # Motionflow
            adcp.Values.Motionflow.SMOOTH_HIGH: "Stark Glätten",
            adcp.Values.Motionflow.SMOOTH_LOW: "Schwach Glätten",
            adcp.Values.Motionflow.IMPULSE: "Impuls",
            adcp.Values.Motionflow.COMBINATION: "Kombination",
            adcp.Values.Motionflow.TRUE_CINEMA: "True Cinema",
            adcp.Values.Motionflow.OFF: "Aus",
            # HDR
            adcp.Values.HDR.AUTO: "Auto",
            adcp.Values.HDR.OFF: "Aus",
            adcp.Values.HDR.HLG: "HLG",
            adcp.Values.HDR.HDR10: "HDR10",
            adcp.Values.HDR.HDR_REF: "HDR Referenz",
            # HDR Dynamic Tone Mapping
            adcp.Values.HDRDynToneMapping.MODE_1: "Modus 1",
            adcp.Values.HDRDynToneMapping.MODE_2: "Modus 2",
            adcp.Values.HDRDynToneMapping.MODE_3: "Modus 3",
            # Lamp Control
            adcp.Values.LampControl.LOW: "Niedrig",
            adcp.Values.LampControl.HIGH: "Hoch",
            # Light/Iris Control
            adcp.Values.LightControl.FULL: "Voll",
            adcp.Values.LightControl.LIMITED: "Begrenzt",
            adcp.Values.LightControl.OFF: "Aus",
            # 2D/3D Mode
            adcp.Values.Mode2D3D.MODE_AUTO: "Auto",
            adcp.Values.Mode2D3D.MODE_3D: "3D",
            adcp.Values.Mode2D3D.MODE_2D: "2D",
            # 3D Format
            adcp.Values.Mode3DFormat.SIMULATED: "Simuliertes 3D",
            adcp.Values.Mode3DFormat.SIDE_BY_SIDE: "Nebeneinander",
            adcp.Values.Mode3DFormat.OVER_UNDER: "Übereinander",
            # Menu Position
            adcp.Values.MenuPosition.BOTTOM_LEFT: "Links unten",
            adcp.Values.MenuPosition.CENTER: "Mitte",
            # Contrast Enhancer
            adcp.Values.ContrastEnhancer.OFF: "Off",
            adcp.Values.ContrastEnhancer.LOW: "Niedrig",
            adcp.Values.ContrastEnhancer.MID: "Mittel",
            adcp.Values.ContrastEnhancer.HIGH: "Hoch",
            # Color Space
            adcp.Values.ColorSpaces.BT709: "BT.709",
            adcp.Values.ColorSpaces.BT2020: "BT.2020",
            adcp.Values.ColorSpaces.ADOBE_RGB: "Adobe RGB",
            adcp.Values.ColorSpaces.COLOR_SPACE1: "Farbraum 1",
            adcp.Values.ColorSpaces.COLOR_SPACE2: "Farbraum 2",
            adcp.Values.ColorSpaces.COLOR_SPACE3: "Farbraum 3",
            adcp.Values.ColorSpaces.CUSTOM: "Benutzerdefiniert",
            adcp.Values.ColorSpaces.DCI: "DCI",
            # Color Temperature
            adcp.Values.ColorTemps.D93: "D93",
            adcp.Values.ColorTemps.D75: "D75",
            adcp.Values.ColorTemps.D65: "D65",
            adcp.Values.ColorTemps.D55: "D55",
            # Gamma
            adcp.Values.GammaValues.GAMMA_1_8: "1.8",
            adcp.Values.GammaValues.GAMMA_2_0: "2.0",
            adcp.Values.GammaValues.GAMMA_2_1: "2.1",
            adcp.Values.GammaValues.GAMMA_2_2: "2.2",
            adcp.Values.GammaValues.GAMMA_2_4: "2.4",
            adcp.Values.GammaValues.GAMMA_2_6: "2.6",
            adcp.Values.GammaValues.GAMMA_7: "Gamma 7",
            adcp.Values.GammaValues.GAMMA_8: "Gamma 8",
            adcp.Values.GammaValues.GAMMA_9: "Gamma 9",
            adcp.Values.GammaValues.GAMMA_10: "Gamma 10",
            adcp.Values.GammaValues.OFF: "Aus",
            # Color Formats
            adcp.Responses.ColorFormats.RGB: "RGB",
            adcp.Responses.ColorFormats.YCBCR444: "YCbCr 4:4:4",
            adcp.Responses.ColorFormats.YCBCR422: "YCbCr 4:2:2",
            adcp.Responses.ColorFormats.YCBCR420: "YCbCr 4:2:0",
            # HDR Formats
            adcp.Responses.HDRFormats.HDR10: "HDR10",
            adcp.Responses.HDRFormats.HLG: "HLG",
            adcp.Responses.HDRFormats.HDR_REF: "HDR-Referenz",
        }



class Handler:
    """Handles internationalization for the integration"""

    _fallback_language = enums.Languages.ENGLISH
    _language = _fallback_language

    @classmethod
    def set_language(cls, language: enums.Languages):
        """Sets the language for the integration"""
        cls._language = language

    @classmethod
    def _get_lookups(cls, language: enums.Languages) -> list[dict]:
        strings = getattr(Strings, language, Strings.en_US)
        return [strings.settings, strings.messages, strings.options]

    @classmethod
    def localize(cls, key: str | list[str], force_language: enums.Languages = None, reverse: bool = False) -> str:
        """Localizes a given key. Uses the currently set language unless force_language is explicitly provided.
        Falls back to the English value if no translation is found for the given language,
        and to the normalized key itself if no English value is found either.

        :param key: The key(s) to look up (enum member, plain string or list of keys).
        :param force_language: (Optional) Language to use instead of the currently set language.
        :param reverse: (Optional) If True, attempt to find a reverse mapping to get the enum from the localized string.
        :return: The localized string, English fallback, or normalized key as last resort.
        """
        if isinstance(key, list):
            return [cls.localize(k, force_language, reverse) for k in key]

        normalized_key = key.value.replace("\"", "") if hasattr(key, "value") else key.replace("\"", "")
        quoted_key = f'"{normalized_key}"'
        language = force_language if force_language is not None else cls._language

        lookups = cls._get_lookups(language)
        fallback_lookups = cls._get_lookups(cls._fallback_language)

        if reverse:
            for lookup in lookups:
                for k, v in lookup.items():
                    if v == normalized_key:
                        return k

        for lookup in lookups:
            if normalized_key in lookup:
                return lookup[normalized_key]
            if quoted_key in lookup:
                return lookup[quoted_key]

        # Fallback 1: Fallback_language
        if language != cls._fallback_language:
            for lookup in fallback_lookups:
                if normalized_key in lookup:
                    _LOG.debug(f'No translation for "{normalized_key}" in "{language}". Falling back to "{cls._fallback_language}"')
                    return lookup[normalized_key]
                if quoted_key in lookup:
                    _LOG.debug(f'No translation for "{quoted_key}" in "{language}". Falling back to "{cls._fallback_language}"')
                    return lookup[quoted_key]

        # Fallback 2: Key itself
        _LOG.warning(f'No localization string found for key "{normalized_key}" in language "{language}" or "{cls._fallback_language}". Returning key as fallback')
        return normalized_key
