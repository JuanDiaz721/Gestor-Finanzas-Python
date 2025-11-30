from datetime import datetime
# Importamos nuestras propias librerías
import persistencia as db  # Le ponemos un alias 'db' para que sea corto
import utilidades as utils # Le ponemos un alias 'utils'

def registrar_entrada(datos_existentes):
    utils.limpiar_pantalla()
    print("--- REGISTRAR ENTRADA DE DINERO ---")
    
    # 1. Fecha (Por ahora simple texto, luego la automatizamos)
    fecha = utils.pedir_fecha()
    
    # 2. Motivo
    motivo = input("Motivo (ej: Salario, Venta): ")
    
    # 3. Valor (Usamos nuestra función segura)
    valor = utils.pedir_monto()
    
    # 4. Crear el objeto
    nuevo_movimiento = {
        "fecha": fecha,
        "motivo": motivo,
        "valor": valor,
        "categoria": "Entrada", # Categoría fija como dijiste
        "tipo": "Entrada"
    }
    
    # 5. Guardar
    datos_existentes.append(nuevo_movimiento)
    db.guardar_datos(datos_existentes)
    print("\n✅ ¡Entrada registrada exitosamente!")
    input("Presiona Enter para volver al menú...")

def registrar_gasto(datos_existentes):
    utils.limpiar_pantalla()
    print("--- REGISTRAR GASTO ---")
    
    # 1. Datos básicos
    fecha = utils.pedir_fecha()
        
    motivo = input("Motivo (ej: Almuerzo, Uber): ")
    valor = utils.pedir_monto()
    
    # 2. Sub-menú de Categorías
    print("\nSelecciona la categoría del gasto:")
    print("1. Gasto Fijo")
    print("2. Gasto Variable")
    print("3. Gasto Inesperado")
    print("4. Gasto de Ocio")
    
    opcion_cat = input("Opción (1-4): ")
    
    # Diccionario para mapear (Mapping) la opción al texto real
    # Esto es más limpio que hacer muchos if/else
    categorias = {
        "1": "Gastos Fijos",
        "2": "Gastos Variables",
        "3": "Gastos Inesperados",
        "4": "Gastos de Ocio"
    }
    
    # .get() busca la clave, si no existe devuelve "Otros"
    categoria_seleccionada = categorias.get(opcion_cat, "Otros Gastos")
    
    nuevo_movimiento = {
        "fecha": fecha,
        "motivo": motivo,
        "valor": valor,
        "categoria": categoria_seleccionada,
        "tipo": "Gasto"
    }
    
    datos_existentes.append(nuevo_movimiento)
    db.guardar_datos(datos_existentes)
    print(f"\n✅ ¡Gasto registrado en '{categoria_seleccionada}' exitosamente!")
    input("Presiona Enter para volver al menú...")

def ver_reporte(datos):
    utils.limpiar_pantalla()
    print("-------------------- REPORTE DE MOVIMIENTOS POR MES --------------------")
    
    # 1. Solicitar filtro al usuario
    # Usamos input para pedir mes y año. 
    # Si lo dejan vacío, asumimos el mes/año actual (automatización).
    hoy = datetime.today()
    
    print(f"Deja vacío para usar la fecha actual ({hoy.month}/{hoy.year})")
    
    filtro_mes = input("Mes (1-12): ")
    filtro_anio = input("Año (ej: 2025): ")
    
    # Lógica de "Fallback" (Valores por defecto)
    if not filtro_mes:
        filtro_mes = str(hoy.month)
    if not filtro_anio:
        filtro_anio = str(hoy.year)
        
    # Convertimos a enteros para poder comparar matemáticamente
    try:
        mes_buscado = int(filtro_mes)
        anio_buscado = int(filtro_anio)
    except ValueError:
        print("❌ Error: Mes o Año inválidos.")
        input("Enter para volver...")
        return # Salimos de la función si hay error

    print(f"\nGenerando reporte para: {mes_buscado}/{anio_buscado}...\n")
    
    # --- CABECERA DE LA TABLA ---
    print(f"{'FECHA':<12} | {'MOTIVO':<20} | {'CATEGORÍA':<20} | {'VALOR':>12}")
    print("-" * 72) 
    
    total_entradas = 0
    total_gastos = 0
    movimientos_encontrados = 0 # Contador para saber si hubo datos
    
    # 2. Iteración con FILTRO
    for mov in datos:
        fecha_str = mov["fecha"] # Esto es un string "2025-11-29"
        
        try:
            # AQUÍ OCURRE LA MAGIA DEL PARSING
            # Le decimos a Python: "Toma este texto y entiéndelo usando el formato Año-Mes-Día"
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
        except ValueError:
            # Si una fecha en el JSON está corrupta, la saltamos para no romper el reporte
            continue
            
        # 3. La condición de filtrado (El "Gatekeeper")
        # Solo procesamos si el mes y año coinciden con lo que pidió el usuario
        if fecha_obj.month == mes_buscado and fecha_obj.year == anio_buscado:
            
            # --- Aquí va la lógica de mostrar y sumar (Igual que antes) ---
            motivo = mov["motivo"]
            categoria = mov["categoria"]
            valor = mov["valor"]
            tipo = mov.get("tipo", "Gasto") 
            
            if tipo == "Entrada":
                total_entradas += valor
                str_valor = f"+ ${valor:,.0f}" 
            else:
                total_gastos += valor
                str_valor = f"- ${valor:,.0f}"

            # Recorte de texto estético
            motivo_corto = (motivo[:18] + '..') if len(motivo) > 18 else motivo
            
            print(f"{fecha_str:<12} | {motivo_corto:<20} | {categoria:<20} | {str_valor:>12}")
            
            movimientos_encontrados += 1

    print("-" * 72)
    
    # 4. Feedback al usuario
    if movimientos_encontrados == 0:
        print(f"⚠️  No se encontraron movimientos en el mes {mes_buscado}/{anio_buscado}.")
    else:
        saldo_disponible = total_entradas - total_gastos
        print("\n--- BALANCE DEL MES ---")
        print(f"Total Entradas:   ${total_entradas:,.0f}")
        print(f"Total Gastos:     ${total_gastos:,.0f}")
        print(f"SALDO DEL MES:    ${saldo_disponible:,.0f}")
    
    input("\nPresiona Enter para volver al menú...")

