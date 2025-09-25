# Función: Configuración de Alerta

## 🎯 Propósito emocional
Brindar a la usuaria control sobre su red de protección, el mensaje que envía y el modo en que se activa la alerta. Esta función convierte la urgencia en autonomía.

---

## 🧠 Comportamiento técnico

### 👥 Contactos de emergencia
- Lista editable (máximo 5 contactos)
- Cada contacto incluye nombre y número
- Funciones: añadir, editar, eliminar
- Validación de formato telefónico

### ✉️ Mensaje personalizado
- Campo editable con texto por defecto: “Estoy en peligro”
- Se guarda localmente en SQLite
- Se adjunta automáticamente al mensaje de alerta

### 🔕 Modo silencioso
- Toggle ON/OFF
- Si está activado:
  - No hay sonido, vibración ni notificación visible
  - Se muestra ícono de silencio en pantalla de alerta

### 🧪 Simular alerta
- Botón “Simular alerta”
- Reproduce la experiencia visual sin enviar datos reales
- Útil para testeo emocional y técnico

---

## 🔐 Seguridad
- Cambios se guardan localmente
- No se requiere conexión a internet
- No se comparten datos con terceros

---

## 🧘 Narrativa emocional
Esta función permite que *Ella* decida cómo protegerse. No todas las mujeres tienen las mismas redes, ni los mismos miedos. Esta pantalla es un acto de respeto a su autonomía.

---

## 🛠️ Próximo paso
- Integrar esta función en el prototipo Kivy  
- Crear archivo `Función_Historial.md` para documentar el registro emocional y técnico de alertas