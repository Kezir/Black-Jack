import karta
import tkinter as tkr
from PIL import Image, ImageTk
from pygame import mixer

root = tkr.Tk()
root.configure(bg="white")
mixer.init()
mixer.music.load(karta.resource_path('Assets/Anatu - Bleach.mp3'))
mixer.music.play(loops=-1)

board = Image.open(karta.resource_path("Assets/board.png"))
board = board.resize((610, 510), Image.ANTIALIAS)
board_render = ImageTk.PhotoImage(board)
root.resizable(0,0)

def menu(bilans):
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()
    # print(nr1,nr2)

    img = tkr.Label(root, image=board_render)
    img.pack()

    button1 = tkr.Button(root, text="Start", font=30, bd=8, bg="white", relief="raised",command=lambda: ustawienia_graczy(1,bilans))
    button1.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.3, anchor='n')

    button2 = tkr.Button(root, text="Ustawienia", font=30, bd=8, bg="white", relief="raised",command = ustawienia)
    button2.place(relx=0.5, rely=0.65, relheight=0.1, relwidth=0.3, anchor='n')

def ustawienia_graczy(ilosc,bilans):
    list = root.place_slaves()
    for l in list:
        l.destroy()

    dodaj_gracza = tkr.Button(root, text="Dodaj gracza", font=30,bd=8, bg="white",relief = "raised", command=lambda: ustawienia_graczy(ilosc+1,bilans))
    dodaj_gracza.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    usun_gracza = tkr.Button(root, text="Usun gracza", font=30, bd=8, bg="white",relief = "raised",command=lambda: ustawienia_graczy(ilosc - 1,bilans))
    usun_gracza.place(relx=0.2, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    rozpoczecie = tkr.Button(root, text="Start", font=30,bd=8, bg="white",relief = "raised", command=lambda: tworzenie_gry(ilosc,0,bilans))
    rozpoczecie.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    if ilosc == 1:
        gracz1 = tkr.Label(root, text="gracz1", font=30,bd=8, bg="white",relief = "raised")
        gracz1.place(relx=0.17, rely=0.57, relheight=0.1, relwidth=0.2, anchor='n')
        usun_gracza.config(state = 'disabled')
    elif ilosc == 2:
        gracz1 = tkr.Label(root, text="gracz1", font=30,bd=8, bg="white",relief = "raised")
        gracz1.place(relx=0.17, rely=0.57, relheight=0.1, relwidth=0.2, anchor='n')

        gracz2 = tkr.Label(root, text="gracz2", font=30,bd=8, bg="white",relief = "raised")
        gracz2.place(relx=0.5, rely=0.65, relheight=0.1, relwidth=0.2, anchor='n')
    elif ilosc == 3:
        gracz1 = tkr.Label(root, text="gracz1", font=30,bd=8, bg="white",relief = "raised")
        gracz1.place(relx=0.17, rely=0.57, relheight=0.1, relwidth=0.2, anchor='n')
        dodaj_gracza.config(state = 'disabled')

        gracz2 = tkr.Label(root, text="gracz2", font=30,bd=8, bg="white",relief = "raised")
        gracz2.place(relx=0.5, rely=0.65, relheight=0.1, relwidth=0.2, anchor='n')

        gracz3 = tkr.Label(root, text="gracz3", font=30,bd=8, bg="white",relief = "raised")
        gracz3.place(relx=0.83, rely=0.57, relheight=0.1, relwidth=0.2, anchor='n')

def ustawienia():
    list = root.place_slaves()
    for l in list:
        l.destroy()

    text = tkr.Label(root, text="Stan poczatkowy", font=30, bd=8, bg="white", relief="raised")
    text.place(relx=0.2, rely=0.1, relheight=0.1, relwidth=0.3, anchor='n')

    bilans_nr = tkr.Spinbox(root,from_= 10, to_=1000,increment=10, bd=8, bg="white", relief="raised")
    bilans_nr.place(relx=0.45, rely=0.1, relheight=0.1, relwidth=0.1, anchor='n')

    ok = tkr.Button(root, text="Zapisz", font=30, bd=8, bg="white", relief="raised",command = lambda : menu([int(bilans_nr.get()),int(bilans_nr.get()),int(bilans_nr.get())]))
    ok.place(relx=0.8, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    sound = tkr.Label(root, text="Dzwiek ", font=30, bd=8, bg="white", relief="raised")
    sound.place(relx=0.2, rely=0.2, relheight=0.1, relwidth=0.3, anchor='n')

    sound_on = tkr.Button(root, text="ON", font=30, bd=8, bg="white", relief="raised",command=lambda:play(1))
    sound_on.place(relx=0.45, rely=0.2, relheight=0.1, relwidth=0.1, anchor='n')

    sound_off = tkr.Button(root, text="OFF", font=30, bd=8, bg="white", relief="raised", command=lambda:play(2))
    sound_off.place(relx=0.55, rely=0.2, relheight=0.1, relwidth=0.1, anchor='n')

def play(option):
    if option == 1:
        mixer.music.unpause()
    elif option == 2:
        mixer.music.pause()

def tworzenie_gry(ilosc_graczy,ilosc_AI,bilans):
    game = karta.start(ilosc_graczy,bilans)
    x = [70,270,470]
    y = [250,270,250]
    for i in range(len(game.players)):
        game.players[i].pozycja = [x[i],y[i]]
    start(1, game)

def kontynuacja_gry(ilosc_graczy,bilans,pozycja):
    game = karta.start(ilosc_graczy,bilans)
    j = 0
    for i in game.players:
        i.pozycja = pozycja[j]
        j+=1
    for i in game.players:
        if i.bilans <= 0:
            game.players.remove(i)
            ilosc_graczy -= 1
        else:
            i.bilans = i.bilans - 10
    if not game.players:
        menu([10,10,10])
    else:
        start(1,game)

def licz(game):

    for i in game.players:
        if i.suma == 21:
            i.bilans += 30
        elif i.suma > game.krupier.suma and i.suma < 21:
            i.bilans += 20
        elif game.krupier.suma > 21 and i.suma < 21:
            i.bilans += 20
        elif game.krupier.suma == 21 and i.suma == 21:
            i.bilans += 10

    for i in game.players:
        if i.bilans < 10:
            i.alive = False


def start(tura,game):
    board = Image.open(karta.resource_path("Assets/board.png"))
    board = board.resize((610, 510), Image.ANTIALIAS)
    temp2 = 260
    k = 70
    list = root.place_slaves()
    for l in list:
        l.destroy()
    list = root.pack_slaves()
    for l in list:
        l.destroy()

    for i in game.players:
        x, y = i.pozycja
        for j in i.reka:
            card = Image.open(j.image)
            board.paste(card, (x, y), card)
            x = x+30
        tkimage = ImageTk.PhotoImage(board)

    if game.krupier.tura == 0:
        card1 = Image.open(game.krupier.image)
        card2 = Image.open(game.krupier.reka[0].image)
        board.paste(card1, (260,70),card1)
        board.paste(card2, (290,70),card2)
        tkimage = ImageTk.PhotoImage(board)
    elif game.krupier.tura == 1:
        for i in game.krupier.reka:
            card = Image.open(i.image)
            board.paste(card, (temp2, k), card)
            temp2 = temp2+30
        tkimage = ImageTk.PhotoImage(board)

    join = tkr.Label(root, image=tkimage)
    join.image = tkimage
    join.pack()

    labelred = tkr.Label(root, font=20, borderwidth=5, bd=8, bg="red", relief="raised")
    gracz = 0
    if tura == 1:
        gracz = game.players[0]
        if game.krupier.tura == 0:
            if gracz.pozycja[0]==70:
                labelred.place(relx=0.1, rely=0.7, relheight=0.05, relwidth=0.17, anchor='w')
            elif gracz.pozycja[0]==270:
                labelred.place(relx=0.43, rely=0.75, relheight=0.05, relwidth=0.17, anchor='w')
            elif gracz.pozycja[0]==470:
                labelred.place(relx=0.76, rely=0.7, relheight=0.05, relwidth=0.17, anchor='w')
    elif tura == 2 and len(game.players) >= 2:
        gracz = game.players[1]
        if gracz.pozycja[0]==270:
            labelred.place(relx=0.43, rely=0.75, relheight=0.05, relwidth=0.17, anchor='w')
        elif gracz.pozycja[0]==470:
            labelred.place(relx=0.76, rely=0.7, relheight=0.05, relwidth=0.17, anchor='w')
    elif tura == 3 and len(game.players) == 3:
        gracz = game.players[2]
        labelred.place(relx=0.76, rely=0.7, relheight=0.05, relwidth=0.17, anchor='w')
    else:
        game.krupier.tura = 1
        tura = 1
        licz(game)
        start(tura,game)

    for i in game.players:
        if i.pozycja[0]==70:
            zmiennax = 0.1
            zmiennay = 0.75
        elif i.pozycja[0]==270:
            zmiennax = 0.43
            zmiennay = 0.8
        elif i.pozycja[0]==470:
            zmiennax = 0.76
            zmiennay = 0.75
        labelmoney = tkr.Label(root, text=i.bilans, font=20, borderwidth=5,bd=5, bg="white", relief="raised")
        labelmoney.place(relx=zmiennax, rely=zmiennay, relheight=0.05, relwidth=0.17, anchor='w')


    dodaj_karte = tkr.Button(root, text="Dodaj karte", font=30,bd=8, bg="white", relief="raised", command=lambda: dodaj(gracz,game,tura))
    dodaj_karte.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

    zakoncz_ture = tkr.Button(root, text="Zakoncz ture", font=30, bd=8, bg="white", relief="raised",command=lambda: end_turn(tura,game))
    zakoncz_ture.place(relx=0.7, rely=0.85, relheight=0.1, relwidth=0.3, anchor='n')

def dodaj(gracz,game,tura):
    if game.krupier.tura == 0:
        gracz.dodaj_karte(game.talia)
    start(tura,game)

def end_turn(tura,game):
    if game.krupier.tura == 0:
        start(tura+1,game)
    else:
        tab = []
        pozycja = []
        for i in game.players:
            tab.append(i.bilans)
            pozycja.append(i.pozycja)
        kontynuacja_gry(len(game.players),tab,pozycja)

menu([10,10,10])

root.mainloop()
