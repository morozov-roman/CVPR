import numpy as np
import cv2


def lab1():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: camera")

    # Create a video capture object and set some parameters
    fps = 24.0
    capsize = (1280, 720)

    # Define the codec and create VideoWriter Object
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter()
    success = out.open('output.avi', fourcc, fps, capsize, True)

    while cap.isOpened():

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        back2rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        # draw lin
        start_point = (100, 90)
        end_point = (1000, 90)
        color = (0, 0, 255)
        thickness = 3
        back2rgb = cv2.line(img=back2rgb, pt1=start_point, pt2=end_point, color=color, thickness=thickness, lineType=8,
                            shift=0)

        # draw rectangle
        x1, y1 = 500, 100
        x2, y2 = 850, 550
        back2rgb = cv2.rectangle(back2rgb, (x1, y1), (x2, y2), (0, 255, 0), 7)

        cv2.imshow('webcam(2)', back2rgb)

        out.write(back2rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    lab1()
