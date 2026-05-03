# Findings & Decisions

## Requirements
- Criar `/home/hermes/brain_cade/CLAUDE.md` para orientar a extração semântica do projeto Digital Brain CADE.
- O schema deve refletir a metodologia do artigo de Schrepel: grafo semântico, autoridade documental, conceitos-centrais, claims e base para wiki/query.
- O corpus principal está em `/home/hermes/brain_cade/md/` com 59 arquivos markdown derivados de PDFs/OCR.
- O projeto já possui um grafo inicial baseado em regex em `/home/hermes/brain_cade/graph/`, que será substituído/expandido.

## Research Findings
- Repositório identificado em `/home/hermes/brain_cade`.
- Existem artefatos prévios de extração e visualização: `graph/entities.json`, `graph/triples.json`, `graph/knowledge_graph.html`, `index.html`.
- Há scripts legados em `/home/hermes/brain_cade/scripts/` para OCR, extração e normalização.
- O próximo insumo crítico para a etapa semântica é um `CLAUDE.md` com instruções de domínio CADE.
- O `README.md` confirma o pipeline já executado: 59 PDFs baixados, 59 markdowns gerados e um grafo estrutural prévio via regex.
- A amostra `Nota_T_cnica_n__47___Ato_de_Concentra__o_n__08700_002569_2020_86.md` mostra a estrutura típica do corpus: identificadores processuais, requerentes, advogados, ementa, descrição da operação, análise econômica, métodos quantitativos e conclusões.
- O corpus contém menções recorrentes a `mercado relevante` e `remédios` concorrenciais, o que reforça a necessidade de modelar definição de mercado, riscos, evidências, poder de mercado, fechamento e mitigação.
- A `skill.md` do Graphify deixa claro que o produto esperado é `graphify-out/graph.json` + `GRAPH_REPORT.md` + wiki em markdown, com distinção explícita entre arestas `EXTRACTED`, `INFERRED` e `AMBIGUOUS`.
- O comando `graphify --help` expõe operações úteis para a próxima fase: `update`, `cluster-only`, `query`, `path`, `explain` e geração de wiki.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Usar arquivos de planejamento locais (`task_plan.md`, `findings.md`, `progress.md`) | Facilita continuidade e evita perda de contexto |
| Basear o schema em categorias analíticas de antitruste | Permite extrair relações úteis para hipóteses, wiki e consulta |
| Instruir o `CLAUDE.md` a distinguir fato, inferência e ambiguidade | Alinha a extração ao modelo de auditoria do Graphify |
| Priorizar claims analíticos em nível de argumento, não apenas entidades nominais | O objetivo é reproduzir o Digital Brain semântico, não um inventário regex |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| `python3` não importou o módulo `graphify` diretamente em um teste ad hoc | Seguir usando o binário `graphify` para inspeção/execução e registrar essa discrepância para validar antes da rodada final |

## Resources
- `/home/hermes/brain_cade`
- `/home/hermes/brain_cade/md`
- `/home/hermes/brain_cade/graph`
- `/home/hermes/brain_cade/scripts`

## Visual/Browser Findings
- Nenhum uso de browser nesta etapa.

---
*Update this file after every 2 view/browser/search operations*
*This prevents visual information from being lost*
