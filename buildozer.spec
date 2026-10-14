[app]

# (str) Título de tu aplicación
title = Infinity API Apicultura

# (str) Nombre del paquete
package.name = infinityapi

# (str) Dominio del paquete
package.domain = org.apicultura

# (str) Directorio donde está el código fuente
source.dir = .

# (list) Archivos a incluir
source.exts = py,png,jpg,kv,atlas

# (list) Versión de la aplicación
version = 1.0

# (list) Requisitos esenciales de la app
requirements = python3,kivy

# (str) Orientación de la pantalla
orientation = portrait

# (list) Permisos necesarios para almacenamiento local
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Configuración moderna de API y SDK estables
android.target = 33
android.min_api = 21

# (str) Versión de NDK recomendada para evitar conflictos en GitHub
android.ndk = 25b

[buildozer]

# (int) Nivel de log/depuración
log_level = 2

# (int) Construcción en modo depuración
warn_on_root = 1
