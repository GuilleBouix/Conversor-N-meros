from tkinter import *
from customtkinter import *
import pyperclip
import os


# DIRECTORIO
if getattr(sys, 'frozen', False):
    directorio_base = sys._MEIPASS
else:
    directorio_base = os.path.dirname(os.path.abspath(__file__))
icono = os.path.join(directorio_base, "icon.ico")


# VENTANA PRINCIPAL
root = Tk()
root.resizable(False,False)
root.title("Conversor de Números")
root.config(background="#141414")
if os.path.exists(icono):
    root.iconbitmap(icono)


# COLORES
color_fondo = "#141414"
color_negro = "#282828"
color_negro2 = "#191919"
color_violeta = "#230046"
color_violeta2 = "#320064"


# FRAME PRINCIPAL
main_frame = Frame(root, bg=color_fondo)
main_frame.grid(padx=50, pady=25)


# TITULO
frame_titulo = Frame(main_frame, bg=color_fondo)
frame_titulo.grid(padx=50)
lbl_titulo = CTkLabel(frame_titulo,
                   text='CONVERSOR DE NUMEROS',
                   font=('Montserrat Bold', 25),
                   fg_color=('white','#141414'))
lbl_titulo.grid()


# INGRESAR NUMERO
def validar_integer(nuevo_valor):
    # Permitir valores vacíos
    if nuevo_valor == "":
        return True
    return nuevo_valor.isdigit() or nuevo_valor == ""
validar_entero = root.register(validar_integer)
frame_entry = Frame(main_frame, bg=color_fondo)
frame_entry.grid(row=1,pady=5)
txt_numero = CTkEntry(frame_entry,
                    justify="center",
                    validate="key",
                    validatecommand=(validar_entero, "%P"),
                    width=420,
                    height=80,
                    font=('Montserrat', 25),
                    fg_color=('white',color_negro),
                    placeholder_text='Ingresar número',
                    border_width=0,
                    corner_radius=20)
txt_numero.grid(pady=5,columnspan=2)


# REALIZAR CONVERSION
btn_convertir = CTkButton(frame_entry,
                      width=420,
                      height=65,
                      text="\uf021 Convertir",
                      font=('Montserrat', 25),
                      fg_color=('white',color_violeta2),
                      hover_color=color_violeta,
                      border_width=0,
                      corner_radius=20,
                      cursor='hand2',
                      command=lambda:convertir_numero())
btn_convertir.grid(row=1,pady=10,columnspan=2)


# BINARIO
lbl_binario = Label(frame_entry,
                    text='BIN:',
                    font=('Montserrat', 12),
                    bg=color_fondo,
                    fg='white')
lbl_binario.grid(row=2,columnspan=2,sticky=W,padx=5)
txt_binario = CTkEntry(frame_entry,
                      state='readonly',
                      width=345,
                      height=60,
                      font=('Montserrat', 25),
                      fg_color=('white',color_negro2),
                      border_width=0,
                      corner_radius=20)
txt_binario.grid(row=3,pady=5)
btn_binario = CTkButton(frame_entry,
                      state='disabled',
                      width=10,
                      height=65,
                      text="\uf0c5",
                      font=('Montserrat', 25),
                      fg_color=('white',color_violeta),
                      hover_color=color_violeta,
                      border_width=0,
                      corner_radius=20,
                      command=lambda:copiar_binario())
btn_binario.grid(row=3,column=1,pady=5,padx=5)


# OCTAL
lbl_oct = Label(frame_entry,
                    text='OCT:',
                    font=('Montserrat', 12),
                    bg=color_fondo,
                    fg='white')
lbl_oct.grid(row=4,columnspan=2,sticky=W,padx=5)
txt_oct = CTkEntry(frame_entry,
                      state='readonly',
                      width=345,
                      height=60,
                      font=('Montserrat', 25),
                      fg_color=('white',color_negro2),
                      border_width=0,
                      corner_radius=20)
txt_oct.grid(row=5,pady=5)
btn_oct = CTkButton(frame_entry,
                      state='disabled',
                      width=10,
                      height=65,
                      text="\uf0c5",
                      font=('Montserrat', 25),
                      fg_color=('white',color_violeta),
                      hover_color=color_violeta,
                      border_width=0,
                      corner_radius=20,
                      command=lambda:copiar_octal())
btn_oct.grid(row=5,column=1,pady=5,padx=5)


# HEXADECIMAL
lbl_hex = Label(frame_entry,
                    text='HEX:',
                    font=('Montserrat', 12),
                    bg=color_fondo,
                    fg='white')
