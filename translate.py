from googletrans import Translator

translator = Translator()
txt = str(input("Enter text: "))
output = translator.Translator(txt, dest='en')

print(output.text)
