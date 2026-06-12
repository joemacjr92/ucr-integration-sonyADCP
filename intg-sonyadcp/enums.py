"""This module defines all enums used in the integration"""

from enum import StrEnum

class Languages(StrEnum):
    """Defines all supported language codes for the integration"""

    ENGLISH = "en_US"
    GERMAN = "de_DE"

    @classmethod
    def get_values(cls):
        """Get a list of all language codes defined in this class"""
        return [lang.value for lang in cls]

class Messages(StrEnum):
    """Defines all messages used in the integration"""

    POLLING_ERROR = "polling_error"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"
    NO_SIGNAL = "no_signal"
    VIDEO_MUTED = "video_muted"
    UNKNOWN = "unknown"
    REMOTE = "remote"

class Sources (StrEnum):
    """Defines all sources for the media player entity"""

    HDMI_1 = "HDMI 1"
    HDMI_2 = "HDMI 2"

class SimpleCommands (StrEnum):
    """Defines all simple commands for the media player and remote entity.
    Maximum 20 upper case only characters including -/_.:+#*°@%()? allowed"""

    INPUT_HDMI1 =                                               "INPUT_HDMI_1"
    INPUT_HDMI2 =                                               "INPUT_HDMI_2"
    MODE_PRESET_REF =                                           "MODE_PIC_REF"
    MODE_PRESET_USER =                                          "MODE_PIC_USER"
    MODE_PRESET_USER1 =                                         "MODE_PIC_USER1"
    MODE_PRESET_USER2 =                                         "MODE_PIC_USER2"
    MODE_PRESET_USER3 =                                         "MODE_PIC_USER3"
    MODE_PRESET_TV =                                            "MODE_PIC_TV"
    MODE_PRESET_PHOTO =                                         "MODE_PIC_PHOTO"
    MODE_PRESET_GAME =                                          "MODE_PIC_GAME"
    MODE_PRESET_BRIGHT_CINEMA =                                 "MODE_PIC_BRT_CINEMA"
    MODE_PRESET_BRIGHT_TV =                                     "MODE_PIC_BRT_TV"
    MODE_PRESET_CINEMA_FILM_1 =                                 "MODE_PIC_CINE_FILM_1"
    MODE_PRESET_CINEMA_FILM_2 =                                 "MODE_PIC_CINE_FILM_2"
    MODE_ASPECT_RATIO_NORMAL =                                  "MODE_AR_NORMAL"
    MODE_ASPECT_RATIO_ZOOM_1_85 =                               "MODE_AR_ZOOM_1.85"
    MODE_ASPECT_RATIO_ZOOM_2_35 =                               "MODE_AR_ZOOM_2.35"
    MODE_ASPECT_RATIO_V_STRETCH =                               "MODE_AR_V_STRETCH"
    MODE_ASPECT_RATIO_SQUEEZE =                                 "MODE_AR_SQUEEZE"
    MODE_ASPECT_RATIO_STRETCH =                                 "MODE_AR_STRETCH"
    MODE_ASPECT_RATIO_ASPECT_RATIO_SCALING =                    "MODE_AR_RATIO_SCALE"
    MODE_MOTIONFLOW_OFF =                                       "MODE_MOTION_OFF"
    MODE_MOTIONFLOW_SMOOTH_HIGH =                               "MODE_MOTION_SMTH_HIGH"
    MODE_MOTIONFLOW_SMOOTH_LOW =                                "MODE_MOTION_SMTH_LOW"
    MODE_MOTIONFLOW_IMPULSE =                                   "MODE_MOTION_IMPULSE"
    MODE_MOTIONFLOW_COMBINATION =                               "MODE_MOTION_COMB"
    MODE_MOTIONFLOW_TRUE_CINEMA =                               "MODE_MOTION_TRUE_CIN"
    MODE_HDR_ON =                                               "MODE_HDR_ON"
    MODE_HDR_OFF =                                              "MODE_HDR_OFF"
    MODE_HDR_AUTO =                                             "MODE_HDR_AUTO"
    MODE_HDR_HDR10 =                                            "MODE_HDR_HDR10"
    MODE_HDR_HDR_REF =                                          "MODE_HDR_HDR_REF"
    MODE_HDR_HLG =                                              "MODE_HDR_HLG"
    MODE_HDR_DYNAMIC_TONE_MAPPING_1 =                           "MODE_HDR_TONEMAP_1"
    MODE_HDR_DYNAMIC_TONE_MAPPING_2 =                           "MODE_HDR_TONEMAP_2"
    MODE_HDR_DYNAMIC_TONE_MAPPING_3 =                           "MODE_HDR_TONEMAP_3"
    MODE_HDR_DYNAMIC_TONE_MAPPING_OFF =                         "MODE_HDR_TONEMAP_OFF"
    MODE_CONTRAST_ENHANCER_HIGH =                               "MODE_CONTR_ENHA_HIGH"
    MODE_CONTRAST_ENHANCER_MID =                                "MODE_CONTR_ENHA_MID"
    MODE_CONTRAST_ENHANCER_LOW =                                "MODE_CONTR_ENHA_LOW"
    MODE_CONTRAST_ENHANCER_OFF =                                "MODE_CONTR_ENHA_OFF"
    MODE_2D_3D_SELECT_AUTO =                                    "MODE_2D/3D_SEL_AUTO"
    MODE_2D_3D_SELECT_3D =                                      "MODE_2D/3D_SEL_3D"
    MODE_2D_3D_SELECT_2D =                                      "MODE_2D/3D_SEL_2D"
    MODE_3D_FORMAT_SIMULATED_3D =                               "MODE_3D_SIM_3D"
    MODE_3D_FORMAT_SIDE_BY_SIDE =                               "MODE_3D_SIDE_BY_SIDE"
    MODE_3D_FORMAT_OVER_UNDER =                                 "MODE_3D_OVER_UNDER"
    MODE_DYNAMIC_IRIS_CONTROL_OFF =                             "MODE_DYN_IRIS_OFF"
    MODE_DYNAMIC_IRIS_CONTROL_FULL =                            "MODE_DYN_IRIS_FULL"
    MODE_DYNAMIC_IRIS_CONTROL_LIMITED =                         "MODE_DYN_IRIS_LIM"
    MODE_DYNAMIC_LIGHT_CONTROL_OFF =                            "MODE_DYN_LIGHT_OFF"
    MODE_DYNAMIC_LIGHT_CONTROL_FULL =                           "MODE_DYN_LIGHT_FULL"
    MODE_DYNAMIC_LIGHT_CONTROL_LIMITED =                        "MODE_DYN_LIGHT_LIM"
    INPUT_LAG_REDUCTION_ON =                                    "MODE_LAG_REDUCE_ON"
    INPUT_LAG_REDUCTION_OFF =                                   "MODE_LAG_REDUCE_OFF"
    LENS_SHIFT_UP =                                             "LENS_SHIFT_UP"
    LENS_SHIFT_DOWN =                                           "LENS_SHIFT_DOWN"
    LENS_SHIFT_LEFT =                                           "LENS_SHIFT_LEFT"
    LENS_SHIFT_RIGHT =                                          "LENS_SHIFT_RIGHT"
    LENS_FOCUS_FAR =                                            "LENS_FOCUS_FAR"
    LENS_FOCUS_NEAR =                                           "LENS_FOCUS_NEAR"
    LENS_ZOOM_LARGE =                                           "LENS_ZOOM_LARGE"
    LENS_ZOOM_SMALL =                                           "LENS_ZOOM_SMALL"
    PICTURE_POSITION_SELECT_1_85 =                              "PIC_POS_SEL_1:85"
    PICTURE_POSITION_SELECT_2_35 =                              "PIC_POS_SEL_2:35"
    PICTURE_POSITION_SELECT_CUSTOM_1 =                          "PIC_POS_SEL_CUSTOM_1"
    PICTURE_POSITION_SELECT_CUSTOM_2 =                          "PIC_POS_SEL_CUSTOM_2"
    PICTURE_POSITION_SELECT_CUSTOM_3 =                          "PIC_POS_SEL_CUSTOM_3"
    PICTURE_POSITION_SELECT_CUSTOM_4 =                          "PIC_POS_SEL_CUSTOM_4"
    PICTURE_POSITION_SELECT_CUSTOM_5 =                          "PIC_POS_SEL_CUSTOM_5"
    PICTURE_POSITION_SAVE_1_85 =                                "PIC_POS_SAV_1:85"
    PICTURE_POSITION_SAVE_2_35 =                                "PIC_POS_SAV_2:35"
    PICTURE_POSITION_SAVE_CUSTOM_1 =                            "PIC_POS_SAV_CUSTOM_1"
    PICTURE_POSITION_SAVE_CUSTOM_2 =                            "PIC_POS_SAV_CUSTOM_2"
    PICTURE_POSITION_SAVE_CUSTOM_3 =                            "PIC_POS_SAV_CUSTOM_3"
    PICTURE_POSITION_SAVE_CUSTOM_4 =                            "PIC_POS_SAV_CUSTOM_4"
    PICTURE_POSITION_SAVE_CUSTOM_5 =                            "PIC_POS_SAV_CUSTOM_5"
    PICTURE_MUTING_ON =                                         "MUTING_PIC_ON"
    PICTURE_MUTING_OFF =                                        "MUTING_PIC_OFF"
    PICTURE_MUTING_TOGGLE =                                     "MUTING_PIC_TOGGLE"
    LASER_BRIGHTNESS_UP =                                       "LASER_DIM_UP"
    LASER_BRIGHTNESS_DOWN =                                     "LASER_DIM_DOWN"
    IRIS_BRIGHTNESS_UP =                                        "IRIS_BRIGHTNESS_UP"
    IRIS_BRIGHTNESS_DOWN =                                      "IRIS_BRIGHTNESS_DOWN"
    LAMP_CONTROL_LOW =                                          "LAMP_CONTROL_LOW"
    LAMP_CONTROL_HIGH =                                         "LAMP_CONTROL_HIGH"
    MENU_POSITION_BOTTOM_LEFT =                                 "MENU_POS_BOTTOM_LEFT"
    MENU_POSITION_CENTER =                                      "MENU_POS_CENTER"
    BLANKING_ON =                                               "BLANKING_ON"
    BLANKING_OFF =                                              "BLANKING_OFF"
    BLANKING_TOGGLE =                                           "BLANKING_TOGGLE"
    UPDATE_VIDEO_INFO =                                         "UPDATE_VIDEO_INFO"
    UPDATE_HEALTH_STATUS =                                      "UPDATE_HEALTH_STATUS"
    UPDATE_ALL_SENSORS =                                        "UPDATE_ALL_SENSORS"
    UPDATE_SELECT_OPTIONS =                                     "UPDATE_SELECT_OPTION"

