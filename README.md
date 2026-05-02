# 🧠 Digital Brain CADE — Status do Projeto

## Visão Geral
Construção de um grafo de conhecimento a partir das Notas Técnicas do CADE para análise concorrencial.

## Progresso

### ✅ Etapas Concluídas
1. **Download de PDFs**: 59 Notas Técnicas baixadas do Google Drive
2. **Conversão para Markdown**: Todos os 59 PDFs convertidos com sucesso
   - `markitdown` → 29 PDFs convertidos
   - `pymupdf4llm` (fallback) → 30 PDFs restantes convertidos
3. **Extração Estrutural (regex)**: 1379 triplas de 599 entidades
   - Empresas: 175
   - Processos: 217
   - Autores: 114
   - Notas Técnicas: 53
   - Metodologias: 15
   - Mercados: 8 (precisa melhorar com LLM)
   - Anos: 12
   - Tipos de Operação: 5

### 🔄 Em Andamento
4. **Enriquecimento com LLM**: Usar modelo de linguagem para:
   - Melhorar detecção de mercados relevantes (atual: apenas 8 vs ~30+ esperados)
   - Extrair relações semânticas (quem adquire quem, impacto competitivo)
   - Normalizar nomes de empresas com mais precisão

### 📋 Próximos Passos
5. **Integração com Claude Code**: Análise profunda do grafo, queries complexas
6. **Wiki do Digital Brain**: Documentação navegável com páginas por empresa/mercado

## Estrutura de Arquivos
```
~/brain_cade/
├── raw/notas/        # 59 PDFs originais
├── md/               # 59 arquivos Markdown
├── graph/
│   ├── entities.json       # 599 entidades
│   ├── triples.json        # 1379 triplas
│   ├── triples.csv         # Exportação CSV
│   ├── entities.csv        # Exportação CSV
│   ├── documents.json      # Metadados dos documentos
│   └── knowledge_graph.html  # Grafo interativo D3.js
└── scripts/
    ├── convert_pdfs.py          # Conversão PDF→MD
    ├── extract_triples.py       # Extração v1
    ├── extract_triples_v2.py    # Extração v2 (melhorada)
    ├── normalize_v3.py          # Normalização de entidades
    ├── cleanup_markets.py      # Limpeza de mercados
    └── build_graph_v2.py       # Geração do grafo HTML
```

## Scripts Comando Rápido
```bash
# Re-extrair triplas
cd ~/brain_cade && /usr/bin/python3 scripts/extract_triples_v2.py

# Re-normalizar
cd ~/brain_cade && /usr/bin/python3 scripts/normalize_v3.py && /usr/bin/python3 scripts/cleanup_markets.py

# Reconstruir grafo
cd ~/brain_cade && /usr/bin/python3 scripts/build_graph_v2.py
```