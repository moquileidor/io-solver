import io
import contextlib
import streamlit as st

import codigolarryfinalinvop as core

st.set_page_config(
    page_title="IO Solver",
    page_icon="📘",
    layout="wide",
)

st.title("Sistema de Investigación de Operaciones")
st.caption("Pega el enunciado y obtén la solución con formato tipo terminal.")

pregunta = st.text_area("Enunciado del ejercicio", height=260, placeholder="Pega aquí tu ejercicio de IO...")
self_consistency = st.toggle("Self-consistency (más lento, 3 muestreos)", value=False)


@st.cache_resource(show_spinner=False)
def _modelo_embeddings():
    return core.embedding_model


@st.cache_data(show_spinner=False, ttl=3600)
def _df_libro():
    return core.cargar_df_docs()


if st.button("Resolver", type="primary"):
    if not pregunta.strip():
        st.warning("Pega un enunciado primero.")
        st.stop()

    with st.spinner("Resolviendo..."):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            _modelo_embeddings()
            df = _df_libro()
            resultado = core.preguntar_io(
                pregunta.strip(),
                df_libro=df,
                guardar=True,
                self_consistency=self_consistency,
            )
        logs = buf.getvalue()

    st.subheader("Respuesta")
    st.code(resultado.respuesta, language="text")

    if logs.strip():
        with st.expander("Ver logs del proceso"):
            st.code(logs, language="text")
