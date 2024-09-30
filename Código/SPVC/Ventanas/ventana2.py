import tkinter as tk
from PIL import ImageTk, Image
import os

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ancho_ventana = 830
alto_ventana = 600

# Establecer el título de la ventana
ventana.title("Sistema de predicción del valor de casas")

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2

# Establecer la posición y tamaño de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Establecer el color de fondo azul oscuro
ventana.configure(bg="#030918")

# Cargar la imagen de fondo
ruta_fondo = os.path.join("Fondos", "image2.jpg")
fondo_img = Image.open(ruta_fondo)
fondo_img = fondo_img.resize((ancho_ventana // 2, alto_ventana))
fondo = ImageTk.PhotoImage(fondo_img)

# Crear el lienzo para mostrar la imagen de fondo
lienzo = tk.Canvas(ventana, width=ancho_ventana // 2, height=alto_ventana, highlightthickness=0)
lienzo.place(x=0, y=0)
lienzo.create_image(0, 0, anchor="nw", image=fondo)

# Agregar el logotipo
ruta_logo = os.path.join("Fondos", "logo.png")
logotipo_img = Image.open(ruta_logo)
logotipo_img = logotipo_img.resize((100, 100))
logotipo = ImageTk.PhotoImage(logotipo_img)
logotipo_label = tk.Label(ventana, image=logotipo, bg="#030918")
logotipo_label.place(x=ancho_ventana // 2 + 50, y=50)

# Agregar el título
titulo_label = tk.Label(ventana, text="SOFTWARE", font=("Arial", 24, "bold"), fg="#51d1f6", bg="#030918", anchor="w", justify="left")
titulo_label.place(x=ancho_ventana // 2 + 50, y=200)

# Agregar el texto
texto_label = tk.Label(ventana, text="Sistema eficiente y preciso que permita estimar\ncon mayor exactitud los precios de las casas\nen el mercado inmobiliario.\nEl sistema se enfocará en utilizar análisis\nde datos y técnicas predictivas para proporcionar\nestimaciones confiables\n\nUTILIZA EL PROGRAMA A CONTINUACIÓN", font=("Georgia", 12), fg="white", bg="#030918", anchor="w", justify="left")
texto_label.place(x=ancho_ventana // 2 + 50, y=250)

# Agregar el botón "Siguiente"
def abrir_ventana3():
    ventana.withdraw()
    ruta_ventana3 = os.path.join("Ventanas", "ventana3.py")
    os.system(f"python {ruta_ventana3}")
    ventana.destroy()
    
siguiente_btn = tk.Button(ventana, text="Siguiente", font=("Arial", 16, "bold"), command=abrir_ventana3)
siguiente_btn.place(x=ancho_ventana // 2 + 50, y=450)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()