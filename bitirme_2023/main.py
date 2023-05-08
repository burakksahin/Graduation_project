import cv2
import time

from playsound import playsound
import numpy as np
from drowsy_detection import VideoFrameHandler
from drowsy_detection import plot_text


def main():
    frame_count = 0

    # Initialize the VideoFrameHandler object
    frame_handler = VideoFrameHandler()

    # Set the thresholds for the drowsiness detection algorithm
    thresholds: dict = {"WAIT_TIME": 2.5, "EAR_THRESH": 0.14}

    # Set up the camera capture object
    cap = cv2.VideoCapture(0)

    # Loop through the frames from the camera
    while True:
        frame_count += 1
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was successfully read
        if not ret:
            print("Error reading frame from camera")
            break

        # Process the frame using the VideoFrameHandler object
        processed_frame, play_alarm = frame_handler.process(frame, thresholds)

        # Add EAR and alarm text to the frame

        ##ear_text = f"EAR: {frame_handler.ear:.2f}"
        ##alarm_text = "ALARM ON" if play_alarm else "ALARM OFF"
        ##cv2.putText(frame, ear_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        ##cv2.putText(frame, alarm_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Display the processed frame on the console
        print(processed_frame.shape)
        print(f"Alarm should be played: {play_alarm}")
        
        # play sound if alarm is on
        if play_alarm and frame_count % 15 == 0:
            playsound('wake_up.mp3', block=False)


        cv2.imshow("frame", processed_frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
