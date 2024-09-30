import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
titulo_label = tk.Label(ventana, text="MAPA DE CALOR: CORRELACIÓN BIVARIADA", font=("Arial", 20, "bold"), fg="white", bg="#030918")
titulo_label.pack(pady=10)

def cargar_archivo():
    # Lógica para cargar el archivo aquí
    with open("config.txt", "w") as file:
        file.write("True")

def retroceder():
    ventana.destroy()
    ruta_ventana4 = os.path.join("Ventanas", "ventana4.py")
    os.system(f"python {ruta_ventana4}")

# Botones

retroceder_btn = tk.Button(ventana, text="Retroceder", font=("Arial", 16, "bold"), command=retroceder)
retroceder_btn.pack(pady=10)

# Cargar el dataset limpio en un DataFrame
dataset_path = "dataset_limpio.csv"  
df = pd.read_csv(dataset_path)

# Calcular la matriz de correlación
correlation_matrix = df.corr()

# Crear el mapa de calor utilizando seaborn
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")

# Crear la figura de matplotlib y asociar el mapa de calor
figure = heatmap.get_figure()

# Crear el lienzo de visualización en la ventana
canvas = FigureCanvasTkAgg(figure, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()


