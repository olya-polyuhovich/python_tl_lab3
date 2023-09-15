import pack

print("deeptl module functional:")

text="hello world"
print("\nfunction TransLate: " + pack.deeptlm.TransLate(text,"en","ja"))


print("\nfunction LangDetect with parameter lang: " + pack.deeptlm.LangDetect(text,"lang"))
print("function LangDetect with parameter confidence: " + str(pack.deeptlm.LangDetect(text,"confidence")))
print("function LangDetect with parameter all: " + pack.deeptlm.LangDetect(text,"all"))

print("\nfunction CodeLang: " + pack.deeptlm.CodeLang("ja"))

print("\nfunction LanguageList with parameter screen: ")
pack.deeptlm.LanguageList("screen",text)
print("\nfunction LanguageList with parameter screen without text: ")
pack.deeptlm.LanguageList("screen")
print("\nfunction LanguageList with parameter file: ")
pack.deeptlm.LanguageList("file",text)
