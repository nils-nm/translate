import pyperclip
import pyttsx3
from translate import Translator

# from googletrans import *
#
#
cop = ''
translator = Translator(from_lang='en', to_lang='ru')
lis = []


#
# print(translator.translate('дом'))
#

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('', 'ru')
    print(text)
    engine.say(text)
    engine.runAndWait()


while True:
    if pyperclip.paste() != cop:

        say(translator.translate(pyperclip.paste()))

        cop = pyperclip.paste()

# translator = Translator()
# result = translator.translate('hello world', src='en', dest='ru')
# print(result.text)
