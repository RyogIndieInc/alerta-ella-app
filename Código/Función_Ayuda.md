# Función: Ayuda y recursos

## 🎯 Propósito emocional
Brindar orientación, contención y recursos legales a mujeres en situación de vulnerabilidad. Esta función convierte la información en refugio.

---

## 🧠 Comportamiento técnico

### 📞 Números de emergencia
- Lista por país (configurable)
- Incluye:
  - Policía
  - Línea de ayuda para mujeres
  - ONGs locales
- Se actualiza desde archivo local o API externa

### 📚 Guía emocional
- Texto estático con consejos:
  - Qué hacer si estás en peligro
  - Cómo pedir ayuda
  - Autocuidado post-alerta
- Se muestra en formato de lista o tarjetas

### 🌐 Enlaces útiles
- Chat de ayuda online
- Mapa de comisarías cercanas
- Enlaces a ONGs y recursos legales

### 📍 Geolocalización de comisarías
- Se obtiene ubicación actual con Plyer
- Se consulta API pública (OpenStreetMap, Google Places, etc.)
- Se filtran resultados por categoría: “police station”
- Se muestran en lista con:
  - Nombre
  - Dirección
  - Distancia desde ubicación actual
  - Botón para abrir en mapa externo

---

## 🔐 Seguridad
- No se guarda historial de búsqueda
- No se comparten datos personales
- Enlaces se abren en navegador externo

---

## 🧘 Narrativa emocional
Esta función es un abrazo informativo. No todas las mujeres saben a quién acudir. Aquí, cada número, cada enlace, cada mapa es una mano extendida. La frase “Ella merece apoyo, no silencio” guía cada decisión.

---

## 🎨 Interfaz visual
- Secciones separadas por líneas coral
- Íconos discretos: teléfono, libro, mapa
- Frase simbólica inferior: “Ella merece apoyo, no silencio”

---

## 🛠️ Próximo paso
- Integrar esta función en el prototipo Kivy  
- Crear archivo `Función_Homenaje.md` para documentar el tributo por versión