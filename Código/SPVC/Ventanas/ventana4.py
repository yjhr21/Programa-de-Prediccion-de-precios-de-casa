import tkinter as tk
from PIL import ImageTk, Image
import os

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ancho_ventana = 800
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

# Cargar la imagen de la izquierda
ruta_izquierda = os.path.join("Fondos", "image4.jpg")
imagen_izquierda = Image.open(ruta_izquierda)
imagen_izquierda = imagen_izquierda.resize((400, alto_ventana))
imagen_izquierda = ImageTk.PhotoImage(imagen_izquierda)

# Crear el lienzo para mostrar la imagen de la izquierda
lienzo_izquierda = tk.Canvas(ventana, width=400, height=alto_ventana, highlightthickness=0, bg="#030918")
lienzo_izquierda.place(x=0, y=0)
lienzo_izquierda.create_image(0, 0, anchor="nw", image=imagen_izquierda)

# Agregar el logotipo
ruta_logo = os.path.join("Fondos", "logo2.png")
logotipo_img = Image.open(ruta_logo)
logotipo_img = logotipo_img.resize((100, 100))
logotipo = ImageTk.PhotoImage(logotipo_img)
logotipo_label = tk.Label(ventana, image=logotipo, bg="#030918")
logotipo_label.place(x=410, y=30)

# Agregar el título
titulo_label = tk.Label(ventana, text="ANÁLISIS DE DATOS", font=("Arial", 24, "bold"), fg="#51d1f6", bg="#030918", anchor="w", justify="left")
titulo_label.place(x=410, y=180)

# Funciones para los botones
def mostrar_mapa_de_calor():
    print("Mostrando mapa de calor")

def mostrar_histograma():
    print("Mostrando histograma")

def mostrar_grafico_de_barras():
    print("Mostrando gráfico de barras")
    
def abrir_mapabarras():
    ventana.withdraw()
    ruta_barras = os.path.join("Ventanas", "mapabarras.py")
    os.system(f"python {ruta_barras}")
    ventana.destroy()   
    
def abrir_mapacalor():
    ventana.withdraw()
    ruta_calor = os.path.join("Ventanas", "mapadecalor.py")
    os.system(f"python {ruta_calor}")
    ventana.destroy()  

def abrir_mapahistograma():
    ventana.withdraw()
    ruta_histograma = os.path.join("Ventanas", "mapahistograma.py")
    os.system(f"python {ruta_histograma}")
    ventana.destroy()   

# Crear los botones
boton_mapa_de_calor = tk.Button(ventana, text="Mapa de calor", font=("Arial", 16), command= abrir_mapacalor, width=20)
boton_mapa_de_calor.place(x=410, y=250)

boton_histograma = tk.Button(ventana, text="Histograma", font=("Arial", 16), command=abrir_mapahistograma, width=20)
boton_histograma.place(x=410, y=300)

boton_grafico_de_barras = tk.Button(ventana, text="Gráfico de barras", font=("Arial", 16), command=abrir_mapabarras, width=20)
boton_grafico_de_barras.place(x=410, y=350)

# Agregar el botón "Atras"
def abrir_ventana3():
    ventana.withdraw()
    ruta_ventana3 = os.path.join("Ventanas", "ventana3.py")
    os.system(f"python {ruta_ventana3}")
    ventana.destroy()

def destruir():
    ventana.withdraw()
    ventana.destroy()

siguiente_btn = tk.Button(ventana, text="Atras", font=("Arial", 16, "bold"), command=abrir_ventana3)
siguiente_btn.place(x=410, y=550)

siguiente_bt = tk.Button(ventana, text="Finalizar", font=("Arial", 16, "bold"),command=destruir)
siguiente_bt.place(x=500, y=550)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
