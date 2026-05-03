# CLAUDE.md — Digital Brain CADE

## Objetivo
Este repositório contém um corpus de **Notas Técnicas do CADE/DEE** convertidas de PDF para Markdown. Ao analisar este corpus, priorize **extração semântica em nível de argumento** para construir um **grafo de conhecimento de antitruste**: não apenas quem é quem, mas **quais mercados foram definidos, quais teorias de dano foram aventadas, quais evidências foram aceitas/rejeitadas, quais eficiências foram alegadas, quais remédios foram recomendados/impostos e qual foi a conclusão analítica**.

O objetivo final é reproduzir um **Digital Brain** do CADE: grafo semântico + comunidades + wiki + consulta por hipóteses.

---

## Escopo do corpus
Assuma que os documentos podem conter:
- notas técnicas do **DEE/CADE**,
- referências a **SG/CADE**, **Tribunal do CADE**, **Conselheiro-Relator**, **ProCADE**,
- referências a **Lei 12.529/2011**, ACC/TCC, despachos, pareceres, testes de mercado, bases de dados, pareceres econômicos de requerentes,
- trechos com **OCR imperfeito**, caracteres corrompidos, cabeçalhos repetidos do SEI e indicações como `picture intentionally omitted`.

Trate o corpus como **documentação institucional e analítica**, não como texto narrativo genérico.

---

## Unidade principal de extração
A unidade analítica mais importante é a **proposição substantiva**. Extraia:
1. **Entidades** relevantes,
2. **Relações** entre entidades,
3. **Claims analíticos** quando o texto faz uma afirmação economicamente ou juridicamente relevante,
4. **Evidências** que suportam ou enfraquecem claims,
5. **Resultados** (conclusão, recomendação, remédio, monitoramento, descumprimento, revisão, multa).

Não se limite a nomes próprios. O valor do grafo está em capturar estruturas como:
- `Operação -> gera preocupação -> fechamento de mercado`
- `Nota Técnica -> questiona -> hipótese de Nash-Cournot`
- `ACC cláusula 2.1 -> foi descumprida por -> compromissária`
- `Avaliação ex-post -> estima -> aumento de preço de 4,9% a 13,5%`
- `DEE -> recomenda -> remédios comportamentais`

---

## Hierarquia de autoridade documental
Ao extrair claims, registre implicitamente a **autoridade da fonte**. Use a seguinte hierarquia:

### Nível A — autoridade normativa/decisória
- Lei 12.529/2011 e demais bases legais citadas
- decisões do Tribunal/Plenário do CADE
- ACC, TCC e outros compromissos formais
- despachos decisórios e determinações formais

### Nível B — autoridade institucional probatória
- pareceres da SG/CADE
- manifestações da ProCADE
- respostas a ofícios, testes de mercado, dados oficiais dos autos
- cláusulas específicas de ACC/TCC e seu monitoramento

### Nível C — autoridade analítica
- notas técnicas do DEE
- pareceres econômicos apresentados pelas requerentes
- estudos econométricos, modelos quantitativos e simulações

### Nível D — baixa autoridade / alta cautela
- argumentos alegados sem comprovação suficiente
- proxies frágeis
- hipóteses não testadas
- texto redigido com OCR defeituoso ou excessivamente ambíguo

**Regra crítica:** quando a nota técnica apenas relata o argumento de terceiros, modele isso como `argumenta`, `alega`, `sustenta`, `questiona`, `rejeita`, e não como fato estabelecido.

---

## Classes de nós prioritárias
Ao extrair, priorize os seguintes tipos de nó.

### 1. Caso / procedimento
- Ato de Concentração
- Processo administrativo
- Apartado
- Revisão de operação
- Monitoramento de ACC/TCC

### 2. Documento institucional
- Nota técnica
- Parecer
- Despacho
- Decisão
- Ofício
- Teste de mercado
- Parecer econômico

### 3. Atores
- Requerentes
- Empresas adquirentes / alvo
- Grupos econômicos
- Concorrentes
- Clientes
- Fornecedores
- Órgãos e unidades do CADE (DEE, SG, Tribunal, ProCADE)
- Conselheiro-Relator

