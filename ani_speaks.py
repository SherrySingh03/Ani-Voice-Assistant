import pyttsx3
num = 1
engine = pyttsx3.init()
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_id)


def assistant_speaks(output):
    global num

    num += 1
    # print("Ani: ", output)

    # speak = gTTS(output, lang='en-uk', slow=False)
    # file = str(num) + '.mp3'
    # speak.save(file)

    # playsound.playsound(file, True)
    # os.remove(file)
    engine.say(output)
    engine.runAndWait()
