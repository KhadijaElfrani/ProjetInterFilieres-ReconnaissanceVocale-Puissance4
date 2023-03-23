from speech_recognition import Recognizer, Microphone


def reconnaissance():
    recognizer = Recognizer()
    # On enregistre le son
    with Microphone() as source:
        print("Réglage du bruit ambiant...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        recorded_audio = recognizer.listen(source)
        print("Enregistrement terminé !")

    # Reconnaissance de l'audio
    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(
            recorded_audio,
            language="fr-FR"
        )
        #print("Vous avez dit : {}".format(text))
        return format(text)

    except Exception as ex:
        print(ex)
