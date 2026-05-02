## **NOTA TÉCNICA DEE/CADE** 

**Referência** : Ato de Concentração sobre autos abaixo mencionados 

Autos nº 08700.005683/2016-81 (público) 

Autos nº 08700.005684/2016-26 (restrito) 

Autos nº 08700.005898/2016-01 (restrito) 

**Requerentes:** 

- SOLVAY INDUPA S.A.I.C. & SOLVAY INDUPA DO BRASIL S.A. 

- UNIPAR CARBOCLORO S.A. 

**EMENTA:** Ato de Concentração referente à aquisição do controle societário da Solvay Indupa pela Unipar Carbocloro. Análise dos mercados de soda cáustica, hipoclorito de sódio e ácido clorídrico. Análise Kolmogorov-Smirnov. Verificação da distribuição acumulada de preços. Análise de demanda. Não há evidências conclusivas nesta nota em favor de possíveis efeitos anticompetitivos com a referida operação. 

Versão PÚBLICA 

1 

## 1. Escopo da nota 

Esta nota técnica trata do Ato de Concentração de n° 08700.005683/2016-81 referente à aquisição do controle societário da SOLVAY INDUPA S.A.I.C. (“Solvay”, no restante desta nota), sociedade anônima de capital aberto com sede na Argentina e representação no Brasil via SOLVAY INDUPA DO BRASIL S.A. (“Indupa Brasil”), pela UNIPAR CARBOCLORO S.A (“Carbocloro”, no restante desta nota). 

As Requerentes atuam nos mercados de soda cáustica, hipoclorito de sódio e ácido clorídrico, sendo esses os mercados com sobreposição na operação. A Solvay atua na produção e comercialização de PVC (Policloreto de Polivinila), ocorrendo nesse mercados apenas a substituição de um _player_ . 

Serão aplicados aqui métodos quantitativos para avaliar a “proximidade” (a substituibilidade) dos produtos das empresas requerentes, e se esses produtos têm algum grau de proximidade maior frente aos produtos das demais firmas. Há também a questão sobre a definição do produto soda cáustica, que pode ser produzido sob três tecnologias diferentes: a produção por meio de células de mercúrio, diafragma e membrana. Assim, avaliar-se-á também a “proximidade” entre as três tecnologias com indícios de substituição entre os produtos das diferentes tecnologias, com uma atenção especial à soda do tipo membrana, que é a produzida pela Solvay. 

A hipótese assumida é de que há alguma diferenciação entre as firmas nos mercados da operação. Essa hipótese permite a estimação de demanda de produtos diferenciados, o que será substanciado de forma indireta por meio dos gráficos de preços, das distribuições acumuladas dos preços e das próprias estimações de demanda. 

No que diz respeito à diferenciação, há uma discussão acerca da influência do método de produção de soda (a saber: por meio do uso de células de mercúrio, diafragma ou membrana, já mencionadas) sobre a diferenciação do produto no mercado, além de outras possíveis diferenciações (e.g. geográfica), que afetam os demais produtos analisados. As análises de distribuição e as estimações de demanda entre as três tecnologias discutirão a possibilidade de substituição entre as tecnologias. Ademais, possíveis efeitos anticompetitivos poderiam existir em virtude de uma maior “proximidade” entre os produtos das requerentes, isto é, se há um grande desvio de demanda entre os produtos das requerentes, o que poderia permitir aumentos de preço sensíveis com a operação. Esse resultado é passível de ser obtido com estimações de demanda. 

As Requerentes forneceram médias mensais de seus preços por tonelada para o período de janeiro de 2001 até setembro de 2016, bem como outras variáveis – _custos, produção e capacidade instalada_ . Obtiveram-se, também, dados de concorrentes para as análises. 

No que diz respeito à dimensão geográfica dos mercados, considera-se que o de soda tem amplitude nacional, enquanto que os mercados de hipoclorito de sódio e ácido clorídrico são de abrangência regional, mais especificamente as regiões Sul e Sudeste. 

2 

## 2. Métodos 

## 2.1. Distribuições acumuladas dos preços e o teste Kolmogorov- Smirnov 

