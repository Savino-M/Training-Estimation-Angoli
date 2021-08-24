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


def angoliSquat(results, mpPose):
    listaAngoli = list()

    # ricava le coordinate dei landamrks
    spalladx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_SHOULDER.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_SHOULDER.value].y
    spallasx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_SHOULDER.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_SHOULDER.value].y

    cavigliadx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_ANKLE.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_ANKLE.value].y
    cavigliasx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_ANKLE.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_ANKLE.value].y

    ginocchiodx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_KNEE.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_KNEE.value].y
    ginocchiosx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_KNEE.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_KNEE.value].y

    fiancodx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_HIP.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_HIP.value].y
    fiancosx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_HIP.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_HIP.value].y

    # calcola gli angoli
    angoloSpallaFiancoGinocchioDx = Angolo("Fianco Destro", calcolaAngolo(spalladx, fiancodx, ginocchiodx))
    angoloSpallaFiancoGinocchioSx = Angolo("Fianco Sinistro", calcolaAngolo(spallasx, fiancosx, ginocchiosx))
    angoloFiancoGinocchioCavigliaDx = Angolo("Gamba Destra", calcolaAngolo(fiancodx, ginocchiodx, cavigliadx))
    angoloFiancoGinocchioCavigliaSx = Angolo("Gamba Sinistra", calcolaAngolo(fiancosx, ginocchiosx, cavigliasx))

    listaAngoli.append(angoloSpallaFiancoGinocchioDx)
    listaAngoli.append(angoloSpallaFiancoGinocchioSx)
    listaAngoli.append(angoloFiancoGinocchioCavigliaDx)
    listaAngoli.append(angoloFiancoGinocchioCavigliaSx)

    return listaAngoli, 170


def angoliBicipiti(results, mpPose):
    listaAngoli = list()

    # ricava le coordinate dei landamrks
    spalladx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_SHOULDER.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_SHOULDER.value].y
    spallasx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_SHOULDER.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_SHOULDER.value].y

    gomitodx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_ELBOW.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_ELBOW.value].y
    gomitosx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_ELBOW.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_ELBOW.value].y

    polsodx = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_WRIST.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_WRIST.value].y
    polsosx = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_WRIST.value].x, results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_WRIST.value].y

    # calcola gli angoli
    angoloBicipiteSx = Angolo("Bicipite sinistro", calcolaAngolo(spallasx, gomitosx, polsosx))
    angoloBicipiteDx = Angolo("Bicipite Destro", calcolaAngolo(spalladx, gomitodx, polsodx))

    listaAngoli.append(angoloBicipiteDx)
    listaAngoli.append(angoloBicipiteSx)

    return listaAngoli, 160
