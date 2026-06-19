@echo off
echo 🚀 Iniciando despliegue de Raul Torrescano - Consultoria...
echo.

REM 1. Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no encontrado. Instala Python 3.11 desde python.org
    pause
    exit /b 1
)

REM 2. Crear entorno virtual si no existe
if not exist "venv" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
) else (
    echo ✅ Entorno virtual ya existe
)

REM 3. Activar entorno virtual
echo 📦 Activando entorno virtual...
call venv\Scripts\activate

REM 4. Instalar dependencias
echo 📦 Instalando dependencias...
pip install -r requirements.txt

REM 5. Configurar variables de entorno
if not exist ".env" (
    echo 🔑 Creando archivo .env...
    copy .env.example .env
    echo.
    echo ⚠️  EDITA EL ARCHIVO .env CON TUS DATOS
    echo    - SECRET_KEY: r4u7m4r1f3rv4n3
    echo    - EMAIL_HOST_USER: raul.torrescanog@gmail.com
    echo    - EMAIL_HOST_PASSWORD: r4u7m4r1
    echo.
    pause
)

REM 6. Migrar base de datos
echo 🗄️  Migrando base de datos...
python manage.py makemigrations
python manage.py migrate

REM 7. Crear superuser
echo 👤 Creando superuser...
python manage.py createsuperuser

REM 8. Recolectar archivos estaticos
echo 📁 Recolectando archivos estaticos...
python manage.py collectstatic --noinput

REM 9. Crear carpetas necesarias
if not exist "static\css" mkdir static\css
if not exist "static\js" mkdir static\js
if not exist "static\images" mkdir static\images
if not exist "media\proyectos" mkdir media\proyectos
if not exist "media\blog" mkdir media\blog

echo.
echo ✅ Despliegue completado!
echo.
echo 📋 PROXIMOS PASOS:
echo 1. Ejecuta: python manage.py runserver
echo 2. Ve a: http://127.0.0.1:8000
echo 3. Admin: http://127.0.0.1:8000/admin
echo.
pause