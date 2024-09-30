#Programa-de-Prediccion-de-precios-de-casa

#Práctica 4: Revisión de Código

El módulo que se está evaluando es realizar_predicción(), que proviene de un proyecto en python
 
VENTANA 3

CASO 1
Fragmento de código:
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


Violación:
Define a constant instead of duplicating this literal "estado_limpieza.txt" 3 times. [+2 locations]sonarlint(python:S1192)

La violación de la regla sonarlint(python:S1192) ocurre porque el literal "estado_limpieza.txt" se repite tres veces en el código. Esto va en contra de las buenas prácticas de desarrollo, ya que el uso de literales repetidos reduce la mantenibilidad y legibilidad del código. Si en el futuro se necesita cambiar este valor, tendríamos que actualizarlo en varios lugares, lo cual es propenso a errores.


Refactorización:
Definir

ESTADO_LIMPIEZA_FILE = "estado_limpieza.txt"

Reemplazar

with open(ESTADO_LIMPIEZA_FILE, "r") as file:

La solución es definir una constante ESTADO_LIMPIEZA_FILE para almacenar el valor del literal "estado_limpieza.txt". Esto sigue el principio DRY (Don’t Repeat Yourself), haciendo que el código sea más limpio y fácil de mantener.


CASO 2
Fragmento de código:

        # Eliminar valores duplicados
        df.drop_duplicates(inplace=True)

Violación:

Do not use "inplace=True" when modifying a dataframe.sonarlint(python:S6734)


La regla sonarlint(python:S6734) indica que no se debe utilizar inplace=True al modificar un DataFrame. Esto se debe a que inplace=True modifica el DataFrame original, lo que puede llevar a confusión y errores, especialmente en flujos de trabajo más complejos donde se reutiliza el DataFrame. Además, el uso de inplace=True es menos eficiente en términos de memoria en algunos casos.


Refactorización:

df.drop_duplicates()

En lugar de modificar el DataFrame en su lugar, la solución es devolver una nueva versión del DataFrame sin duplicados y reasignar esta nueva versión a la variable df.




VENTANA 5

CASO 1

Fragmento de código:

 Dividir el conjunto de datos en entrenamiento y prueba

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


Violación:

Rename this local variable "X_test" to match the regular expression ^[_a-z][a-z0-9_]*$.sonarlint(python:S117)

La regla sonarlint(python:S117) sugiere renombrar variables locales para que sigan la convención de nombres en minúscula y guiones bajos, es decir, deben coincidir con la expresión regular ^[_a-z][a-z0-9_]*$. En este caso, X_test no sigue esa convención, ya que empieza con una letra mayúscula. Las variables locales deben tener nombres en minúscula para mantener la coherencia en el código y seguir las buenas prácticas de nomenclatura.

Refactorización:

 Dividir el conjunto de datos en entrenamiento y prueba

        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


Renombrar las variables para que sigan las convenciones de nombres en minúscula.

CASO 2

Fragmento de código:
 
        # Entrenar el modelo de Random Forest
        modelo = RandomForestRegressor(random_state=42)
        modelo.fit(x_train, y_train)

Violación:

Specify important hyperparameters when instantiating a Scikit-learn estimator.sonarlint(python:S6973)
La regla sonarlint(python:S6973) recomienda especificar hiperparámetros importantes al instanciar un estimador de Scikit-learn. En el fragmento de código original, solo se establece el random_state al crear el modelo de RandomForestRegressor, lo que puede llevar a un rendimiento subóptimo del modelo. Definir hiperparámetros adicionales permite un control más preciso sobre el comportamiento del modelo y puede mejorar su rendimiento general.


Refactorización:
 
        # Entrenar el modelo de Random Forest
        modelo = RandomForestRegressor(
            n_estimators=100,          
            max_depth=10,              
            min_samples_split=2,        
            min_samples_leaf=1,        
            max_features="sqrt",        
            random_state=42      
        )
        modelo.fit(x_train, y_train)


Especificar los hiperparámetros más relevantes al crear el modelo de RandomForestRegressor para optimizar su rendimiento.

