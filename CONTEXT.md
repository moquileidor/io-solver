# IO Solver — Contexto del Proyecto

## ¿Qué es esto?

Sistema que resuelve automáticamente problemas de **Investigación de Operaciones** usando clasificación LLM + solvers determinísticos (scipy, networkx, PuLP) + RAG con el libro Hillier desde Supabase.

El motor actual soporta: LP, IP, Transporte (2 capas y con intermedios), Asignación (Húngaro), Flujo Máximo, Ruta Corta, PERT/CPM, Colas M/M/1 y M/M/c, EOQ, NLP.

## Estado actual (7 mayo 2026)

El proyecto empezó como un **notebook de Colab** (`CodigoLarryFinalInvOp.ipynb`) que fue exportado a Python. Hoy se migró a una **app web Streamlit** desplegable gratis en Hugging Face Spaces.

### Commit base: `3590a86 feat: add Streamlit web app for IO solver with RAG`

Archivos en el repo:

| Archivo | Rol |
|---|---|
| `codigolarryfinalinvop.py` | Motor principal (clasificación, solvers, RAG, prompts, historial). Todo el pipeline. |
| `app.py` | Streamlit UI (textarea + botón + spinner + salida terminal). Cachea modelo y libro. |
| `requirements.txt` | Dependencias para build en HF Spaces. |
| `.gitignore` | Ignora `.env`, caches, secretos locales. |
| `README.MD` | Documentación de instalación y deploy. |
| `CONTEXT.md` | Este archivo. |

## Cambios aplicados en el commit actual

1. **Limpieza de código Colab/CLI**:
   - Eliminada línea `!python sistema_io_sqlite.py` (solo funciona en Colab).
   - Eliminado `import subprocess` + `_ensure()` que hacía `pip install` en runtime.

2. **Seguridad** (parcial):
   - Claves API movidas a `os.environ["..."]` sin defaults hardcodeados.
   - Las claves se configuran como Secrets en HF Spaces.

3. **Paginación en carga del libro** (`cargar_df_docs()`):
   - Ahora lee en bloques de 1000 filas (`.range()`) para no truncar si hay > 1000 chunks.

4. **Caché de historial optimizado** (`respuesta_en_cache()`):
   - Limitado a las últimas 200 filas en vez de escanear toda la tabla `ejercicios_io`.

5. **Nueva UI web** (`app.py`):
   - Streamlit: textarea + toggle self-consistency + botón + salida en `st.code()`.
   - Cachea modelo de embeddings y DataFrame del libro con `st.cache_resource` / `st.cache_data`.
   - Captura `print()` del motor via `redirect_stdout` y los muestra en expander opcional.
   - Historial se guarda silenciosamente.

6. **README actualizado** con instrucciones de instalación y deploy.

## Pendiente / por mejorar

### Seguridad
- [ ] **Rotar/revocar las claves Groq y Supabase** que estaban hardcodeadas en la versión original (visible en Colab, se subió al repo, etc.). Las claves viejas ya están expuestas y deben revocarse desde los dashboards. Cualquiera que las tenga puede gastar crédito Groq o acceder a Supabase.
- [ ] Endurecer `eval` en NLP. Hoy usa `compile()` + `eval()` con `__builtins__={}`, pero no es un sandbox seguro para web pública. Alternativa: parser AST con whitelist de nodos.

### Performance
- [ ] Migrar retrieval RAG a **pgvector en Supabase** (RPC `match_documentos`) en vez de descargar todos los embeddings al servidor.
- [ ] Hacer lazy la carga del modelo `SentenceTransformer` para que no bloquee el import (usar `@st.cache_resource` ya, pero igual se carga al importar el módulo).
- [ ] Considerar modelo de embeddings más pequeño si cold start es muy lento.

### UX / Funcionalidad
- [ ] Verificar que tipos "LP", "IP", "TRANSPORTE", "ASIGNACION", "FLUJO_MAX", "RUTA_CORTA", "PERT_CPM", "COLAS_MM1", "COLAS_MMC", "EOQ", "NLP", "OTRO" se resuelven correctamente en la web.
- [ ] Probar con enunciados reales y comparar output con la versión Colab.
- [ ] Evaluar si `self-consistency` (3 muestras) tiene sentido en web o se puede simplificar.

### Infraestructura
- [ ] Probar deploy en Hugging Face Spaces (SDK Streamlit).
- [ ] Verificar que `requirements.txt` no tenga conflictos de versiones.
- [ ] Opcional: CI/CD con GitHub Actions para deploy automático a Spaces.

## Arquitectura

```
Usuario (navegador)
    │
    ▼
app.py (Streamlit)
    │
    ├── cache modelo embeddings (SentenceTransformer)
    ├── cache DataFrame libro (desde Supabase)
    │
    ▼
codigolarryfinalinvop.py  (motor)
    │
    ├── 1. Cache de repetición (sim ≥ 0.99 contra últimas 200 consultas)
    ├── 2. Clasificar tipo (heurísticas + LLM Groq)
    ├── 3. Solver determinístico (scipy / PuLP / networkx)
    ├── 4. RAG → top-k chunks del libro Hillier (cosine local)
    ├── 5. Prompt enriquecido → LLM explicación (Groq)
    └── 6. Guardar historial en Supabase (silencioso)
```

Dependencias externas:
- **Groq** (LLM para clasificación y explicación)
- **Supabase** (almacena chunks del libro + embeddings + historial)
- **Hugging Face** (modelo `paraphrase-multilingual-MiniLM-L12-v2` para embeddings)

## Cómo contribuir

1. Clonar repo, `pip install -r requirements.txt`.
2. Configurar `GROQ_API_KEY`, `SUPABASE_URL`, `SUPABASE_KEY`.
3. `streamlit run app.py`.
4. El libro ya está cargado en Supabase, no hace falta tener el PDF local.
