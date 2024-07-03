import speech_recognition as sr
from ani_speaks import assistant_speaks
count = 0


def get_audio():
    global count
    r = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:

        print('Speak something..')

        audio = r.listen(source, phrase_time_limit=6)
    print('Stop.')

    text = r.recognize_google(audio)

    print('You: ', text)
    count += 1
    return text
    
