import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Cargar el conjunto de datos
df = pd.read_csv("dataset_limpio.csv")

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el tamaño de la ventana
ancho_ventana = 1000
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
ruta_izquierda = os.path.join("Fondos", "image5.jpeg")
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
titulo_label = tk.Label(ventana, text="PREDICCIÓN", font=("Arial", 24, "bold"), fg="#51d1f6", bg="#030918", anchor="w", justify="left")
titulo_label.place(x=550, y=55)

# Crear el marco para los campos de entrada
campos_frame = tk.Frame(ventana, bg="#030918")
campos_frame.place(x=420, y=180)

# Etiquetas de los campos de entrada
etiquetas = [
    "Área:", "Habitaciones:", "Baños:",
    "Pisos:", "Carretera:", "Huéspedes:",
    "Sótano:", "Calefacción:", "AC:",
    "Estacionamiento:", "Preferencial:",
    "Mobiliario:"
]

num_etiquetas = len(etiquetas)
num_filas = num_etiquetas // 2 

for i, etiqueta in enumerate(etiquetas):
    label = tk.Label(campos_frame, text=etiqueta, font=("Georgia", 11), fg="white", bg="#030918", anchor="w")
    label.grid(row=i % num_filas, column=i // num_filas * 2, padx=9, pady=9, sticky="w")

# Campos de entrada
entradas = []
comboboxes = []
for i in range(num_etiquetas):
    if i in [4, 5, 6, 7, 8, 10]:
        combobox = ttk.Combobox(campos_frame, values=["Sí", "No"])
        combobox.grid(row=i % num_filas, column=i // num_filas * 2 + 1, padx=9, pady=9)
        combobox.set("Sí")  # Opción predeterminada
        comboboxes.append(combobox)
    elif i == 11:
        combobox = ttk.Combobox(campos_frame, values=["Amueblado", "Semi-amueblado", "Sin amueblar"])
        combobox.grid(row=i % num_filas, column=i // num_filas * 2 + 1, padx=9, pady=9)
        combobox.set("Amueblado")  # Opción predeterminada
        comboboxes.append(combobox)
    else:
        entrada = tk.Entry(campos_frame)
        entrada.grid(row=i % num_filas, column=i // num_filas * 2 + 1, padx=9, pady=9)
        entradas.append(entrada)

# Función de predicción
def realizar_prediccion():
    # Obtener los valores de los campos de entrada
    valores_frames = [entrada.get() if entrada else "" for entrada in entradas]
    valores_comboboxes = [combobox.get() for combobox in comboboxes]
    
    # Validar si algún campo está vacío
    if any(not valor for valor in valores_frames):
        messagebox.showerror("Error", "Debe completar todos los campos.")
        return
    
    # Validar los rangos de cada campo
    try:
        area = int(valores_frames[0])
        habitaciones = int(valores_frames[1])
        banios = int(valores_frames[2])
        pisos = int(valores_frames[3])
        estacionamiento = int(valores_frames[4])
        
        if not (1000 <= area <= 10000):
            raise ValueError("Área debe estar entre 1000 y 10000.")
        if not (1 <= habitaciones <= 30):
            raise ValueError("Habitaciones debe estar entre 1 y 30.")
        if not (1 <= banios <= 30):
            raise ValueError("Baños debe estar entre 1 y 30.")
        if not (1 <= pisos <= 30):
            raise ValueError("Pisos debe estar entre 1 y 30.")
        if not (0 <= estacionamiento <= 30):
            raise ValueError("Estacionamiento debe estar entre 0 y 30.")
        
        # Preparar los datos para entrenar el modelo
        X = df.drop("Precio", axis=1)
        y = df["Precio"]
        
        # Convertir los valores "Sí" y "No" a 1 y 0, respectivamente
        for i in [0, 1, 2, 3, 4, 5]:
            if valores_comboboxes[i] == "Sí":
                valores_comboboxes[i] = 1
            else:
                valores_comboboxes[i] = 0
        
        # Convertir el valor "Amueblado", "Semi-amueblado" y "Sin amueblar" a 0, 1 y 2, respectivamente
        if valores_comboboxes[6] == "Amueblado":
            valores_comboboxes[6] = 0
        elif valores_comboboxes[6] == "Semi-amueblado":
            valores_comboboxes[6] = 1
        else:
            valores_comboboxes[6] = 2
        
        # Crear un DataFrame con los valores ingresados
        datos = pd.DataFrame([valores_frames + valores_comboboxes], columns=X.columns)
        
        # Dividir el conjunto de datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Entrenar el modelo de Random Forest
        modelo = RandomForestRegressor(random_state=42)
        modelo.fit(X_train, y_train)
        
        # Realizar la predicción usando los datos ingresados
        precio_predicho = modelo.predict(datos)[0]
        
        # Calcular el porcentaje de precisión del modelo
        y_pred = modelo.predict(X_test)
        precision = r2_score(y_test, y_pred) * 100
        
        # Mostrar los resultados en una ventana de diálogo

        for i in range(6):
            if valores_comboboxes[i] == 0:
                valores_comboboxes[i] = "No"
            elif valores_comboboxes[i] == 1:
                valores_comboboxes[i] = "Sí"
        
        # Convertir 0 a "Amueblado", 1 a "Semi-amueblado" y 2 a "Sin amueblar" en la posición 6
        if valores_comboboxes[6] == 0:
            valores_comboboxes[6] = "Amueblado"
        elif valores_comboboxes[6] == 1:
            valores_comboboxes[6] = "Semi-amueblado"
        elif valores_comboboxes[6] == 2:
            valores_comboboxes[6] = "Sin amueblar"

        resultado = f"Datos de entrada:\n\nÁrea: {valores_frames[0]}\nHabitaciones: {valores_frames[1]}\nBaños: {valores_frames[2]}\nPisos: {valores_frames[3]}\nEstacionamiento: {valores_frames[4]}\nCarretera: {valores_comboboxes[0]}\nHuéspedes: {valores_comboboxes[1]}\nSótano: {valores_comboboxes[2]}\nCalefacción: {valores_comboboxes[3]}\nAC: {valores_comboboxes[4]}\nPreferencial: {valores_comboboxes[5]}\nMobiliario: {valores_comboboxes[6]}\n\nPrecio predicho: ${precio_predicho}\n\nModelo de predicción (R2 score): {precision:.2f}%"
        messagebox.showinfo("Predicción Random Forest", resultado)

        # Guardar el resultado en un archivo de texto
        with open("Precios_predichos.txt", "a") as archivo:
            archivo.write(resultado + "\n\n")
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Botón "Predicción"
boton_prediccion = tk.Button(ventana, text="Predecir", font=("Arial", 12, "bold"), command=realizar_prediccion)
boton_prediccion.place(x=ancho_ventana // 2 + 330, y=550)


# Agregar el botón "Atras"
def abrir_ventana3():
    ventana.withdraw()
    ruta_ventana3 = os.path.join("Ventanas", "ventana3.py")
    os.system(f"python {ruta_ventana3}")
    ventana.destroy()


def destruir():
    ventana.withdraw()
    ventana.destroy()

boton_atras = tk.Button(ventana, text="Atras", font=("Arial", 16, "bold"), command=abrir_ventana3)
boton_atras.place(x=410, y=550)

boton_salir = tk.Button(ventana, text="Finalizar", font=("Arial", 16, "bold"),command=destruir)
boton_salir.place(x=500, y=550)


# Ejecutar el bucle principal de la ventana
ventana.mainloop()
