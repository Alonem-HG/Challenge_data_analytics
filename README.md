# Challenge Data Analytics - Python by Alonso Hernandez 

#### Descripcion del proyecto

### Recursos:  
Obtenemos los 3 archivos de fuente utilizando la librería requests y almacenarse en forma local.   
o Datos Argentina - Museos  
o Datos Argentina - Salas de Cine  
o Datos Argentina - Bibliotecas Populares  

#### Objetivos:  
Procesamiento de datos  
Creación de tablas en la Base de datos  
Actualización de la base de datos  

#### Complementos:
logging  
venv  
decouple  
pandas  

#### Detalles:
**download_data.py** : Podemos ver el siguiente flujo de instrucciones.  
    -> Permite descargar la informacion mediante beatifulsoap 4  
     -> Obtiene los links de los csv y los guarda en una lista  
      -> Convierte los links en dataframes  
       -> Organiza los archivos en rutas siguiendo la siguiente estructura: “categoría\año-mes\categoria-dia-mes-año.csv”  
        -> Finalmente almacena los dataframes en formato csv de forma local  
        
        
**data_preprocessing.py** : Hace un analisis exploratorio de datos para realizar limpieza a los datos por medio de pandas. 

**querys.py** : Ejecuta scripts sql almacenados que estan almacenados de forma local junto con SQLAlchemy hacer una conexion(connection_sqlalchemy.py) con la base de datos. 

**manage_data_collection.py** : Insertamos los registros en servidor Postgress de forma local.

**main.py** : Ejecuta el programa.

      
