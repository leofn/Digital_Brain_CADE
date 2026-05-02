**==> picture [63 x 62] intentionally omitted <==**

## **Ministério da Justiça e Segurança Pública – MJSP Conselho Administrativo de Defesa Econômica – CADE** 

SEPN 515 Conjunto D, Lote 4 Ed. Carlos Taurisano, 4º andar - Bairro Asa Norte, Brasília/DF, CEP 70770-504 Telefone: (61) 3221-8409 e Fax: (61) 3326-9733 – www.cade.gov.br 

## **NOTA TÉCNICA Nº 2/2017/DEE/CADE** 

**Referência:** Ato de Concentração nº 08700.002165/2017-97 

**Requerentes:** ArcelorMittal & Votorantim Siderurgia S.A. 

**Ementa:** Ato de Concentração referente à aquisição, pela ArcelorMittal, da integralidade das ações representativas do capital social da Votorantim Siderurgia S.A. Avaliação do remédio proposto pelas requerentes. Avaliação estrutural pós-remédio pelo cálculo de HHI, delta HHI e razões de concentração. Análise dos resultados pósremédio dos efeitos unilaterais pelo cálculo de GUPPI e UPP. 

**Versão:** Pública 

## **1. Escopo da nota** 

Esta nota analisa o ato de concentração referente à aquisição, pela ArcelorMittal, da integralidade das ações representativas do capital social da Votorantim Siderurgia S.A (a “Operação”). A presente nota técnica do Departamento de Estudos Econômicos do Cade (DEE/Cade) atende ao Despacho Decisório nº 14/2017/GAB6/CADE, que solicita a avaliação dos efeitos decorrentes da adoção de um remédio estrutural para tal operação. Portanto, tal estudo é uma continuidade da análise dos possíveis efeitos anticompetitivos decorrentes da operação que já foram elencados na NT 30/2017/DEE/CADE e no Parecer 23/2017/SG/CADE. 

A proposta de remédio foi discutida no documento apresentado pela LCA Consultores intitulado “Aquisição da Votorantim Siderurgia pela ArcelorMittal Aços Longos: 

_Nota Técnica nº 2/2018/DEE/CADE_ 

Considerações sobre Remédios”[1] (SEI n° 0413604), protocolado na data 27/11/2017. **[ACESSO RESTRITO]** . 

Tal proposta apresenta um plano de produção cuja adoção pelas requerentes é considerada provável pelas mesmas. Como as plantas são flexíveis, a proposta engloba um _mix_ (conjunto) de produtos e seus respectivos volumes, bem como o nível de utilização da capacidade instalada (NUCI) da planta projetado pelas requerentes. A razoabilidade dessas premissas será pontuada ao longo desta nota técnica. Além disso, serão propostos outros dois cenários alternativos de NUCI com base no comportamento atual do mercado com o objetivo de checar a sensibilidade dos resultados. 

Destaca-se que o objetivo desta nota é revisitar a análise quantitativa realizada na NT 30/2017/DEE/CADE[2] e no Parecer 23/2017/SG/CADE. Portanto, à luz do remédio proposto são calculados os indicadores HHI, ΔHHI, C2, C3, C4 e GUPPI, supondo nova participação de mercado decorrente da implementação do remédio estrutural. 

A presente nota técnica está dividida em seis seções. Na segunda seção são descritas, resumidamente, as fontes das bases de dados utilizadas, os _softwares_ e demais informações técnicas. A seção 3 descreve mais pormenorizadamente o remédio e as hipóteses associadas à sua implementação. A seção 4 descreve os métodos da avaliação quantitativa empregados nesta nota: HHI, ΔHHI, C2, C3, C4 e GUPPI (e UPP). Em seguida, na seção 5, são apresentados os resultados dos testes quantitativos para cada um dos nove mercados relevantes examinados, em cada cenário de NUCI proposto. A sexta e última seção traz as considerações finais da análise empreendida. 

> 1 A partir daqui, referenciado como LCA (2017). 

> 2 O presente estudo relaciona-se diretamente com a NT 30/2017/DEE/CADE, fazendo uso de bases e métodos que foram anteriormente apresentados naquela nota. Dessa forma, evitar-se-á aqui repetir detalhamentos já apresentados. 

2 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **2. Base de dados,** _**softwares**_ **e informações técnicas** 

Houve neste processo duas áreas no Cade que utilizaram informações de volume produzido: A Superintendência Geral (SG), que utilizou dados agregados anuais categorizados por produto, e o Departamento de Estudos Econômicos (DEE) que, adicionalmente, solicitou dados mais desagregados mensais atingindo o nível geográfico de UF. 

Nem todas as empresas conseguiram apresentar os dados no nível de desagregação solicitado pelo DEE. Já a SG, que solicitou informações mais agregadas de volume, obteve respostas de um maior número de empresas. Ademais, a SG também foi capaz de incluir informações sobre a participação das importações. Nesse sentido, a base de volume da SG tornou-se a mais completa e, por isso, será utilizada nesta nota. 

No que diz respeito aos dados de preços e custos, recorre-se à consolidação do DEE. A forma como estes dados foram tratados está explicitada na página 3 da NT 30/2017/DEE/CADE. 

Cabe recordar que os resultados quantitativos utilizando diferentes consolidações dos bancos de dados geraram conclusões muito similares, portanto a escolha de uma consolidação não gera grandes implicações sobre a precisão dos resultados. 

Por fim, em LCA (2017) constam os elementos do remédio: capacidade instalada, NUCI esperado, bem como o plano de produção proposto. Ressalta-se que o remédio será avaliado para o ano de 2016. Para as análises, foi utilizado o software R. 

## **3. Descrição do remédio proposto** 

Os resultados obtidos nas NT 30/2017/DEE/CADE e no Parecer 23/2017/SG/CADE evidenciam potenciais efeitos de natureza anticompetitiva na maioria dos mercados. A tabela a seguir resume os resultados obtidos em ambos os documentos, identificando se há ou não a percepção de problemas associados àquele tipo de avaliação. 

3 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **Tabela 01 – Presença de potenciais efeitos de natureza anticoncorrenciais segundo a NT 30/2017/DEE/CADE e o Parecer 23/2017/SG/CADE** 

|Mercados relevantes|HHI e ΔHHI|Efeitos unilaterais|
|---|---|---|
|Vergalhões|SIM|SIM|
|Perfis leves|SIM|SIM|
|Perfis médios|SIM|SIM|
|Fio-máquina comum|SIM|SIM|
|Trefilados CA-60|SIM|SIM|
|Telas eletrosoldadas|SIM|SIM|
|Arame recozido|SIM|SIM|
|Treliças|SIM|SIM|
|Barras|NÃO|NÃO|



Elaboração: DEE. 

Na análise realizada pela SG, o Índice Herfindahl-Hirschman (HHI) e o ΔHHI suscitam preocupações concorrenciais com a fusão em quase todos os mercados elencados na tabela acima, com exceção do mercado de barras. 

Ademais, utilizando dados de 2016, a Nota Técnica nº30/2017/DEE/CADE observou aumentos de preços superiores às eficiências alegadas em quase todos os mercados onde há sobreposição, exceto no mercado de barras. 

Com a finalidade de sanar as preocupações concorrenciais oriundas da operação, as requerentes propõem a alienação de parte da capacidade instalada da qual dispõem. 

Extrai-se do documento LCA (2017, p.2) o trecho em que é apresentado o pacote de remédios propostos pelas requerentes: 

## **[ACESSO RESTRITO]** _[3] ._ 

Existem alguns fatos associados à adoção do remédio, bem como algumas hipóteses sobre o impacto na composição do mercado, que serão discutidos a seguir. 

> 3 **[ACESSO RESTRITO]** 