class SensorVideoSignalTypes (StrEnum):
    """
    Defines all setting types needed for the video signal sensor.
    These are separated from the other sensor types as they are combined in the video signal sensor and need to be queried separately
    Color Space and 2d/3d mode are settings and included in SensorTypes
    """
    RESOLUTION = "resolution"
    DYNAMIC_RANGE = "dynamic-range"
    COLOR_FORMAT = "color-format"

class SensorSystemStatusTypes (StrEnum):
    """
    Defines all setting types needed for the system status sensor.
    These are separated from the other sensor types as they are combined in the system status sensor and need to be queried separately
    """
    ERROR = "error"
    WARNING = "warning"

class SensorHealthPollerTypes (StrEnum):
    """Defines all sensor type entities that will be updated by the health poller"""
    TEMPERATURE = "temp"
    LIGHT_TIMER = "light"
    SYSTEM_STATUS = "system"

    @staticmethod
    def get_all():
        """Get a list of all sensor types defined in this class"""
        values = [member.value for member in SensorHealthPollerTypes]

        return values

class SensorTypes (StrEnum):
    """Defines all setting types that can be queried from the projector and used for sensors in the integration"""
    VIDEO_SIGNAL = "video"
    TEMPERATURE = "temp"
    LIGHT_TIMER = "light"
    SYSTEM_STATUS = "system"
    POWER_STATUS = "power-status"
    INPUT = "input"
    PICTURE_MUTING = "picture-muting"
    PICTURE_PRESET = "picture-preset"
    ASPECT = "aspect"
    PICTURE_POSITION = "picture-position"
    HDR_STATUS = "hdr-status"
    HDR_DYNAMIC_TONE_MAPPING = "hdr-dynamic-tone-mapping"
    LAMP_CONTROL = "lamp-control"
    DYNAMIC_IRIS_CONTROL = "dynamic-iris-control"
    DYNAMIC_LIGHT_CONTROL = "dynamic-light-control"
    MOTIONFLOW = "motionflow"
    FORMAT_3D = "3d-format"
    INPUT_LAG_REDUCTION = "input-lag-reduction"
    MENU_POSITION = "menu-position"
    COLOR_TEMPERATURE = "color-temperature"
    COLOR_SPACE = "color-space"
    GAMMA = "gamma"
    CONTRAST_ENHANCER = "contrast-enhancer"
    MODE_2D_3D = "2d/3d-mode"
    LASER_BRIGHTNESS = "laser-brightness"
    IRIS_BRIGHTNESS = "iris-brightness"
    BLANKING = "blanking"

    @staticmethod
    def get_all():
        """Get a list of all sensor types defined in this class"""
        values = [member for member in SensorTypes]

        return values

