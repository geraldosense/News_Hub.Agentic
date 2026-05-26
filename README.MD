# 🤖 Agentic Newsroom – Arquitetura de Micro-Agentes com IA

## 📌 Visão Geral

Este repositório contém o **Hub Central** para o projeto de **Programação Avançada em Python** (50 Horas).

O projeto funciona como um **ecossistema de micro-serviços** onde cada aluno desenvolve o seu próprio **Agente Independente** que envia notícias processadas por IA para o servidor do professor via API.

---

## 🎯 Objetivo do Projeto

Desenvolver um sistema agêntico descentralizado que utilize as seguintes tecnologias:

| Tecnologia | Aplicação no Projeto |
|:---|:---|
| **APIs & Webhooks** | Comunicação entre servidores via métodos `POST` |
| **Segurança** | Uso de `Headers` e `Tokens` para autenticação de APIs |
| **Programação Assíncrona** | Uso de `asyncio` e `httpx` para não bloquear o servidor |
| **Inteligência Artificial** | Processamento de linguagem natural com Hugging Face |

---

## 🏗️ Estrutura do Ecossistema

| Componente | Responsabilidade | Responsável |
|:---|:---|:---|
| **O Hub** | Recebe e exibe as notícias de todos os alunos em tempo real | Professor |
| **Os Agentes** | Cada aluno corre o seu próprio código que "caça" notícias e as "empurra" (Push) para o Hub | Alunos |

### Diagrama da Arquitetura


---

## 🔐 Dados de Conexão ao Hub

Para que a tua notícia apareça no site da turma, deves usar os seguintes parâmetros:

### Parâmetros de Conexão

| Parâmetro | Valor |
|:---|:---|
| **Método HTTP** | `POST` |
| **Endpoint** | `/publish` |
| **URL Completa** | `http://[IP_DO_PROFESSOR]:8080/publish` |
| **Header de Autenticação** | `x-token: epf2026_secret` |
| **Content-Type** | `application/json` |

### Formato do Payload (JSON)

| Campo | Tipo | Obrigatório | Descrição | Exemplo |
|:---|:---|:---:|:---|:---|
| `agent_name` | string | ✅ | Nome do aluno | `"João Silva"` |
| `topic` | string | ✅ | Categoria da notícia | `"Tecnologia"` |
| `title` | string | ✅ | Título original da notícia | `"Nova IA da Google"` |
| `summary` | string | ✅ | Resumo gerado por IA (max 300 chars) | `"A Google anunciou hoje..."` |
| `url` | string | ✅ | Link da fonte original | `"https://exemplo.com/noticia"` |
| `confidence` | float | ✅ | Nível de confiança (0.0 a 1.0) | `0.95` |

### Exemplo de Payload Completo

```json
{
  "agent_name": "João Silva",
  "topic": "Tecnologia",
  "title": "Google anuncia novo modelo de IA",
  "summary": "A Google revelou hoje o seu mais recente modelo de inteligência artificial, prometendo revolucionar o mercado...",
  "url": "https://tecnologia.pt/google-ia",
  "confidence": 0.95
}


teu_projeto/
│
├── 📂 agents/
│   ├── 📄 __init__.py
│   ├── 📄 base_agent.py
│   └── 📄 joao_silva_agent.py    # ← O teu agente (substituir pelo teu nome)
│
├── 📄 requirements.txt
├── 📄 fake_hub.py                 # Para testes locais
└── 📄 README.md