Serão analisadas as distribuições de frequência acumulada dos preços médios desses produtos, através de visualização gráfica e do teste Kolmogorov-Smirnov. O último consiste em testar se as distribuições de probabilidade (frequência acumulada) desses preços vêm da mesma distribuição – intuitivamente, a ideia é testar se esses preços são próximos ou não. Esse resultado daria uma medida dessa proximidade entre os produtos, através do preço, e um argumento para a estimação de produtos diferenciados. Ainda, o uso do Kolmogorov-Smirnov é interessante porque é um teste nãoparamétrico, que não faz assunções sobre as distribuições de probabilidade das variáveis observadas para o teste (e.g. assunção de uma distribuição normal). 

Os testes serão feitos aos pares entre os preços das requerentes e das concorrentes e entre as próprias requerentes. Assim, poder-se-á observar a indistinção estatística entre as variáveis. O teste, com duas amostras, pode ser resumido pela seguinte equação: 

**==> picture [173 x 12] intentionally omitted <==**

Onde é a maior diferença entre as duas distribuições acumuladas; e são respectivamente as distribuições acumuladas empíricas do que se pode chamar de produto _a_ e produto _b_ ; _n_ e _n’_ são respectivamente o número de observações. E a estatística que verificará a significância do teste é a seguinte: 

**==> picture [39 x 19] intentionally omitted <==**

Onde é um nível de significância relacionado à função , com valores calculados estabelecidos[1] . A função do Stata – _ksmirnov_ – produz uma segunda estimativa com p- valores menos conservadores, que serão apresentados na coluna de p-valores corrigidos. 

## 2.1. Estimações de Demanda 

A equação de demanda apresenta a seguinte forma funcional: 

(3) 

Onde é a variável de atividade escolhida para o setor com o propósito de ser um deslocador de demanda e é o coeficiente respectivo. 

As variáveis e representam, respectivamente, as quantidades e os preços; são os resíduos da equação. Todas as variáveis foram logaritmizadas, de forma que descreve o valor da elasticidade. O número de preços para o cálculo de elasticidades cruzadas no somatório da especificação em (3) é alterado nas colunas apresentadas nos resultados e 

> 1 Pode se ver um resumo dos valores críticos calculados no seguinte link: http://www.soest.hawaii.edu/wessel/courses/gg313/Critical_KS.pdf. 

3 

foram utilizadas _dummies_ para outliers específicos em algumas estimações[2] . Uma referência para uma especificação econométrica similar pode ser encontrada no livrotexto de Davis e Garcés (2010)[3] , no capítulo de estimação de demanda. Como se pode ver por (3), faz-se uso da hipótese de que há alguma diferenciação e não há um preço único, deixando de lado a hipótese de produtos homogêneos. 

As séries mensais analisadas compreendem o período de janeiro de 2011 a dezembro de 2015. A grande maioria das séries analisadas aparentaram estacionariedade em análises preliminares, mas não se discute ordem de integração ou cointegração das equações em virtude do número baixo de observações e o baixo poder dos testes de raiz unitária, em razão das poucas observações – ver Haldrup e Jansson (2005)[4] . Toma-se a hipótese de que há algum tipo de diferenciação e que (3) está suficientemente bem especificada para a discussão desta nota, exceto pelos possíveis vieses de endogeneidade que serão discutidos abaixo. 

Em virtude da dificuldade de se obter uma estimativa em 2 estágios adequada com os custos que foram obtidos através de ofícios enviados às requerentes e às concorrentes, apresentam-se os resultados sem utilizar instrumentos para as variáveis de preço. O método de estimação para a equação (3) é a função _rreg_ do Stata, que produz um técnica de regressão robusta para _outliers –_ esses foram verificados em análises de _leverage_ e dos resíduos quadráticos normalizados. Regressões robustas englobam um número grande de opções, mas uma descrição do método de estimação pode ser encontrado em Hamilton (1991)[5] . No anexo apresentam-se as mesmas regressões via MQO. 

Salvo exceções limites, a estimação de demanda sem uma correção do viés de simultaneidade é sempre viesada. Contudo, executamos o teste assumindo que o viés de endogeneidade dos preços das firmas seja próximo nas diferentes equações, de forma que esse seria reduzido, por exemplo, na fração de um _diversion ratio[6]_ . Trata-se de uma hipótese forte, mas há também o fato de que uma das requerentes, a Solvay, comercializa os produtos analisados nesta nota em virtude de serem o resto da produção de PVC, o que permite considerar a hipótese de que a demanda pelo produto dessa empresa é mais exógena à oferta do que se poderia assumir a princípio, possuindo também um viés reduzido. Pelo fato de que a produção se dá em virtude da produção de outro produto, o PVC, não haveria o viés de simultaneidade entre oferta e demanda ou 

