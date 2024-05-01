import pyautogui
import keyboard
import customtkinter
import time
import PIL
import os

with open("wah.png", "rb") as f:
    logo = PIL.Image.open(f)

a = 476 + 85
contatos = 16742
contatos_restantes = contatos - a
quantos = 0
app = customtkinter.CTk()
app.geometry("1000x600")
app.title("Bot Ultra De Whatsapp")

def encaminhar():
    if contatosinput.get() == "" or not contatosinput.get().isdigit():
        erro_texto.configure(text="Por favor, digite a quantidade de contatos.")
    else:
        erro_texto.configure(text="")

text = customtkinter.CTkLabel(app, text="Bot Ultra De Whatsapp 1.0", font=("MS Comic Sans", 40))
text.place(relx=0.5, rely=0.1, anchor="center")

contatosinputtext = customtkinter.CTkLabel(app, text="Quantidade de contatos:", font=("MS Comic Sans", 20))
contatosinputtext.place(relx=0.2, rely=0.3, anchor="center")

contatosinput = customtkinter.CTkEntry(app, placeholder_text="Digite aqui.", font=("MS Comic Sans", 20))
contatosinput.place(relx=0.2, rely=0.4, anchor="center")

encaminhara = customtkinter.CTkButton(app, text="Encaminhar", command=encaminhar, font=("MS Comic Sans", 40))
encaminhara.place(relx=0.5, rely=0.5, anchor="center")

erro_texto = customtkinter.CTkLabel(app, text="", text_color="red", font=("MS Comic Sans", 20))
erro_texto.place(relx=0.5, rely=0.6, anchor="center")

app.mainloop()