# import pyttsx3
# import speech_recognition as sr
# import playsound
# from gtts import gTTS
# import os
# import pywhatkit as kit

# num = 1
# engine = pyttsx3.init()
# voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
# engine.setProperty('voice', voice_id)


# def assistant_speaks(output):
#     global num

#     num += 1
#     print("Ani: ", output)

#     # speak = gTTS(output, lang='en-uk', slow=False)
#     # file = str(num) + '.mp3'
#     # speak.save(file)

#     # playsound.playsound(file, True)
#     # os.remove(file)
#     engine.say(output)
#     engine.runAndWait()


# def get_audio():
#     r = sr.Recognizer()
#     audio = ''

#     with sr.Microphone() as source:

#         print('Speak something..')

#         audio = r.listen(source, phrase_time_limit=5)
#     print('Stop.')

#     try:
#         text = r.recognize_google(audio)

#         print('You: ', text)
#         return text
#     except:

#         assistant_speaks(
#             "I was not able to interpret that, could you please try again?")
#         return 0


# def process_text(input):
#     input = input.lower()
#     # try:
#     if 'play' in input and 'youtube' in input:
#         if 'something' in input:
#             assistant_speaks('What exactly do you want me to play?')
#             input = get_audio()
#             assistant_speaks(f'Okay. Playing {input} on YouTube.')
#             kit.playonyt(input)
#             return
#         input = input.replace('play', '')
#         input = input.replace('on youtube', '')
#         # input = input.replace('play on youtube', '')
#         assistant_speaks(f'Okay. Playing {input} on YouTube.')
#         kit.playonyt(input)
#         return
#     if 'search' in input:
#         search_web(input)
#         return
#     elif 'who are you' in input or 'introduce yourself' in input:
#         speak = "I am Ani. Your personal assistant. I'm here to make your life easier. You can ask me to do " \
#                 "various tasks, for instance, I can do calculations, open " \
#                 "applications and search anything on the web for you. I'm like " \
#                 "a friend, a friend who's there for you, when and whenever you " \
#                 "require assistance."
#         assistant_speaks(speak)
#         return
#     elif 'who made you' in input or 'created you' in input:
#         speak = "I've been programmed by Sherry and just like me, he's a good friend too. And he's always there for me whenever I require his assistance."
#         assistant_speaks(speak)
#         return
#     elif 'sherry' in input or 'shetty' in input:
#         speak = "Sherry? oh, words can't define the type of person " \
#                 "he is. I would just like to say he's the best there is," \
#                 "the best there ever was and the best there everwillbe."
#         assistant_speaks(speak)
#         return
#     elif 'great' in input or 'awesome' in input:
#         assistant_speaks('Glad I could be of help.')
#     elif 'calculate' in input.lower():
#         try:
#             app_id = "YVEE6A-732VY737VV"
#             client = wolframalpha.Client(app_id)

#             indx = input.lower().split().index('calculate')
#             query = input.split()[indx + 1:]
#             res = client.query(' '.join(query))
#             answer = next(res.results).text
#             assistant_speaks('The answer is ' + answer)
#             return
#         except:
#             assistant_speaks("I am not able to understand what I"
#                              "am supposed to calculate exactly. Please "
#                              "try again.")
#             return
#     elif 'open' in input:
#         open_app(input.lower())
#     else:
#         assistant_speaks('I can search that on the web, do you'
#                          ' want me to continue?')
#         ans = get_audio()
#         if 'yes' in str(ans) or 'yeah' in str(ans) or 'yep' in str(ans):
#             search_web(input)
#         else:
#             return
# # except:

#     #     assistant_speaks("I'm sorry, I could not understand that, do you want "
#     #                      "me to search the web?")
#     #     ans = get_audio()
#     #     if 'yes' in str(ans) or 'yeah' in str(ans):
#     #         search_web(input)


# def search_web(input):
#     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     driver.implicitly_wait(1)
#     driver.maximize_window()

