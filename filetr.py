import os
import nltk
import pack

try:
    f = open("conf.txt", "r")
    alist = f.read().splitlines()

    name=alist[0]
    lang=alist[1]
    set=alist[2]
    chars=int(alist[3])
    word=int(alist[4])
    sent=int(alist[5])
except FileNotFoundError:
    print('configuration file does not exist')
except:
    print("an error occurred while reading configuration file")


try:
    file_size = os.path.getsize(name)

    f=open(name,'r')
    text=f.read()

    num_sent = len(nltk.sent_tokenize(text))
    num_words = len(text.split())
    num_chars = len(text)

    print("file name: " + name + ", \nsize: " + str(file_size) + " kb")
    print("number of characters: " + str(num_chars) + ", words: " + str(num_words) + ", sentences: " + str(num_sent))
except FileNotFoundError:
    print('file does not exist')
except:
    print("an error occurred while reading the file")


if num_chars>chars:
    tl_str= text[:chars]
elif num_words>word:
    tl_str = " ".join(text.split()[:word])
elif num_sent>sent:
    tl_str=" ".join(nltk.sent_tokenize(text)[:sent])
else:
    tl_str=text

result=pack.deeptlm.TransLate(tl_str,"auto",lang)


try:
    if set=="screen":
        print("\ntranslated to " + lang + " - " + pack.deeptlm.CodeLang(lang))
        print("\n"+result)
    elif set=="file":
        new_file="translated_"+lang+".txt"
        with open(new_file, 'w', encoding="utf-8") as fp:
            fp.write(result)
    else:
        print("\ninvalid set parameter in configuration file")
except:
    print("an error occurred while outputing translation")
else:
    print("\nok")



