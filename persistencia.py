import json

ARCHIVO_DATOS = "finanzas.json"

def guardar_datos(datos):
    # Es buena práctica utilizar la ESTRUCTURA with open, para abrir
    # un archivo de forma segura.
    # w (write) si el archivo no existe, lo crea
    with open(ARCHIVO_DATOS, "w", encoding='utf-8') as archivo:

    # json.dump toma los datos y los "vuelca" en el archivo
    
    # json.dump(obj, fp, ...) donde:
    #   obj: objetos (datos) que quiero guardar.
    #   fp: "file pointer" donde quiero que se guarden
    #   indent=4 es para que se vea ordenado    
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos():
    try:
        # Intentamos abrir el archivo en modo 'r' (read/lectura)
        with open(ARCHIVO_DATOS, 'r') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        # Si el archivo no existe, no entramos en pánico.
        # Simplemente retornamos una lista vacía, porque aún no hay datos.
        return []
    except json.JSONDecodeError:
        # Si el archivo existe pero está vacío o corrupto,
        # también retornamos una lista vacía para evitar errores.
        return []