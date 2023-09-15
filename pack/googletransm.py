import googletrans as gt


def TransLate(text:str,
              src:str,
              dest:str):
    """translator"""
    try:
        tl = gt.Translator().translate(text, dest=dest, src=src)
        return tl.text

    except:
        print("an error occurred in TransLate function")



def LangDetect(text:str,
               set:str="all"):
    """detect language"""
    try:
        result=gt.Translator().detect(text)
        if set=="lang":
            return result.lang
        elif set=="confidence":
            return result.confidence
        elif set=="all":
            return result.lang, result.confidence
    except:
        print("an error occurred in LangDetect function")

def CodeLang(lang:str):
    """get language name or code"""
    try:
        if lang in gt.LANGUAGES:
            sourcelang = gt.LANGUAGES[lang]
        else:
            sourcelang = list(gt.LANGUAGES.keys())[list(gt.LANGUAGES.values()).index(lang)]
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
                for key, value in gt.LANGUAGES.items():
                    i=i+1
                    print("{:<5} {:<30} {:<10}".format(i,value, key))
                print("-" * 50)
            else:
                print("{:<5} {:<30} {:<15} {:<15}".format("num", "language", "code", "text"))
                print("-" * 60)
                for key, value in gt.LANGUAGES.items():
                    i = i + 1
                    print("{:<5} {:<30} {:<10} {:<15}".format(i, value, key, TransLate(text, "auto", key)))
                    """обмеження щоб не чекати поки виконається функція перекладу для всіх мов
                    на моєму комп'ютері це було дуже довго :_)"""
                    if i == 10:
                        break
                print("-" * 60)

        elif out=="file":
            with open('langlist_gt.txt','w',encoding="utf-8") as fp:
                for key, value in gt.LANGUAGES.items():
                    i=i+1
                    if text==" ":
                        newstr = str(i) + " " + value + " "*5 + key +"\n"
                        fp.write(newstr)
                    else:
                        newstr = str(i) + " " + value + " "*5 + key + " "*5 + TransLate(text,"auto", key) +"\n"
                        fp.write(newstr)
                        """обмеження щоб не чекати поки виконається функція перекладу для всіх мов"""
                        if i==10:
                            break
    except:
        print("an error occurred in LanguageList function")
    else:
        print("ok")