> 2 A retirada de _outliers_ ocorreu pela simples observação gráfica do _leverage_ da regressão com as variâncias dos resíduos e retirou-se a observação quando essa apresentava valores extremamente díspares graficamente. O que ocorreu essencialmente nas observações 23 e 45, nas demandas de soda cáustica e Ácido Clorídrico, considerando que foram utilizadas no geral 60 observações, de Jan/2011 a Dez/2015. Por Parcimônia, somente se fez _dummies_ para esses valores. 

> 3 DAVIS, P., & GARCES, E. G. (2010). _Quantitative Techniques for Competition and Antitrust Analysis._ Princenton: Princeton University Press 

> 4 HALDRUP, NIELS. JANSSON, MICHAEL. Improving Size and Power in Unit Root Testing. _Economics Working Papers 2005-02_ , Department of Economics and Business Economics, Aarhus University, p.1-26, 2005. 

> 5 Hamilton, L. How robust is robust regression? Stata Technical Bulletin nº 2, p. 21-26. Reprinted in Stata Technical Bulletin Reprints, vol. 1, pp. 169–175, C. 1991. 

> 6 Supondo que o viés da fórmula de _diversion ratio_ seja similar na estimação da elasticidade própria e cruzada – de uma outra demanda -, uma hipótese evidentemente forte, se chegaria ao desvio de demanda. 

4 

esse viés seria reduzido. Abaixo discutem-se brevemente os vieses de uma estimação MQO de demanda. A regressão robusta possui um coeficiente aproximadamente igual ao de MQO na ausência de _outliers_ , portanto se aproveita em algo da mesma intuição para os vieses que seriam obtido com MQO. 

Para ilustrar brevemente o viés – existente também nas coeficientes cruzados mas que não se discute aqui --, apresentar-se-á aqui de forma simplificada uma demanda com preço , quantidade e erros ; e uma oferta com preço , quantidade e erros . As relações das covariâncias e a equação de oferta, que oferecem a identificação do resultado abaixo passo a passo, podem ser encontradas em Hayashi (2000, pág. 188). 

Assim, segue a equação da demanda direta e de oferta: 

**==> picture [122 x 35] intentionally omitted <==**

**==> picture [119 x 13] intentionally omitted <==**

Com , temos que: 

**==> picture [75 x 22] intentionally omitted <==**

Onde e representam, respectivamente, a quantidade demandada e ofertada; representa o preço; e são, respecticamente, outros fatores que explicam a demanda e oferta além do preço, com as assunções adicionais e . Por existir o processo da equação de oferta (5), que também compreende e temos necessariamente, pelo resultado em (6), que . Logo, as estimações de MQO de demanda sofrerão um viés em amostras finitas, assim como um viés assintótico. Abaixo, esse viés assintótico possui uma determinada direção: 

**==> picture [62 x 23] intentionally omitted <==**

Como, porém, e , tem-se que: 

**==> picture [61 x 23] intentionally omitted <==**

**==> picture [82 x 22] intentionally omitted <==**

Como a covariância entre o preço e o deslocador de demanda é positiva se , pois ~~,~~ sabe-se que há um viés que leva à subestimação de (em módulo) estimado por MQO em (8) e (9) -- com as variáveis devidamente logaritmizadas. Em razão disso, é possível que as estimativas em MQO de elasticidade, principalmente se forem negativas e altas em módulo, podem indicar a existência de uma alta elasticidade, sob a hipótese de que essa fosse estimada adequadamente. 

5 

## 3. Resultados 

3.1. Descrição e análise de demanda da soda cáustica 

A soda cáustica líquida (NaOH) é uma _commodity_ produzida a partir da eletrólise da água com o cloreto de sódio através de três tecnologias: diafragma (soda cáustica Líquida Comercial), mercúrio (soda Caústica Líquida Rayon Grade) e membrana[7] . 

Esta nota toma por hipótese que o mercado relevante é nacional, muito embora não seja uma hipótese crucial neste trabalho. Dentre as estimações de demanda utilizadas, considera-se também as importações, muito embora estejam agregadas às quantidades das requerentes. 

Nesta seção também se executa uma análise dos preços dos diversos tipos de soda cáustica, sob a hipótese de que deve existir uma substituição entre os produtos produzidos com as três diferentes tecnologias, a soda cáustica membrana, mercúrio e diafragma de forma que não se descarta a hipótese de que são produtos indistintos para o consumidor. Também se incluem no anexo desta nota técnica análises de demanda que consideram os tipos de soda em separado. 

