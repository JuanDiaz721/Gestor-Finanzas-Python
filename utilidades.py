import os #Libreria encargada de interactuar con el sistema operativo
from datetime import datetime # Para poner la fecha de hoy automáticamente si queremos

def limpiar_pantalla():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

def pedir_monto():
    """Solicita un número repetidamente hasta que el usuario ingrese uno válido."""
    while True:
        try:
            monto = float(input("Ingresa el valor del movimiento: "))
            if monto <= 0:
                print("⚠️  El valor debe ser positivo.")
            else:
                return monto
        except ValueError:
            print("❌ Error: Debes ingresar un número válido (ej: 50000).")

def pedir_fecha():
    """Solicita una fecha y valida que tenga el formato correcto YYYY-MM-DD."""
    while True:
        fecha_str = input(f"Fecha (YYYY-MM-DD) [Enter para hoy {datetime.today().date()}]: ")
        
        # Caso 1: Usuario presiona Enter (quiere fecha de hoy)
        if not fecha_str:
            return str(datetime.today().date())
        
        # Caso 2: Usuario escribió algo, validamos formato
        try:
            # Intentamos parsear. Si falla, saltará al 'except'
            datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha_str # Si llega aquí, es válida
        except ValueError:
            print("❌ Error: Formato incorrecto. Debe ser Año-Mes-Día (ej: 2025-11-29).")

def pedir_mes_anio():
    """Solicita mes y año al usuario y devuelve enteros."""
    hoy = datetime.today()
    print(f"Deja vacío para usar la fecha actual ({hoy.month}/{hoy.year})")
    
    mes_str = input("Mes (1-12): ")
    anio_str = input("Año (ej: 2025): ")
    
    if not mes_str: mes_str = str(hoy.month)
    if not anio_str: anio_str = str(hoy.year)
    
    try:
        return int(mes_str), int(anio_str)
    except ValueError:
        print("❌ Mes o Año inválidos.")
        return None, None