4 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## 3.1. Plantas de produção flexível 

A flexibilidade na produção é entendida aqui como a possibilidade de usar uma mesma planta para a produção de itens distintos ou mesmo de um conjunto deles, tendo em vista que, no limite (uso pleno da capacidade), o aumento de produção de um dado item representa a redução da produção de outro. 

Um exemplo da flexibilidade é obtido no documento da LCA (2017). **[ACESSO RESTRITO]** . 

A decorrência imediata é que se faz necessário “prever” qual será o uso da capacidade que será realizado pela firma adquirente, ou seja, o _mix_ de produtos que será produzido com a nova capacidade instalada, bem como qual será o NUCI[4] observado. 

Para as análises quantitativas realizadas a seguir, considera-se da proposição das requerentes o conjunto dos produtos e a respectiva alocação de capacidade para a produção de cada um, imputando: 

- a) NUCI de 70% (cenário proposto pelas requerentes) 

- b) NUCI de 40% ( **[ACESSO RESTRITO]** ) 

## c) NUCI de 50% ( **[ACESSO RESTRITO]** ) 

O DEE não atribuiu pesos aos cenários propostos. Entretanto as requerentes apresentaram apenas o cenário “a” e argumentaram que: 

> “A escolha do mix de produtos, por sua vez, é influenciada pela demanda do mercado e visa a otimizar a produção da empresa. Por isso, a determinação da capacidade produtiva de uma planta de aços longos, por produto, deve levar em consideração o player que detém a planta e seu posicionamento de mercado (LCA, 2017, p. 4).” 

> 4 Nível de utilização da capacidade instalada. Razão entre a produção atual e a produção potencial da planta. 

5 

_Nota Técnica nº 2/2018/DEE/CADE_ 

Ou seja, os planos de produção aqui apresentados são apenas alguns dos vários que podem ser adotados pela adquirente. No entanto, pesa o fato de que nem todos os planos são interessantes para dirimir os efeitos anticompetitivos produzidos pela operação. Não obstante, aqui será avaliado o plano de produção proposto pelas requerentes. 

## 3.2. Nível de utilização da capacidade instalada (NUCI) 

Foge ao escopo desta nota comprovar o quão factível é ou não o cenário apresentado pelas requerentes. Não obstante, cabe relatar qual a realidade atual, seja do plano de produção adotado, seja do NUCI observado para **[ACESSO RESTRITO]** . A Tabela 02, também extraída da nota técnica da LCA (2017, p. 5), mostra a ocupação atual **[ACESSO RESTRITO]** em 2016: 

## **Tabela 02 – [ACESSO RESTRITO]** 

Considerando-se as **[ACESSO RESTRITO].** Por esse motivo, foi proposto um cenário “b” com NUCI igual a 40% para a realização das análises quantitativas. Por sua vez, **[ACESSO RESTRITO]** %[5] . Dessa forma, justifica-se o exercício com o cenário “c” com 50% de NUCI. 

## 3.3. Uso possível da capacidade e determinação do plano de produção 

A fórmula para determinar o plano de produção a ser imputado para os cálculos dos efeitos do remédio foi proposto pelas requerentes. Limitado pela capacidade de **[ACESSO RESTRITO]** , e tendo em vista as limitações de seus laminadores, foi proposta uma distribuição da capacidade entre os diversos itens. 

No caso específico, conforme LCA (2017, p. 4), tem-se que os laminadores detém as seguintes características: 

## **[ACESSO RESTRITO]** 

5 **[ACESSO RESTRITO]** . 

6 

_Nota Técnica nº 2/2018/DEE/CADE_ 

No documento da LCA (2017, p. 6) é apresentado o plano para o uso da capacidade que as requerentes entendem ser o mais provável: 

## **Tabela 03: [ACESSO RESTRITO]** 

Dadas as capacidades, basta multiplicar a coluna de capacidade pelos três cenários de NUCI. Eis o resumo para os três cenários que serão utilizados por esta nota: 

## **Tabela 04 – Produção de laminados em mil toneladas para os cenários de NUCI de 70%, 40% e 50%** 

## **[ACESSO RESTRITO]** 

O exercício aqui realizado (o remédio proposto) consiste em transferir essa produção, hoje realizada pela ArcelorMittal, para a Silat ou Simec (em uma simulação hipotética de possíveis empresas adquirentes). Ou seja, esse vetor de produção será agregado às produções atuais de Silat ou Simec (a simulação será feita para ambas), ao mesmo tempo que é subtraído da produção atual da ArcelorMittal. 

Em trefilados o exercício é similar, mas a produção foi subtraída da Votorantim segundo cálculos apresentados por LCA (2017). 

## **Tabela 05 – Produção de trefilados em mil toneladas para os cenários de NUCI de 70%, 40% e 50%** 

## **[ACESSO RESTRITO]** 

## 3.4. Cenário pós remédio. 

A tabela a seguir apresenta a produção atual em mil toneladas por produto e firma para o ano de 2016, segundo os dados da SG: 

7 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **Tabela 06 – Produção de 2016 em mil toneladas por item e empresa** 

## **[ACESSO RESTRITO]** 

Para o mercado segregado por produto são apresentados os _shares_ atuais por firma para o ano de 2016, calculados com base na Tabela 06. 

## **Tabela 07 –** _**Market Share**_ **de 2016 por item e empresa** 

## **[ACESSO RESTRITO]** 

De modo a exemplificar como se dá a constituição do cenário pós-remédio, apresentam-se as tabelas a seguir. A Tabela 08 resulta da transferência de produção para a Simec, dado o cenário de 70% de uso dos ativos de **[ACESSO RESTRITO]** . Na mesma tabela é adicionada uma linha[6] com a produção total da nova firma que se formará depois da fusão intitulada “requerentes”. 

Dito de outra forma, retirou-se da produção de 2016 da ArcelorMittal e Votorantim os valores de produção que foram calculados com um NUCI de 70%, para cada item considerado. Esses valores foram então transferidos para a produção da Simec. A partir daí, dá-se a fusão entre as requerentes. Eis o cenário pós-remédio: 

## **Tabela 08 – Produção pós remédio e fusão em mil toneladas por item e empresa (transferência de capacidade para SIMEC)** 

## **[ACESSO RESTRITO]** 

Usando os dados de produção da Tabela 08, é possível apresentar os _shares_ pós-fusão, depois da implementação do remédio. Neste ponto é possível calcular as medidas de concentração. 

> 6 Para efeito do cálculo da linha de totais, esta linha deve ser desconsiderada. 

8 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **Tabela 09 –** _**Market Share**_ **pós remédio e fusão por item e empresa** 

## **(transferência de capacidade para SIMEC)** 

## **[ACESSO RESTRITO]** 

Foi possível, dessa forma, explicar como os números pré-fusão e pós-fusão (com implementação do remédio) foram calculados. Este é o procedimento a ser adotado nos outros dois cenários propostos na nota (NUCI = 50% e NUCI = 40%). 

**4. Breve descrição dos métodos quantitativos** 

## 4.1. HHI e ΔHHI 

O Índice Herfindahl-Hirschman (HHI) mede o grau de concentração do mercado. É calculado com base no somatório do quadrado das participações de mercado de todas as empresas de um dado mercado. 

**==> picture [90 x 38] intentionally omitted <==**

Onde: 

- 𝑠𝑖: Share de mercado da firma i 

- 𝑞𝑖: Quantidade produzida pela firma i 

- n 

- Q = ∑i=1 qi: Quantidade produzida pelo mercado 

- 𝑛: Número de firmas do mercado 

Já o ΔHHI mede a variação do HHI decorrente de uma fusão entre empresas neste mercado. O nexo de causalidade, conforme estabelecido pelo “Guia para Análise de Atos 