No Gráfico 1 pode-se observar a liderança da Braskem no período, bem como [CONFIDENCIAL]. 

## _Gráfico 1_ [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. 

No Gráfico 2, observa-se os dados de preços obtidos das requerentes e suas concorrentes. Os preços da Braskem, Solvay, Carbocloro e CMPC têm comportamento similar, enquanto que os da Canexus aparentam ser mais altos e os da Dow, mais baixos[8] . A proximidade gráfica dos preços de Carbocloro, Solvay e Braskem permite a inferência inicial de que esses devem ser os competidores mais próximos no mercado. A CMPC interrompe a sua comercialização em 2013 e, portanto, não se trata de um competidor de fato no mercado atual. 

> _7_ Conforme descrição do produto encontrada no site da Unipar Carbocloro sobre a utilização da soda cáustica: _“É utilizada na fabricação de sabões e detergentes, no tratamento de superfícies de metais ferrosos, na formulação de banhos de eletrodeposição, na mercerização de têxteis, na regeneração de resinas de troca iônica e na correção de pH em vários processos industriais, como os da indústria de alimento, álcool e farmacêutica”._ Disponível em: http://www.uniparcarbocloro.com.br/uniparcarbocloro/web/conteudo_pt.asp?idioma=0&conta=28&tipo= 48941&id=181905 Acessado em 24/11/2016. 

> 8 Todos os preços foram calculados a partir das quantidades em base seca, contudo pediu-se, na orientação para preenchimento dos dados em ofícios enviados, que o preço fosse dado no valor em que chega ao seu consumidor final. Não se descarta a hipótese de que exista alguma inconsistência no envio dos dados, mas os preços mais intrigantes são das empresas de pequena atuação no mercado (Katrium e Canexus) ou com uma atuação mais errática nas quantidades analisadas (como a Dow). 

6 

