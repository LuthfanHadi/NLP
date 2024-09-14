from textblob import Word


text = 'Tonight, showers and possibly thunderstorms are expected with a low around 64°F'


from googletrans import Translator
translator = Translator()

detect = translator.translate(text,dest='id')

print(detect.text)


txt = 'theyr'
w = Word(txt)

print(w.pluralize())
print(w.spellcheck())
print(w.correct())