9 

_Nota Técnica nº 2/2018/DEE/CADE_ 

de Concentração Horizontal”, a partir daqui o Guia-H, páginas 24-27, pode ser sumarizado na tabela a seguir. 

**Tabela 10 – HHI, ΔHHI e nexo de causalidade** 

**==> picture [426 x 368] intentionally omitted <==**

**----- Start of picture text -----**<br>
Variação decorrente da fusão<br>Caracterização<br>dos mercados<br>ΔHHI < 100  100 ≤ ΔHHI < 200  ΔHHI ≥ 200<br>pós-fusão.<br>Provavelmente não  Provavelmente não  Provavelmente não<br>geram efeitos  geram efeitos  geram efeitos<br>competitivos  competitivos  competitivos<br>adversos.  adversos.  adversos.<br>Usualmente não  Usualmente não  Usualmente não<br>requerem análise  requerem análise  requerem análise<br>detalhada.  detalhada.  detalhada.<br>Provavelmente não<br>Têm potencial de  Têm potencial de<br>geram efeitos<br>gerar preocupações  gerar preocupações<br>competitivos<br>concorrenciais.  concorrenciais.<br>adversos.<br>Recomendável uma  Recomendável uma<br>Usualmente não<br>análise mais  análise mais<br>requerem análise<br>detalhada.  detalhada.<br>detalhada.<br>Provavelmente não  Têm potencial de<br>geram efeitos  gerar preocupações  Presumivelmente<br>competitivos adversos.  concorrenciais.  geram aumento de<br>Usualmente não  Recomendável uma  poder de poder de<br>requerem análise  análise mais  mercado.<br>detalhada.  detalhada.<br>Elaboração: DEE.<br>HHI < 1500<br>Não concentrados<br>concentrados<br>Moderadamente<br>1.500 ≤ HHI < 2.500<br>Altamente<br>concentrados  HHI ≥ 2.500<br>**----- End of picture text -----**<br>


O referido Guia-H ressalta que as indicações de nexo causal apresentadas na tabela anterior são apenas uma suposição inicial, se mantendo sensível então a apresentação de outros argumentos. 

## 4.2. Razões de concentração (C2, C3, C4) 

A razão de concentração apresenta a somatório dos _market shares_ dos K maiores concorrentes de um dado mercado. Em que os K maiores podem ser os dois maiores (C2), três maiores (C3) ou quatro maiores (C4): 

10 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**==> picture [55 x 40] intentionally omitted <==**

Trata-se de um indicativo de predominância de um dado grupo de empresas em um dado mercado, e pode estar correlacionado com a existência de um potencial para coordenação. 

## 4.3. GUPPI e UPP 

A referência adotada para o GUPPI ( _Gross Upward Pricing Pressure Index)_ é Salop e Moresi (2009)[7] e, também, o _Competition Competence Report_ (2013) e a sua expressão final sintetizada no documento. Trata-se de um teste em que se assume competição em preços e produtos diferenciados, mas não se assume a existência de eficiências na expressão final, tal como na expressão final do UPP ( _Upward Pricing Pressure)_ , além de apresentar o resultado em proporção ao preço para o qual o GUPPI está sendo calculado. 

Assim, a expressão usada para o GUPPI resulta em: 

**==> picture [129 x 30] intentionally omitted <==**

Essa expressão é, por definição, positiva e devolve um valor percentual para a pressão por aumento de preços do produto após a fusão. Conforme explicado pela _Competition Competence Report_ (2013), a probabilidade de um aumento de preços após a fusão é influenciada por dois fatores: (i) o primeiro fator é a migração dos consumidores, também chamada taxa de desvio ( _diversion ratio_ ), do produto 1 para o produto 2 (D12). A taxa de desvio busca responder a seguinte pergunta: se o preço do produto 1 aumentar, qual parte dos consumidores irá mudar para o produto 2?; (ii) o segundo fator relevante é a margem de lucro bruta definida como a diferença entre o preço (p2) e o custo marginal (mc2). Em 

> 7 SALOP, STEVEN. MORESI, SERGE. Updating the Merger Guidelines: Comments. 2009. Disponível em: https://www.ftc.gov/sites/default/files/documents/public_comments/horizontal-merger-guidelinesreview-project-545095-00032/545095-00032.pdf 

11 

_Nota Técnica nº 2/2018/DEE/CADE_ 

suma, a probabilidade de um aumento de preços após a fusão é calculada pela multiplicação da margem de lucro bruta e a taxa de desvio. 

No presente caso, a taxa de desvio foi calculada com base nos _market shares_ , conforme segue: 

**==> picture [68 x 26] intentionally omitted <==**

A fórmula acima pode ser multiplicada por uma “taxa de recaptura do mercado” (REC). Eis a aproximação usada no artigo original de Farrel e Shapiro (2010) para a taxa de desvio ( _diversion ratio_ ): 

**==> picture [93 x 26] intentionally omitted <==**

O REC pode ser inferior a 1 (um) na medida que se consideram aqueles consumidores que, por decorrência do aumento de preço, ou abandonam o consumo dos bens das empresas definidas para aquele mercado, ou adotam o consumo de outro substituto mais distante (e que não foi incluído no mercado relevante de produto). 

Nesta nota técnica serão simulados alguns cenários de REC que vão de 80% a 100%. O DEE não atribuiu pesos a esses cenários. Cabe ressaltar que, em casos passados, o DEE já utilizou REC no valor de 85% para um mercado com características semelhantes[8] . 

Com essa hipótese, o percentual de vendas perdidas pela empresa 1 (ArcelorMittal) que é capturado pela empresa 2 (Votorantim) é representado pela expressão acima, envolvendo os _market shares_ dessas empresas e o REC do mercado. 

Outro ponto a destacar é que o GUPPI mede a pressão por aumento de preços (em termos percentuais) resultante da Operação. O índice é calculado para cada produto de cada firma envolvida na fusão. Tem-se, por exemplo, a possibilidade de observar os aumentos de preço para o vergalhão vendido por cada uma das requerentes. Sendo assim, 

> 8 Ver Nota Técnica nº 29/2017/DEE/CADE referente ao AC nº 08700.002155/2017-51 (Ultragaz & Liquigás). 

12 

_Nota Técnica nº 2/2018/DEE/CADE_ 

os resultados da secção 5 serão apresentados para cada empresa em todos os mercados envolvidos. 

Considerando a cesta de bens da nova firma, formada pelos produtos atualmente vendidos pela ArcelorMittal e Votorantim, é que fazemos a média ponderada da pressão por aumentos de preço. Ou seja, para aquele produto analisado, observaremos um GUPPI equivalente a: 

**==> picture [246 x 29] intentionally omitted <==**

Ou dividindo pelo mercado total 𝑄. 

**==> picture [235 x 26] intentionally omitted <==**

É adequado sopesar que os _shares_ de Arcelormittal (A) e Votorantim (V) são determinados de forma endógena, ou seja, são função de todos os preços daquele mercado. Assim, com o aumento de preço apontado pelo GUPPI para uma dada empresa em certo mercado, seria esperada uma redução do _share_ dessa empresa, neste mercado. Portanto, o uso dos _shares_ anteriores a fusão só servem para aproximar os valores dos _shares_ pós-fusão. De toda forma, este GUPPI médio será mostrado na seção de resultados com o intuito de resumir as informações de GUPPI das duas empresas. 

De maneira complementar, avaliamos também os efeitos esperados da Operação, com remédios, usando o índice de pressão para aumento de preços ( _Upward Pricing Pressure_ - UPP) desenvolvido por Farrel e Shapiro (2010) e que incorpora um percentual de eficiências decorrente da Operação. A expressão usada pelos autores para a pressão de aumento de preço sofrida pela empresa 1, após fusão com a empresa 2 é: 