### 4. Mercados
- mercado relevante de produto
- mercado relevante geográfico
- elo da cadeia / estágio vertical
- segmento setorial

Sempre que possível, represente **mercado de produto** e **mercado geográfico** separadamente, além do mercado combinado quando explicitamente definido.

### 5. Teorias de dano / preocupações concorrenciais
- efeitos unilaterais
- efeitos coordenados
- fechamento de mercado
- aumento de custos de rivais
- discriminação de concorrentes
- alavancagem vertical
- integração vertical problemática
- barreiras à entrada
- dominância / poder de mercado
- risco de coordenação tácita
- redução de rivalidade

### 6. Eficiências
- sinergias
- integração vertical eficiente
- economias de escala
- ganhos de produtividade
- inovação / P&D
- repasse de eficiências ao consumidor

### 7. Evidências e métricas
- market share
- HHI / concentração
- GUPPI / vGUPPI / CPPI
- teste do monopolista hipotético (TMH)
- teste de Forni
- ADF / KPSS / Phillips-Perron
- elasticidades
- taxas de desvio
- margens
- séries de preços
- coeficiente de importação
- custos logísticos
- manifestações de clientes/concorrentes
- precedentes e jurisprudência do CADE

### 8. Remédios e resultados
- remédio comportamental
- remédio estrutural
- ACC / TCC
- obrigação de fazer / não fazer
- monitoramento
- multa
- descumprimento de cláusula
- aprovação sem restrições
- aprovação com restrições
- revisão / reabertura / intervenção ex-post

### 9. Cláusulas específicas
Quando houver ACC/TCC, crie nós para cláusulas materiais relevantes, por exemplo:
- `ACC Cláusula 2.1 — produção mínima`
- `ACC Cláusula 2.7 — investimento em P&D`
- `ACC Cláusula 2.9 — plano de repasse de eficiências`

### 10. Claims analíticos
Crie nós de claim quando a proposição tiver valor analítico próprio, por exemplo:
- `Claim: operação gera incentivos para fechamento de mercado`
- `Claim: não há evidência robusta de eficiências repassáveis`
- `Claim: teste de Forni é inadequado neste caso`
- `Claim: houve aumento ex-post de preços`

---

## Relações prioritárias
Use relações semanticamente fortes e reaproveitáveis. Prefira verbos claros.

### Relações documentais
- `analisa`
- `refere_se_a`
- `cita`
- `responde_a`
- `decorre_de`
- `subsidiar`
- `revisa`

### Relações entre caso e partes
- `envolve_parte`
- `tem_adquirente`
- `tem_alvo`
- `tem_concorrente`
- `tem_cliente`
- `tem_fornecedor`

### Relações de mercado
- `define_mercado_produto`
- `define_mercado_geografico`
- `atua_em`
- `verticalmente_relacionado_a`
- `compete_em`
- `afeta_mercado`

### Relações de teoria de dano
- `apresenta_teoria_de_dano`
- `gera_incentivo_para`
- `pode_levar_a`
- `aumenta_risco_de`
- `reduz_rivalidade_em`
- `fecha_mercado_para`
- `aumenta_custos_de`
- `discrimina`

### Relações de evidência
- `mede_com`
- `estima`
- `usa_proxy_para`
- `apoia`
- `enfraquece`
- `contradiz`
- `corrobora`
- `não_corrobora`
- `depende_de_hipotese`
- `baseia_se_em`

### Relações de posição analítica
- `alega`
- `argumenta`
- `conclui`
- `recomenda`
- `questiona`
- `rejeita`
- `considera_insuficiente`
- `considera_adequado`
- `não_descarta`
- `sugere`

### Relações de remédio e enforcement
- `recomenda_remedio`
- `impõe_remedio`
- `monitora_cumprimento`
- `descumpre`
- `cumpre`
- `aplica_multa_a`
- `condiciona_aprovacao_a`
- `revisa_operacao`

### Relações temporais/causais
- `antes_de`
- `depois_de`
- `resulta_em`
- `decorre_de`
- `mitiga`
- `agrava`

---

