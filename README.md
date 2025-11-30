# 💰 Gestor de Finanzas Personales (CLI)

Una aplicación de línea de comandos (CLI) construida en Python para gestionar ingresos y gastos personales. Permite registrar movimientos, categorizarlos y visualizar reportes mensuales con cálculo automático de saldos.

## 🚀 Características

- **Registro de Entradas y Gastos:** Clasificación por categorías (Fijos, Variables, Ocio, Inesperados).
- **Persistencia de Datos:** Almacenamiento local en archivo JSON.
- **Reportes Mensuales:** Filtrado inteligente por mes y año.
- **Gestión de Registros:** Edición y eliminación de movimientos históricos.
- **Validaciones Robustas:** Control de errores en fechas y montos negativos.
- **Arquitectura Modular:** Código refactorizado en capas (Lógica, Persistencia, Utilidades).

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librerías:** `json`, `os`, `datetime`
- **Control de Versiones:** Git & GitHub

## 📋 Cómo Ejecutarlo

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/Gestor-Finanzas-Python.git](https://github.com/TU_USUARIO/Gestor-Finanzas-Python.git)

2. Navega a la carpeta del proyecto:
   ```bash
   cd Gestor-Finanzas-Python

3. Ejecuta el archivo principal:
   ```bash
   python main.py


## 📂 Estructura del proyecto

- main.py: Punto de entrada y menú principal.

- logica.py: Reglas de negocio y orquestación de funciones.

- persistencia.py: Manejo de lectura/escritura en JSON.

- utilidades.py: Herramientas auxiliares (validaciones, limpieza de pantalla).

Desarrollado como proyecto de práctica de Ingeniería de Software.