**==> picture [161 x 13] intentionally omitted <==**

A expressão do UPP é resultado da diferença das otimizações antes e depois da operação (já com a imposição do remédio), e insere um termo de eficiência ( _E_ ) para a Operação multiplicado ao valor do custo marginal ( _mc_ ) na expressão acima. Dessa forma, considera-se no cálculo do índice, de maneira mais precisa, a possibilidade de eficiências 

13 

_Nota Técnica nº 2/2018/DEE/CADE_ 

em razão da operação. Adota-se o valor de **[ACESSO RESTRITO]** % de eficiências alegadas[9] . Em relação às eficiências alegadas, não se está aqui referindo que o DEE deva aceitar ou rejeitar tais eficiências, já que, como será demonstrado a seguir, ainda que eventualmente todas as eficiências alegadas sejam consideradas, as mesmas não são suficientes para mitigar efeitos anticompetitivos derivados da presente operação em parte dos mercados analisados. A interpretação do teste reside no valor do UPP ser positivo ou negativo. O teste não devolve um valor do tamanho (ou percentual) do aumento, ou da queda, de preços. Se o teste for positivo, há pressão para aumento de preços. Se for negativo, o contrário. 

## **5. Apresentação e análise dos resultados** 

Esta seção está dividida em três partes, a primeira para HHI e ΔHHI, a segunda para os indicadores de poder coordenado (C2, C3, C4), e a última para a apresentação dos resultados de efeitos unilaterais por meio do cálculo de GUPPI. 

Os cenários de NUCI de 70%, 50% e 40% serão apresentados conjuntamente para cada medida. 

## 5.1. HHI e ΔHHI 

Os resultados[10] encontrados pelo DEE para a fusão sem a adoção de remédios são os que seguem: 

> 9Parecer LCA: “ _Aquisição da Votorantim Siderurgia pela ArcelorMittal Aços Longos: Análise de eficiências_ ”. 

> 10 As pequenas diferenças nos valores de HHI e ΔHHI entre esta nota técnica e o Parecer 23/2017/SG/CADE são explicadas pelo uso de arredondamentos por parte da SG. 

14 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Tabela 11 – HHI pré e pós-operação e ΔHHI, sem a adoção de remédios.** 

|**Itens**|**HHI PRÉ HHI PÓS DELTA HHI**|
|---|---|
|**Vergalhão**|2151<br>2881<br>730|
|**Barra MBQ**|2416<br>2549<br>133|
|**Perfis Leves**|2707<br>3686<br>979|
|**Perfis Médios**|5556<br>5951<br>395|
|**Fio-Máquina Comum**|3123<br>3556<br>433|
|**CA-60**|2234<br>3531<br>1297|
|**Telas Eletrosoldadas**|2261<br>3396<br>1135|
|**Treliça**|2139<br>2683<br>544|
|**Arame Recozido**|3265<br>4102<br>837|



Elaboração: DEE. 

Como quase todos os ΔHHI superam a marca dos 200 pontos, a exceção do mercado de barras MBQ com 133 pontos, e como todos os HHI pós-fusão são superiores aos 2.500 pontos, pode-se então presumir que a fusão sem a adoção de um remédio gera aumento de poder de mercado na maioria dos mercados analisados. A exceção é o mercado de barras MBQ que não apresenta nexo de causalidade. 

A seguir, estes cálculos são realizados considerando-se o cenário de transferência de capacidade das requerentes para a Simec e posterior fusão das requerentes. Os resultados para HHI pós-fusão e ΔHHI, consideradas transferências de produção equivalentes à 70%, 50% e 40% da capacidade (do remédio), estão explicitados nas colunas da Tabela 12. 

15 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Tabela 12 – HHI pré e pós-operação e ΔHHI, com transferência de capacidade para a Simec. Cenários de NUCI de 70%, 50% e 40%.** 

|**Cenário**<br>**NUCI**|**70%**|**50%**|**40%**|
|---|---|---|---|
|**Itens**|**HHI**<br>**PÓS**<br>**DELTA**<br>**HHI**<br>2508<br>357|**HHI**<br>**PÓS**<br>**DELTA**<br>**HHI**<br>2594<br>443|**HHI**<br>**PÓS**<br>**DELTA**<br>**HHI**<br>2643<br>492|
|||||
|**Vergalhão**||||
|**Barra MBQ**|2374<br>-42|2413<br>-3|2436<br>20|
|**Perfis Leves**|2846<br>139|3009<br>302|3113<br>406|
|**Perfis Médios**|5556<br>0|5554<br>-2|5571<br>15|
|**Fio-Máquina**<br>**Comum**|3556<br>433|3556<br>433|3556<br>433|
|**CA-60**|2617<br>383|2825<br>591|2944<br>710|
|**Telas**<br>**Eletrosoldadas**|2754<br>493|2914<br>653|3001<br>740|
|**Treliça **|2683<br>544|2683<br>544|2683<br>544|
|**Arame Recozido**|3628<br>363|3752<br>487|3817<br>552|



Elaboração: DEE. 

Cabe recordar que a fusão se daria depois de diluir a concentração do mercado por meio de um remédio estrutural. Assim, é possível encontrar HHIs pós-fusão inferiores aos do cenário pré-fusão, gerando variações negativas, como no mercado de barras. 

Para o mercado de barras MBQ e perfis médios, pode-se considerar que não há aumento de poder de mercado, pois todos os ΔHHI são menores que 100. No cenário de 70%, o mais otimista para as requerentes, o mercado de perfis leves ainda tem potencial de gerar preocupações concorrenciais. Em todos os demais cenários e mercados há um aumento plausível do poder de mercado. 

Quanto ao cenário de transferência de capacidade para a Silat, tem-se: 

16 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Tabela 13 – HHI pré e pós-operação e ΔHHI, com transferência de capacidade para a Silat. Cenários de NUCI de 70%, 50% e 40%.** 

|**Cenário**<br>**NUCI**|**70%**|**50%**|**40%**|
|---|---|---|---|
|**Itens**|**HHI**<br>**PÓS**<br>**DELTA**<br>**HHI**<br>2462<br>311|**HHI**<br>**PÓS**<br>**DELTA**<br>**HHI**<br>2561<br>410|**HHI**<br>**PÓS**<br>**DELTA**<br>**HHI**<br>2616<br>465|
|||||
|**Vergalhão**||||
|**Barra MBQ**|2374<br>-42|2413<br>-3|2436<br>20|
|**Perfis Leves**|2846<br>139|3009<br>302|3113<br>406|
|**Perfis Médios**|5556<br>0|5554<br>-2|5571<br>15|
|**Fio-Máquina**<br>**Comum**|3556<br>433|3556<br>433|3556<br>433|
|**CA-60**|2671<br>437|2863<br>629|2975<br>741|
|**Telas**<br>**Eletrosoldadas**|2799<br>538|2946<br>685|3027<br>766|
|**Treliça **|2683<br>544|2683<br>544|2683<br>544|
|**Arame Recozido**|3628<br>363|3752<br>487|3817<br>552|



Elaboração: DEE. 

No cenário com transferência para Silat, os ΔHHI são menores que 100 nos mercados de barras MBQ e perfis médios, assim como no remédio para a Simec. Portanto, não há aumento de poder de mercado para estes produtos. Nos demais mercados e cenários, também é possível presumir um aumento de poder de mercado. 

Em suma, sob a ótica do Guia-H supracitado, o remédio parece endereçar os problemas concorrenciais dos mercados de barras MBQ e perfis médios, enquanto que os demais mercados continuam a ser caracterizados como problemáticos. 

