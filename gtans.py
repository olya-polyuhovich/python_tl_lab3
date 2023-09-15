import pack

print("googletrans module functional:")

text="hello world"
print("\nfunction TransLate: " + pack.googletransm.TransLate(text,"en","ja"))

lan = pack.googletransm.LangDetect(text,"all")[0]
con = pack.googletransm.LangDetect(text,"all")[1]
print("\nfunction LangDetect with parameter lang: " + pack.googletransm.LangDetect(text,"lang"))
print("function LangDetect with parameter confidence: " + str(pack.googletransm.LangDetect(text,"confidence")))
print("function LangDetect with parameter all: language - " + lan + ", confidence - " + str(con))

print("\nfunction CodeLang: " + pack.googletransm.CodeLang("ja"))

print("\nfunction LanguageList with parameter screen: ")
pack.googletransm.LanguageList("screen",text)
print("\nfunction LanguageList with parameter screen without text: ")
pack.googletransm.LanguageList("screen")
print("\nfunction LanguageList with parameter file: ")
pack.googletransm.LanguageList("file",text)
