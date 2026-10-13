[app]

# (str) Título de tu aplicación
title = Infinity API Apicultura

# (str) Nombre del paquete (sin espacios ni mayúsculas extrañas)
package.name = infinityapi

# (str) Dominio del paquete
package.domain = org.apicultura

# (str) Directorio donde está el código fuente (donde está main.py)
source.dir = .

# (list) Archivos a incluir (incluyendo tus módulos personalizados .py)
source.exts = py,png,jpg,kv,atlas

# (list) Aplicación y versiones requeridas
version = 1.0

# (list) Requisitos de la aplicación (incluyendo kivy y librerías base)
requirements = python3,kivy

# (str) Orientación de la pantalla (portrait para vertical)
orientation = portrait

# (list) Permisos necesarios para almacenamiento local
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Versión mínima de API de Android soportada
android.api = 33

# (str) Versión de SDK a utilizar
android.sdk = 33

# (str) Versión de NDK recomendada para evitar conflictos de compilación en GitHub
android.ndk = 25b

[buildozer]

# (int) Nivel de log/depuración (2 muestra más detalles si algo falla)
log_level = 2

# (int) Construcción en modo depuración
warn_on_root = 1