## 5.2. Razão de Concentração: C2, C3, C4 

Inicialmente, vale destacar que na NT 30/2017/DEE/CADE, o DEE já havia analisado os efeitos coordenados decorrentes da operação. Nesta subseção cabe refazer os exercícios de razão de concentração incluindo o remédio proposto. 

Como um padrão geral, é possível observar que os mercados envolvidos na operação são caracterizados pela presença de dois ou três _players_ que detém a maior fatia do mercado. Os gráficos a seguir mostram os cálculos de C2, C3 e C4 para os cenários considerados, a saber, pré-fusão, pós-fusão (fusão sem remédios), pós-remédios sendo a 

17 

_Nota Técnica nº 2/2018/DEE/CADE_ 

Simec a adquirente dos ativos e pós-remédios sendo a Silat a adquirente dos ativos. Nos cenários com remédio é possível ver o efeito de cada NUCI adotado no produto analisado. 

Em geral, a fusão afeta as razões de concentração, o que significa que as requerentes estão entre as empresas mais importantes nos distintos mercados. Quanto aos remédios, como aspecto geral, há uma redução dos valores das razões de concentração após a introdução do remédio proposto. 

**Gráfico 01 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - Vergalhão.** 

**==> picture [426 x 299] intentionally omitted <==**

Elaboração: DEE. 

O impacto do remédio, no mercado de vergalhão, tem efeito nos índices de concentração principalmente quando se considera um cenário de NUCI igual a 70%. Por exemplo, antes da fusão, as três maiores empresas concentravam 73% do mercado de vergalhão (C3), após a fusão elas teriam 83% de participação. Por sua vez, com a introdução do remédio (sendo a Silat a adquirente) a razão de concentração C3 diminuiria para 76%. 

18 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Gráfico 02 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - Barras MBQ.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

No mercado de barras, a adoção dos remédios Simec ou Silat provocam, para todos os cenários, igual redução da concentração, chegando até a produzir, para NUCIs de 50% e 70%, respectivamente, níveis de concentração iguais ou menores aos observados préfusão. Portanto, a adoção do remédio apresenta indícios de eficácia. 

19 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Gráfico 03 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - Perfis Leves.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

Simec e Silat não atuam no mercado de perfis leves e surgirá um novo _player_ caso o remédio seja implementado. A depender do remédio, podem se tornar o 3° ou 4° maiores _shares_ . Para um NUCI de 70%, é possível manter o C3 a níveis pré-fusão, não obstante, isso não significa que o mercado não se torne mais concentrado (ΔHHI entre 139 a 406). 

20 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **Gráfico 04 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se** 

**os cenários de NUCI de 40%, 50% e 70% - Perfis Médios.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

No mercado de perfis médios, o remédio evita a formação de um duopólio. A depender do cenário de NUCI, a firma pode se tornar tão grande quanto a nova fusionada. Dessa forma, o remédio cumpre seu papel no mercado de perfis médios. 

21 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Gráfico 05 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - Fio-Máquina Comum.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

Não há qualquer proposta de remédio para o mercado de fio-máquina, portanto, não há mudança em relação ao cenário pós-fusão. Ressalta-se que o fio-máquina é um recurso muito importante na cadeia produtiva, sendo insumo para vários produtos trefilados. Desse modo, a concentração (C3) de 94% nos três maiores _players_ pode ser interpretada como algo problemático em termos concorrenciais. 

22 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Gráfico 06 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - CA-60.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

No caso do mercado de CA-60, observando o C4 é possível notar que o remédio Simec é menos prejudicial à concentração de mercado que o remédio Silat. São, respectivamente, 91% contra 93% do mercado detido pelas quatro maiores firmas, resultado que corrobora a análise dos HHIs: Para o cenário de NUCI de 70%, por exemplo, o remédio Simec provoca um ΔHHI de 383 pontos, enquanto que o remédio Silat, 437 pontos. 

Ademais, a ArcelorMittal consolidaria, e muito, a posição de liderança nestes cenários de fusão, saindo de **[ACESSO RESTRITO]** % de _share_ para algo em torno de **[ACESSO RESTRITO]** %, com adoção de remédio, e **[ACESSO RESTRITO]** %, sem adoção de remédio. 

23 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Gráfico 07 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 70%, 50% e 40% - Telas Eletrosoldadas.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

A solução menos prejudicial para o mercado de telas eletrosoldadas é a da Simec. Tanto os resultados das razões de concentração como dos HHI corroboram essa conclusão. 

24 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Gráfico 08 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - Treliça.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

Não há qualquer proposta de remédio para o mercado de treliça, portanto, não há qualquer mudança em relação ao cenário pós-fusão. 

25 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **Gráfico 09 – C2, C3, C4 pré e pós-operação, com e sem remédio, considerando-se os cenários de NUCI de 40%, 50% e 70% - Arame Recozido.** 

**==> picture [426 x 298] intentionally omitted <==**

Elaboração: DEE. 

A obtenção de C3 a níveis pré-fusão é possível para o cenário de NUCI de 70%. Situação em que Simec ou Silat ocuparão a 4° colocação do mercado. Hoje ambas não atuam neste mercado. Salienta-se que, mesmo assim, o mercado torna-se mais concentrado (ΔHHI entre 363 a 552). 

Em termos das razões de concentração, o remédio Simec é o menos prejudicial nos mercados de CA-60 e telas eletrosoldadas, enquanto que para o mercado de vergalhão o remédio Silat seria o melhor. Para os demais mercados, não há distinção dos impactos de se optar pelos remédios Simec ou Silat. No próximo tópico, busca-se avaliar se tal padrão se repetirá na análise de efeitos unilaterais por meio dos testes de pressão por aumento de preço. 

## 5.3. GUPPI e UPP 

Uma decorrência da forma de cálculo do GUPPI é que não importa para quem são direcionadas as capacidades de **[ACESSO RESTRITO]** . Importa apenas como ficam os 

26 

_Nota Técnica nº 2/2018/DEE/CADE_ 

_shares_ de ArcelorMittal e Votorantim depois da transferência desses ativos. Portanto, os resultados de GUPPI pós-remédio não serão discriminados por possível firma adquirente. Quanto aos níveis de NUCI, aí sim os valores de GUPPI apresentam variação, portanto, serão calculados. 

As pressões por aumentos de preço da ArcelorMittal para os diferentes mercados, considerados NUCIs de 70%, 50% e 40% para RECs que vão de 80% a 100%, são apresentados adiante. 

No Anexo A desta nota técnica são elencados todos os resultados de GUPPI para a ArcelorMittal e Votorantim separadamente. A título de resumo, a média ponderada parece ser uma medida que pode sumarizar, razoavelmente bem, a pressão por aumento de preço médio, pois um dado aumento de preço para uma empresa pode estar associado a um conjunto maior (ou menor) de bens tendo em vista a produção da firma fusionada. Basta ver nos dados das Tabelas A.1 e A.4 (constantes no Anexo A) o resultado no mercado de arame recozido: Sem remédio, a pressão por aumento de preço da ArcelorMittal era de 2,8%, enquanto que o registrado para a Votorantim era de 12,2%. Como o _share_ da ArcelorMittal é mais relevante nesse mercado, observarmos um resultado médio de pressão por elevação de preços da ordem de 4,8% (ver Tabela 14). 

**Tabela 14 – GUPPI médio da firma fusionada com adoção de remédio, NUCI de 70% e cenários de REC de 80% a 100%.** 

