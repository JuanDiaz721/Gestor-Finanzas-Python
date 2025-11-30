# main.py
import persistencia as db
import utilidades as utils
import logica

def menu_principal():
    datos = db.cargar_datos() # Cargamos la memoria al iniciar
    
    while True:
        utils.limpiar_pantalla()
        print("=== GESTOR DE FINANZAS PERSONALES ===")
        print(f"Registros actuales: {len(datos)}") # Feedback inmediato
        print("1. Registrar Entrada de Dinero")
        print("2. Registrar Gasto")
        print("3. Ver Reporte de Movimientos")
        print("4. Modificar un registro")
        print("5. Eliminar un registro")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción (1-6): ")
        
        if opcion == '1':
            logica.registrar_entrada(datos)
        elif opcion == '2':
            logica.registrar_gasto(datos)
        elif opcion == '3':
            logica.ver_reporte(datos)
        elif opcion == '4':
            logica.modificar_registro(datos)
        elif opcion == '5':
            logica.eliminar_registro(datos)
        elif opcion == '6':
            utils.limpiar_pantalla()
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")
            input("Intenta de nuevo...")

# Y finalmente, el punto de entrada que activa todo:
if __name__ == "__main__":
    menu_principal()
