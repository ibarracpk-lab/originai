import streamlit as st

st.set_page_config(
    page_title="OriginAI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #081120 0%, #0d1528 100%);
    }
    .bloque {
        padding: 1.2rem;
        border-radius: 18px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1rem;
    }
    .titulo-principal {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }
    .subtitulo {
        font-size: 1.05rem;
        color: #cbd5e1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

voces = [
    "Narrador oscuro",
    "Voz femenina suave",
    "Voz comercial",
    "Épica cinematográfica",
    "Relajante nocturna",
    "Cuenta cuentos",
]

funciones = [
    "Texto a voz",
    "Biblioteca de voces",
    "Historias para TikTok",
    "Panel de proyectos",
    "Clonación de voz",
    "Planes y créditos",
]

casos_de_uso = [
    "Narraciones de terror",
    "Historias para TikTok",
    "Audiolibros cortos",
    "Mensajes publicitarios",
    "Contenido para YouTube",
    "Voces para videojuegos",
]

ruta = [
    "Lanzar la versión funcional de texto a voz",
    "Permitir guardar proyectos y audios",
    "Descargar en MP3 o WAV",
    "Agregar cuentas de usuario",
    "Integrar pagos y membresías",
    "Implementar clonación de voz",
]

with st.sidebar:
    st.title("🎙️ OriginAI")
    st.write("Voces, historias y creación sonora.")
    st.divider()
    st.subheader("Estado")
    st.success("Diseño base activo")
    st.info("Texto a voz en construcción")
    st.warning("Clonación de voz para fase futura")
    st.divider()
    st.subheader("Enfoque")
    st.write("Plataforma para creadores, narradores y proyectos de audio.")

st.markdown('<div class="bloque">', unsafe_allow_html=True)
st.markdown('<div class="titulo-principal">Convierte ideas en voces, y voces en impacto.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitulo">OriginAI está pensada para convertirse en una plataforma completa de audio: texto a voz, historias, proyectos, voces y crecimiento a futuro.</div>',
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Texto a voz", "Activo")
col2.metric("Biblioteca", "Planeada")
col3.metric("Clonación", "Futura")

st.divider()

izq, der = st.columns([1.3, 0.9], gap="large")

with izq:
    st.subheader("Generador principal")
    texto = st.text_area(
        "Escribe tu texto",
        value="Aquella noche, el teléfono volvió a sonar desde la habitación que llevaba años vacía...",
        height=220
    )

    c1, c2 = st.columns(2)
    with c1:
        voz = st.selectbox("Tipo de voz", voces)
    with c2:
        formato = st.selectbox("Formato", ["MP3", "WAV"])

    c3, c4 = st.columns(2)
    with c3:
        velocidad = st.slider("Velocidad", 0, 100, 50)
    with c4:
        emocion = st.slider("Emoción", 0, 100, 65)

    b1, b2, b3 = st.columns(3)
    with b1:
        generar = st.button("🎧 Generar audio", use_container_width=True)
    with b2:
        demo = st.button("▶️ Escuchar demo", use_container_width=True)
    with b3:
        guardar = st.button("💾 Guardar proyecto", use_container_width=True)

    if generar:
        st.success("Aquí conectaremos el motor real de voz.")
        st.write(f"Caracteres: {len(texto)}")
        st.write(f"Voz: {voz}")
        st.write(f"Formato: {formato}")
        st.write(f"Velocidad: {velocidad}")
        st.write(f"Emoción: {emocion}")

    if demo:
        st.info("La demo real vendrá en la siguiente versión.")

    if guardar:
        st.success("Más adelante este botón guardará textos, audios y versiones.")

with der:
    st.subheader("Visión del proyecto")
    st.info(
        "OriginAI no será solo una página. La meta es convertirla en tu taller de voces, "
        "tu fábrica de historias y tu plataforma de creación sonora."
    )

    st.subheader("Lo que debe poder hacer")
    for item in [
        "Generar audio desde texto",
        "Ofrecer distintos estilos de voz",
        "Guardar proyectos",
        "Permitir descarga de resultados",
        "Escalar a usuarios y planes",
    ]:
        st.write(f"• {item}")

st.divider()

st.subheader("Funciones del proyecto")
f1, f2, f3 = st.columns(3)
for col, item in zip([f1, f2, f3], funciones[:3]):
    with col:
        st.container(border=True)
        st.write(f"**{item}**")

f4, f5, f6 = st.columns(3)
for col, item in zip([f4, f5, f6], funciones[3:]):
    with col:
        st.container(border=True)
        st.write(f"**{item}**")

st.divider()

u1, u2 = st.columns(2, gap="large")

with u1:
    st.subheader("Casos de uso")
    for item in casos_de_uso:
        st.write(f"• {item}")

with u2:
    st.subheader("Ruta de crecimiento")
    for i, item in enumerate(ruta, start=1):
        st.write(f"{i}. {item}")

st.divider()
st.caption("OriginAI © 2026 · Plataforma en evolución")