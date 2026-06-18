# Raúl Torrescano - Consultoría y Desarrollo Web

Sitio web profesional para promover servicios de consultoría y desarrollo web.

## Stack Tecnológico
- Django 4.2
- Tailwind CSS
- SQLite (desarrollo) / PostgreSQL (producción)
- PythonAnywhere (hosting)

## Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/raul_consultoria.git
cd raul_consultoria

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env

# Migrar base de datos
python manage.py migrate

# Crear superuser
python manage.py createsuperuser

# Correr servidor
python manage.py runserver