#     if 'youtube' in input.lower():
#         assistant_speaks('Opening in YouTube.')
#         indx = input.lower().split().index('youtube')
#         query = input.split()[indx + 1:]
#         driver.get(
#             'https://www.youtube.com/results?search_query=' + '+'.join(query))
#         return
#     if 'amazon' in input.lower():
#         assistant_speaks('Searching in Amazon')
#         indx = input.lower().split().index('amazon')
#         query = input.split()[indx + 1:]
#         driver.get('https://www.amazon.in/s?k=' + '+'.join(query))
#         return
#     else:

#         if 'google' in input.lower():
#             assistant_speaks('Searching on google.')
#             indx = input.lower().split().index('google')
#             query = input.split()[indx + 1:]
#             driver.get("https://www.google.com/search?q=" + '+'.join(query))

#         elif 'search' in input:
#             indx = input.lower().split().index('search')
#             query = input.split()[indx + 1:]
#             driver.get("https://www.google.com/search?q=" + '+'.join(query))
#         else:

#             driver.get("https://www.google.com/search?q=" +
#                        '+'.join(input.split()))
#         return


# def open_app(input):
#     if 'opera' in input:
#         assistant_speaks('Opening Opera GX')
#         os.startfile(
#             'C:/Users/Sharandeep Singh/AppData/Local/Programs/Opera GX/75.0.3969.259/opera.exe')
#         return

#     elif 'edge' in input:
#         assistant_speaks('Opening Microsoft Edge')
#         os.startfile(
#             "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
#         return
#     elif 'word' in input:
#         assistant_speaks('Opening Microsoft Word')
#         os.startfile(
#             "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.exe")
#         return
#     elif 'excel' in input:
#         assistant_speaks('Opening Microsoft Excel')
#         os.startfile(
#             'C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.exe')
#         return
#     elif 'ubisoft' in input.lower() or 'connect' in input.lower():
#         assistant_speaks('Opening Ubisoft Connect')
#         os.startfile(
#             'C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/UbisoftConnect.exe')
#         return
#     elif 'rainbow' in input or 'siege' in input or 'six' in input:
#         assistant_speaks('Gaming time huh? Opening Rainbow Six Siege')
#         os.startfile("F:/Tom Clancy's Rainbow Six Siege/RainbowSix_Vulkan.exe")
#         return
#     elif 'python' in input or 'pycharm' in input:
#         assistant_speaks('Coding time I see, opening Pi Charm.')
#         os.startfile(
#             "C:/Program Files/JetBrains/PyCharm 2021.1.1/bin/pycharm64.exe")
#         return
#     else:
#         assistant_speaks('Application not available')
#         return


# def initiate():
#     assistant_speaks("Tell me, what's your name, human?")
#     name = 'Human'
#     # noinspection PyRedeclaration
#     name = get_audio()
#     name = name.lower()
#     hmni = 'hey my name is '
#     mni = 'my name is '
#     if mni in name:
#         name = name.replace(mni, '')
#     elif hmni in name:
#         name = name.replace(hmni, '')
#     assistant_speaks("Well hello there, " + str(name) + '.')
#     if str(name).lower() == 'sherry' or str(name).lower() == 'shetty' or str(name).lower() == 'shady' or str(
#             name).lower() == 'sharon' or str(name).lower() == 'shity':
#         name = 'Sherry'
#         assistant_speaks(
#             'Oh hi Sherry! Want me to open the daily routine things?')
#         ans = get_audio()
#         if str(ans).lower() == 'yeah' or str(ans).lower() == 'yes':
#             assistant_speaks('On it')
#             open_app('opera')
#             open_app('ubisoft')
#             open_app('python')
#             quit()

#         else:
#             while True:
#                 assistant_speaks('How can I help you?')
#                 text = str(get_audio()).lower()

#                 if text == 0:
#                     continue
#                 if 'exit' in str(text) or 'bye' in str(text) or 'sleep' in str(text) or 'quit' in str(text):
#                     assistant_speaks("Okay bye, " + name + '.')
#                     break
#                 else:
#                     process_text(text)
#     else:
#         while True:

#             assistant_speaks('How can I help you?')
#             text = str(get_audio()).lower()

#             if text == 0:
#                 continue
#             if 'exit' in str(text) or 'bye' in str(text) or 'sleep' in str(text) or 'quit' in str(text):
#                 assistant_speaks("Okay bye, " + name + '.')
#                 break
#             else:
#                 process_text(text)
