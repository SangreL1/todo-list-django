# 📝 To-Do List Django

Proyecto de lista de tareas desarrollado con **Django**, **Bootstrap**, **MySQL**, **JavaScript** y **CSS**.  
Permite crear, editar, marcar como completadas y eliminar tareas de manera interactiva.

✨ Autor

 **BloodL**

⚠️ **Atención**: Este proyecto es una versión simple de ejemplo. Todas las tareas se muestran para todos los usuarios, sin privacidad individual.

## 🚀 Funcionalidades

- Crear nuevas tareas con título y descripción.
- Marcar tareas como completadas o desmarcarlas.
- Editar y eliminar tareas.
- Confirmación visual antes de eliminar con opción "No volver a preguntar".
- Interfaz responsiva y moderna usando Bootstrap.
- Guardado de datos en MySQL.

## 🛠 Tecnologías usadas

- **Backend:** Django 5
- **Base de datos:** MySQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Control de versiones:** Git y GitHub

## 📂 Estructura del proyecto

todo_list/
│
├── task/ # Aplicación principal
│ ├── migrations/
│ ├── templates/task/
│ └── models.py
├── todo_list/ # Configuración del proyecto
├── manage.py
└── .gitignore


## ⚡ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/todo-list-django.git

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

