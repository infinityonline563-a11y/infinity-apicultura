# main.py - Núcleo del Agente Apícola con Interfaz Futurista (Kivy)
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Forzar color de fondo oscuro cibernético en la ventana (#0a1118)
Window.clearcolor = (0.039, 0.066, 0.094, 1)

# Importamos módulos de lógica local si están disponibles en el sistema
try:
    from cerebro import pensar
    from herramientas import (
        cargar_registros,
        guardar_memoria_local,
        ver_estado_dispositivo,
    )
except ImportError:
    # Funciones de respaldo para pruebas aisladas
    def pensar(prompt): return "Análisis de apiario completado: Parámetros estables."
    def cargar_registros(): return [1, 2, 3, 4]
    def guardar_memoria_local(texto): print("Guardado:", texto)
    def ver_estado_dispositivo(): return "Batería OK, Sensores Activos"


class InfinityAPIApp(App):
    def build(self):
        # Contenedor principal vertical con espaciado ciber-físico
        root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 1. Título Superior Estilo Neón
        title_label = Label(
            text='[b]INFINITY-API // APICULTURA[/b]',
            markup=True,
            font_size='20sp',
            color=(0, 0.94, 1, 1),  # Cian brillante
            size_hint_y=None,
            height=40
        )
        root.add_widget(title_label)
        
        # 2. Consola de Estado / Log (Pantalla central)
        registros = cargar_registros()
        total_registros = len(registros) if registros else 0
        estado_inicial = (
            f"Infinity-API V1.0 - Sistema Iniciado.\n"
            f"Control del apiario ciber-físico activo.\n"
            f"Registros locales detectados: {total_registros}\n"
            f"Esperando comandos del apicultor...\n"
        )
        
        self.console = Label(
            text=estado_inicial,
            halign='left',
            valign='top',
            color=(0.7, 0.9, 1, 1),
            font_size='14sp'
        )
        self.console.bind(size=self.console.setter('text_size'))
        root.add_widget(self.console)
        
        # 3. Campo de Entrada Estilo Terminal
        self.user_input = TextInput(
            hint_text='Escribe un comando para el agente...',
            background_color=(0.06, 0.13, 0.2, 1),
            foreground_color=(0, 0.94, 1, 1),
            cursor_color=(0, 0.94, 1, 1),
            size_hint_y=None,
            height=50,
            multiline=False
        )
        root.add_widget(self.user_input)
        
        # 4. Botones de Acción Futuristas (Ejecutar / Ayuda)
        btn_layout = BoxLayout(size_hint_y=None, height=55, spacing=12)
        
        btn_ejecutar = Button(
            text='EJECUTAR CICLO',
            background_color=(0, 0.7, 0.9, 1),
            color=(0.03, 0.05, 0.07, 1),
            bold=True
        )
        btn_ejecutar.bind(on_press=self.ejecutar_ciclo_visual)
        
        btn_ayuda = Button(
            text='ESTADO / AYUDA',
            background_color=(0.1, 0.25, 0.35, 1),
            color=(0, 0.94, 1, 1),
            bold=True
        )
        btn_ayuda.bind(on_press=self.mostrar_ayuda)
        
        btn_layout.add_widget(btn_ejecutar)
        btn_layout.add_widget(btn_ayuda)
        root.add_widget(btn_layout)
        
        return root

    def ejecutar_ciclo_visual(self, instance):
        try:
            estado_telefono = ver_estado_dispositivo()
            registros = cargar_registros()
            total_registros = len(registros) if registros else 0
            
            comando_usuario = self.user_input.text.strip()
            prompt_situacion = (
                f"Registros actuales: {total_registros}. "
                f"Estado del dispositivo: {estado_telefono}. "
                f"Comando manual: {comando_usuario if comando_usuario else 'Ninguno'}"
            )
            
            decision = pensar(prompt_situacion)
            guardar_memoria_local(f"Ciclo ejecutado. Total registros: {total_registros} | Decisión: {decision}")
            
            self.console.text = (
                f"[✔] Ciclo ejecutado con éxito.\n"
                f"- Registros: {total_registros}\n"
                f"- Dispositivo: OK\n"
                f"- Decisión IA: {decision}"
            )
        except Exception as e:
            self.console.text = f"[!] Error en ciclo: {str(e)}"

    def mostrar_ayuda(self, instance):
        self.console.text = (
            "--- AYUDA DEL SISTEMA ---\n"
            "Presiona 'EJECUTAR CICLO' para procesar\n"
            "el estado actual de las colmenas y guardar\n"
            "los registros de forma autónoma."
        )

if __name__ == '__main__':
    InfinityAPIApp().run()