## Regras para claims analíticos
Crie nós de claim quando houver uma afirmação do tipo:
- conclusão sobre efeitos concorrenciais,
- aceitação ou rejeição de definição de mercado,
- validação ou crítica metodológica,
- conclusão sobre eficiências,
- conclusão sobre cumprimento/descumprimento,
- recomendação de remédio,
- constatação ex-post relevante.

Cada claim deve, sempre que possível, estar ligado a:
- **quem afirma** (`DEE`, `SG`, `requerentes`, `relator`, `Tribunal`),
- **sobre qual caso/mercado**,
- **qual evidência ou método sustenta o claim**,
- **qual é a polaridade** (apoia, rejeita, não descarta, sugere),
- **qual o status epistêmico** (fato observado, inferência, hipótese, recomendação).

### Exemplos de claims valiosos
- `DEE conclui que há incentivos para fechamento de mercado`
- `SG aprovou sem restrições`
- `Nota técnica questiona a adequação do teste de Forni`
- `Avaliação ex-post identifica aumento de preços`
- `ACC não foi cumprido em cláusula específica`

### O que NÃO virar claim
- cabeçalho burocrático repetido
- telefone/endereço institucional
- rodapé do SEI
- URL repetida de impressão
- indicação de imagem omitida
- mera repetição de número de página

---

## Normalização de nomes
### Processos e atos
- Preserve o identificador completo do processo, ex.: `08700.006345/2018-29`.
- Una variações como `Ato de Concentração nº X`, `AC X` e `operação X` ao mesmo caso quando claramente forem o mesmo objeto.

### Empresas
- Use a forma corporativa mais estável do nome.
- Se houver nome do grupo e nome da subsidiária, mantenha ambos quando a distinção for analiticamente relevante.

### Mercados
- Normalize para rótulos claros, por exemplo:
  - `mercado de poliestireno (PS)`
  - `mercado brasileiro de poliestireno`
  - `mercado nacional de credenciamento e captura de meios de pagamento`
- Não junte mercados apenas por similaridade superficial.

### Métodos
- Normalize siglas e nomes completos:
  - `TMH` = `Teste do Monopolista Hipotético`
  - `Phillips-Perron`
  - `ADF`
  - `KPSS`
  - `GUPPI`
  - `vGUPPI`

### Remédios
- Distingua `remédio comportamental`, `remédio estrutural`, `ACC`, `TCC`, `multa`, `monitoramento`, `obrigação de licenciamento`, `produção mínima`, `investimento em P&D`.

---

## Regras de qualidade da evidência
### EXTRACTED
Use quando o vínculo estiver explicitamente no texto.
Exemplos:
- a nota diz que a operação envolve certas requerentes;
- a nota afirma que o DEE recomenda remédios comportamentais;
- a cláusula 2.1 foi descumprida;
- a avaliação ex-post estimou aumento de preços entre 4,9% e 13,5%.

### INFERRED
Use quando a inferência for plausível e útil, mas não textual literal.
Exemplos:
- uma cláusula de ACC relacionada a produção mínima pode ser conectada à mitigação de risco concorrencial;
- uma crítica metodológica enfraquece a robustez de um argumento de mercado relevante.

### AMBIGUOUS
Use quando houver OCR ruim, redação truncada, sigla indefinida, ou quando o texto sugerir algo sem base suficiente.
Nunca converta ambiguidade em certeza.

---

## Tratamento de posição institucional
Em disputas analíticas, preserve a assimetria entre atores.
Exemplos:
- `Requerentes -> alegam -> mercado geográfico internacional`
- `DEE -> questiona -> adequação do teste de Forni`
- `SG -> aprovou_sem_restricoes -> operação`
- `Relator -> solicita -> quantificação dos incentivos para fechamento`
- `Tribunal/Plenário -> reconhece -> descumprimento de ACC`

Não apague conflitos: **conflito analítico é informação valiosa**.

---

