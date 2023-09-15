import deep_translator as dt
import detectlanguage

langlist = dt.GoogleTranslator().get_supported_languages(as_dict=True)

def TransLate(text : str,
              scr : str,
              dest : str):
    """translator"""
    try:
        tl = dt.GoogleTranslator(source=scr, target=dest).translate(text=text)
        return tl
    except:
        print("an error occurred in TransLate function")


def LangDetect(text : str,
               set : str="all"):
    """detect language"""
    try:
        detectlanguage.configuration.api_key = "613d80890fceafba4e076c51f6f1dbf2"
        result = detectlanguage.detect(text)
        if set=="lang":
            lang= [sub['language'] for sub in result]
            return lang[0]
        elif set=="confidence":
            con= [sub['confidence'] for sub in result]
            return con[0]
        elif set=="all":
            return str(result[0])
    except:
        print("an error occurred in LangDetect function")


def CodeLang(lang : str):
    """get language name or code"""
    try:
        if lang in langlist:
            sourcelang = langlist[lang]
        else:
            sourcelang = list(langlist.keys())[list(langlist.values()).index(lang)]
        return sourcelang
    except:
        print("an error occurred in CodeLang function")

def LanguageList(out:str,
                 text:str=" "):
    """get language list"""
    try:
        i=0
        if out=="screen":
            if text == " ":
                print("{:<5} {:<30} {:<15}".format("num","language", "code"))
                print("-" * 50)
                for key, value in langlist.items():
                    i=i+1
                    print("{:<5} {:<30} {:<10}".format(i,key, value))
                print("-" * 50)
            else:
                print("{:<5} {:<30} {:<15} {:<15}".format("num", "language", "code", "text"))
                print("-" * 60)
                for key, value in langlist.items():
                    i = i + 1
                    print("{:<5} {:<30} {:<10} {:<15}".format(i, key, value, TransLate(text, "auto", key)))
                    """обмеження щоб не чекати поки виконається функція перекладу для всіх мов
                    на моєму комп'ютері це було дуже довго :_)"""
                    if i == 10:
                        break
                print("-" * 60)

        elif out=="file":
            with open('langlist_dt.txt','w',encoding="utf-8") as fp:
                for key, value in langlist.items():
                    i=i+1
                    if text==" ":
                        newstr = str(i) + " " + key + " "*5 + value +"\n"
                        fp.write(newstr)
                    else:
                        newstr = str(i) + " " + key + " "*5 + value + " "*5 + TransLate(text,"auto", key) +"\n"
                        fp.write(newstr)
                        """обмеження щоб не чекати поки виконається функція перекладу для всіх мов"""
                        if i==10:
                            break
    except:
        print("an error occurred in LanguageList function")
    else:
        print("ok")
