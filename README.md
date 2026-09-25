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
<img width="297" height="264" alt="loginrellenado" src="https://github.com/user-attachments/assets/8c9f3fc6-ae35-4a75-b761-ffcac8a149af" />


### 2. Panel Principal / Feed y Gestión (Admin & User)
- **Feed Interactivo:** Visualización de posts en orden cronológico inverso, mostrando autor, fecha, categorías asociadas, etiquetas (badges verdes y sección desplegable de comentarios.
<img width="698" height="202" alt="vista de blog" src="https://github.com/user-attachments/assets/b7cee329-14a7-41f4-b706-df692f2488a0" />

- **Filtrado Dinámico:** Selector combobox para filtrar publicaciones por categoría.
<img width="747" height="450" alt="filtrado de blogs por categoria" src="https://github.com/user-attachments/assets/25a4c753-4c5e-4dab-9438-6fdfdc701a04" />

- **Pestaña de Publicación:** Creación de artículos con selección múltiple mediante checkboxes para categorías y tags.
- **Pestañas Exclusivas de Administrador:**
  - *Gestionar Usuarios:* Alta de nuevos usuarios con rol asignado (`ADMIN` / `USER`) y eliminación de usuarios existentes.
<img width="710" height="164" alt="gestion de usuarios(solo admins)" src="https://github.com/user-attachments/assets/0d195e1e-1746-492a-b867-83d6398144fc" />

  - *Categorías & Tags:* Creación rápida de nuevas taxonomías para el blog.

<img width="259" height="151" alt="agregar categorias y tags(solo admins)" src="https://github.com/user-attachments/assets/cfaa4e6b-ed34-4361-a442-955ff430ea02" />

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

