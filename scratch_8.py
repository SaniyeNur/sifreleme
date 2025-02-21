from tkinter import *

pencere = Tk()
pencere.title("LogDef Sezar Aracı ")


def geriCevir(x):
    return chr(x)


def yapistir():
    global metin
    metin = giris.get(0.0, END)
    sifre = list(map(f, metin))
    cikis1.delete(0.0, END)
    cikis1.insert(INSERT, str(sifre[:-1])[1:-1])
    print("Ascii li sifre:", sifre)
    sifrelimetin = ''.join(geriCevir(i) for i in sifre)
    cikis2.delete(0.0, END)
    cikis2.insert(INSERT, str(sifrelimetin))
    print("Karakterli şifrenin metin hali:", sifrelimetin)
    cozulen = list(map(coz, sifrelimetin))
    print("Çözülen ASCII'li şifre:", cozulen)
    print("Çözülen Şifrenin Metin Hali:", ''.join(geriCevir(i) for i in cozulen))


def sifreCoz():
    global metin
    metin = giris.get(0.0, END)

    sifre = list(map(coz, metin[:-1]))
    cikis1.delete(0.0, END)
    cikis1.insert(INSERT, str(sifre)[1:-1])
    print("Ascii li sifre:", sifre)
    sifrelimetin = ''.join(geriCevir(i) for i in sifre)
    cikis2.delete(0.0, END)
    cikis2.insert(INSERT, str(sifrelimetin))
    print("Karakterli şifrenin metin hali:", sifrelimetin)
    cozulen = list(map(coz, sifrelimetin))
    print("Çözülen ASCII'li şifre:", cozulen)
    print("Çözülen Şifrenin Metin Hali:", ''.join(geriCevir(i) for i in cozulen))


def f(x):
    return ord(x) + 3


def coz(x):
    return ord(x) - 3


karsilama = Label(pencere)
karsilama.config(text=u"Sezar Şifreleme ve Kırma")
karsilama.pack()

girisMetni = Label(pencere)
girisMetni.config(text=u"Metni giriniz")
girisMetni.pack()

giris = Text(pencere)
giris.config(width=40, height=8, font="arial 12")
giris.pack()

karsilama1 = Label(pencere)
karsilama1.config(text=u"ASCII Hali")
karsilama1.pack()

cikis1 = Text(pencere)
cikis1.config(width=40, height=8, font="arial 12")
cikis1.pack()

karsilama2 = Label(pencere)
karsilama2.config(text=u"Metin Hali")
karsilama2.pack()

cikis2 = Text(pencere)
cikis2.config(width=40, height=8, font="arial 12")
cikis2.pack()

print("Sezar şifre oluşturma ve kırma")

metin = ""

hesapButon = Button(pencere)
hesapButon.config(text="Hesapla!", command=yapistir)
hesapButon.pack()

cozButon = Button(pencere)
cozButon.config(text="Şifre Çöz!", command=sifreCoz)
cozButon.pack()

mainloop()