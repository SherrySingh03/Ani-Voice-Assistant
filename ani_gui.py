from ani_listens import get_audio
# from tkinter import *
from mttkinter.mtTkinter import *
# from mttkinter.mtTkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from tkvideo import tkvideo
from ani_speaks import assistant_speaks
import time
import pywhatkit as kit
from text_processing import search_web, calculate_input, open_app

name = 'Specimen'
root = Tk()
root.geometry('600x1040')

root.config(background='#24273A')
root.config(background='#000000')


# video_label = Label(root, borderwidth=0)
# player = tkvideo("media\logo_3.mp4", video_label, loop=1, size=(480, 340))
# video_label.pack()
# player.play()


root.update_idletasks()

# Placeholder for video
img = Image.open('media\logo_3.png')
# img = img.resize((250, 230))
img = img.resize((820, 480))

img_tk = ImageTk.PhotoImage(img)
image_label = ctk.CTkLabel(height=340,
                           width=450,
                           text='')
image_label.place(relx=0.5, y=150, anchor='c')
image_label.configure(image=img_tk)

# root.update()
# time.sleep(2)

textbox = ctk.CTkLabel(height=50,
                       width=50,
                       text='Ani.',
                       text_font=('Terminal', 38),
                       #    text_color='#663560',
                       text_color='#2E6174',
                       fg_color='#000000')
textbox.place(x=155, y=320)

mic_bw = Image.open('media\mic_bw.png')
mic_bw = mic_bw.resize((75, 75))
mic_bw_image = ImageTk.PhotoImage(mic_bw)

mic = Image.open('media\mic.png')
mic = mic.resize((75, 75))
mic_image = ImageTk.PhotoImage(mic)

mic_label = ctk.CTkLabel(height=200, width=200, text='')
mic_label.place(x=100, y=510)
mic_label.configure(image=mic_bw_image)

assistant_box = ctk.CTkLabel(height=50,
                             width=50,
                             text='Hey there.',
                             text_font=('Helvetica', 12),
                             text_color='#663560',
                             #  text_color='#2E6174',
                             fg_color='#000000')

assistant_box.place(relx=0.5, y=430, anchor='c')


def edit_text_box(input):
    assistant_box.configure(text=input)


def change_mic(mic):
    mic_label.configure(image=mic)


def process_text(input):
    input = input.lower()
    # try:
    if 'play' in input and 'youtube' in input:
        if 'something' in input:
            base = 'What exactly do you want me to play?'
            base_txt = adjusting_base(base)
            ani_does(base, base_txt, 200)
            input = ani_listens_for_response()
            base = f'Okay. Playing {input} on YouTube.'
            base_txt = adjusting_base(base)
            ani_does(base, base_txt, 200)
            kit.playonyt(input)
            return
        input = input.replace('play', '')
        input = input.replace('on youtube', '')
        # input = input.replace('play on youtube', '')
        base = f'Okay. Playing {input} on YouTube.'
        ani_does(base, base, 200)
        kit.playonyt(input)
        return
    if 'search' in input:
        search_web(input)
        return
    elif 'who' in input:
        if 'am i' in input:
            base = f'You are {name}, I think you should always keep that in mind!'
            base_txt = adjusting_base(base)
            ani_does(base, base_txt, 200)

        if 'are you' in input:
            base = """I am Ani. Your personal assistant. I'm here to make your life easier. 
                      You can ask me to do various tasks, for instance, I can do calculations, open
                      applications and search anything on the web for you. I'm like
                      a friend, a friend who's there for you, when and whenever you
                      require assistance."""
            base_txt = adjusting_base(base)
            ani_does(base, base, 200)

        elif 'made you' in input or 'created you' in input:
            base = "I've been programmed by Sherry and just like me, he's a good friend too. And he's always there for me whenever I require his assistance."
            base_txt = adjusting_base(base)
            ani_does(base, base_txt, 200)

        elif 'is' in input:
            base = "I'm sorry, who are you talking about?"
            base_txt = adjusting_base(base)
            ani_does(base, base_txt, 200)

            input = ani_listens_for_response()
            input = input.lower()
            if input[:2] == 'sh' and input[-1] in ['y', 'i']:
                base = "Sherry? oh, words can't define the type of person " \
                    "he is. I would just like to say he's the best there is," \
                    "the best there ever was, and the best there ever will be."
                base_txt = adjusting_base(base)
                ani_does(base, base_txt, 200)
            else:
                base = f'Searching for {input} on the web.'
                base_txt = adjusting_base(base)
                search_web(input)

        else:
            base = f'Searching for {input}'
            ani_does(base, base, 200)
            search_web(input)
        return

    # elif 'great' in input or 'awesome' in input:
    #     assistant_speaks('Glad I could be of help.')

    elif 'calculate' in input.lower():
        try:
            ans = calculate_input(input)
            base = f'The result of {input} is {round(ans, 3)}'
            base_txt = adjusting_base(base)
            ani_does(base, base_txt, 200)
            return
        except:
            assistant_speaks("I am not able to understand what I"
                             "am supposed to calculate exactly. Please "
                             "try again.")
            return

    elif 'open' in input:
        base = open_app(input.lower())
        base = 'Opening ' + base[4:]
        ani_does(base, base, 200)
        return
    else:
        assistant_speaks('I can search that on the web, do you'
                         ' want me to continue?')
        ans = ani_listens_for_response()
        if 'yes' in str(ans) or 'yeah' in str(ans) or 'yep' in str(ans):
            search_web(input)
        else:
            return


