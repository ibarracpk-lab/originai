import os
import streamlit as st
from TTS.api import TTS

st.set_page_config(page_title="OriginAI", page_icon="🎙️")

st.title("OriginAI")
st.subheader("Texto a voz con inteligencia artificial")

texto = st.text_area("Escribe tu texto aquí", height=200)

modelo = "tts_models/es/mai/tacotron2-DDC"

@st.cache_resource
def cargar_tts():
    return TTS(model_name=modelo)

if st.button("Generar voz"):
    if texto.strip():
        with st.spinner("Generando audio..."):
            tts = cargar_tts()

            os.makedirs("outputs", exist_ok=True)
            archivo_salida = "outputs/audio.wav"

            tts.tts_to_file(
                text=texto,
                file_path=archivo_salida
            )

        st.success("Audio generado correctamente")
        st.audio(archivo_salida)

        with open(archivo_salida, "rb") as f:
            st.download_button(
                label="Descargar audio",
                data=f,
                file_name="originai_audio.wav",
                mime="audio/wav"
            )
    else:
        st.warning("Escribe algo primero")