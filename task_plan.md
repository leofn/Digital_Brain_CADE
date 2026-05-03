# Task Plan: Digital Brain CADE — CLAUDE.md e preparo do Graphify

## Goal
Criar um `CLAUDE.md` robusto em `/home/hermes/brain_cade` para orientar a extração semântica do corpus CADE e deixar o projeto pronto para a etapa seguinte de execução do Graphify.

## Current Phase
Phase 5

## Phases
### Phase 1: Requirements & Discovery
- [x] Confirmar objetivo imediato do usuário
- [x] Localizar repositório, corpus markdown e artefatos atuais
- [x] Inspecionar amostras do corpus e requisitos da ferramenta
- [x] Consolidar achados em `findings.md`
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Definir schema semântico do CADE
- [x] Definir hierarquia de autoridade documental
- [x] Definir entidades, relações, claims e perguntas analíticas prioritárias
- **Status:** complete

### Phase 3: Implementation
- [x] Redigir `/home/hermes/brain_cade/CLAUDE.md`
- [x] Revisar consistência com o corpus existente
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Verificar se o `CLAUDE.md` cobre autoridade, mercado, dano, remédios e evidências
- [x] Verificar aderência ao objetivo do Graphify/Digital Brain
- [x] Registrar próximos comandos de execução
- **Status:** complete

### Phase 5: Delivery
- [x] Entregar resumo objetivo ao usuário
- [x] Informar arquivo criado e próximos passos imediatos
- **Status:** complete

## Key Questions
1. Quais campos semânticos o Graphify deve priorizar para notas técnicas do CADE?
2. Como codificar hierarquia de autoridade, conflitos e remédios concorrenciais no schema?
3. Quais âncoras conceituais precisam aparecer explicitamente para suportar a wiki e o protocolo analítico?

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Criar arquivos de planejamento no diretório do projeto antes de editar o corpus | Preserva contexto e segue o workflow de planejamento obrigatório |
| Redigir o `CLAUDE.md` em linguagem orientada a extração semântica, não a regex | O objetivo é migrar do grafo estrutural para o grafo semântico do artigo |
| Incluir regras explícitas de autoridade e de qualidade de evidência | O corpus mistura descrição factual, avaliação econômica e recomendação institucional |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| `python3 -c "import graphify"` falhou em teste direto | 1 | Registrar discrepância e manter uso do binário `graphify` até validar o ambiente da execução final |

## Notes
- Usar caminhos absolutos.
- Revalidar o plano antes de decisões maiores.
- Registrar achados do corpus antes de escrever a versão final do schema.
