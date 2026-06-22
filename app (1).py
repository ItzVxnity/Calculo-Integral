import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Sólido de Revolución", layout="wide")
st.title("Sólido de Revolución · Instrumento de cálculo")
st.markdown(
    "Este proyecto usa la interfaz existente de `index.html` y la carga dentro de Streamlit. "
    "Si la vista no se renderiza bien, puedes abrir `index.html` directamente."
)

html_path = Path(__file__).parent / "index.html"
if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    components.html(html, height=900, scrolling=True)
else:
    st.error("No se encontró el archivo `index.html`. Asegúrate de que esté en la raíz del repositorio.")