class SelectTypes (StrEnum):
    """Defines all setting types that can be set with select commands and need to be queried for their options"""
    POWER = "power" #No query possible. Use power-status ? instead which is query only
    INPUT = "input"
    PICTURE_MUTING = "picture-muting"
    PICTURE_PRESET = "picture-preset"
    ASPECT = "aspect"
    PICTURE_POSITION_SELECT = "picture-position-select"
    PICTURE_POSITION_SAVE = "picture-position-save"
    HDR_FORMAT = "hdr-format"
    HDR_DYNAMIC_TONE_MAPPING = "hdr-dynamic-tone-mapping"
    LAMP_CONTROL = "lamp-control"
    DYNAMIC_IRIS_CONTROL = "dynamic-iris-control"
    DYNAMIC_LIGHT_CONTROL = "dynamic-light-control"
    MOTIONFLOW = "motionflow"
    FORMAT_3D = "3d-format"
    INPUT_LAG_REDUCTION = "input-lag-reduction"
    MENU_POSITION = "menu-position"
    COLOR_TEMPERATURE = "color-temperature"
    COLOR_SPACE = "color-space"
    GAMMA = "gamma"
    CONTRAST_ENHANCER = "contrast-enhancer"
    BLANKING = "blanking"

    @staticmethod
    def get_all():
        """Get a list of all select types defined in this class"""
        values = [member for member in SelectTypes]

        return values
