from tkinter import *
from PIL import ImageTk, Image

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def button_action():
    description_label.config(text="Das Spiel wird gestartet...")

    # !!HIER WIRD DAS SPIEL GESTARTET!!

# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen (mit Copyright Symbol)
fenster.title(u'One Second Game\u00A9'.encode('latin-1'))
# Hintergrund-Farbe von Fenster
fenster.configure(background='royal blue')
# Größe des Fensters
fenster.geometry("1000x500")

# Anzeige des Logos
logo = ImageTk.PhotoImage(Image.open("Logo_1_Second_Game.png"))
logo_label = Label(image=logo)

# Starten des Spiels
description_label = Label(fenster, text="Spiel starten?", bg="black", fg="white")
description_label.config(font=('Arial', 20))

start_button = Button(fenster, text="Spiel starten", command=button_action, bg="green", fg="black")
start_button.config(font=('Arial', 10))

# Verlassen des Menüs
info_label = Label(fenster, text="Spiel verlassen?", bg="black", fg="white")
info_label.config(font=('Arial', 20))

exit_button = Button(fenster, text="Beenden", command=fenster.quit, bg="red", fg="black")
exit_button.config(font=('Arial', 10))

# Festlegen Position von Buttons und Labels
logo_label.pack()
description_label.pack(fill=X, pady=10, side=TOP)
start_button.pack(pady=10, side=TOP)
exit_button.pack(pady=10, side=BOTTOM)
info_label.pack(fill=X, pady=10, side=BOTTOM)
#exit_button.pack(pady=10, side=BOTTOM)

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()

