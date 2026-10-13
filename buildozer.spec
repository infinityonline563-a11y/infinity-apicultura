[app]

# (str) Título de tu aplicación
title = Infinity API Apicultura

# (str) Nombre del paquete (sin espacios ni mayúsculas extrañas)
package.name = infinityapi

# (str) Dominio del paquete
package.domain = org.apicultura

# (str) Directorio donde está el código fuente (donde está main.py)
source.dir = .

# (list) Archivos a incluir (agrega .py para que incluya todos tus módulos)
source.exts = py,png,jpg,kv,atlas

# (list) Aplicación y versiones requeridas
version = 1.0

# (list) Aplicación requisitos
# Indicamos que dependemos de python3 y kivy para la interfaz gráfica
requirements = python3,kivy

# (str) Orientación de la pantalla (portrait para vertical, ideal para celular en campo)
orientation = portrait

# (list) Permisos necesarios (por ejemplo, para leer/escribir registros locales)
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]

# (int) Nivel de log/depuración
log_level = 2
