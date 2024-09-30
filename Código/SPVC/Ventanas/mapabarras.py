import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image
import os

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ancho_ventana = 800
alto_ventana = 650

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

# Título
titulo_label = tk.Label(ventana, text="GRÁFICO DE BARRAS", font=("Arial", 20, "bold"), fg="white", bg="#030918")
titulo_label.pack(pady=10)

def abrir_ventana4():
    # Ruta del archivo a destruir
    archivo_a_destruir = "grafico.png"

    # Verificar si el archivo existe antes de destruirlo
    if os.path.exists(archivo_a_destruir):
        os.remove(archivo_a_destruir)
    ventana.withdraw()
    ruta_ventana4 = os.path.join("Ventanas", "ventana4.py")
    os.system(f"python {ruta_ventana4}")
    ventana.destroy()

boton_atras = tk.Button(ventana, text="Atras", font=("Arial", 16, "bold"), command=abrir_ventana4)
boton_atras.place(x=10, y=10)

# Leer el dataset
datos = pd.read_csv("dataset_limpio.csv")

# Campos a graficar
campos = ["Habitaciones", "Banios", "Pisos", "Carretera", "Huespedes", "Sotano", "Calefaccion", "AC", "Estacionamiento", "Preferencial", "Mobiliario"]

# Variables para el control de imágenes
imagen_actual = 0
imagen_label = tk.Label(ventana)
imagen_label.pack()


def graficar_siguiente():
    global imagen_actual
    if imagen_actual < len(campos) - 1:
        imagen_actual += 1
    else:
        imagen_actual = 0
    graficar_imagen()


def graficar_anterior():
    global imagen_actual
    if imagen_actual > 0:
        imagen_actual -= 1
    else:
        imagen_actual = len(campos) - 1
    graficar_imagen()


def graficar_imagen():
    campo_actual = campos[imagen_actual]
    
    # Crear la figura y el eje
    figure, ax = plt.subplots(figsize=(6, 4))
    
    if campo_actual in ["Carretera", "Huespedes", "Sotano", "Calefaccion", "AC", "Preferencial"]:
        x = [0, 1]
        etiquetas = ["No", "Sí"]
        frecuencias = [datos[campo_actual].value_counts().get(0, 0), datos[campo_actual].value_counts().get(1, 0)]
    elif campo_actual == "Mobiliario":
        x = [0, 1, 2]
        etiquetas = ["Amueblado", "Semi-amueblado", "Sin amueblar"]
        frecuencias = [datos[campo_actual].value_counts().get(0, 0), datos[campo_actual].value_counts().get(1, 0), datos[campo_actual].value_counts().get(2, 0)]
    else:
        # Calcular las frecuencias
        frecuencias = datos[campo_actual].value_counts().sort_index()
        x = range(len(frecuencias))
        etiquetas = frecuencias.index.tolist()
    
    # Colores intensos
    colores = plt.cm.Set1(range(len(frecuencias)))
    
    # Graficar las barras
    ax.bar(x, frecuencias, color=colores, width=0.6)  # Ancho de las barras es 0.6
    
    # Configurar el título y los ejes
    ax.set_title(f"Gráfico de barras de {campo_actual}")
    ax.set_xlabel(campo_actual)
    ax.set_ylabel("Frecuencia")
    
    # Establecer las etiquetas del eje x
    plt.xticks(x, etiquetas)
    
    # Guardar la figura como imagen y mostrarla en la interfaz
    imagen_grafico = "grafico.png"
    plt.savefig(imagen_grafico)
    plt.close()
    
    imagen = Image.open(imagen_grafico)
    imagen = imagen.resize((600, 400), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)
    imagen_label.configure(image=imagen)
    imagen_label.image = imagen


# Mostrar el primer gráfico al iniciar la ventana
graficar_imagen()

# Botones de navegación
boton_anterior = tk.Button(ventana, text="Anterior", font=("Arial", 16, "bold"), command=graficar_anterior)
boton_anterior.place(x=10, y=550)

boton_siguiente = tk.Button(ventana, text="Siguiente", font=("Arial", 16, "bold"), command=graficar_siguiente)
boton_siguiente.place(x=680, y=550)

# Mantener la ventana en la parte superior
ventana.attributes('-topmost', True)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()




