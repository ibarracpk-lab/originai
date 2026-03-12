import streamlit as st

st.set_page_config(
    page_title="OriginAI",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# ESTILOS
# =========================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #050816 0%, #0b1020 40%, #12182b 100%);
        color: white;
    }

    .main > div {
        padding-top: 1rem;
    }

    h1, h2, h3, h4, h5, h6, p, label, div, span {
        color: white !important;
    }

    .hero-box {
        padding: 2.5rem;
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(0,255,255,0.08), rgba(255,0,170,0.08));
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        margin-bottom: 1.5rem;
    }

    .card {
        padding: 1.4rem;
        border-radius: 24px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 20px rgba(0,0,0,0.20);
        height: 100%;
    }

    .mini-card {
        padding: 1rem;
        border-radius: 18px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        text-align: center;
    }

    .tag {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 700;
        background: rgba(0,255,255,0.12);
        color: #9eefff !important;
        border: 1px solid rgba(0,255,255,0.20);
        margin-bottom: 0.8rem;
    }

    .feature-tag {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 700;
        background: rgba(255,0,170,0.12);
        color: #ffb2e6 !important;
        border: 1px solid rgba(255,0,170,0.18);
        margin-bottom: 0.8rem;
    }

    .roadmap-item {
        padding: 0.9rem 1rem;
        border-radius: 16px;
        background: rgba(0,0,0,0.22);
        border: 1px solid rgba(255,255,255,0.06);
        margin-bottom: 0.8rem;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        margin-top: 0.5rem;
        margin-bottom: 0.3rem;
    }

    .section-subtitle {
        color: #c9d0e3 !important;
        margin-bottom: 1.2rem;
    }

    .footer-box {
        padding: 1.2rem;
        text-align: center;
        color: #b9c2d8 !important;
        border-top: 1px solid rgba(255,255,255,0.08);
        margin-top: 2rem;
    }

    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.18), rgba(255,255,255,0));
        margin: 1.5rem 0;
    }

    div[data-baseweb="select"] > div {
        background-color: rgba(10, 15, 30, 0.9) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
    }

    .stTextArea textarea {
        background-color: rgba(10, 15, 30, 0.92) !important;
        color: white !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
    }

    .stSlider > div > div {
        color: white !important;
    }

    .stButton > button {
        border-radius: 14px !important;
        font-weight: 700 !important;
        padding: 0.6rem 1rem !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
    }

    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .sidebar-text {
        color: #c9d0e3 !important;
        font-size: 0.95rem;
    }