def seleccionar_registro_por_mes(datos):
    """Filtra por mes y devuelve el ÍNDICE REAL de la lista principal."""
    utils.limpiar_pantalla()
    print("--- BUSCAR REGISTRO POR FECHA ---")
    
    # 1. Pedimos el filtro
    mes, anio = utils.pedir_mes_anio()
    if mes is None: return None # Si falló la fecha, salimos
    
    print(f"\nBuscando registros de {mes}/{anio}...")
    
    # 2. Creamos una lista temporal que guarda tuplas: (INDICE_REAL, MOVIMIENTO)
    candidatos = []
    
    for i, mov in enumerate(datos):
        try:
            fecha_obj = datetime.strptime(mov["fecha"], '%Y-%m-%d')
            if fecha_obj.month == mes and fecha_obj.year == anio:
                # ¡Aquí está el truco! Guardamos 'i' para no perder su rastro
                candidatos.append((i, mov)) 
        except ValueError:
            continue
            
    # 3. Validamos si hay resultados
    if not candidatos:
        print("⚠️  No se encontraron registros en esa fecha.")
        input("Enter para continuar...")
        return None
        
    # 4. Mostramos solo los filtrados
    print(f"\n--- REGISTROS ENCONTRADOS ({len(candidatos)}) ---")
    # 'idx_visual' es 1, 2, 3... para el usuario
    # 'tupla' contiene (indice_real, diccionario_datos)
    for idx_visual, tupla in enumerate(candidatos):
        indice_real = tupla[0]
        mov = tupla[1]
        print(f"{idx_visual + 1}. {mov['fecha']} | {mov['motivo']} | ${mov['valor']:,.0f}")
        
    print("0. Cancelar")
    
    # 5. Selección del usuario
    try:
        seleccion = int(input("\nSelecciona el número de la lista: "))
        if seleccion == 0: return None
        
        if 1 <= seleccion <= len(candidatos):
            # Recuperamos el dato de la lista de candidatos
            tupla_elegida = candidatos[seleccion - 1]
            # Devolvemos SOLO el índice real para que modificar/eliminar funcionen
            return tupla_elegida[0] 
        else:
            print("❌ Número fuera de rango.")
            input("Enter para continuar...")
            return None
    except ValueError:
        print("❌ Debes ingresar un número.")
        input("Enter para continuar...")
        return None

def eliminar_registro(datos):
    indice = seleccionar_registro_por_mes(datos)
    
    if indice is not None:
        # Confirmación de seguridad (Best Practice)
        confirmacion = input(f"¿Seguro que quieres borrar '{datos[indice]['motivo']}'? (s/n): ")
        if confirmacion.lower() == 's':
            eliminado = datos.pop(indice)
            db.guardar_datos(datos)
            print(f"✅ Registro '{eliminado['motivo']}' eliminado.")
        else:
            print("Operación cancelada.")
        
        input("Enter para volver...")

def modificar_registro(datos):
    indice = seleccionar_registro_por_mes(datos)
    
    if indice is not None:
        mov = datos[indice] # Obtenemos el registro actual
        print(f"\nEditando: {mov['motivo']} (${mov['valor']})")
        print("Deja el campo vacío y presiona Enter para mantener el valor actual.\n")
        
        # 1. Nueva Fecha
        nueva_fecha = input(f"Nueva Fecha [{mov['fecha']}]: ")
        if nueva_fecha:
             # Aquí deberíamos validar también, pero por simplicidad en este ejemplo:
             try:
                 datetime.strptime(nueva_fecha, '%Y-%m-%d')
                 mov['fecha'] = nueva_fecha
             except ValueError:
                 print("Fecha inválida, se conservará la anterior.")
        
        # 2. Nuevo Motivo
        nuevo_motivo = input(f"Nuevo Motivo [{mov['motivo']}]: ")
        if nuevo_motivo:
            mov['motivo'] = nuevo_motivo
            
        # 3. Nuevo Valor (CORREGIDO)
        nuevo_valor_str = input(f"Nuevo Valor [{mov['valor']}]: ")
        if nuevo_valor_str:
            try:
                nuevo_monto = float(nuevo_valor_str)
                # AQUÍ AGREGAMOS EL GUARDIÁN
                if nuevo_monto > 0:
                    mov['valor'] = nuevo_monto
                else:
                    print("⚠️  Error: El valor debe ser positivo. Se conservó el valor anterior.")
            except ValueError:
                print("⚠️  Error: No es un número válido. Se conservó el valor anterior.")
        
        # Guardamos cambios
        db.guardar_datos(datos)
        print("\n✅ ¡Registro actualizado exitosamente!")
        input("Enter para volver...")        
