# -------------------------------------------------
# REGISTERS
# -------------------------------------------------

# I2C
I2C_BUS         = 0
I2C_PRIM_ADDR   = 0x68
I2C_SEC_ADDR    = 0x69

# General
CHIP_ID_ADDRESS = 0x00
SENSORTIME_0    = 0x18
SENSORTIME_1    = 0x19
SENSORTIME_2    = 0x1A
INTERNAL_STATUS = 0x21
DATA_REG        = 0x0C
FIFO_CONFIG_0   = 0x48
FIFO_CONFIG_1   = 0x49
INIT_CTRL       = 0x59
INIT_ADDR_0     = 0x5B
INIT_ADDR_1     = 0x5C
INIT_DATA       = 0x5E
CMD             = 0x7E
PWR_CONF        = 0x7C
PWR_CTRL        = 0x7D

# Accelerometer
ACC_CONF        = 0x40
ACC_RANGE       = 0x41
ACC_X_7_0       = 0x0C
ACC_X_15_8      = 0x0D
ACC_Y_7_0       = 0x0E
ACC_Y_15_8      = 0x0F
ACC_Z_7_0       = 0x10
ACC_Z_15_8      = 0x11

# Gyroscope
GYR_CONF        = 0x42
GYR_RANGE       = 0x43
GYR_X_7_0       = 0x12
GYR_X_15_8      = 0x13
GYR_Y_7_0       = 0x14
GYR_Y_15_8      = 0x15
GYR_Z_7_0       = 0x16
GYR_Z_15_8      = 0x17

# Temperature
TEMP_7_0        = 0x22
TEMP_15_8       = 0x23
