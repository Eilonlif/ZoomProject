import speech_recognition as sr
from playsound import playsound


def playHere(fileIndex):
    playsound(f'Present/{str(fileIndex)}.mp3')


def detectWho(audio, names):
    for i in range(len(names)):
        for alternativeName in names[i]:
            if alternativeName.lower() in audio.lower():
                return i
    print("Didn't match any name")
    return -1


def devices():
    return "Devices name list:", sr.Microphone.list_microphone_names()


def listen(sensitivity, adjustTime):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)

    SnowBoyPath = "/Users/eilonlif/PycharmProjects/zoom/snobo_repo/examples/Python3/"
    SnowboyRecordingsPath = ["/Users/eilonlif/PycharmProjects/zoom/snobo/Eilon.pmdl", "/Users/eilonlif/PycharmProjects/zoom/snobo/idan.pmdl"]

    with mic as source:
        r.adjust_for_ambient_noise(source, duration=adjustTime)
        print(f"Current energy threshold: {r.energy_threshold}")

        print("Listening for sentence: ")
        audio = r.listen(source, snowboy_configuration=(SnowBoyPath, SnowboyRecordingsPath), sensetivity=str(sensitivity))
        print("Sentence recognized... ")

    result = r.recognize_google(audio)
    print(f"Sentence result: {result}")

    whoIndex = detectWho(result, [["eilon", "ilan", "alone", "Aiden", "Pilon"],
                                  ["idan", "Ethan", "Eden"]])
    try:
        playHere(whoIndex)
    except OSError as err:
        print(err)


# listen(4, 2)