|**Itens**|**REC**||
|---|---|---|
|||**Sem**<br>**Remédio11**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,5%<br>4,8%<br>5,1%<br>5,3%<br>5,6%|6,9%|
|**Barra MBQ**|1,1%<br>1,1%<br>1,2%<br>1,3%<br>1,3%|1,6%|
|**Perfis Leves**|2,4%<br>2,6%<br>2,7%<br>2,9%<br>3,0%|5,7%|
|**Perfis Médios**|1,6%<br>1,7%<br>1,8%<br>1,9%<br>2,0%|4,4%|
|**Fio-Máquina Comum**|3,2%<br>3,5%<br>3,7%<br>3,9%<br>4,1%|4,1%|
|**CA-60**|4,3%<br>4,5%<br>4,8%<br>5,1%<br>5,3%|8,0%|
|**Telas Eletrosoldadas**|4,3%<br>4,6%<br>4,9%<br>5,2%<br>5,4%|7,4%|
|**Treliça **|2,6%<br>2,7%<br>2,9%<br>3,1%<br>3,2%|3,2%|
|**Arame Recozido**|2,8%<br>3,0%<br>3,2%<br>3,3%<br>3,5%|4,8%|



Elaboração: DEE. 

> 11 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

27 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Tabela 15 – GUPPI médio da firma fusionada com adoção de remédio, NUCI de 50% e cenários de REC de 80% a 100%.** 

|**Itens**|**REC**||
|---|---|---|
|||**Sem**<br>**Remédio12**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,8%<br>5,1%<br>5,4%<br>5,7%<br>6,0%|6,9%|
|**Barra MBQ**|1,1%<br>1,2%<br>1,3%<br>1,3%<br>1,4%|1,6%|
|**Perfis Leves**|3,0%<br>3,2%<br>3,4%<br>3,6%<br>3,8%|5,7%|
|**Perfis Médios**|1,7%<br>1,8%<br>1,9%<br>2,1%<br>2,2%|4,4%|
|**Fio-Máquina Comum**|3,2%<br>3,5%<br>3,7%<br>3,9%<br>4,1%|4,1%|
|**CA-60**|4,9%<br>5,2%<br>5,5%<br>5,8%<br>6,1%|8,0%|
|**Telas Eletrosoldadas**|4,8%<br>5,1%<br>5,4%<br>5,7%<br>6,0%|7,4%|
|**Treliça **|2,6%<br>2,7%<br>2,9%<br>3,1%<br>3,2%|3,2%|
|**Arame Recozido**|3,1%<br>3,3%<br>3,5%<br>3,7%<br>3,9%|4,8%|



Elaboração: DEE. 

**Tabela 16 – GUPPI médio da firma fusionada com adoção de remédio, NUCI de 40% e cenários de REC de 80% a 100%.** 

|**Itens**|**REC**||
|---|---|---|
|||**Sem**<br>**Remédio13**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,9%<br>5,2%<br>5,5%<br>5,8%<br>6,2%|6,9%|
|**Barra MBQ**|1,2%<br>1,2%<br>1,3%<br>1,4%<br>1,4%|1,6%|
|**Perfis Leves**|3,3%<br>3,5%<br>3,7%<br>4,0%<br>4,2%|5,7%|
|**Perfis Médios**|2,1%<br>2,2%<br>2,4%<br>2,5%<br>2,6%|4,4%|
|**Fio-Máquina Comum**|3,2%<br>3,5%<br>3,7%<br>3,9%<br>4,1%|4,1%|
|**CA-60**|5,2%<br>5,5%<br>5,8%<br>6,2%<br>6,5%|8,0%|
|**Telas Eletrosoldadas**|5,0%<br>5,3%<br>5,7%<br>6,0%<br>6,3%|7,4%|
|**Treliça **|2,6%<br>2,7%<br>2,9%<br>3,1%<br>3,2%|3,2%|
|**Arame Recozido**|3,2%<br>3,4%<br>3,6%<br>3,8%<br>4,0%|4,8%|



Elaboração: DEE. 

Ressalta-se que as pressões por aumentos de preços indicadas pelo GUPPI nos mercados de vergalhão (entre 4,5% a 6,2%), CA-60 (4,3%-6,5%) e telas eletrosoldadas (4,3%-6,3%) são superiores às eficiências alegadas, a saber, **[ACESSO RESTRITO]** %[14] . 

> 12 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

> 13 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

> 14 Vale destacar que a adoção do valor de **[ACESSO RESTRITO]** % é o limite superior extremo para a comparação direta das eficiências alegadas com o GUPPI. De fato, como CMg/p < 1, um termo adicional na expressão original do GUPPI seria ainda menor do que E (eficiências alegadas). Se há problemas mesmo 

28 

_Nota Técnica nº 2/2018/DEE/CADE_ 

Os resultados médios dos mercados de vergalhão e CA-60 são compatíveis com os resultados individuais das firmas. Ou seja, em todo o contínuo de aumentos, os valores obtidos são superiores as eficiências consideradas. Já para telas eletrosoldadas o resultado individual da ArcelorMittal encontrava interseção com as eficiências alegadas, ao contrário do resultado observado para a Votorantim, que era bem maior. 

De maneira mais precisa, o UPP retorna resultados já descontadas as eficiências alegadas. Ao analisar os resultados de UPP (para qualquer cenário NUCI), chega-se a conclusões semelhantes, após a adoção de remédios: os mercados de vergalhão, CA-60 e telas eletrosoldadas apresentam pressões para aumento de preços (tanto para a ArcelorMittal quanto para Votorantim). No Anexo B, são apresentadas as Tabelas B.1 (ArcelorMittal) e B.2 (Votorantim) com os resultados de UPP em um cenário de NUCI de 70%[15] . 

Na análise do GUPPI, nos mercados de perfis leves (2,4%-4,2%) e arame recozido (2,8%-4,0%) temos a situação em que para alguns cenários existe interseção entre os aumentos e as eficiências propostas, a saber, quando o NUCI for de 70% e observar-se RECs de 95% e 80%, para perfis leves e arame recozido, respectivamente. De maneira similar, é possível encontrar resultados de UPP positivo ou negativo a depender do cenário analisado para os mercados de perfis leves e arame recozido. 

Em relação aos resultados de GUPPI para barras MBQ (1,1%-1,4%) e perfis médios (1,6%-2,6%), todos os aumentos tornaram-se, na presença do remédio, inferiores as eficiências alegadas. Tal conclusão também se mantem para os resultados de UPP[16] . 

> nesta abordagem menos rigorosa de comparação direta entre GUPPI e eficiências, haverá problemas também na análise mais precisa. 

> 15 Com o intuito de resumir os vários resultados de UPP, mostram-se, nesta nota, apenas os resultados de UPP no cenário de NUCI de 70%, tendo em vista que, se o resultado mostra problemas concorrenciais neste cenário, com certeza tal preocupação aparecerá nos outros dois cenário (NUCI= 50% e NUCI= 40%). 

> 16 Ressalta-se que, em alguns cenários para determinada empresa (ArcelorMittal ou Votorantim), o UPP é positivo, mas ao se levar em conta uma média ponderada de ambas empresas, os resultados são sempre negativos para estes dois produtos. 

29 

_Nota Técnica nº 2/2018/DEE/CADE_ 

Em fio-máquina e treliças não houve a proposição de remédios estruturais, portanto não há alterações nas conclusões obtidas na NT 30/2017/DEE/CADE. Apenas foi acrescido cálculos com RECs entre 80% a 95%, 

## **6. Conclusões** 

Em resposta ao Despacho Decisório nº 14/2017/GAB6/CADE, que solicitou a avaliação dos efeitos decorrentes do remédio proposto pelas requerentes (ArcelorMittal e Votorantim Siderurgia), o DEE realizou exercícios quantitativos complementares àqueles discutidos na NT 30/2017/DEE/CADE à luz do referido remédio com o intuito de averiguar a existência de possíveis efeitos anticoncorrenciais presentes na proposta encaminhada. 

