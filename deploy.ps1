# deploy.ps1
Write-Host "🚀 Iniciando despliegue de Raul Torrescano - Consultoria..." -ForegroundColor Cyan
Write-Host ""

# Verificar Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python no encontrado. Instala Python 3.11 desde python.org" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

# Crear entorno virtual
if (-not (Test-Path "venv")) {
    Write-Host "📦 Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv venv
} else {
    Write-Host "✅ Entorno virtual ya existe" -ForegroundColor Green
}

# Activar entorno virtual
Write-Host "📦 Activando entorno virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Instalar dependencias
Write-Host "📦 Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

# Configurar .env
if (-not (Test-Path ".env")) {
    Write-Host "🔑 Creando archivo .env..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host ""
    Write-Host "⚠️  EDITA EL ARCHIVO .env CON TUS DATOS" -ForegroundColor Red
    Write-Host "   - SECRET_KEY: genera una clave segura"
    Write-Host "   - EMAIL_HOST_USER: tu email"
    Write-Host "   - EMAIL_HOST_PASSWORD: tu contrasena"
    Write-Host ""
    Read-Host "Presiona Enter cuando hayas editado el archivo .env"
}

# Migrar base de datos
Write-Host "🗄️  Migrando base de datos..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate

# Crear superuser
Write-Host "👤 Creando superuser..." -ForegroundColor Yellow
python manage.py createsuperuser

# Recolectar archivos estaticos
Write-Host "📁 Recolectando archivos estaticos..." -ForegroundColor Yellow
python manage.py collectstatic --noinput

# Crear carpetas
$folders = @("static\css", "static\js", "static\images", "media\proyectos", "media\blog")
foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
    }
}

Write-Host ""
Write-Host "✅ Despliegue completado!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 PROXIMOS PASOS:" -ForegroundColor Cyan
Write-Host "1. Ejecuta: python manage.py runserver"
Write-Host "2. Ve a: http://127.0.0.1:8000"
Write-Host "3. Admin: http://127.0.0.1:8000/admin"
Write-Host ""
Read-Host "Presiona Enter para salir"