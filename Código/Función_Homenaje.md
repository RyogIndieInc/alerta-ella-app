# Función: Homenaje por versión

## 🎯 Propósito emocional
Honrar la memoria de una mujer real en cada versión de la app. Esta función convierte el diseño en justicia emocional, y cada actualización en un acto de recuerdo.

---

## 🧠 Comportamiento técnico

### 🖼️ Contenido del homenaje
- Imagen simbólica (silueta, ilustración, retrato estilizado)
- Historia breve (nombre opcional, contexto, legado)
- Frase inspiradora (ej. “Su voz vive en esta app”)
- Frase simbólica inferior: “Ella merece ser recordada”

### 🔄 Rotación por versión
- Cada versión de la app incluye un homenaje distinto
- Se define en archivo `homenajes.json` con estructura:

```json
{
  "1.0.0": {
    "nombre": "María",
    "historia": "Abogada valiente que defendió a mujeres en situación de violencia.",
    "frase": "Su voz vive en esta app.",
    "imagen": "maria_silueta.png"
  },
  "1.1.0": {
    "nombre": "Lucía",
    "historia": "Activista que creó redes de apoyo comunitario.",
    "frase": "Ella tejió esperanza.",
    "imagen": "lucia_rosa.png"
  }
}

Al instalar o actualizar, se carga el homenaje correspondiente a la versión

Si no hay conexión, se usa el homenaje local por defecto

📅 Rotación por fecha (opcional)

En fechas conmemorativas (8M, 25N), se muestra homenaje especial

Se define en homenajes_evento.json con lógica de override temporal

🔐 Seguridad

Las historias se almacenan localmente

No se permite edición por parte del usuario

Las imágenes se optimizan para no revelar identidad real

🧘 Narrativa emocional

Esta función es un altar digital. Cada homenaje es una historia que merece ser contada, sin ruido, sin morbo, con respeto. La app no solo protege: recuerda. Cada versión es una vela encendida.

🎨 Interfaz visual
Imagen simbólica centrada

Historia en texto claro y breve

Frase inspiradora destacada

Frase simbólica inferior: “Ella merece ser recordada”

🛠️ Próximo paso

Integrar esta función en el prototipo Kivy

Crear archivo homenajes.json con las primeras historias

Diseñar Pantalla_Homenaje.kv con estructura modular