Avaliando o conjunto dos indicadores para cada mercado, é possível descrever o cenário geral que caracteriza os impactos da fusão com a adoção de remédios. Estes mercados podem ser classificados em três: (i) aqueles mercados cujos prejuízos à concorrência são dirimidos pelos remédios, (ii) aqueles mercados que não superam os problemas concorrenciais e (iii) aqueles mercados em que o remédio é eficaz somente em alguns cenários de NUCI. 

Em geral, os indicadores quantitativos analisados mostram que o mercado de barras MBQ e perfis médios podem ter seus problemas concorrenciais dirimidos com a adoção dos remédios. 

De outra parte, os mercados de vergalhão, CA-60 e telas eletrosoldadas apresentam, como padrão geral, indicadores que apontam para prejuízos concorrenciais decorrentes da fusão que não podem ser endereçados pelo remédio proposto. 

Por sua vez, nos mercados de perfis leves e arame recozido existem, para alguns cenários de NUCI, situações em que os problemas concorrenciais poderiam ser mitigados pelos remédios. Cabe recordar que o DEE não atribuiu peso aos cenários descritos nessa nota. 

30 

_Nota Técnica nº 2/2018/DEE/CADE_ 

Ademais, a ausência do endereçamento de remédios estruturais para os mercados de treliça[17] e, principalmente, fio-máquina, trazem dúvidas quanto à efetividade do remédio em endereçar os problemas em todos os mercados inicialmente apontados como problemáticos. 

Por fim, vale destacar que esta nota técnica apresenta os resultados da avaliação quantitativa e suas conclusões estão limitadas tanto pelas hipóteses dos modelos quanto pelas hipóteses descritas na seção três deste documento. O intuito desta nota foi trazer mais insumos quantitativos a fim de subsidiar a decisão do Tribunal. Porém existe toda uma análise de fatores qualitativos que esta nota não encerra. 

12 de janeiro de 2018. DEE. 

> 17 O mercado de treliça é menos problemático, ao menos do ponto de vista da pressão por aumento de preço. 

31 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **Referências** 

CADE (2017a). Despacho Decisório nº 14. Gabinete 6. SEI n° 0398684. 

CADE (2017b). Nota Técnica n° 30. Departamento de Estudos Econômicos – DEE. SEI n° 0379875. 

CADE (2017c). Anexo ao parecer n° 23. Superintendência Geral – SG. SEI n° 0382684. 

LCA (2017). Aquisição da Votorantim Siderurgia pela ArcelorMittal Aços Longos: Considerações sobre Remédios. SEI n° 0413604. 

CADE (2016). Guia para Análise de Atos de Concentração Horizontal. Disponível em 02 jan. 2018, no link: http://www.cade.gov.br/acesso-a-informacao/publicacoesinstitucionais/guias_do_Cade/guia-para-analise-de-atos-de-concentracao-horizontal.pdf. 

SALOP, STEVEN. MORESI, SERGE (2009). _Updating the Merger Guidelines: Comments_ . Disponível em: https://www.ftc.gov/sites/default/files/documents/public_comments/horizontal-mergerguidelines-review-project-545095-00032/545095-00032.pdf. 

COMPETITION COMPETENCE REPORT (2013). _UPP, GUPPI and IPR – Merger Screening Tools_ . p. 1-6. Disponível em http://www.eemc.com/uploads/media/Merger_Screening_Tools.pdf. Acesso em: 02 jan. 2018. 

FARRELL, JOSEPH. SHAPIRO, CARL (2010). _Antitrust Evaluation of Horizontal Mergers: An Economic Alternative to Market Definition_ . _The B.E. Journal of Theoretical Economics_ , vol. 10 (1), p. 1-41. 

32 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **ANEXO A** 

**Tabela A.1 – GUPPI da ArcelorMittal com adoção de remédio, NUCI de 70% e cenários de REC de 80% a 100%.** 

||**cenários de REC de 80% a 100%.**||
|---|---|---|
|**Itens**|**REC**||
|||**Sem**<br>**Remédio18**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,4%<br>4,7%<br>4,9%<br>5,2%<br>5,5%|6,0%|
|**Barra MBQ**|0,7%<br>0,8%<br>0,8%<br>0,8%<br>0,9%|0,9%|
|**Perfis Leves**|2,4%<br>2,6%<br>2,7%<br>2,9%<br>3,0%|3,5%|
|**Perfis Médios**|3,0%<br>3,2%<br>3,4%<br>3,5%<br>3,7%|4,4%|
|**Fio-Máquina Comum**|6,0%<br>6,3%<br>6,7%<br>7,1%<br>7,5%|7,5%|
|**CA-60**|3,0%<br>3,2%<br>3,4%<br>3,6%<br>3,8%|8,7%|
|**Telas Eletrosoldadas**|2,8%<br>2,9%<br>3,1%<br>3,3%<br>3,5%|6,1%|
|**Treliça **|2,1%<br>2,2%<br>2,3%<br>2,5%<br>2,6%|2,6%|
|**Arame Recozido**|1,1%<br>1,2%<br>1,2%<br>1,3%<br>1,4%|2,8%|



Elaboração: DEE. 

**Tabela A.2 – GUPPI da ArcelorMittal com adoção de remédio, NUCI de 50% e cenários de REC de 80% a 100%.** 

||**cenários de REC de 80% a 100%.**||
|---|---|---|
|**Itens**|**REC**||
|||**Sem**<br>**Remédio19**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,5%<br>4,8%<br>5,0%<br>5,3%<br>5,6%|6,0%|
|**Barra MBQ**|0,7%<br>0,8%<br>0,8%<br>0,9%<br>0,9%|0,9%|
|**Perfis Leves**|2,5%<br>2,7%<br>2,8%<br>3,0%<br>3,1%|3,5%|
|**Perfis Médios**|3,0%<br>3,2%<br>3,4%<br>3,6%<br>3,8%|4,4%|
|**Fio-Máquina Comum**|6,0%<br>6,3%<br>6,7%<br>7,1%<br>7,5%|7,5%|
|**CA-60**|3,9%<br>4,2%<br>4,4%<br>4,7%<br>4,9%|8,7%|
|**Telas Eletrosoldadas**|3,4%<br>3,6%<br>3,8%<br>4,0%<br>4,2%|6,1%|
|**Treliça **|2,1%<br>2,2%<br>2,3%<br>2,5%<br>2,6%|2,6%|
|**Arame Recozido**|1,4%<br>1,5%<br>1,6%<br>1,7%<br>1,8%|2,8%|



Elaboração: DEE. 

> 18 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

> 19 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

33 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Tabela A.3 – GUPPI da ArcelorMittal com adoção de remédio, NUCI de 40% e cenários de REC de 80% a 100%.** 

||**cenários de REC de 80% a 100%.**||
|---|---|---|
|**Itens**|**REC**||
|||**Sem**<br>**Remédio20**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,5%<br>4,8%<br>5,1%<br>5,4%<br>5,7%|6,0%|
|**Barra MBQ**|0,7%<br>0,8%<br>0,8%<br>0,9%<br>0,9%|0,9%|
|**Perfis Leves**|2,6%<br>2,7%<br>2,9%<br>3,1%<br>3,2%|3,5%|
|**Perfis Médios**|3,1%<br>3,3%<br>3,5%<br>3,7%<br>3,9%|4,4%|
|**Fio-Máquina Comum**|6,0%<br>6,3%<br>6,7%<br>7,1%<br>7,5%|7,5%|
|**CA-60**|4,4%<br>4,7%<br>4,9%<br>5,2%<br>5,5%|8,7%|
|**Telas Eletrosoldadas**|3,7%<br>3,9%<br>4,1%<br>4,4%<br>4,6%|6,1%|
|**Treliça **|2,1%<br>2,2%<br>2,3%<br>2,5%<br>2,6%|2,6%|
|**Arame Recozido**|1,6%<br>1,7%<br>1,8%<br>1,9%<br>2,0%|2,8%|



