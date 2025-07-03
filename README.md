# Sistema de Gestión de Empleados y Departamentos

Este proyecto es un sistema simple de gestión interna para una empresa, que permite administrar empleados y departamentos utilizando **Python** y **MySQL**. Fue diseñado con un enfoque educativo para aprender integración de bases de datos con Python, buenas prácticas y organización modular del código.

---

## 📦 Características principales

- ABM (Alta, Baja, Modificación) de empleados y departamentos
- Validación de datos (email, salario, etc.)
- Uso de variables de entorno con `.env`
- Interfaz por consola con menú
- Organización modular y clara del código

---

## 📁 Estructura del proyecto
bdo_gestion/
├── .env
├── db/
│ ├── connection.py
│ └── init_db.sql
├── models/
│ ├── empleados.py
│ └── departamentos.py
├── services/
│ └── validaciones.py
├── main.py
├── requirements.txt
└── README.md
---

## Pasos para correr el proyecto

### 1. Clonar o descargar el repositorio

```bash
git clone https://github.com/capacitacionRHR/test.git
cd <carpeta_que_se_crea>

---

## Activar el entorno

# En Linux / macOS
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
-> pip install -r requirements.txt

-> Crear la bd:
CREATE DATABASE bdo_gestion;
USE bdo_gestion;
-> Ejecutar el script sql

-> crear .env a partir del .env.example y completar con los datos

-> correr con : py main.py

