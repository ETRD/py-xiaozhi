import time
from robot_hat import (
    Pin,
    PWMDriverConfig,
    PWMFactory,
    Servo,
    ServoCalibrationMode,
    ServoService,
    setup_env_vars,
)

setup_env_vars()  # autosetup environment, e.g.: GPIOZERO_PIN_FACTORY, ROBOT_HAT_MOCK_SMBUS etc

#led = Pin("LED", Pin.OUT)
#led.value(1)  # Turn on the LED to indicate the program is running.
#time.sleep(1)  # Wait for a moment to ensure the LED state is visible before proceeding.
#led.value(0)  # Turn off the LED after the delay.

mcu_rst = Pin("MCURST", Pin.OUT)
mcu_rst.value(0)  # Hold the MCU in reset
time.sleep(0.1)  # Wait for a moment to ensure the reset is registered
mcu_rst.value(1)  # Release the reset to allow the MCU to boot up

pwm_config = PWMDriverConfig(
    name="Sunfounder",  # 'PCA9685' or 'Sunfounder', or register a custom driver.
    address=0x14,  # I2C address of the device
    bus=1,  # The I2C bus number used to communicate with the PWM driver chip
    # The parameters below are optional and have default values:
    frame_width=20000,
    freq=50,
)
driver = PWMFactory.create_pwm_driver(
    bus=pwm_config.bus,  # either a bus number or an smbus instance.
    config=pwm_config,
)

left_leg_servo = ServoService(
    servo=Servo(
        driver=driver,
        channel="P0",  # Either an integer or a string with a numeric suffix.
        # The parameters below are optional and have default values:
        # The minimum and maximum logical angles (in degrees) that can be commanded to the servo.
        min_angle=-90.0,
        max_angle=90.0,
        # The minimum and maximum pulse widths (in microseconds) corresponding to the servo's physical movement.
        min_pulse=500,
        max_pulse=2500,
        # The minimum and maximum physical angles (in degrees) that the servo can achieve.
        # These values are used to map the logical angle to the physical angle.
        real_min_angle=-90.0,
        real_max_angle=90.0,
    ),
    name="steering",  # A human-readable name for the servo (useful for debugging/logging).
    min_angle=-90,
    max_angle=90,
    calibration_mode=ServoCalibrationMode.SUM,
    calibration_offset=0,
)
right_leg_servo = ServoService(
    servo=Servo(
        driver=driver,
        channel="P2",  # Either an integer or a string with a numeric suffix.
        # The parameters below are optional and have default values:
        # The minimum and maximum logical angles (in degrees) that can be commanded to the servo.
        min_angle=-90.0,
        max_angle=90.0,
        # The minimum and maximum pulse widths (in microseconds) corresponding to the servo's physical movement.
        min_pulse=500,
        max_pulse=2500,
        # The minimum and maximum physical angles (in degrees) that the servo can achieve.
        # These values are used to map the logical angle to the physical angle.
        real_min_angle=-90.0,
        real_max_angle=90.0,
    ),
    name="steering",  # A human-readable name for the servo (useful for debugging/logging).
    min_angle=-90,
    max_angle=90,
    calibration_mode=ServoCalibrationMode.SUM,
    calibration_offset=-8,
)

left_sole_servo = ServoService(
    servo=Servo(
        driver=driver,
        channel="P1",  # Either an integer or a string with a numeric suffix.
        # The parameters below are optional and have default values:
        # The minimum and maximum logical angles (in degrees) that can be commanded to the servo.
        min_angle=-90.0,
        max_angle=90.0,
        # The minimum and maximum pulse widths (in microseconds) corresponding to the servo's physical movement.
        min_pulse=500,
        max_pulse=2500,
        # The minimum and maximum physical angles (in degrees) that the servo can achieve.
        # These values are used to map the logical angle to the physical angle.
        real_min_angle=-90.0,
        real_max_angle=90.0,
    ),
    name="steering",  # A human-readable name for the servo (useful for debugging/logging).
    min_angle=-90,
    max_angle=90,
    calibration_mode=ServoCalibrationMode.SUM,
    calibration_offset=0,
)
right_sole_servo = ServoService(
    servo=Servo(
        driver=driver,
        channel="P3",  # Either an integer or a string with a numeric suffix.
        # The parameters below are optional and have default values:
        # The minimum and maximum logical angles (in degrees) that can be commanded to the servo.
        min_angle=-90.0,
        max_angle=90.0,
        # The minimum and maximum pulse widths (in microseconds) corresponding to the servo's physical movement.
        min_pulse=500,
        max_pulse=2500,
        # The minimum and maximum physical angles (in degrees) that the servo can achieve.
        # These values are used to map the logical angle to the physical angle.
        real_min_angle=-90.0,
        real_max_angle=90.0,
    ),
    name="steering",  # A human-readable name for the servo (useful for debugging/logging).
    min_angle=-90,
    max_angle=90,
    calibration_mode=ServoCalibrationMode.SUM,
    calibration_offset=-2,
)
driver.set_pwm_freq(pwm_config.freq)

def do_action(action_type="stop"):
    if action_type == "dance":
        # 执行跳舞动作：原有的循环
        for angle in range(0, -46, -1):
            left_sole_servo.set_angle(-angle)
            right_sole_servo.set_angle(angle)
            time.sleep(0.02)

        for angle in range(-45, 1, 1):
            left_sole_servo.set_angle(-angle)
            right_sole_servo.set_angle(angle)
            time.sleep(0.02)
    if action_type == "forward":
        for angle in range(0, -46, -1):
            left_sole_servo.set_angle(-angle)
            time.sleep(0.02)
        for angle in range(0, -46, -1):
            left_leg_servo.set_angle(angle)
            time.sleep(0.02)
        for angle in range(0, -46, -1):
            right_leg_servo.set_angle(angle)
            time.sleep(0.02)                    
    elif action_type == "stop":
        # 执行停止动作：重置舵机到中心位置
        reset_servos()
    else:
        # 默认动作：跳舞
        reset_servos()

def reset_servos():
    left_sole_servo.reset()
    right_sole_servo.reset()
    left_leg_servo.reset()
    right_leg_servo.reset()

if __name__ == "__main__":
    # 测试函数
    print("开始测试舵机动作...")
    reset_servos()
    #do_action("forward")
    print("测试完成。")