lbl_hex.grid(row=6,columnspan=2,sticky=W,padx=5)
txt_hex = CTkEntry(frame_entry,
                      state='readonly',
                      width=345,
                      height=60,
                      font=('Montserrat', 25),
                      fg_color=('white',color_negro2),
                      border_width=0,
                      corner_radius=20)
txt_hex.grid(row=7,pady=5)
btn_hex = CTkButton(frame_entry,
                      state='disabled',
                      width=10,
                      height=65,
                      text="\uf0c5",
                      font=('Montserrat', 25),
                      fg_color=('white',color_violeta),
                      hover_color=color_violeta,
                      border_width=0,
                      corner_radius=20,
                      command=lambda:copiar_hex())
btn_hex.grid(row=7,column=1,pady=5,padx=5)


# LIMPIAR
btn_limpiar = CTkButton(frame_entry,
                      state='disabled',
                      width=420,
                      height=65,
                      text="\uf12d Limpiar",
                      font=('Montserrat', 25),
                      fg_color=('white',color_violeta),
                      hover_color=color_violeta,
                      border_width=0,
                      corner_radius=20,
                      command=lambda:limpiar())
btn_limpiar.grid(row=8,pady=10,columnspan=2)


# FUNCIONES
def convertir_numero(Event=None):
    if txt_numero.get() == "" or txt_numero.get() == "Ingresar numero":
        txt_numero.configure(border_width=1, border_color='red')
    else:
        btn_convertir.configure(state='disabled',fg_color=('white',color_violeta))
        txt_numero.configure(border_width=0)
        
        numero = int(txt_numero.get())
        numero_bin = bin(numero)[2:]
        numero = int(txt_numero.get())
        numero_oct = oct(numero)[2:]
        numero = int(txt_numero.get())
        numero_hex = hex(numero)[2:]
        
        btn_limpiar.configure(state='normal',fg_color=('white',color_violeta2),cursor='hand2')
        btn_binario.configure(state='normal',fg_color=('white',color_violeta2),cursor='hand2')
        btn_oct.configure(state='normal',fg_color=('white',color_violeta2),cursor='hand2')
        btn_hex.configure(state='normal',fg_color=('white',color_violeta2),cursor='hand2')
        
        txt_binario.configure(state='normal', fg_color=('white',color_negro))
        txt_binario.insert(0,str(numero_bin))
        txt_binario.configure(state='readonly')
        
        txt_oct.configure(state='normal', fg_color=('white',color_negro))
        txt_oct.insert(0,str(numero_oct))
        txt_oct.configure(state='readonly')

        txt_hex.configure(state='normal', fg_color=('white',color_negro))
        txt_hex.insert(0,str(numero_hex).upper())
        txt_hex.configure(state='readonly')
        
        btn_limpiar.focus()
txt_numero.bind('<Return>', convertir_numero)

def limpiar():
    btn_convertir.configure(state='normal',fg_color=('white',color_violeta2))
    txt_numero.delete(0, END)

    txt_binario.configure(state='normal')
    txt_oct.configure(state='normal')
    txt_hex.configure(state='normal')
    txt_binario.delete(0, END)
    txt_oct.delete(0, END)
    txt_hex.delete(0, END)
    txt_binario.configure(state='readonly')
    txt_oct.configure(state='readonly')
    txt_hex.configure(state='readonly')

    txt_binario.configure(fg_color=('white',color_negro2))
    txt_oct.configure(fg_color=('white',color_negro2))
    txt_hex.configure(fg_color=('white',color_negro2))

    btn_limpiar.configure(state='disabled',fg_color=('white',color_violeta),cursor='arrow')
    btn_binario.configure(state='disabled',fg_color=('white',color_violeta),cursor='arrow')
    btn_oct.configure(state='disabled',fg_color=('white',color_violeta),cursor='arrow')
    btn_hex.configure(state='disabled',fg_color=('white',color_violeta),cursor='arrow')

    txt_numero.focus()

def copiar_binario():
    contenido_entry = txt_binario.get()
    pyperclip.copy(contenido_entry)

def copiar_octal():
    contenido_entry = txt_oct.get()
    pyperclip.copy(contenido_entry)

def copiar_hex():
    contenido_entry = txt_hex.get()
    pyperclip.copy(contenido_entry)

def lost_focus(Event):
    if(Event.widget == root):
        root.focus()
root.bind("<Button-1>", lost_focus)


# CENTRAR VENTANA
root.update_idletasks()
width = root.winfo_reqwidth()
height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f'{width}x{height}+{x}+{y-20}')


# BUCLE PRINCIPAL
root.mainloop()