import streamlit as st

# -------------------------------
# 🧠 PREGUNTAS directamente en el código
# -------------------------------
preguntas = [
    {
        "pregunta": "¿Qué es el trauma psicológico?",
        "opciones": [
            "Un trastorno de la personalidad",
            "Una respuesta emocional frente a una experiencia dolorosa o amenazante",
            "Un tipo de esquizofrenia",
            "Una fase normal del desarrollo"
        ],
        "respuesta_correcta": 1,
        "justificacion": "El trauma psicológico es una respuesta emocional intensa frente a una experiencia percibida como peligrosa, abrumadora o aterradora."
    },
    {
        "pregunta": "¿Qué evento podría potencialmente causar un trauma psicológico?",
        "opciones": [
            "Una discusión amistosa",
            "Un examen académico",
            "Un accidente grave o abuso",
            "Un malentendido en el trabajo"
        ],
        "respuesta_correcta": 2,
        "justificacion": "Eventos como abusos, accidentes graves, desastres naturales o violencia pueden superar la capacidad de afrontamiento de una persona, generando una respuesta traumática."
    },
    {
        "pregunta": "¿Qué trastorno se asocia comúnmente con el trauma psicológico?",
        "opciones": [
            "Trastorno obsesivo-compulsivo",
            "Trastorno de ansiedad generalizada",
            "Trastorno de estrés postraumático (TEPT)",
            "Trastorno bipolar"
        ],
        "respuesta_correcta": 2,
        "justificacion": "El TEPT es la condición más comúnmente vinculada con trauma psicológico. Se manifiesta con recuerdos intrusivos, pesadillas, hipervigilancia y evitación."
    },
    {
        "pregunta": "¿Cuál de los siguientes síntomas es típico del TEPT?",
        "opciones": [
            "Alucinaciones auditivas",
            "Reexperimentación del evento traumático",
            "Euforia constante",
            "Dependencia emocional"
        ],
        "respuesta_correcta": 1,
        "justificacion": "Las personas con TEPT suelen revivir el trauma a través de recuerdos intrusivos, pesadillas o flashbacks."
    },
    {
        "pregunta": "¿Qué significa 'disociación' en el contexto del trauma?",
        "opciones": [
            "Pérdida de habilidades cognitivas",
            "Inestabilidad emocional extrema",
            "Desconexión de pensamientos, emociones o identidad frente al trauma",
            "Incapacidad para tomar decisiones"
        ],
        "respuesta_correcta": 2,
        "justificacion": "La disociación es un mecanismo de defensa que separa a la persona del evento traumático, como si no le estuviera ocurriendo a ella misma."
    },
    {
        "pregunta": "¿Cuál afirmación sobre el trauma complejo es correcta?",
        "opciones": [
            "Solo se produce por una única experiencia traumática",
            "Está relacionado con múltiples experiencias traumáticas prolongadas, especialmente en la infancia",
            "Afecta solo a personas con trastornos genéticos",
            "No tiene relación con las relaciones interpersonales"
        ],
        "respuesta_correcta": 1,
        "justificacion": "El trauma complejo suele desarrollarse tras experiencias repetidas de abuso, negligencia o abandono, especialmente en la infancia."
    },
    {
        "pregunta": "¿Qué factor puede aumentar la vulnerabilidad al trauma?",
        "opciones": [
            "Tener una red de apoyo sólida",
            "Habilidades de afrontamiento efectivas",
            "Historia previa de abuso o negligencia",
            "Buen estado físico"
        ],
        "respuesta_correcta": 2,
        "justificacion": "Experiencias traumáticas previas hacen a la persona más vulnerable a futuros eventos traumáticos."
    },
    {
        "pregunta": "¿Qué técnica se utiliza para tratar el trauma psicológico?",
        "opciones": [
            "Terapia electroconvulsiva",
            "Terapia cognitivo-conductual enfocada en el trauma",
            "Psicoanálisis clásico",
            "Hipnosis de entretenimiento"
        ],
        "respuesta_correcta": 1,
        "justificacion": "La terapia cognitivo-conductual enfocada en el trauma es eficaz para tratar TEPT y otros trastornos relacionados."
    },
    {
        "pregunta": "¿Qué es la 'ventana de tolerancia'?",
        "opciones": [
            "El tiempo de recuperación del trauma",
            "Una técnica para evaluar la memoria",
            "El rango emocional donde una persona puede funcionar sin desregularse",
            "Un tipo de trauma infantil"
        ],
        "respuesta_correcta": 2,
        "justificacion": "La ventana de tolerancia es el rango óptimo de activación emocional donde una persona puede procesar información sin entrar en pánico o desconectarse."
    },
    {
        "pregunta": "¿Cuál es una posible manifestación del trauma no procesado?",
        "opciones": [
            "Alta autoestima",
            "Sueño reparador",
            "Reacciones emocionales intensas ante estímulos menores",
            "Razonamiento lógico aumentado"
        ],
        "respuesta_correcta": 2,
        "justificacion": "El trauma no procesado puede causar reacciones emocionales desproporcionadas frente a estímulos que activan recuerdos traumáticos."
    }
]

# -------------------------------
# ESTADO DE SESIÓN
# -------------------------------
if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'puntaje' not in st.session_state:
    st.session_state.puntaje = 0
if 'respuesta_mostrada' not in st.session_state:
    st.session_state.respuesta_mostrada = False
if 'respuesta_correcta' not in st.session_state:
    st.session_state.respuesta_correcta = None

# -------------------------------
# FUNCIONES
# -------------------------------

def mostrar_pregunta():
    idx = st.session_state.indice
    pregunta = preguntas[idx]
    
    st.markdown(f"### Pregunta {idx + 1} de {len(preguntas)}")
    st.write(pregunta["pregunta"])

    opciones = pregunta["opciones"]
    correcta = pregunta["respuesta_correcta"]
    justificacion = pregunta["justificacion"]

    opcion = st.radio("Selecciona una opción:", opciones, key=f"opcion_{idx}")

    if st.button("Responder"):
        if st.session_state.respuesta_mostrada:
            st.warning("Ya respondiste esta pregunta.")
            return

        if opciones.index(opcion) == correcta:
            st.success("✅ ¡Correcto!")
            st.session_state.puntaje += 1
            st.session_state.respuesta_correcta = True
        else:
            st.error("❌ Incorrecto.")
            st.session_state.respuesta_correcta = False

        st.info(f"**Justificación:** {justificacion}")
        st.session_state.respuesta_mostrada = True

    if st.session_state.respuesta_mostrada:
        if st.button("Siguiente"):
            st.session_state.indice += 1
            st.session_state.respuesta_mostrada = False
            st.session_state.respuesta_correcta = None

def mostrar_resultado():
    total = len(preguntas)
    correctas = st.session_state.puntaje
    porcentaje = round((correctas / total) * 100, 2)

    st.balloons()
    st.success("🎉 ¡Has completado el cuestionario!")
    st.write(f"**Respuestas correctas:** {correctas} de {total}")
    st.write(f"**Porcentaje de aciertos:** {porcentaje}%")

    if st.button("Reiniciar"):
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.respuesta_mostrada = False
        st.session_state.respuesta_correcta = None

# -------------------------------
# INTERFAZ PRINCIPAL
# -------------------------------
st.set_page_config(page_title="Cuestionario Trauma Psicológico", page_icon="🧠")
st.title("🧠 Cuestionario: Trauma Psicológico")

if st.session_state.indice < len(preguntas):
    mostrar_pregunta()
else:
    mostrar_resultado()
