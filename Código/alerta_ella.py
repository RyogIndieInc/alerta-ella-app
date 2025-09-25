from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import gps, notification
import time

class AlertaEllaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, background_color=(0, 0, 0, 1))
        self.alert_button = Button(text="Activar Alerta", size_hint=(1, 0.5), background_color=(1, 0, 0, 1), color=(1, 1, 1, 1))
        self.alert_button.bind(on_press=self.activate_alert)
        layout.add_widget(self.alert_button)
        return layout

    def activate_alert(self, instance):
        # Simulación de alerta (reemplazar con lógica real)
        message = "¡Alerta! Estoy en peligro. Ubicación: [a implementar]."
        notification.notify(title="Alerta Activada", message=message, timeout=10)
        print("Alarma silenciosa activada. Enviando notificación...")

if __name__ == "__main__":
    AlertaEllaApp().run()