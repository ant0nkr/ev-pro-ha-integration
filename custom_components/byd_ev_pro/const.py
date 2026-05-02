"""Constants for BYD EV Pro integration."""

DOMAIN = "byd_ev_pro"
MANUFACTURER = "BYD"

# Sensor definitions: (key, name, device_class, unit, state_class, icon, precision)
# device_class: https://developers.home-assistant.io/docs/core/entity/sensor/#available-device-classes
# state_class: "measurement" for instantaneous, "total_increasing" for monotonic counters
# precision: suggested_display_precision (None = HA default)
SENSOR_DEFINITIONS: list[tuple[str, str, str | None, str | None, str | None, str | None, int | None]] = [
    # Battery
    ("battery_soc", "Battery Level", "battery", "%", "measurement", None, 0),
    ("battery_health", "Battery Health", None, "%", "measurement", "mdi:battery-heart-variant", 1),
    ("battery_voltage", "HV Battery Voltage", "voltage", "V", "measurement", None, 1),
    ("battery_current", "HV Battery Current", "current", "A", "measurement", None, 1),
    ("battery_power", "Battery Power", "power", "kW", "measurement", None, 2),
    ("aux_voltage", "12V Battery", "voltage", "V", "measurement", None, 1),
    ("cell_max_voltage", "Cell Max Voltage", "voltage", "V", "measurement", None, 3),
    ("cell_min_voltage", "Cell Min Voltage", "voltage", "V", "measurement", None, 3),
    # Temperature
    ("cabin_temp", "Cabin Temperature", "temperature", "\u00b0C", "measurement", None, 1),
    ("outside_temp", "Outside Temperature", "temperature", "\u00b0C", "measurement", None, 1),
    ("battery_max_temp", "Battery Max Temperature", "temperature", "\u00b0C", "measurement", None, 1),
    ("battery_min_temp", "Battery Min Temperature", "temperature", "\u00b0C", "measurement", None, 1),
    ("front_motor_temp", "Front Motor Temperature", "temperature", "\u00b0C", "measurement", None, 0),
    ("rear_motor_temp", "Rear Motor Temperature", "temperature", "\u00b0C", "measurement", None, 0),
    # Driving
    ("range", "EV Range", "distance", "km", "measurement", None, 0),
    ("odometer", "Odometer", "distance", "km", "total_increasing", None, 1),
    ("speed", "Speed", "speed", "km/h", "measurement", None, 0),
    ("vehicle_state", "Vehicle State", None, None, None, "mdi:car", None),
    # Charging
    ("charging_state", "Charging State", None, None, None, "mdi:ev-station", None),
    ("charging_gun", "Charging Gun", None, None, None, "mdi:ev-plug-type2", None),
    ("charging_power_dd", "Charging Power", "power", "kW", "measurement", None, 1),
    # Climate
    ("ac_power", "Climate", None, None, None, "mdi:air-conditioner", None),
    ("driver_temp_set", "Driver Temperature Setting", "temperature", "\u00b0C", "measurement", None, 1),
    ("fan_speed", "Fan Speed", None, None, None, "mdi:fan", None),
    # Access
    ("lock_lf", "Driver Door Lock", None, None, None, "mdi:car-door-lock", None),
    ("lock_rf", "Passenger Door Lock", None, None, None, "mdi:car-door-lock", None),
    ("lock_lr", "Rear Left Door Lock", None, None, None, "mdi:car-door-lock", None),
    ("lock_rr", "Rear Right Door Lock", None, None, None, "mdi:car-door-lock", None),
    ("door_lf", "Driver Door", None, None, None, "mdi:car-door", None),
    ("door_rf", "Passenger Door", None, None, None, "mdi:car-door", None),
    ("door_lr", "Rear Left Door", None, None, None, "mdi:car-door", None),
    ("door_rr", "Rear Right Door", None, None, None, "mdi:car-door", None),
    ("door_hood", "Hood", None, None, None, "mdi:car-door", None),
    ("trunk_open", "Trunk", None, None, None, "mdi:car-back", None),
    # Windows and roof
    ("window_lf_pos", "Driver Window", None, "%", "measurement", "mdi:car-door", 0),
    ("window_rf_pos", "Passenger Window", None, "%", "measurement", "mdi:car-door", 0),
    ("window_lr_pos", "Rear Left Window", None, "%", "measurement", "mdi:car-door", 0),
    ("window_rr_pos", "Rear Right Window", None, "%", "measurement", "mdi:car-door", 0),
    ("window_lf_status", "Driver Window Status", None, None, None, "mdi:window-open-variant", None),
    ("window_rf_status", "Passenger Window Status", None, None, None, "mdi:window-open-variant", None),
    ("window_lr_status", "Rear Left Window Status", None, None, None, "mdi:window-open-variant", None),
    ("window_rr_status", "Rear Right Window Status", None, None, None, "mdi:window-open-variant", None),
    ("sunroof_state", "Sunroof Status", None, None, None, "mdi:car-estate", None),
    ("sunroof_pos", "Sunroof Position", None, "%", "measurement", "mdi:car-estate", 0),
    ("sunshade_state", "Panorama Sunshade Status", None, None, None, "mdi:roller-shade", None),
    # TPMS
    ("tyre_pressure_lf", "Driver Tyre Pressure", "pressure", "bar", "measurement", None, 2),
    ("tyre_pressure_rf", "Passenger Tyre Pressure", "pressure", "bar", "measurement", None, 2),
    ("tyre_pressure_lr", "Rear Left Tyre Pressure", "pressure", "bar", "measurement", None, 2),
    ("tyre_pressure_rr", "Rear Right Tyre Pressure", "pressure", "bar", "measurement", None, 2),
    ("tyre_temp_lf", "Driver Tyre Temperature", "temperature", "\u00b0C", "measurement", None, 0),
    ("tyre_temp_rf", "Passenger Tyre Temperature", "temperature", "\u00b0C", "measurement", None, 0),
    ("tyre_temp_lr", "Rear Left Tyre Temperature", "temperature", "\u00b0C", "measurement", None, 0),
    ("tyre_temp_rr", "Rear Right Tyre Temperature", "temperature", "\u00b0C", "measurement", None, 0),
    ("tyre_state_lf", "Driver Tyre Status", None, None, None, "mdi:car-tire-alert", None),
    ("tyre_state_rf", "Passenger Tyre Status", None, None, None, "mdi:car-tire-alert", None),
    ("tyre_state_lr", "Rear Left Tyre Status", None, None, None, "mdi:car-tire-alert", None),
    ("tyre_state_rr", "Rear Right Tyre Status", None, None, None, "mdi:car-tire-alert", None),
    # Other
    ("steering_heat", "Steering Wheel Heat", None, None, None, "mdi:steering", None),
    ("driver_seat_heat", "Driver Seat Heat", None, None, None, "mdi:car-seat-heater", None),
    ("front_motor_rpm", "Front Motor Speed", None, "RPM", "measurement", "mdi:engine", 0),
]

