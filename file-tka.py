import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json

# Conexión con API para obtener las divisas
url = "https://api.exchangerate-api.com/v4/latest/0d755b7dbc-527a2f064f-s5726qD"

response = requests.get(url)
data = response.json()

def actualizar_tasa():
    if combo_divisa.get() != "Seleccione divisa":
        label_resultado["text"] = "Tasa de conversión: " + str(round(data['rates'][combo_divisa.get()], 2)))

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Convertidor de Divisas")
ventana.geometry("350x400")
ventana.configure(bg="#f2f2f2")

# Creación de widgets
etiqueta_titulo = ttk.Label(ventana, text="Convertidor de Divisas", font=("Arial", 20, "bold"))
etiqueta_titulo.pack(pady=20)

frame_entrada = ttk.Frame(ventana)
frame_entrada.pack(pady=10)

label_monto = ttk.Label(frame_entrada, text="Monto a convertir:")
label_monto.grid(column=0, row=0, padx=5, pady=5, sticky="w")

entry_monto = ttk.Entry(frame_entrada, width=20)
entry_monto.grid(column=1, row=0, padx=5, pady=5)

frame_divisa = ttk.Frame(ventana)
frame_divisa.pack(pady=10)

label_divisa = ttk.Label(frame_divisa, text="Divisa a convertir:")
label_divisa.grid(column=0, row=0, padx=5, pady=5, sticky="w")

combo_divisa = ttk.Combobox(frame_divisa, width=20, values=list(data['rates'].keys()))
combo_divisa.grid(column=1, row=0, padx=5, pady=5)
combo_divisa.set("Seleccione divisa")

button_convertir = ttk.Button(ventana, text="Convertir", command=actualizar_tasa)
button_convertir.pack(pady=10)

label_resultado = ttk.Label(ventana, text="Tasa de conversión:")
label_resultado.pack(pady=10)

# Imagen de fondo
def center_image(image, new_width, new_height):
    new_image = Image.new("RGB", (new_width, new_height))
    new_image.paste(image, ((new_width - image.width) // 2, (new_height - image.height) // 2))
    return new_image

imagen = Image.open("imagen_fondo.jpg")
imagen = imagen.resize((350, 400), Image.ANTIALIAS)
imagen = ImageTk.PhotoImage(imagen)

etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.pack()

ventana.mainloop()