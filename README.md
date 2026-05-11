---
title: IO Solver
emoji: 📘
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.45.1"
python_version: "3.11"
app_file: app.py
pinned: false
license: mit
---

# 🎯 Sistema de Investigación de Operaciones — Web App

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Spaces-Live-blue)](https://huggingface.co/spaces/JorgeAlvarado19/io-solver)

Sistema inteligente que resuelve **automáticamente** problemas de Investigación de Operaciones usando clasificación LLM + solvers determinísticos (scipy, networkx, PuLP) + RAG con el libro Hillier.

## 🚀 Características

- 12 tipos de problemas (LP, IP, Transporte, Flujo Máximo, PERT/CPM, Colas, EOQ, NLP, Asignación, Ruta Corta, etc.)
- Resolución numéricamente exacta con solvers determinísticos
- Respuestas en texto plano (formato terminal)
- RAG con el libro Hillier desde Supabase
- Self-consistency para problemas sin solver

## 📋 Requisitos

- Python 3.10+
- Claves de API: [Groq](https://console.groq.com) y [Supabase](https://supabase.com)

## 💻 Ejecución local

```bash
git clone https://github.com/moquileidor/io-solver
cd io-solver
pip install -r requirements.txt
```

Configurar variables de entorno:
```bash
export GROQ_API_KEY="tu_key"
export SUPABASE_URL="https://tuproject.supabase.co"
export SUPABASE_KEY="tu_key"
```

Iniciar la app web:
```bash
streamlit run app.py
```

## ☁️ Despliegue gratis (Hugging Face Spaces)

1. Crear cuenta en [huggingface.co](https://huggingface.co)
2. Crear Space → SDK **Streamlit** → conectar repo
3. En **Settings → Secrets**:
   - `GROQ_API_KEY`
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
4. Build automático → URL pública