import numpy as np

from Angolo import Angolo


def calcolaAngolo(a, b, c):
    a = np.array(a)  # first
    b = np.array(b)  # mid
    c = np.array(c)  # end
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return round(angle, 3)


def calcolaAngoli(results, mp_pose):
    listaAngoli = list()

    # ricava le coordinate dei landamrks
    spallaSinistra = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    spallaDestra = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    gomitoSinistro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    gomitoDestro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    polsoSinistro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    polsoDestro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
    fiancoSinistro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    fiancoDestro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
    ginocchioSinistro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    ginocchioDestro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
    cavigliaSinistra = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
    cavigliaDestra = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
    indicePiedeSinistro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
    indicePiedeDestro = [results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x, results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]

    angoloSpallaGomitoPolsoSX = calcolaAngolo(spallaSinistra, gomitoSinistro, polsoSinistro)
    listaAngoli.append(angoloSpallaGomitoPolsoSX)

    angoloSpallaGomitoPolsoDX = calcolaAngolo(spallaDestra, gomitoDestro, polsoDestro)
    listaAngoli.append(angoloSpallaGomitoPolsoDX)

    angoloGomitoSpallaFiancoSX = calcolaAngolo(gomitoSinistro, spallaSinistra, fiancoSinistro)
    listaAngoli.append(angoloGomitoSpallaFiancoSX)

    angoloGomitoSpallaFiancoDX = calcolaAngolo(gomitoDestro, spallaDestra, fiancoDestro)
    listaAngoli.append(angoloGomitoSpallaFiancoDX)

    angoloSpallaFiancoGinocchioSX = calcolaAngolo(spallaSinistra, fiancoSinistro, ginocchioSinistro)
    listaAngoli.append(angoloSpallaFiancoGinocchioSX)

    angoloSpallaFiancoGinocchioDX = calcolaAngolo(spallaDestra, fiancoDestro, ginocchioDestro)
    listaAngoli.append(angoloSpallaFiancoGinocchioDX)

    angoloFiancoGinocchioCavigliaSX = calcolaAngolo(fiancoSinistro, ginocchioSinistro, cavigliaSinistra)
    listaAngoli.append(angoloFiancoGinocchioCavigliaSX)

    angoloFiancoGinocchioCavigliaDX = calcolaAngolo(fiancoDestro, ginocchioDestro, cavigliaDestra)
    listaAngoli.append(angoloFiancoGinocchioCavigliaDX)

    angoloGinocchioCavigliaIndicePiedeSX = calcolaAngolo(ginocchioSinistro, cavigliaSinistra, indicePiedeSinistro)
    listaAngoli.append(angoloGinocchioCavigliaIndicePiedeSX)

    angoloGinocchioCavigliaIndicePiedeDX = calcolaAngolo(ginocchioDestro, cavigliaDestra, indicePiedeDestro)
    listaAngoli.append(angoloGinocchioCavigliaIndicePiedeDX)

    angoloGinocchioFiancoDXFiancoSX = calcolaAngolo(ginocchioDestro, fiancoDestro, fiancoSinistro)
    listaAngoli.append(angoloGinocchioFiancoDXFiancoSX)

    angoloGinocchioFiancoSXFiancoDX = calcolaAngolo(ginocchioSinistro, fiancoSinistro, fiancoDestro)
    listaAngoli.append(angoloGinocchioFiancoSXFiancoDX)

    return listaAngoli


def angoliSquat(results, mpPose):
    listaAngoliSquat = list()

    # calcola tutti gli angoli
    listaAngoli = calcolaAngoli(results, mpPose)

    # calcola gli angoli rilevanti per lo squat
    angoloSpallaFiancoGinocchioDX = Angolo("Fianco Destro", listaAngoli[5])
    angoloSpallaFiancoGinocchioSX = Angolo("Fianco Sinistro", listaAngoli[4])
    angoloFiancoGinocchioCavigliaDX = Angolo("Gamba Destra", listaAngoli[6])
    angoloFiancoGinocchioCavigliaSX = Angolo("Gamba Sinistra", listaAngoli[7])

    listaAngoliSquat.append(angoloSpallaFiancoGinocchioDX)
    listaAngoliSquat.append(angoloSpallaFiancoGinocchioSX)
    listaAngoliSquat.append(angoloFiancoGinocchioCavigliaDX)
    listaAngoliSquat.append(angoloFiancoGinocchioCavigliaSX)

    return listaAngoliSquat, 170


def angoliBicipiti(results, mpPose):
    listaAngoliBicipiti = list()

    # calcola tutti gli angoli
    listaAngoli = calcolaAngoli(results, mpPose)

    # calcola gli angoli rilevanti per i bicipiti
    angoloSpallaGomitoPolsoSX = Angolo("Bicipite sinistro", listaAngoli[0])
    angoloSpallaGomitoPolsoDX = Angolo("Bicipite Destro", listaAngoli[1])

    listaAngoliBicipiti.append(angoloSpallaGomitoPolsoDX)
    listaAngoliBicipiti.append(angoloSpallaGomitoPolsoSX)

    return listaAngoliBicipiti, 160
