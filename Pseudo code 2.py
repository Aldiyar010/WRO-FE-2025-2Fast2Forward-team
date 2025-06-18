# Constants
SIGNATURE_LEFT = 1       # Detected object is red
SIGNATURE_RIGHT = 2      # Detected object is green
SIGNATURE_FORWARD = 3    # No detected object

LINE_THRESHOLD = 50      # Light sensor threshold for turning
BASE_SPEED = 30          # Base speed for forward movement
DRIVE_TIME = 1.0         # Time to drive forward after turning (in seconds)

# Main loop
while True:
    # Read detected objects from the Pixy2 camera
    blocks = pixy2.get_blocks()

    if blocks:
        # Find the largest object based on width * height
        largest = max(blocks, key=lambda b: b.width * b.height)
        signature = largest.signature

        if signature == SIGNATURE_LEFT:
            # Object is green → turn left
            steering_motor.turn_to_angle(-45)  # steer left
            drive_motor.move_forward(BASE_SPEED)
            wait(DRIVE_TIME)
            drive_motor.stop()
            steering_motor.turn_to_angle(0)  # return wheels to center

        elif signature == SIGNATURE_RIGHT:
            # Object is red → turn right
            steering_motor.turn_to_angle(45)  # steer right
            drive_motor.move_forward(BASE_SPEED)
            wait(DRIVE_TIME)
            drive_motor.stop()
            steering_motor.turn_to_angle(0)

        elif signature == SIGNATURE_FORWARD:
            # Object is not detected → drive straight
            steering_motor.turn_to_angle(0)
            drive_motor.move_forward(BASE_SPEED)
            wait(DRIVE_TIME)
            drive_motor.stop()