def ani_does(base, base_text, time_ms):
    assistant_box.after(time_ms, edit_text_box(base_text))
    root.update()
    time.sleep(0.3)
    assistant_speaks(base)


def ani_listens_for_name():
    global name
    change_mic(mic_image)
    root.update()
    name = get_audio()
    change_mic(mic_bw_image)
    root.update()
    if name is None:
        base = "Okay then let's call you a Specimen!"
        ani_does(base, base, 200)
        name = 'Specimen'
    return name


def ani_listens_for_response():
    change_mic(mic_image)
    root.update()
    text = get_audio()
    change_mic(mic_bw_image)
    root.update()
    if text is None:
        base = 'Exiting then! Bye.'
        ani_does(base, base, 200)
        quit()
    return text


def adjusting_base(base):
    i = 27
    if len(base) > 27:
        while (i < len(base)):
            if base[i] == ' ':
                base = base[:i] + '\n' + base[i:]
                i += 27
            else:
                i += 1
        return base
    else:
        return base


def initiate():
    global name
    root.update()
    # time.sleep(0.3)
    base = 'Hey there!'
    ani_does(base, base, 500)
    # assistant_speaks('Hey there.')

    # assistant_box.after(1000, edit_text_box(base))
    # root.update()
    # time.sleep(0.5)
    # assistant_speaks(base)
    base = "Tell me, what's your name, human?"
    ani_does(base, base, 500)
    name = ani_listens_for_name()

    # name = name.lower()
    # hmni = 'hey my name is '
    # mni = 'my name is '
    # if mni in name or hmni in name:

    name = name.split()[-1]

    if name[:2].lower() == 'sh' and name[-1].lower() in ['y', 'i']:
        name = 'Sherry'
        base = 'Oh hi Sherry! Want me to open the daily routine things?'
        base_txt = adjusting_base(base)
        ani_does(base, base_txt, 300)
        ans = ani_listens_for_response()
        if ans[0].lower() == 'y':
            ani_does('On it!', 'On it!', 300)
            open_app('Apex Legends')
            kit.playonyt('Creepin')
            ani_does('Here you go!', 'Here you go!', 500)
            quit()

    base = "Well hello there, " + str(name) + '.'
    ani_does(base, base, 500)

    # assistant_box.after(2000, edit_text_box(base))
    # root.update()
    # assistant_speaks(base)
    while True:
        base = 'How can I help you?'
        ani_does(base, base, 300)
        text = ani_listens_for_response()

        if 'exit' in str(text) or 'bye' in str(text) or 'sleep' in str(text) or 'quit' in str(text):
            base = "Okay bye, " + name + '.'
            ani_does(base, base, 300)
            quit()
        else:
            process_text(text)


initiate()

root.mainloop()