# Human-readable state mappings
VEHICLE_STATE_MAP = {0: "OFF", 1: "ACC", 2: "READY"}
CHARGING_STATE_MAP = {0: "Not Charging", 1: "Charging", 2: "Charge Complete"}
# gun_state=1 is a phantom value on BYD — only ≥2 means physically connected.
GUN_STATE_MAP = {0: "Disconnected", 1: "Disconnected", 2: "AC", 3: "DC"}
AC_POWER_MAP = {0: "Off", 1: "On"}
# BYD seat heat: 1=Off, 2=Level 1, 3=Level 2 (NOT 0-based).
SEAT_HEAT_MAP = {0: "Off", 1: "Off", 2: "Level 1", 3: "Level 2"}
# BYD steering wheel heat: 1=Off, 2=On (inverted).
STEERING_HEAT_MAP = {0: "Off", 1: "Off", 2: "On"}
LOCK_STATE_MAP = {0: "Unknown", 1: "Unlocked", 2: "Locked"}
OPEN_CLOSED_MAP = {0: "Closed", 1: "Open"}
TYRE_STATE_MAP = {0: "Normal", 1: "Low", 2: "High"}
SUNROOF_STATE_MAP = {0: "Closed", 1: "Open", 2: "Closing", 3: "Opening"}
SUNSHADE_STATE_MAP = {0: "Closed", 1: "Open", 2: "Closing", 3: "Opening"}