_Gráfico 2_ [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços Nominais. 

No Gráfico 3, foram traçadas as distribuições de frequências acumuladas. Novamente, Carbocloro, Solvay e Braskem apresentam os preços mais próximos. Seguindo as características destacadas no gráfico anterior, em geral – Dow, preços menores em toda sua distribuição de frequência, Canexus e Katrium, com preços mais altos. 

## _Gráfico 3_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços em Dez/2015 pelo IPA-FGV. 

Na Tabela 1, são mostrados os resultados do teste Kolmogorov-Smirnov para os preços deflacionados e que apresentaram maior proximidade gráfica. Nas comparações das distribuições acumuladas de preço da Solvay e da Braskem, e da Solvay e da Carbocloro, rejeitou-se a hipótese nula do teste (para um nível de significância de 5%) de que as distribuições são iguais. Assim, existe alguma evidência para a existência de patamares distantes entre as séries. A Carbocloro e a Braskem possuem preços mais similares e não se rejeita a hipótese nula de igualdade. 

_Tabela 1_ 

||_Tabela 1_|||
|---|---|---|---|
|**Hipóteses Testadas**|**Dif.**|**P-valor**|**P-Valor Corrigido**|
|H0: Solvay=Carbocloro|0.433|0.000|0.000|
|H0: Solvay=Braskem|0.483|0.000|0.000|
|H0: Carbocloro=Braskem|0.167|0.375|0.304|



Fonte: Requerentes. Elaboração DEE. Teste com Preços em Dez/2015 pelo IPA-FGV. 

## 3.2. Análise dos Diferentes Tipos de Soda Cáustica 

Segue com o Gráfico 4 as quantidades dos diferentes tipos de soda cáustica e as visualizações de preços, no Gráfico 5, para as empresas que apresentaram maior proximidade de preços (Carbocloro, Solvay e Braskem) na seção anterior. Quanto às quantidades, a Braskem continua com a maior venda, mas para um tipo específico, a soda diafragma; A Solvay possui a maior venda de soda membrana dentre as três empresas, aparentemente; a Carbocloro, possui uma venda mais distribuída entre os três tipos de soda. Há uma diferença de patamares, mas a tendência é similar. O preço da soda cáustica mercúrio fornecido pela Braskem está consideravelmente abaixo dos demais. 

_Gráfico 4_ [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. 

7 

_Gráfico 5_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços Nominais. 

No Gráfico 6 as distribuições de frequência acumuladas são apresentadas por empresa e tipo, com a ordenação anterior entre os preços se mantendo. Os preços mais caros são os de célula de mercúrio da Carbocloro e o mais barato, como destacado anteriormente, da célula de mercúrio da Braskem. 

## _Gráfico 6_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços em Dez/2015 pelo IPA-FGV. 

Na tabela 2, os testes Kolmogorov-Smirnov são apresentados. Nesse caso específico, analisa-se somente o preço da soda cáustica membrana da Solvay, [CONFIDENCIAL]. Rejeita-se a hipótese de igualdade das distribuições em quatro casos, mas não se rejeita a hipótese nula na comparação com a distribuição acumulada da soda cáustica mercúrio da Carbocloro. Isto é, o preço da soda cáustica membrana da Solvay é consideravelmente próximo ao preço da soda produzida através de outra tecnologia. Tal fato reforça o argumento de que os tipos de soda são substituíveis, apesar de destacar, também, a existência de preços que são também distintos em patamar, apesar de provavelmente seguirem a mesma tendência estocástica. 

_Tabela 2_ 

||_Tabela 2_|||
|---|---|---|---|
|**Hipóteses Testadas**|**Dif.**|**P-valor**|**P-Valor Corrigido**|
|H0: Membrana Solvay= Membrana Carbocloro|0.600|0.000|0.000|
|H0: Membrana Solvay= Mercúrio Carbocloro|0.1333|0.660|0.587|
|H0: Membrana Solvay=Diafragma Carbocloro|0.5167|0.000|0.000|
|H0: Membrana Solvay= Mercúrio Braskem|0.9333|0.000|0.000|
|H0: Membrana Solvay=Diafragma Braskem|0.2667|0.028|0.018|



Fonte: Requerentes. Elaboração DEE. Teste com Preços em Dez/2015 pelo IPA-FGV. 

No Anexo desta nota encontram-se os resultados da estimação de demanda para as diferentes tecnologias entre as três empresas – os resultados aparecem nas Tabelas A.1, A.2 e A.3. Em suma, pelos resultados obtidos, não se descarta a hipótese de substituição entre as diversas tecnologias. A tabela A.2, que apresenta resultados sem significância, impõe um limite a extensão das conclusões. 

Adiante, na Tabela 3, segue a análise de demanda da Carbocloro, com referência à especificação econométrica destacada na seção anterior. As colunas são referentes às distintas formas funcionais das regressões realizadas, que se diferenciam pelas variáveis 

8 

consideradas (as que estão nas linhas), ou seja, pelos demais preços, resultando em elasticidades cruzadas, e o IBC-Br[9] . 

Na primeira coluna, em que se utiliza somente uma elasticidade cruzada há coeficientes intuitivos e significantes, com exceção do deslocador de demanda utilizado, o logaritmo do IBC-Br. De fato, em todas as colunas, os poucos resultados minimamente intuitivos e significantes incluem elasticidades próprias e cruzadas para Carbocloro e Solvay (em adição à primeira, a quinta e a sétima coluna). Há, assim, alguma evidência de que quando a Solvay aumenta preços, há um aumento da demanda da Carbocloro, considerando as hipóteses que foram feitas na seção anterior. 

No que tange a Tabela 4, já não se acha efeitos claros de aumento de preços da Carbocloro sobre a Solvay. De fato, não se encontra estimação de demanda que produza resultados intuitivos, sendo, talvez, pouco elucidativa sobre a discussão de substituição de demanda no mercado de soda cáustica. 

Em resumo, a partir da analise de demanda da soda cáustica pode-se dizer que não se descarta a possibilidade de substituição ocorrer entre os produtos da empresas requerentes em virtude de um aumento de preços, mas só há evidência por um lado – aumento de preços da Solvay aumentam a demanda da Carbocloro, mas não há evidência clara do contrário. 

> 9 Índice de Atividade Econômica do Banco Central do Brasil, que pode ser obtido no sistema de séries temporais do Banco Central no seguinte link: https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries Acessado em 25 de Novembro. 

9 

_Tabela 3_ 

## [CONFIDENCIAL] 

_Tabela 4_ 

[CONFIDENCIAL] 

10 

## 3.3. Descrição e análise de demanda do hipoclorito de sódio 

O hipoclorito de sódio é um produto de difícil transporte, utilizado na produção de água sanitária, desinfecção de água potável e hospitalar e branqueamento de celulose e têxteis[10] . 

O mercado geográfico considerado foram os das regiões sul e sudeste, dado o difícil transporte. Além desta última característica, o que também permite desconsiderar as importações são os dados de importações de hipoclorito de sódio disponibilizados pelo AliceWeb[11] ; No período de janeiro de 2011 até dezembro de 2015 somam-se apenas 3,8 toneladas, o que é muito pouco representativo quando se observa o Gráfico 7. 

Além da Carbocloro e Solvay, as empresas consideradas no mercado relevante da operação são CMPC, Canexus e Katrium. Neste mercado, a Carbocloro tem uma liderança significativa. [CONFIDENCIAL]. 

## _Gráfico 7_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. 

No que tange aos preços, o comportamento observado pelas requerentes é distinto. A razão do padrão “acidentado” dos preços da Solvay pode estar relacionados à natureza residual desses produtos para a empresa. Do Gráfico 8, destaca-se a Katrium com uma tendência similar à da Carbocloro; a CMPC e a Canexus com preços próximos. 

## _Gráfico 8_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços Nominais. 

As distribuições acumuladas no Gráfico 9 dão uma outra visão à ordenação de preços acima, com destaque para a distribuição acumulada da Solvay que cruza a distribuição acumulada da Carbocloro. Na Tabela 5, o teste Kolmogorov-Smirnov não rejeita a hipótese nula de 5% de diferença entre as distribuições de preços da Solvay e da Carbocloro, mas ao que isso deve pesar a visualização gráfica acima e que os preços são trazidos para os preços de dez/2015 no teste através do IPA (Índice ao Produtor Amplo), que pode incidir de maneira mais alta ou mais baixa em diferentes pontos da série. Os preços altos da Solvay ocorrem no início da série e os preços seguem mais baixos ao final, uma distinção que não é observada ao se executar o teste do KolmogorovSmirnov. 

## _Gráfico 9_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços em Dez/2015 pelo IPA-FGV. 

> 10 Acessado em 24/11/2016: 

> 11 Disponível em: http://www.aliceweb.mdic.gov.br/ 

http://www.uniparcarbocloro.com.br/uniparcarbocloro/web/conteudo_pt.asp?idioma=0&tipo=48940& conta=28 

11 

Considerando que a Tabela 5 apresentou resultados pouco intuitivos em relação aos gráficos de preço, apresenta-se também uma versão do mesmo teste com os preços em nível na Tabela 6. Com as duas tabelas, verifica-se uma falta de proximidade entre a Katrium e Carbocloro e uma indistinção estatística na Tabela 6 entre as duas séries em nível; no caso da Solvay e da Carbocloro, rejeita-se a hipótese nula do teste em 10% na Tabela 5 e se rejeita fortemente a hipótese nula do teste, de igualdade das distribuições, na Tabela 6. A conclusão mais parcimoniosa é de que as séries de preços da Solvay e da Carbocloro pertencem a processos distintos. 

|o pertencem a processos distintos.|o pertencem a processos distintos.|o pertencem a processos distintos.|o pertencem a processos distintos.|
|---|---|---|---|
|_Tabela 5_||||
|**Hipóteses Testadas**|**Dif.**|**P-valor**|**P-Valor Corrigido**|
|H0: Solvay=Carbocloro|0.2167|0.12|0.085|
|H0: Katrium=Carbocloro|0.3|0.009|0.005|



Fonte: Req. e Concorrentes. Elaboração DEE. Teste com Preços em Dez/2015 pelo IPA-FGV. 

|_Tabela 6_|_Tabela 6_|_Tabela 6_|_Tabela 6_|
|---|---|---|---|
|**Hipóteses Testadas**|**Dif.**|**P-valor**|**P-Valor Corrigido**|
|H0: Solvay=Carbocloro|0.3667|0.001|0.000|
|H0: Katrium=Carbocloro|0.1833|0.266|0.206|



Fonte: Req. e Concorrentes. Elaboração DEE. Teste com Preços Nominais. 

Nas análises de demanda expostas nas Tabelas 7 e 8 existem alguns poucos resultados a se discutir, principalmente da estimação de demanda da Carbocloro e da Katrium. De acordo com a proximidade verificada nos gráficos e testes anteriores, a Katrium aparenta ter a substituição mais pronunciada em relação ao produto da Carbocloro, em virtude de um aumento de preços. 

Em relação a Solvay, não existe um indício de que um aumento de preço dessas produza uma queda na demanda da Carbocloro e vice-versa. 

12 

_Tabela 7_ 

## [CONFIDENCIAL] 

_Tabela 8_ 

## [CONFIDENCIAL] 

13 

## 3.4. Descrição e análise de demanda do ácido clorídrico 

O ácido clorídrico também é um produto de difícil transporte, utilizado na fabricação de coagulantes, tratamento de água e esgoto, processamento de minérios, entre outras utilizações[12] . Dados os aspectos logísticos, assume-se nesta nota a hipótese de que o produto possui a mesma dimensão geográfica de mercado que a do hipoclorito de sódio, isto é, o mercado é regional e composto das regiões sul e sudeste. 

A decisão de não realizar análise de importações decorre do fato de que no período de 2011-2015 foram importadas em média 2.172 toneladas por ano de cloreto de hidrogênio (ácido clorídrico) em solução aquosa (a moda é algo em torno de 684 toneladas), enquanto que para o cloreto de hidrogênio (ácido clorídrico) em estado gasoso ou liquefeito foram importadas apenas 22 toneladas em média, segundo o AliceWeb[13] . 

Além da Carbocloro e Solvay, as empresas consideradas no mercado relevante da operação são CMPC, Canexus e Katrium, tal como no caso do hipoclorito de sódio, descrito na seção anterior desta Nota Técnica. 

No Gráfico 10 apresenta-se um cenário similar ao do hipoclorito de sódio na ordenação das quantidades transacionadas, com a Carbocloro liderando novamente o mercado. [CONFIDENCIAL]. 

## _Gráfico 10_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. 

No Gráfico 11 também se observa o padrão “acidentado” dos preços da Solvay em relação às demais empresas. Observa-se, também, que há possivelmente mais diferenciação neste mercado, com as empresas utilizando diferentes estratégias de precificação. Ademais, nota-se que há uma mudança brusca no preço da CMPC ao longo da série e o preço maior da Katrium durante a maior parte da série. 

## _Gráfico 11_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços Nominais. 

Nos Gráficos 11 e 12, observa-se a falta de proximidade dos preços, em que os patamares são bastante diferentes, com o destaque para a Katrium com o maior preço e a distribuição “quebrada” da CMPC. As requerentes possuem maior proximidade, em termos de distribuição acumulada, em relação às demais concorrentes. Contudo, ao se observar a Tabela 8, se rejeita fortemente a hipótese nula de igualdade das distribuições. 

> 12 Disponível em: 

> http://www.uniparcarbocloro.com.br/uniparcarbocloro/web/conteudo_pt.asp?idioma=0&conta=28&ti po=48937&id=181885. Acessado em 24/11/2016. 

> 13Disponível em: http://www.aliceweb.mdic.gov.br/ 

14 

_Gráfico 12_ 

## [CONFIDENCIAL] 

Fonte: Requerentes e Concorrentes. Elaboração DEE. Preços em Dez/2015 pelo IPA-FGV. 

|_Tabela 9_|_Tabela 9_|_Tabela 9_|_Tabela 9_|
|---|---|---|---|
|**Grupos**|**Dif.**|**P-valor**|**P-Valor Corrigido**|
|H0: Solvay=Carbocloro|0.567|0.000|0.000|



Fonte: Requerentes. Elaboração DEE. 

Por fim, são analisadas as estimações de demanda referente ao ácido clorídrico. Na Tabela 10, na primeira coluna, tem-se um resultado intuitivo, com elasticidade própria significante, elasticidade-cruzada significante e os sinais intuitivos para uma demanda entre as requerentes. Note-se, porém, que a Canexus também adquire significância, com uma elasticidade-cruzada mais alta e que se mantém significante com a introdução de mais preços nas colunas seguintes. 

Na Tabela 11, não há os mesmos resultados intuitivos entre as requerentes na primeira coluna, mas há a elasticidade cruzada da CMPC que se mantém significante e aumentando de valor, mesmo com a introdução de mais preços, como se vê na sétima e na oitava coluna. Há também, novamente, a Canexus adquirindo um coeficiente intuitivo e significante nas últimas colunas, 7 e 8. Ou seja, mesmo com a introdução de mais parâmetros, a elasticidade cruzada da CMPC traz indício de maior proximidade entre essa empresa e a Solvay. Há o mesmo indício com a Canexus. 

Em resumo, este resultado do ponto de vista da análise antitruste, sugere que não há indícios conclusivos de efeitos anticompetitivos entre as requerentes no mercado analisado. 

15 

_Tabela 10_ 

## [CONFIDENCIAL] 

_Tabela 11_ 

[CONFIDENCIAL] 

16 

## 4. Conclusões 

Esta Nota Técnica fez uma avaliação dos produtos soda cáustica, hipoclorito de sódio e ácido clorídrico em virtude da aquisição da Solvay pela Carbocloro Unipar, operação descrita na introdução deste trabalho. 

Buscou-se examinar a proximidade das requerentes e as demais concorrentes no mercado com o fim de avaliar possíveis efeitos anticompetitivos da operação. Inicialmente, foram analisadas as distribuições de frequência acumulada dos preços médios dos produtos, por meio de visualização gráfica e do teste Kolmogorov-Smirnov. Este último testa se as distribuições de preço são indistintas estatisticamente. 

Ademais, foram realizadas estimações de demanda sem instrumentalização dos preços, por meio de regressões robustas para _outliers_ . O método possui fragilizadades, o que foi discutido em texto. 

Especificamente, em relação à soda cáustica, também se avaliou pelos métodos descritos acima se haveria uma proximidade entre os preços dos diferentes tipos de soda cáustica (mercúrio, diafragma e membrana) e se poderia existir uma relação de substituição entre os tipos de soda comparando estimações de demanda com os preços e quantidades de soda cáustica produzida por essas diferentes tecnologias. Há pelo menos uma proximidade grande, entre a soda membrana da Solvay e da mercúrio da Carbocloro, e não se descarta a possibilidade de substituição entre diferentes tipos de tecnologias, de acordo com os resultados das Tabelas A.1, A.2 e A.3 do anexo. 

Nos testes de preços, gráficos de preços nominais e distribuições acumuladas para os demais produtos e a soda agregada, a Braskem é mais próxima da Carbocloro; em hipoclorito de sódio, as requerentes não são próximas, sendo a Carbocloro provavelmente mais próxima da Katrium; em ácido clorídrico, os preços das várias empresas apresentaram pouca similaridade, sugerindo uma possível diferenciação maior no mercado. Do ponto de vista da análise antitruste, isso sugere uma distinção importante entre os preços das requerentes, indicando que é possível que os produtos não sejam tão próximos em relação às demais concorrentes e que a hipótese de produtos diferenciados esteja adequada. 

Nas estimações de demanda, em todos três mercados, não se pode descartar inteiramente a existência de substituição de demanda entre as requerentes, mas tal avaliação é prejudicada em virtude da baixa significância de grande parte das estimativas de elasticidade-cruzada ou a perda de significância com a inserção de mais variáveis. Contudo, mesmo assumindo que os coeficientes são válidos mesmo sem significância estatística, o desvio capturado da Carbocloro pela Solvay [CONFIDENCIAL] no caso do ácido clorídrico – no caso do hipoclorito de sódio não é possível obter esse resultado, devido à elasticidade própria positiva da Carbocloro. No caso da soda cáustica, o desvio [CONFIDENCIAL], mas a elasticidade-cruzada não é significante - ou seja, não há evidência contrária que esses mesmos resultados possam ser diferentes de zero. 

Assim, não há evidência conclusiva nesta nota em favor de possíveis efeitos anticompetitivos com a operação. 

17 

Brasília, 06 de dezembro de 2016. 

Assinado eletronicamente no âmbito da Nota Técnica 41 (Documento SEI 0276708) 

## DEE/CADE 

18 

## APÊNDICE 

PARTE I – Especificações por métodos distintos 

_Tabela A. 1_ 

## [CONFIDENCIAL] 

_Tabela A. 2_ 

## [CONFIDENCIAL] 

_Tabela A. 3_ 

## [CONFIDENCIAL] 

19 

PARTE II – Especificaçõs por MQO 

_Tabela A. 4_ 

## [CONFIDENCIAL] 

_Tabela A. 5_ 

## [CONFIDENCIAL] 

_Tabela A. 6_ 

[CONFIDENCIAL] _Tabela A. 7_ 

[CONFIDENCIAL] 

_Tabela A. 8_ 

[CONFIDENCIAL] 

_Tabela A. 8_ 

[CONFIDENCIAL] 

20 

