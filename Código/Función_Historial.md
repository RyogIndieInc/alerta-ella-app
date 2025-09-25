# Función: Historial de alertas

## 🎯 Propósito emocional
Registrar cada alerta enviada como acto de memoria, seguimiento y protección. Esta función convierte el pasado en legado, sin vulnerar la privacidad de la usuaria.

---

## 🧠 Comportamiento técnico

### 📅 Registro de alertas
- Cada alerta se guarda con:
  - Fecha y hora
  - Estado: Enviada, Fallida, Simulada
  - Ubicación compartida
  - Contactos que la recibieron
  - Mensaje enviado

- Se almacena en base de datos local (SQLite)

### 🔐 Acceso seguro
- Requiere PIN de 4 dígitos
- Campo de ingreso con validación
- Intentos fallidos limitados (máx. 3)
- Opción de recuperación con pregunta secreta

### 🧠 Reconocimiento facial (opcional)
- Integración con librería de cámara (OpenCV o KivyMD)
- Solo en dispositivos compatibles
- Se activa desde configuración
- No se almacena imagen, solo patrón biométrico local

### 🔒 Cifrado de datos
- Cifrado AES para campos sensibles
- Clave generada localmente y almacenada en archivo oculto
- Datos cifrados: ubicación, contactos, mensaje

---

## 🧘 Narrativa emocional
Cada alerta registrada es una historia que merece ser protegida. El historial no es solo una lista: es un archivo de resistencia, un testimonio silencioso. La privacidad es parte del homenaje.

---

## 🎨 Interfaz visual
- Lista cronológica con fecha, estado y ubicación
- Íconos discretos para cada tipo de alerta
- Acceso con PIN o rostro
- Frase simbólica inferior: “Ella recuerda para protegerse”

---

## 🛠️ Próximo paso
- Integrar esta función en el prototipo Kivy  
- Crear archivo `Función_Ayuda.md` para documentar recursos emocionales y legales