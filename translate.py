from googletrans import Translator

translator = Translator()
print("Translate EN => FR")
text_to_translate = str(input("Enter text: "))

translated_text = translator.translate(text_to_translate, src="en", dest="fr")

print(translated_text.text)
