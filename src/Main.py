import os
import tkinter as tk
from functools import partial
from tkinter import LEFT

import cv2
import dlib
import easygui
import face_recognition

import SceltaEsercizi as se


def Accedi(window):
    # caricamento fotocamera
    webcam = cv2.VideoCapture(0)
    webcam.read()

    risposta = "No"

    # confronta l'immagine dell'utente con tutte quelle degli utenti registrati
    for image in os.listdir("../res/utenti/"):

        imgConosciuta = face_recognition.load_image_file("../res/utenti/" + image)

        # acquisisce l'immagine da webcam
        return_value, imgSconosciuta = webcam.read()

        encodingImgConosciuta = face_recognition.face_encodings(imgConosciuta)[0]

        try:
            encodingImgSconosciuta = face_recognition.face_encodings(imgSconosciuta)[0]
        except:
            easygui.msgbox("Nessun volto riconosciuto, prova a registrarti", title="Accesso fallito")

        # confronta le immagini
        results = face_recognition.compare_faces([encodingImgConosciuta], encodingImgSconosciuta)
        risposta = "Si" if results[0] else "No"

        # se il volto è stato riconosciuto
        if risposta == "Si":
            utente = image.split(".")[0].strip()
            print("Utente riconosciuto. Ciao", utente)
            window.destroy()
            s = se.SceltaEsercizi(utente)
            s.sceltaEsercizi()

    if risposta == "No":
        easygui.msgbox("Nessun volto riconosciuto, prova a registrarti", title="Accesso fallito")


def Registrati(window):
    window.withdraw()

    windowRegistrazione = tk.Tk()
    windowRegistrazione.geometry("340x100")
    windowRegistrazione.title("Training Estimation")
    windowRegistrazione.resizable(False, False)
    # windowRegistrati.iconphoto(False, tk.PhotoImage(file="../res/icone/icon.png"))

    frameRegistrazione = tk.Frame(windowRegistrazione)
    frameRegistrazione.grid(row=1, column=1)

    label_nome_utente = tk.Label(frameRegistrazione, text="Nome:")
    label_nome_utente.grid(row=0, column=0)

    label_password = tk.Label(frameRegistrazione, text="Cognome:")
    label_password.grid(row=0, column=1)

    entry_nome = tk.Entry(frameRegistrazione)
    entry_nome.grid(row=1, column=0)

    entry_cognome = tk.Entry(frameRegistrazione)
    entry_cognome.grid(row=1, column=1)

    login_button = tk.Button(frameRegistrazione, text="Registrati", command=partial(salvaRegistrazione, entry_nome, entry_cognome, windowRegistrazione, window, frameRegistrazione))
    login_button.grid(row=2, column=0)

    windowRegistrazione.mainloop()


def salvaRegistrazione(entry_nome, entry_cognome, windowRegistrazione, window, frameRegistrazione):
    nome = entry_nome.get()
    cognome = entry_cognome.get()

    # caricamento fotocamera
    webcam = cv2.VideoCapture(0)
    webcam.read()

    volti = []

    while len(volti) < 1:
        # acquisizione frame
        return_value, foto = webcam.read()

        detector = dlib.get_frontal_face_detector()

        volti = detector(foto, 1)

    label_nome_utente = tk.Label(frameRegistrazione, text="Volto rilevato. Salvataggio in corso...")
    label_nome_utente.grid(row=3, column=0)

    cv2.imwrite("../res/utenti/" + nome + " " + cognome + ".jpg", foto)

    easygui.msgbox("Registrazione avvenuta con successo!", title="Registrazione")
    windowRegistrazione.destroy()
    window.update()
    window.deiconify()


if __name__ == "__main__":
    # crea la finestra
    window = tk.Tk()
    window.geometry("300x50")
    window.title("Training Estimation")
    window.resizable(False, False)
    window.iconphoto(False, tk.PhotoImage(file="../res/icone/icon.png"))

    # crea i frame
    frameBenvenuto = tk.Frame(window)
    frameBenvenuto.grid(row=0)

    frameBottoni = tk.Frame(window)
    frameBottoni.grid(row=1)

    # aggiunge il label di benvenuto
    LabelBenvenuto = tk.Label(frameBenvenuto, text="Che cosa vuoi fare?")
    LabelBenvenuto.pack(side=LEFT)

    bottoneAccedi = tk.Button(frameBottoni, text="Accedi", command=partial(Accedi, window))
    bottoneAccedi.pack(side=LEFT)

    bottoneRegistrati = tk.Button(frameBottoni, text="Registrati", command=partial(Registrati, window))
    bottoneRegistrati.pack(side=LEFT)
    window.mainloop()