</style>
""", unsafe_allow_html=True)

# =========================
# DATOS
# =========================
features = [
    {
        "title": "Texto a voz",
        "desc": "Convierte guiones, reflexiones, anuncios y relatos en audios con voces naturales.",
        "tag": "Base del proyecto"
    },
    {
        "title": "Biblioteca de voces",
        "desc": "Organiza voces por estilos: terror, épico, suave, comercial, infantil y relajante.",
        "tag": "Escalable"
    },
    {
        "title": "Historias para TikTok",
        "desc": "Crea narraciones cortas con ritmo, impacto y estructura pensada para video corto.",
        "tag": "Creador de contenido"
    },
    {
        "title": "Panel de proyectos",
        "desc": "Guarda textos, títulos, audios y versiones para no perder ninguna idea.",
        "tag": "Organización"
    },
    {
        "title": "Clonación de voz",
        "desc": "Sección futura para crear voces personalizadas a partir de muestras de audio.",
        "tag": "Próximamente"
    },
    {
        "title": "Planes y créditos",
        "desc": "Prepara el sistema para usuarios gratis, premium, límites y recargas.",
        "tag": "Negocio"
    }
]

use_cases = [
    "Narraciones de terror",
    "Historias para TikTok",
    "Audiolibros cortos",
    "Mensajes publicitarios",
    "Contenido para YouTube",
    "Voces para videojuegos",
    "Podcasts",
    "Personajes y doblaje"
]

roadmap = [
    "Lanzar una versión funcional de texto a voz",
    "Permitir guardar proyectos y audios",
    "Descargar resultados en MP3 o WAV",
    "Crear biblioteca de voces por estilos",
    "Añadir cuentas de usuario",
    "Integrar pagos y membresías",
    "Implementar clonación de voz",
    "Abrir una API para terceros"
]

voices = [
    "Narrador oscuro",
    "Voz femenina suave",
    "Voz comercial",
    "Épica cinematográfica",
    "Relajante nocturna",
    "Cuenta cuentos"
]

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown('<div class="sidebar-title">🎙️ OriginAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-text">Voces, historias y creación sonora en un solo lugar.</div>', unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    st.subheader("Estado del proyecto")
    st.success("Texto a voz: activo")
    st.info("Diseño visual: listo")
    st.warning("Clonación de voz: futura fase")
    st.caption("La idea es empezar funcional y luego convertirlo en plataforma completa.")

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    st.subheader("Ruta rápida")
    for i, item in enumerate(roadmap[:5], start=1):
        st.markdown(f"**{i}.** {item}")

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    st.subheader("Marca")
    st.write("**Nombre:** OriginAI")
    st.write("**Estilo:** oscuro, futurista, creativo")
    st.write("**Enfoque:** creadores, narradores y negocio")

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero-box">
    <div class="tag">Plataforma creativa de voz con visión de crecimiento</div>
    <h1 style="font-size: 3.4rem; font-weight: 900; line-height: 1.1; margin-bottom: 0.8rem;">
        Convierte ideas en voces, y voces en impacto.
    </h1>
    <p style="font-size: 1.1rem; max-width: 850px; color: #d2d9ea !important;">
        OriginAI nace para crear audios, narraciones y proyectos de voz desde un solo lugar.
        Empieza como herramienta de texto a voz, pero está pensado para crecer hacia una plataforma completa:
        historias, voces, proyectos, clonación y monetización.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="mini-card">
        <div style="font-size: 0.95rem; color: #bfc8dd !important;">Texto a voz</div>
        <div style="font-size: 1.25rem; font-weight: 800;">Activo</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="mini-card">
        <div style="font-size: 0.95rem; color: #bfc8dd !important;">Biblioteca</div>
        <div style="font-size: 1.25rem; font-weight: 800;">Planeada</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="mini-card">
        <div style="font-size: 0.95rem; color: #bfc8dd !important;">Clonación de voz</div>
        <div style="font-size: 1.25rem; font-weight: 800;">Futura</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

# =========================
# GENERADOR PRINCIPAL
# =========================
left, right = st.columns([1.15, 0.85], gap="large")

with left:
    st.markdown('<div class="section-title">Generador principal</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Esta será la herramienta central de OriginAI. Aquí empieza la magia.</div>', unsafe_allow_html=True)

    text_input = st.text_area(
        "Escribe tu texto",
        value="Aquella noche, el teléfono volvió a sonar desde la habitación que llevaba años vacía...",
        height=220
    )

    col_a, col_b = st.columns(2)
    with col_a:
        selected_voice = st.selectbox("Tipo de voz", voices)
    with col_b:
        output_format = st.selectbox("Formato", ["MP3", "WAV"])

    col_c, col_d = st.columns(2)
    with col_c:
        speed = st.slider("Velocidad", 0, 100, 50)
    with col_d:
        emotion = st.slider("Emoción", 0, 100, 65)

    col_e, col_f, col_g = st.columns(3)
    with col_e:
        generate = st.button("🎧 Generar audio", use_container_width=True)
    with col_f:
        preview = st.button("▶️ Escuchar demo", use_container_width=True)
    with col_g:
        save_project = st.button("💾 Guardar proyecto", use_container_width=True)

    if generate:
        st.success("Aquí irá la generación real del audio cuando conectemos el motor de voz.")
        st.info(f"Texto recibido: {len(text_input)} caracteres | Voz: {selected_voice} | Formato: {output_format}")

    if preview:
        st.warning("La vista previa aún es visual. En el siguiente paso la conectamos al motor de voz real.")

    if save_project:
        st.success("Más adelante este botón guardará textos, audios y versiones del proyecto.")

with right:
    st.markdown("""
    <div class="card">
        <div class="tag">Visión del proyecto</div>
        <h3 style="margin-top: 0;">OriginAI no será solo una página</h3>
        <p style="color: #d2d9ea !important;">
            Será tu taller de voces, tu fábrica de historias y tu laboratorio creativo.
            La meta no es solo narrar texto, sino construir una plataforma propia que después puedas vender,
            mejorar y expandir.
        </p>
        <h4 style="margin-top: 1.5rem;">Lo que debe poder hacer</h4>
        <ul>
            <li>Generar audio desde texto</li>
            <li>Ofrecer estilos de voz</li>
            <li>Guardar proyectos</li>
            <li>Descargar resultados</li>
            <li>Crear una experiencia bonita y profesional</li>
            <li>Crecer a planes y usuarios</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

# =========================
# FUNCIONES
# =========================
st.markdown('<div class="section-title">Funciones que le dan forma al proyecto</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Primero resolvemos la herramienta central y luego levantamos el castillo completo, piedra por piedra.</div>', unsafe_allow_html=True)

row1 = st.columns(3)
row2 = st.columns(3)

all_cols = row1 + row2

for col, feature in zip(all_cols, features):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="feature-tag">{feature["tag"]}</div>
            <h3 style="margin-top: 0;">{feature["title"]}</h3>
            <p style="color: #d2d9ea !important;">{feature["desc"]}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

# =========================
# CASOS DE USO Y ROADMAP
# =========================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="section-title">Casos de uso</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Todo lo que puedes mover con una plataforma de voz bien hecha.</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    for item in use_cases:
        st.markdown(f"- {item}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-title">Ruta de crecimiento</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Así pasamos de herramienta bonita a plataforma seria.</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    for i, item in enumerate(roadmap, start=1):
        st.markdown(f"""
        <div class="roadmap-item">
            <strong>{i}.</strong> {item}
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

# =========================
# LLAMADO FINAL
# =========================
st.markdown("""
<div class="hero-box">
    <div class="tag">Siguiente etapa</div>
    <h2 style="font-size: 2.3rem; font-weight: 900; margin-bottom: 0.6rem;">
        Ya tienes imagen, estructura y dirección.
    </h2>
    <p style="font-size: 1.05rem; color: #d2d9ea !important; max-width: 900px;">
        El siguiente paso es conectar esta interfaz con el motor real de voz para que OriginAI no solo se vea bien:
        que también hable, genere, descargue y empiece a funcionar como una plataforma de verdad.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-box">
    OriginAI © 2026 · Plataforma en evolución · Hecha para crear voces con identidad propia
</div>
""", unsafe_allow_html=True)