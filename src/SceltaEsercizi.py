import tkinter as tk
from functools import partial
from tkinter import LEFT

import speech_recognition as sr
from playsound import playsound

import Basics
from ThreadRilevamento import ThreadEsecuzione


# legge gli esercizi supportati da un file e li restituisce
def leggiEserciziDaFile():
    esercizi = []

    with open("../res/esercizi/esercizi.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        esercizi.append(line.strip())

    return esercizi


def SpeechRecognition():
    text = ""
    recognizer_instance = sr.Recognizer()  # Crea una istanza del recognizer
    esercizi = leggiEserciziDaFile()

    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        audio = recognizer_instance.listen(source)
    try:
        esercizioRiconosciuto = recognizer_instance.recognize_google(audio, language="it-IT")
        if esercizioRiconosciuto in esercizi:
            runEsercizio(esercizioRiconosciuto)
        else:
            playsound("../res/sounds/errors/err_scelta.mp3")
    except Exception as e:
        print(e)
    return text


# per ogni esercizio supportato, crea un bottone
def inserisciBottoniEsercizi(esercizi, frameBottoni, window, utente):
    for esercizio in esercizi:
        bottoneEsercizio = tk.Button(frameBottoni, text=esercizio, command=partial(runEsercizio, esercizio, window))
        bottoneEsercizio.pack(side=LEFT)

    # bottone per eseguire la scheda di allenamento
    bottoneScheda = tk.Button(frameBottoni, text="Scheda", command=partial(runScheda, window, utente))
    bottoneScheda.pack(side=LEFT)


# quando si preme il bottone di un esercizio, questo parte
def runEsercizio(esercizio, window):
    window.withdraw()

    # mostra video di esempio
    Basics.Esempio(esercizio)

    # thread che rileva le ripetizioni
    thread = ThreadEsecuzione(None, None, esercizio.lower())
    thread.start()

    window.update()
    window.deiconify()


# si eseguono gli esercizi della scheda
def runScheda(window, utente):
    window.withdraw()

    file = open("../res/schede esercizi/scheda " + utente + ".txt", "r")
    for line in file:
        esercizio = line.split(" ")
        numSerie = esercizio[1].split("x")
        numRipetizioni = numSerie[1]

        # thread che rileva le ripetizioni
        thread = ThreadEsecuzione(int(numSerie[0]), int(numRipetizioni), esercizio[0].lower())
        thread.start()

    file.close()

    # if not (keyboard.is_pressed('q')):
    #    playsound("../res/sounds/mess/scheda completata.mp3")

    window.update()
    window.deiconify()


class SceltaEsercizi:

    def __init__(self, utente):
        self.utente = utente

    def sceltaEsercizi(self):
        utente = self.utente

        # crea la finestra
        window = tk.Tk()
        window.geometry("270x100")
        window.title("Training Estimation")
        window.resizable(False, False)
        window.iconphoto(False, tk.PhotoImage(file="../res/icone/icon.png"))

        # crea i frame
        frameBenvenuto = tk.Frame(window)
        frameBenvenuto.grid(row=0)

        frameBottoni = tk.Frame(window)
        frameBottoni.grid(row=1)

        # aggiunge il label di benvenuto
        LabelBenvenuto = tk.Label(frameBenvenuto, text="Benvenuto in Training Estimation\n Quale esercizio vuoi svolgere?")
        LabelBenvenuto.pack(side=LEFT)

        # aggiunge il bottone del microfono
        imgMic = tk.PhotoImage(file="../res/icone/microfono.png")
        BottoneMicrofono = tk.Button(frameBenvenuto, image=imgMic, command=SpeechRecognition)
        BottoneMicrofono.pack(side=LEFT)

        inserisciBottoniEsercizi(leggiEserciziDaFile(), frameBottoni, window, utente)

        playsound("../res/sounds/mess/benvenuto.mp3")
        playsound("../res/sounds/mess/scelta.mp3")

        window.mainloop()
