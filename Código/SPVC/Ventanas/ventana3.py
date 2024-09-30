import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import os

dataset_cargado = False
dataset_path = ""
dataset_limpio = None

def cargar_dataset():
    global dataset_cargado, dataset_path
    archivo = filedialog.askopenfilename(filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")))
    if archivo:
        dataset_cargado = True
        dataset_path = archivo

        # Mostrar una ventana de éxito al cargar el dataset
        ventana_exito = tk.Toplevel()
        ventana_exito.title("Carga exitosa")
        ventana_exito.geometry("300x100")
        etiqueta_exito = tk.Label(ventana_exito, text="Se ha cargado el dataset exitosamente!", font=("Arial", 12))
        etiqueta_exito.pack(pady=20)
        boton_cerrar = tk.Button(ventana_exito, text="Cerrar", command=ventana_exito.destroy)
        boton_cerrar.pack()

    else:
        dataset_cargado = False

def abrir_ventana4():
    # Verificar si se ha limpiado un dataset antes de abrir la ventana 4
    try:
        with open("estado_limpieza.txt", "r") as file:
            archivo_cargado = file.read().strip()
            if archivo_cargado == "True":
                ventana.withdraw()
                ruta_ventana4 = os.path.join("Ventanas", "ventana4.py")
                os.system(f"python {ruta_ventana4}")
                ventana.destroy()

    except FileNotFoundError:
            ventana_no_dataset = tk.Toplevel()
            ventana_no_dataset.title("Dataset sucio")
            ventana_no_dataset.geometry("300x100")
            etiqueta_no_dataset = tk.Label(ventana_no_dataset, text="No se ha realizado la limpieza del dataset", font=("Arial", 12))
            etiqueta_no_dataset.pack(pady=20)
            boton_cerrar = tk.Button(ventana_no_dataset, text="Cerrar", command=ventana_no_dataset.destroy)
            boton_cerrar.pack()

def abrir_ventana5():
    # Verificar si se ha limpiado un dataset antes de abrir la ventana 5
    
    try:
        with open("estado_limpieza.txt", "r") as file:
            archivo_cargado = file.read().strip()
            if archivo_cargado == "True":
                ventana.withdraw()
                ruta_ventana5 = os.path.join("Ventanas", "ventana5.py")
                os.system(f"python {ruta_ventana5}")
                ventana.destroy()

    except FileNotFoundError:
            ventana_no_dataset = tk.Toplevel()
            ventana_no_dataset.title("Dataset sucio")
            ventana_no_dataset.geometry("300x100")
            etiqueta_no_dataset = tk.Label(ventana_no_dataset, text="No se ha realizado la limpieza del dataset", font=("Arial", 12))
            etiqueta_no_dataset.pack(pady=20)
            boton_cerrar = tk.Button(ventana_no_dataset, text="Cerrar", command=ventana_no_dataset.destroy)
            boton_cerrar.pack()

def se_cargo_dataset():
    global dataset_cargado
    return dataset_cargado

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
ruta_izquierda = os.path.join("Fondos", "image3.jpg")
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
titulo_label = tk.Label(ventana, text="LIMPIEZA DE DATOS", font=("Arial", 24, "bold"), fg="#51d1f6", bg="#030918", anchor="w", justify="left")
titulo_label.place(x=410, y=180)

# Crear el botón "Cargar Dataset"
boton_cargar_dataset = tk.Button(ventana, text="Cargar Dataset", font=("Arial", 16), command=cargar_dataset, width=25)
boton_cargar_dataset.place(x=410, y=250)

def limpiar_dataset():
    global limpieza_realizada, dataset_limpio
    global dataset_path

    if not dataset_cargado:
        ventana_no_dataset = tk.Toplevel()
        ventana_no_dataset.title("No se ha detectado dataset")
        ventana_no_dataset.geometry("300x100")
        etiqueta_no_dataset = tk.Label(ventana_no_dataset, text="No se ha cargado un dataset", font=("Arial", 12))
        etiqueta_no_dataset.pack(pady=20)
        boton_cerrar = tk.Button(ventana_no_dataset, text="Cerrar", command=ventana_no_dataset.destroy)
        boton_cerrar.pack()
    else:

        # Cargar el dataset en un DataFrame
        df = pd.read_csv(dataset_path)

        # Guardar la dimensión inicial del dataset
        dimension_inicial = df.shape

        # Eliminar valores duplicados
        df.drop_duplicates(inplace=True)

        # Guardar la dimensión después de eliminar duplicados
        dimension_sin_duplicados = df.shape

        # Eliminar filas con valores menores a 0
        df = df[(df >= 0).all(axis=1)]

        # Guardar la dimensión después de eliminar valores menores a 0
        dimension_sin_negativos = df.shape

        # Eliminar valores fuera de rango
        df = df[(df['Precio'].between(400000, 4000000)) &
                (df['Area'].between(1000, 10000)) &
                (df['Habitaciones'].between(1, 30)) &
                (df['Banios'].between(1, 30)) &
                (df['Pisos'].between(1, 30)) &
                (df['Carretera'].between(0, 1)) &
                (df['Huespedes'].between(0, 1)) &
                (df['Sotano'].between(0, 1)) &
                (df['Calefaccion'].between(0, 1)) &
                (df['AC'].between(0, 1)) &
                (df['Estacionamiento'].between(0, 30)) &
                (df['Preferencial'].between(0, 1)) &
                (df['Mobiliario'].between(0, 2))]

        # Guardar la dimensión semifinal del dataset
        dimension_semifinal = df.shape

        # Calcular el número de filas eliminadas por valores duplicados
        filas_eliminadas_duplicados = dimension_inicial[0] - dimension_sin_duplicados[0]

        # Calcular el número de filas eliminadas por valores menores a 0
        filas_eliminadas_menores_0 = dimension_sin_duplicados[0] - dimension_sin_negativos[0]

        # Calcular el número de filas eliminadas por valores fuera de rango
        filas_eliminadas_fuera_rango = dimension_sin_negativos[0] - dimension_semifinal[0]

        # Calcular el número de filas eliminadas por valores NaN en cada columna
        filas_eliminadas_nan = dimension_semifinal[0] - df.dropna().shape[0]

        dataset_limpio = df

        ruta_archivo_csv = 'dataset_limpio.csv'

        dataset_limpio.to_csv(ruta_archivo_csv, index=False)

        # Guardar la dimensión final del dataset
        dimension_final = df.shape

        limpieza_realizada = True 

        # Crear una ventana para mostrar la información
        ventana_informacion = tk.Toplevel(ventana)
        ventana_informacion.title("Información del proceso de limpieza")
        ventana_informacion.geometry("400x600")

        # Calcular el porcentaje de datos conservados y perdidos
        datos_conservados = dimension_final[0]
        datos_perdidos = dimension_inicial[0] - dimension_final[0]

        # Crear una lista con los porcentajes
        porcentajes = [datos_conservados, datos_perdidos]

        # Colores para el gráfico circular
        colores = ["green", "red"]

        # Generar el gráfico circular
        plt.figure(figsize=(4, 4))  # Tamaño de la figura (ancho x alto)
        plt.pie(porcentajes, colors=colores, autopct="%1.1f%%")
        plt.axis("equal")  # Para que el gráfico sea un círculo perfecto

        # Definir la leyenda
        leyenda = ["Datos Conservados", "Datos Perdidos"]

        # Mostrar el gráfico en la ventana
        canvas = FigureCanvasTkAgg(plt.gcf(), master=ventana_informacion)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Mostrar la leyenda a la derecha del gráfico
        plt.legend(leyenda, loc="center", bbox_to_anchor=(0.5,0))

        # Mostrar la dimensión inicial y final del dataset
        etiqueta_dimension_inicial = tk.Label(ventana_informacion, text=f"Dimensión inicial: {dimension_inicial}")
        etiqueta_dimension_inicial.pack()
        etiqueta_dimension_final = tk.Label(ventana_informacion, text=f"Dimensión final: {dimension_final}")
        etiqueta_dimension_final.pack()

        # Mostrar el número de filas eliminadas por cada motivo
        etiqueta_duplicados = tk.Label(ventana_informacion, text=f"Número de filas eliminadas por duplicados: {filas_eliminadas_duplicados}")
        etiqueta_duplicados.pack()
        etiqueta_nan = tk.Label(ventana_informacion, text=f"Número de filas eliminadas por valores NaN: {filas_eliminadas_nan}")
        etiqueta_nan.pack()
        etiqueta_menores_0 = tk.Label(ventana_informacion, text=f"Número de filas eliminadas por valores menores a 0: {filas_eliminadas_menores_0}")
        etiqueta_menores_0.pack()
        etiqueta_fuera_rango = tk.Label(ventana_informacion, text=f"Número de filas eliminadas por valores fuera de rango: {filas_eliminadas_fuera_rango}")
        etiqueta_fuera_rango.pack()

        with open("estado_limpieza.txt", "w") as file:
            file.write("True")
    
# Crear el botón "Limpieza Dataset"
boton_limpiar_dataset = tk.Button(ventana, text="Limpieza de Dataset", font=("Arial", 16), command= limpiar_dataset, width=25)
boton_limpiar_dataset.place(x=410, y=300)

# Agregar el título
titulo_label = tk.Label(ventana, text="A CONTINUACIÓN", font=("Arial", 16, "bold"), fg="#51d1f6", bg="#030918", anchor="w", justify="left")
titulo_label.place(x=410, y=450)

# Crear el botón "ANÁLISIS"
siguiente_analisis = tk.Button(ventana, text="Análisis", font=("Arial", 16, "bold"), command=abrir_ventana4)
siguiente_analisis.place(x=410, y=490)

# Crear el botón "PREDICCIÓN"
siguiente_prediccion = tk.Button(ventana, text="Predicción", font=("Arial", 16, "bold"), command=abrir_ventana5)
siguiente_prediccion.place(x=410, y=540)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()


