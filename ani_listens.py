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

    try:
        text = r.recognize_google(audio)

        print('You: ', text)
        return text
    except:
        count += 1
        if (count == 2):
            return 'Specimen'
        else:
            assistant_speaks(
                "I was not able to interpret that, could you please try again?")
            get_audio()
