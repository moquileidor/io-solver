# 🎯 Sistema de Investigación de Operaciones v5

![Visitors](https://img.shields.io/github/visitors/tuuser/io-system?style=flat-square)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Descripción

Sistema inteligente que resuelve **automáticamente** cualquier problema de Investigación de Operaciones usando:

- **Clasificación LLM**: Detecta el tipo de problema
- **Solvers Determinísticos**: scipy, networkx, PuLP para precisión numérica
- **Razonamiento IA**: Groq + OpenAI para explicaciones
- **RAG**: Contextualización con el libro Hillier

## 🚀 Características

✅ 12 tipos de problemas soportados (LP, IP, Transporte, Flujo Máximo, PERT/CPM, Colas, EOQ, NLP, Asignación, Ruta Corta, etc)
✅ Resolución numéricamente exacta (no adivinanzas del LLM)
✅ Respuestas en texto plano legible
✅ Historial en Supabase
✅ Self-consistency para problemas sin solver

## 📋 Instalación

```bash
git clone https://github.com/tuuser/io-system
cd io-system
pip install -r requirements.txt
```

## 🔧 Configuración

```bash
export GROQ_API_KEY="tu_key_aqui"
export SUPABASE_URL="https://tuproject.supabase.co"
export SUPABASE_KEY="tu_secret_key_aqui"
```

## 💻 Uso

```bash
python sistema_io_v5_supabase_final.py
```

Selecciona opción 1 y pega tu problema: