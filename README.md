# Landing Page con Django

Este es un proyecto básico de una Landing Page desarrollado con Django. Incluye funcionalidades como traducción de idiomas y una base de datos para mostrar contenido dinámico. 

## Características

- **Framework**: Django
- **Traducción de idiomas**: Soporte para múltiples idiomas usando el sistema de internacionalización (i18n) de Django.
- **Base de datos**: Uso de una base de datos para mostrar información dinámica en la Landing Page.
- **Diseño Responsivo**: Adaptado para diferentes tamaños de pantalla.
- **Personalización del Contenido**: Interfaz administrativa para gestionar el contenido de la Landing Page.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior
- Django 5.1.3 o superior
- pip para la gestión de paquetes

---

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

1. Clona este repositorio:
```bash
   git clone https://github.com/erixcel/wynwood.git
```
2. Crear entorno virtual:
```bash
   python -m venv env
```
3. Activar el entorno virtual:
```bash
   source env/bin/activate
```
4. Migrar modelos de base de datos:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
1. Insertar datos:
```bash
   python data-insert.py
```
1. Levantar el servidor:
```bash
   python manage.py runserver
```
1. Visualizar el landing page:
```bash
   http://localhost:8000
```







