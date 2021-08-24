import cv2


def Esempio(esercizio):
    cap = cv2.VideoCapture('../res/video/' + esercizio + '.mp4')

    while True:
        try:
            # legge frame video
            success, frame = cap.read()

            cv2.imshow("Dimostrazione", frame)
            cv2.waitKey(1)

        except:
            cv2.destroyAllWindows()
            break
