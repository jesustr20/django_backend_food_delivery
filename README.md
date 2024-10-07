### Tecnologías:
poetry
python v3.10.12 (Deseable usar versionador recomendable: Pyenv)
django 5.1.1
django rest framework 3.15.2

### Tecnologías a implementar
docker
kubernetes

### Instalacion de poetry

```bash
1.- curl -sSL https://install.python-poetry.org | python3 -
2.- export PATH="$HOME/.local/bin:$PATH"
3.- source ~/.bashrc   # Para Bash
    source ~/.zshrc    # Para Zsh
4.- poetry --version (probar version)
```

### Iniciar un proyecto con poetry

```bash
1.- poetry init (para iniciar un proyecto)
$ package name [poetry]: <name_project_poetry> (dejar vacío (enter))
$ version [0.1.0]: nil
$ description [ '' ] : nil
$ author [...., skip]: nil
$ license [..]: nil
$ compatible python versions [3.9]: nil
$ question1: no
$ question2: no
$ question3: yes
```

## Instalamos las dependencias del proyecto que estan en poetry

```bash
1.- poetry install
```

## Ver la lista
```bash
poetry env list
```

### Django viene por defecto como base de datos "SQLite"
Creando proyecto con Django:

```python
1.- django-admin startproject <name_project>
```

creando una app con Django

```python
2.- python3 manage.py startapp <name_app>
```

Creando un "suerusuario" de Django

```python
3.- python3 manage.py createsuperuser
```

fields:
- email
- username
- password
- repeat_password

Iniciamos nuestro proyecto

```python
4.- python3 manage.py runserver
```

### Panel admin de Django
```python
http://127.0.0.1:8000/admin/
```

### Api Swagger
```python
http://127.0.0.1:8000/docs/
```

### Nota
- En cada commit que realice el cual involucre que creo
un nuevo "modelo" o se agrego una nueva columna realizar
las migraciones:

```python
1.- python3 manage.py makemigrations
```
```python
2.- python3 manage.py migrate
```

### Tablas
- User
    - lastname
    - firstname
    - email
    - phone_number
    - biography
    - type_user'

- Address
    - address
    - district
    - province
    - department
    - country
    - postal_code
    - user
    - restaurant

- Rating
    - score
    - comment
    - user
    - restaurant

- Order
    - status
    - order_total
    - delivery_status
    - created_at
    - updated_at
    - user
    - driver
    - restaurant

- Driver
    - name
    - phone_number
    - email
    - location
    - vehicle_model
    - vehicle_plate
    - vehicle_color

- Payment
    - amount
    - payment_method
    - status
    - order

- Restaurant
    - name
    - address
    - phone_number

- Menu
    - name
    - description
    - restaurant

### Se agrego DJango_extensions

El uso de este shell ayuda en la interactuación con los modelos y evitar las importaciones dentro del mismo shell (un poco al estilo de ruby on rails)

Para acceder:

```python
2.- python3 manage.py shell_plus
```

Documentation: ```https://django-extensions.readthedocs.io/en/latest/installation_instructions.html```

### Creacion de archivo para borrar el pycache y las migraciones (temporalmente)

El archivo se llama clean_files_temp.py para eliminar las carpetas "__pycache__" y los archivos de migracion que estan dentro de la carpeta "migrations", es temporal el borrado de los archivos de migracion hasta que encuentre una forma de hacer migraciones sin necesidad de borrar todo.

para correrlo:

```python
1.- python3 clean_files_temp.py
2,. python3 manage.py makemigrations
3.- python3 manage.py migrate
4.- python3 manage.py createsuperuser
```