import cv2


def valutaSquat(listaAngoli, frame):
    j = 50

    for angolo in listaAngoli:

        if angolo.valore > 90:
            cv2.putText(frame, angolo.nome + ": GREEN", (50, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            j += 30
        elif angolo.valore < 80:
            cv2.putText(frame, angolo.nome + ": RED", (60, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            j += 30
        elif 80 < angolo.valore < 90:
            cv2.putText(frame, angolo.nome + ": YELLOW", (70, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            j += 30


def valutaBicipiti(listaAngoli, frame):
    j = 50

    for angolo in listaAngoli:

        if angolo.valore > 90:
            cv2.putText(frame, angolo.nome + ": GREEN", (50, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            j += 30
        elif angolo.valore < 80:
            cv2.putText(frame, angolo.nome + ": RED", (60, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            j += 30
        elif 80 < angolo.valore < 90:
            cv2.putText(frame, angolo.nome + ": YELLOW", (70, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            j += 30