Elaboração: DEE. 

**Tabela A.4 – GUPPI da Votorantim com adoção de remédio, NUCI de 70% e cenários de REC de 80% a 100%.** 

|**Itens**|**REC**||
|---|---|---|
|||**Sem**<br>**Remédio21**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|4,7%<br>5,0%<br>5,3%<br>5,6%<br>5,9%|8,2%|
|**Barra MBQ**|2,8%<br>3,0%<br>3,2%<br>3,3%<br>3,5%|4,9%|
|**Perfis Leves**|2,5%<br>2,6%<br>2,8%<br>2,9%<br>3,1%|7,9%|
|**Perfis Médios**|0,0%<br>0,0%<br>0,0%<br>0,0%<br>0,0%|4,5%|
|**Fio-Máquina Comum**|2,3%<br>2,4%<br>2,6%<br>2,7%<br>2,8%|2,8%|
|**CA-60**|5,9%<br>6,2%<br>6,6%<br>7,0%<br>7,3%|9,3%|
|**Telas Eletrosoldadas**|7,3%<br>7,7%<br>8,2%<br>8,6%<br>9,1%|9,9%|
|**Treliça **|3,7%<br>3,9%<br>4,1%<br>4,4%<br>4,6%|4,6%|
|**Arame Recozido**|9,2%<br>9,8%<br>10,4%<br>11,0%<br>11,5%|12,2%|



Elaboração: DEE. 

> 20 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

> 21 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

34 

_Nota Técnica nº 2/2018/DEE/CADE_ 

**Tabela A.5 – GUPPI da Votorantim com adoção de remédio, NUCI de 50% e cenários de REC de 80% à 100%.** 

||**cenários de REC de 80% à 100%.**||
|---|---|---|
|**Itens**|**REC**||
|||**Sem**<br>**Remédio22**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|5,3%<br>5,6%<br>5,9%<br>6,3%<br>6,6%|8,2%|
|**Barra MBQ**|3,1%<br>3,3%<br>3,5%<br>3,7%<br>3,9%|4,9%|
|**Perfis Leves**|3,6%<br>3,8%<br>4,0%<br>4,2%<br>4,5%|7,9%|
|**Perfis Médios**|0,3%<br>0,3%<br>0,3%<br>0,3%<br>0,3%|4,5%|
|**Fio-Máquina Comum**|2,3%<br>2,4%<br>2,6%<br>2,7%<br>2,8%|2,8%|
|**CA-60**|6,1%<br>6,5%<br>6,9%<br>7,2%<br>7,6%|9,3%|
|**Telas Eletrosoldadas**|7,4%<br>7,9%<br>8,4%<br>8,8%<br>9,3%|9,9%|
|**Treliça **|3,7%<br>3,9%<br>4,1%<br>4,4%<br>4,6%|4,6%|
|**Arame Recozido**|9,4%<br>10,0%<br>10,6%<br>11,1%<br>11,7%|12,2%|



Elaboração: DEE. 

**Tabela A.6 – GUPPI da Votorantim com adoção de remédio, NUCI de 40% e cenários de REC de 80% à 100%.** 

|**Itens**|**REC**||
|---|---|---|
|||**Sem**<br>**Remédio23**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|5,5%<br>5,9%<br>6,2%<br>6,6%<br>6,9%|8,2%|
|**Barra MBQ**|3,3%<br>3,5%<br>3,7%<br>3,9%<br>4,1%|4,9%|
|**Perfis Leves**|4,1%<br>4,4%<br>4,6%<br>4,9%<br>5,1%|7,9%|
|**Perfis Médios**|0,9%<br>1,0%<br>1,0%<br>1,1%<br>1,2%|4,5%|
|**Fio-Máquina Comum**|2,3%<br>2,4%<br>2,6%<br>2,7%<br>2,8%|2,8%|
|**CA-60**|6,2%<br>6,6%<br>7,0%<br>7,4%<br>7,8%|9,3%|
|**Telas Eletrosoldadas**|7,5%<br>8,0%<br>8,5%<br>8,9%<br>9,4%|9,9%|
|**Treliça **|3,7%<br>3,9%<br>4,1%<br>4,4%<br>4,6%|4,6%|
|**Arame Recozido**|9,5%<br>10,1%<br>10,6%<br>11,2%<br>11,8%|12,2%|



Elaboração: DEE. 

> 22 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

> 23 Números obtidos da NT 30/2017/DEE/CADE, considerando os dados da SG. 

35 

_Nota Técnica nº 2/2018/DEE/CADE_ 

## **ANEXO B** 

**Tabela B.1 – UPP da ArcelorMittal com adoção de remédio, NUCI de 70% e cenários de REC de 80% a 100%.** 

||**cenários de REC de 80% a 100%.**||
|---|---|---|
|**Itens**|**REC**||
|||**Sem**<br>**Remédio**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|45,1<br>50,4<br>55,7<br>61,1<br>66,4|76,5|
|**Barra MBQ**|-32,7<br>-31,7<br>-30,8<br>-29,8<br>-28,8|-27,6|
|**Perfis Leves**|5,0<br>8,1<br>11,2<br>14,3<br>17,4|28,5|
|**Perfis Médios**|16,9<br>20,7<br>24,6<br>28,4<br>32,3|45,8|
|**Fio-Máquina Comum**|64,6<br>70,9<br>77,3<br>83,6<br>89,9|89,9|
|**CA-60**|15,1<br>18,9<br>22,8<br>26,6<br>30,4|109,8|
|**Telas Eletrosoldadas**|12,7<br>16,9<br>21,2<br>25,4<br>29,7|94,7|
|**Treliça **|-8,9<br>-6,0<br>-3,1<br>-0,2<br>2,7|2,7|
|**Arame Recozido**|-28,9<br>-26,9<br>-25,0<br>-23,1<br>-21,2|17,3|



Elaboração: DEE. 

**Tabela B.2 – UPP da Votorantim com adoção de remédio, NUCI de 70% e cenários de REC de 80% a 100%.** 

|**Tabela B.2 – UPP**|**da Votorantim com adoção de remédio, NUCI de**<br>**cenários de REC de 80% a 100%.**|**70% e**|
|---|---|---|
|**Itens**|**REC**||
|||**Sem**<br>**Remédio**|
||**80%**<br>**85%**<br>**90%**<br>**95%**<br>**100%**||
||||
|**Vergalhão**|52,1<br>57,8<br>63,5<br>69,2<br>74,9|122,4|
|**Barra MBQ**|11,6<br>15,0<br>18,5<br>21,9<br>25,3|52,0|
|**Perfis Leves**|-0,6<br>2,3<br>5,3<br>8,3<br>11,2|103,7|
|**Perfis Médios**|-40,8<br>-40,8<br>-40,8<br>-40,7<br>-40,7|49,4|
|**Fio-Máquina Comum**|2,5<br>5,0<br>7,5<br>10,0<br>12,5|12,5|
|**CA-60**|70,0<br>76,9<br>83,8<br>90,7<br>97,5|117,9|
|**Telas Eletrosoldadas**|111,0<br>120,8<br>130,6<br>140,4<br>150,2|168,2|
|**Treliça **|26,8<br>31,3<br>35,9<br>40,4<br>45,0|45,0|
|**Arame Recozido**|180,1<br>195,3<br>210,6<br>225,8<br>241,1|259,1|



Elaboração: DEE. 

36 

