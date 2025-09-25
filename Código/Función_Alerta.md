# Función: Enviar alerta silenciosa

## 🎯 Propósito emocional
Permitir que una mujer en peligro pueda enviar una señal silenciosa de auxilio con su ubicación en tiempo real, sin emitir sonido ni vibración. Esta función es el corazón simbólico de Alerta Ella.

---

## 🧠 Comportamiento técnico

### 🔘 Activación
- Se activa al presionar el botón central en la pantalla de inicio.
- No requiere confirmación adicional para evitar demoras.

### 📍 Geolocalización
- Se obtiene la ubicación actual mediante Plyer.
- Se convierte en coordenadas legibles (latitud, longitud).
- Se adjunta al mensaje de alerta.

### ✉️ Mensaje
- Se envía por SMS a los contactos configurados.
- Contenido: mensaje personalizado + ubicación.
- En caso de error, se registra como “Fallida” en el historial.

### 🔕 Modo silencioso
- No se emite sonido, vibración ni notificación visible.
- Se activa desde la pantalla de configuración.

### 🔄 Confirmación visual
- Se muestra pantalla de alerta con mensaje: “Alerta enviada con éxito.”
- Animación coral refuerza la acción.
- Frase simbólica: “Ella está protegida.”

---

## 🧪 Simulación
- Desde configuración, se puede activar “Simular alerta”.
- No envía datos reales, pero reproduce la experiencia visual.

---

## 🔐 Seguridad
- No se guarda la ubicación en la nube.
- Los datos se almacenan localmente en SQLite.
- Se registra en historial con fecha, hora, estado y ubicación.

---

## 🧘 Narrativa emocional
Esta función no es solo código. Es una promesa silenciosa. Cada vez que se activa, se honra una historia real. Cada alerta enviada es un acto de protección, memoria y justicia emocional.

---

## 🛠️ Próximo paso
- Integrar esta función en el prototipo Kivy.
- Crear archivo `Función_Configuración.md` para documentar la personalización.