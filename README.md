# Proyecto 1 - Bases de Datos Avanzadas
## Sistema de Blog

### Integrantes:
- **377043** – Angel Rodriguez Palomino
- **377304** – Zahid Alberto Jimenes Pérez
- **377061** – Jared Isai López Espino

---

##  Descripción del Proyecto
Sistema para la administración y consumo de publicaciones de un blog, con categorización, etiquetado y comentarios, respaldado por una base de datos Oracle con lógica almacenada en procedimientos y funciones PL/SQL.




## Interfaz de Usuario
La interfaz está construida con **CustomTkinter**, proporcionando una experiencia visual fluida, diseño responsivo y estilo tipo panel administrativo moderno.

### 1. Pantalla de Inicio de Sesión
Autenticación de usuarios validada directamente contra el procedimiento `sp_login` en Oracle.

![Login](docs/screenshots/interfaz_login.png)

### 2. Panel Principal / Feed y Gestión (Admin & User)
- **Feed Interactivo:** Visualización de posts en orden cronológico inverso, mostrando autor, fecha, categorías asociadas (badges naranjas), etiquetas (badges verdes) y sección desplegable de comentarios.
- **Filtrado Dinámico:** Selector combobox para filtrar publicaciones por categoría.
- **Pestaña de Publicación:** Creación de artículos con selección múltiple mediante checkboxes para categorías y tags.
- **Pestañas Exclusivas de Administrador:**
  - *Gestionar Usuarios:* Alta de nuevos usuarios con rol asignado (`ADMIN` / `USER`) y eliminación de usuarios existentes.
  - *Categorías & Tags:* Creación rápida de nuevas taxonomías para el blog.

![Interfaz Principal](docs/screenshots/interfaz_admin.png)

---

## Base de Datos y Modelo de Datos

### Conexión a Base de Datos Oracle (`database.py`)
Módulo encargado de la conexión a la instancia de Oracle mediante `oracledb`:

```python
import oracledb

DB_CONFIG = {
    "user": "blog_user",
    "password": "contra",
    "dsn": "localhost/XEPDB1"
}

def conectar_db():
    return oracledb.connect(**DB_CONFIG)
```

![Conexión a Oracle](docs/screenshots/conexion_oracle.png)

