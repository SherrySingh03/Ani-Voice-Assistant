import wolframalpha
from AppOpener import open, close
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pywhatkit as kit


def calculate_input(input):
    app_id = "YVEE6A-732VY737VV"
    client = wolframalpha.Client(app_id)
    indx = input.lower().split().index('calculate')
    query = input.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text
    # assistant_speaks('The answer is ' + answer)
    return answer


def search_web(input):
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver.implicitly_wait(1)
    # driver.maximize_window()
    # indx = input.lower().split().index('google')
    if 'search' in input:
        if 'google' in input:
            input = input.replace('google', "")
            input = input.replace('search for', "")
            input = input.replace('on', "")

    input = input.replace('search', "")

    # query = input.split()[indx + 1:]
    # driver.get("https://www.google.com/search?q=" + '+'.join(query))
    kit.search(input)


def open_app(input):
    # if 'opera' in input:
    #     assistant_speaks('Opening Opera GX')
    #     os.startfile(
    #         'C:/Users/Sharandeep Singh/AppData/Local/Programs/Opera GX/75.0.3969.259/opera.exe')
    #     return

    # elif 'edge' in input:
    #     assistant_speaks('Opening Microsoft Edge')
    #     os.startfile(
    #         "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    #     return
    # elif 'word' in input:
    #     assistant_speaks('Opening Microsoft Word')
    #     os.startfile(
    #         "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.exe")
    #     return
    # elif 'excel' in input:
    #     assistant_speaks('Opening Microsoft Excel')
    #     os.startfile(
    #         'C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.exe')
    #     return
    # elif 'ubisoft' in input.lower() or 'connect' in input.lower():
    #     assistant_speaks('Opening Ubisoft Connect')
    #     os.startfile(
    #         'C:/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/UbisoftConnect.exe')
    #     return
    # elif 'rainbow' in input or 'siege' in input or 'six' in input:
    #     assistant_speaks('Gaming time huh? Opening Rainbow Six Siege')
    #     os.startfile("F:/Tom Clancy's Rainbow Six Siege/RainbowSix_Vulkan.exe")
    #     return
    # elif 'python' in input or 'pycharm' in input:
    #     assistant_speaks('Coding time I see, opening Pi Charm.')
    #     os.startfile(
    #         "C:/Program Files/JetBrains/PyCharm 2021.1.1/bin/pycharm64.exe")
    #     return
    # else:
    #     assistant_speaks('Application not available')
    #     return
    app_name = input.replace("close ", "").strip()
    open(app_name, match_closest=True)
    return app_name