## Sinais de alto valor analítico
Priorize passagens que contenham:
- definição de mercado relevante,
- teoria de dano explícita,
- raciocínio causal sobre incentivos,
- referência a market shares, desvio, margem, preços, elasticidade, cointegração, concentração,
- análise de integração vertical,
- avaliação de poder coordenado,
- análise ex-post,
- remédio recomendado ou imposto,
- descumprimento de ACC/TCC,
- comparação entre entendimento da SG, do DEE e do Tribunal,
- precedente ou jurisprudência do CADE,
- conclusão final da nota.

---

## Âncoras conceituais do projeto
Estas âncoras devem aparecer como comunidades ou nós centrais sempre que o corpus fornecer suporte:
- mercado relevante
- mercado relevante geográfico
- mercado relevante de produto
- rivalidade
- poder de mercado
- concentração
- efeitos unilaterais
- efeitos coordenados
- fechamento de mercado
- aumento de custos de rivais
- discriminação anticompetitiva
- integração vertical
- eficiências
- repasse de eficiências
- barreiras à entrada
- inovação / P&D
- ACC / remédios
- monitoramento / cumprimento
- avaliação ex-post
- jurisprudência do CADE
- teoria de dano
- evidência econométrica

---

## Comunidades desejáveis para a wiki
Ao rotular comunidades, prefira nomes temáticos úteis para pesquisa, por exemplo:
- `Definição de Mercado Relevante`
- `Teorias de Dano em Atos de Concentração`
- `Integração Vertical e Fechamento de Mercado`
- `Eficiências e Repasse ao Consumidor`
- `ACC, Remédios e Monitoramento`
- `Avaliações Ex-Post e Evidência de Preços`
- `Métodos Econométricos e Testes Quantitativos`
- `Jurisprudência, SG, DEE e Tribunal`

Evite nomes vagos como `Community 1`, `Misc`, `Outros`.

---

## Heurísticas específicas para este corpus
1. Ignore boilerplate do SEI, endereços, telefones, páginas e imagens omitidas.
2. Quando houver caracteres corrompidos de OCR, tente recuperar o sentido apenas se houver contexto suficiente.
3. Quando a nota listar conclusões em itens (`a)`, `b)`, `c)`), trate cada item como potencial claim independente.
4. Quando houver comparação entre argumentos das requerentes e crítica do DEE, extraia **os dois lados** e a relação de contestação.
5. Quando houver estimativas numéricas, preserve direção e magnitude.
6. Quando houver remédio ou cláusula, conecte-a ao risco que pretende mitigar.
7. Em análises ex-post, conecte `operação -> resultou_em -> efeito observado`, distinguindo isso de hipótese ex-ante.
8. Em casos verticais, capture a cadeia econômica e os elos afetados.
9. Em notas sobre cumprimento de ACC, modele separadamente `cláusula`, `evidência de cumprimento/descumprimento`, `justificativa apresentada`, `posição institucional` e `consequência`.

---

## Exemplos-guia do próprio corpus
Use como referência mental os seguintes padrões já observáveis neste repositório:
- **Itaú / Ticket**: concentração vertical, incentivos para fechamento de mercado, risco de poder coordenado, remédios comportamentais sugeridos.
- **Videolar / Innova**: ACC, monitoramento, descumprimento de cláusulas, avaliação ex-post, aumento de preços no mercado de PS.
- **Tupy / Teksid**: controvérsia metodológica sobre definição de mercado geográfico, crítica à hipótese de Nash-Cournot e ao uso do teste de Forni.

Esses exemplos mostram o tipo de estrutura causal e argumentativa que deve ser priorizada na extração.

---

## Regra final
Se tiver de escolher entre:
- **muitos nós nominais superficiais**, ou
- **menos nós, porém com claims, evidências, conflitos e remédios bem conectados**,

prefira a segunda opção.

O sucesso deste projeto depende de um grafo que responda perguntas como:
- `quais operações levantaram preocupação de fechamento de mercado?`
- `em quais casos o DEE recomendou remédios comportamentais?`
- `quais notas questionam a definição de mercado relevante proposta pelas requerentes?`
- `onde houve análise ex-post com indício de aumento de preços?`
- `quais cláusulas de ACC foram apontadas como descumpridas?`

Esse é o padrão de extração desejado para o **Digital Brain CADE**.
