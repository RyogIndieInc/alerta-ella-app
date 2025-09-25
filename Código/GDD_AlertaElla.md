# GDD Técnico-Emocional — Alerta Ella

## 🧠 Filosofía RyogDev
Cada función es un acto de homenaje. Cada pantalla es un refugio emocional. Cada decisión técnica se documenta como legado.

---

## 🎯 Propósito de la app
Crear una herramienta gratuita, silenciosa y accesible para mujeres en peligro, que permita enviar una alerta con ubicación en tiempo real a contactos de confianza.

---

## 🧱 Arquitectura base

- **Lenguaje**: Python  
- **Framework móvil**: Kivy  
- **Base de datos local**: SQLite  
- **Geolocalización**: Plyer  
- **Mensajería**: Twilio (SMS) o integración nativa  
- **Modo silencioso**: sin sonido, sin vibración, sin notificaciones visibles

---

## 🧩 Módulos funcionales

### 1. Inicio
- Botón central de alerta
- Lema emocional superior
- Frase simbólica inferior

### 2. Alerta
- Confirmación visual: “Alerta enviada con éxito”
- Animación coral
- Ubicación compartida
- Modo silencioso activo

### 3. Configuración
- Lista editable de contactos (máx. 5)
- Campo de mensaje personalizado
- Toggle de modo silencioso
- Simulación de alerta

### 4. Historial
- Acceso con PIN
- Lista de alertas (fecha, hora, estado, ubicación)
- Detalle por alerta

### 5. Ayuda
- Números de emergencia por país
- Guía emocional
- Enlaces útiles

### 6. Homenaje
- Imagen simbólica
- Historia real
- Frase inspiradora

---

## 🎨 Identidad visual

- **Color principal**: Coral `#FF6F61` — acción urgente sin agresividad  
- **Color secundario**: Violeta suave `#B39DDB` — dignidad femenina  
- **Color de fondo**: Blanco cálido `#FFF8F0` — calma emocional  
- **Tipografía**: Poppins (títulos), Nunito Light (cuerpo)  
- **Iconografía**: Escudo (protección), corazón (empatía), silueta femenina (humanidad)

---

## 🧘 Frases simbólicas por pantalla

| Pantalla       | Frase emocional                     |
|----------------|--------------------------------------|
| Inicio         | Ella no está sola                   |
| Alerta         | Ella está protegida                 |
| Configuración  | Ella decide cómo protegerse         |
| Historial      | Ella recuerda para protegerse       |
| Ayuda          | Ella merece apoyo, no silencio      |
| Homenaje       | Ella merece ser recordada           |

---

## 🧪 Modo simulación
- Permite probar la alerta sin enviar datos reales
- Útil para testeo emocional y técnico

---

## 🔐 Seguridad y privacidad
- Acceso a historial con PIN
- Datos locales, sin almacenamiento en la nube
- Mensajes cifrados en tránsito (si se usa Twilio)

---

## 🧬 Homenaje por versión
Cada versión de la app incluirá una historia real. El diseño se adapta para honrarla: colores, frases, íconos y narrativa.

---

## 🛠️ Próximo paso
- Documentar cada función como entrada pedagógica  
- Crear `Función_Alerta.md`, `Función_Configuración.md`, etc.  
- Iniciar prototipo funcional en Kivy con estructura modular