from ev3dev2.motor import MediumMotor, OUTPUT_D, OUTPUT_A, SpeedPercent
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_4, INPUT_2
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time

# Initialize motors and sensors
drive_motor = MediumMotor(OUTPUT_D)         # Medium motor for movement (port D)
steer_motor = MediumMotor(OUTPUT_A)         # Medium motor for turning (port A)
ultrasonic = UltrasonicSensor(INPUT_4)      # Ultrasonic sensor on port 4
color_sensor = ColorSensor(INPUT_2)         # Color sensor on port 2
sound = Sound()                             # EV3 speaker
screen = Display()                          # EV3 screen

# Variables
line = 0                    # Counter for how many black lines have been detected
target_distance = 61        # Target distance from obstacle in cm
Kp = -4                     # Proportional gain for distance regulation

# Start moving the drive motor backward
drive_motor.on(SpeedPercent(-50))

while True:
    # --- Proportional distance control (P-regulator) ---
    dist = ultrasonic.distance_centimeters   # Read distance from ultrasonic sensor
    error = dist - target_distance           # Calculate the error
    turn = error * Kp                        # Apply proportional gain
    drive_motor.on(SpeedPercent(turn))       # Adjust the motor speed accordingly

    # --- Black line detection logic ---
    if color_sensor.color == ColorSensor.COLOR_BLACK:
        time.sleep(2)                        # Wait 2 seconds to avoid multiple counts
        sound.play_tone(440, 0.5)            # Play a short tone
        line += 1                            # Increase the line counter

    # --- Special behavior when 12 lines are reached ---
    if line == 12:
        steer_motor.on_for_seconds(SpeedPercent(-50), 1)  # Turn the steering motor for 1 second
        sound.speak("Kung Fu!")                            # Speak something fun

    # --- Display line count on screen ---
    screen.clear()                                         # Clear previous display
    screen.text_grid(f"Line count: {line}", x=0, y=0)      # Show the current line count
    screen.update()                                        # Refresh the screen
    time.sleep(1)                                          # Wait 1 second before updating again

