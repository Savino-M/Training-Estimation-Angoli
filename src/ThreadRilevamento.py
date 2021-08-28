from threading import Thread

import cv2
import keyboard
import mediapipe as mp
from playsound import playsound

import CalcolaAngoli
import ValutaAngoli


class ThreadEsecuzione(Thread):

    def __init__(self, numSerie, numRipetizioni, esercizio):
        Thread.__init__(self)
        self.numSerie = numSerie
        self.numRipetizioni = numRipetizioni
        self.esercizio = esercizio

    def scegliEsercizio(self, results, mpPose, frame):
        esercizio = self.esercizio
        listaAngoli = list()
        soglia = None

        # viene restituita una lista contenente gli angoli rilevanti per l'esercizio e la soglia
        # inoltre viene valutata l'esecuzione
        if esercizio == "squat":
            listaAngoli, soglia = CalcolaAngoli.angoliSquat(results, mpPose)
            valutazione = ValutaAngoli.valutaSquat(listaAngoli, frame)
        elif esercizio == "bicipiti":
            listaAngoli, soglia = CalcolaAngoli.angoliBicipiti(results, mpPose)
            valutazione = ValutaAngoli.valutaBicipiti(listaAngoli, frame)

        return listaAngoli, soglia, valutazione

    def run(self):

        numSerie = self.numSerie
        numRipetizioni = self.numRipetizioni

        webcam = cv2.VideoCapture(0)

        # inizializza modello
        mpPose = mp.solutions.pose
        pose = mpPose.Pose()

        # per disegnare i landmarks
        mpDraw = mp.solutions.drawing_utils

        posizione = None
        numRipetizioniContate = 0
        numSerieContate = 0

        while True:

            # legge frame video
            success, frame = webcam.read()

            # converte il frame in RGB
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # rileva i landmarks
            results = pose.process(imgRGB)

            # se trova dei landmarks
            if results.pose_landmarks:

                # disegna i landmarks e le connessioni sull'immagine
                mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
                image_height, image_width, _ = frame.shape

                # vengono calcolati gli angoli rilevanti per l'esercizio scelto
                listaAngoli, soglia, valutazione = ThreadEsecuzione.scegliEsercizio(self, results, mpPose, frame)

                numAngoli = len(listaAngoli)

                i = 0
                j = 0

                for angolo in listaAngoli:

                    if angolo.valore < soglia:
                        i += 1

                    # se tutti gli angoli rilevanti per l'esercizio sono minori della soglia
                    if i == numAngoli:
                        posizione = "Giù"
                        # playsound("../res/sounds/reps/" + str(numRipetizioniContate) + ".mp3")

                    if angolo.valore > soglia:
                        j += 1

                        # se tutti gli angoli rilevanti per l'esercizio sono maggiori della soglia
                    if j == numAngoli and posizione == "Giù" and valutazione == "OK":
                        posizione = "Su"
                        numRipetizioniContate += 1

                cv2.putText(frame, str(numRipetizioniContate), (1100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                if numRipetizioni is not None and numSerie is not None:
                    if numRipetizioniContate == numRipetizioni:
                        numSerieContate += 1
                        numRipetizioniContate = 0
                        if numSerieContate < numSerie:
                            #playsound("../res/sounds/mess/recupero.mp3")
                            cv2.waitKey(90000)
                            #playsound("../res/sounds/mess/ripartenza.mp3")
            # else:
            # playsound("../res/sounds/mess/posizionamento.mp3")

            cv2.imshow("", frame)
            cv2.waitKey(1)

            if keyboard.is_pressed('q') or numSerieContate == numSerie:
                cv2.destroyAllWindows()
                break
