import cv2


def valutaSquat(listaAngoli, frame):
    j = 50
    valutazione = None

    for angolo in listaAngoli:

        if angolo.valore > 90:
            cv2.putText(frame, angolo.nome + ": GREEN", (50, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            j += 30
            valutazione = "OK"
        elif angolo.valore < 80:
            cv2.putText(frame, angolo.nome + ": RED", (60, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            j += 30
            valutazione = "Sbagliato"
        elif 80 < angolo.valore < 90:
            cv2.putText(frame, angolo.nome + ": YELLOW", (70, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            j += 30
            valutazione = "OK"

    return valutazione


def valutaBicipiti(listaAngoli, frame):
    j = 50
    valutazione = None

    for angolo in listaAngoli:

        if angolo.valore > 90 or angolo.valore < 80:
            cv2.putText(frame, angolo.nome + ": GREEN", (50, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            j += 30
            valutazione = "OK"
        elif 80 < angolo.valore < 90:
            cv2.putText(frame, angolo.nome + ": YELLOW", (70, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            j += 30
            valutazione = "OK"
        else:
            cv2.putText(frame, angolo.nome + ": RED", (70, j), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            j += 30
            valutazione = "Sbagliato"

    return valutazione
