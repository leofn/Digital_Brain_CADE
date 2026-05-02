**==> picture [63 x 62] intentionally omitted <==**

## **Ministério da Justiça e Segurança Pública – MJSP Conselho Administrativo de Defesa Econômica – CADE** 

SEPN 515 Conjunto D, Lote 4 Ed. Carlos Taurisano, 4º andar - Bairro Asa Norte, Brasília/DF, CEP 70770-504 Telefone: (61) 3221-8409 e Fax: (61) 3326-9733 – www.cade.gov.br 

## **NOTA TÉCNICA Nº 30/2017/DEE/CADE** 

**Referência:** Ato de Concentração nº 08700.002165/2017-97 

**Requerentes:** ArcelorMittal & Votorantim 

**Ementa:** Ato de Concentração referente à aquisição, pela ArcelorMittal, da integralidade das ações representativas do capital social da Votorantim Siderurgia S.A. Análise de efeitos unilaterais por meio de simulações: PCAIDS e GUPPI. Análise de efeitos coordenados. Permanência de preocupações concorrenciais após análise dos argumentos apresentados pelas requerentes. 

**Versão:** Pública 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **1. Escopo da nota** 

Em atendimento ao despacho nº 963/2017 da Superintendência Geral do Cade, a presente nota técnica do Departamento de Estudos Econômicos do Cade (DEE/Cade) faz uma avaliação dos possíveis efeitos anticompetitivos da operação de aquisição, pela ArcelorMittal[1] , da integralidade das ações representativas do capital social da Votorantim Siderurgia S.A. (“VS”)[2] . Esta nota seguirá se referindo aos dois grupos como “Requerentes/Partes” ou, quando identificados individualmente, como “ArcelorMittal” para a primeira e “Votorantim” para a segunda. 

A presente nota técnica está dividida em oito seções. Na segunda seção são descritas as fontes das bases de dados utilizadas, os softwares e demais informações técnicas. A seção 3 elenca os mercados relevantes analisados empreendendo uma análise descritiva dos dados. A seção 4 descreve os métodos da avaliação quantitativa de efeitos unilaterais empregados nesta nota, o GUPPI e o PCAIDS. Em seguida, na seção 5, são apresentados os resultados dos testes quantitativos para o caso dos nove mercados relevantes examinados. A sexta seção realiza análise de poder coordenado, enquanto a seção 7 é dedicada a examinar o mercado de sucata. Por fim, a oitava seção destaca as conclusões verificadas nesta nota. 

> 1Grupo econômico composto por: ArcelorMittal Brasil S.A. (“ArcelorMittal”), ArcelorMittal Spain Holding SL (“ArcelorMittal Spain”), ArcelorMittal Aceralia Basque Holding SL (“ArcelorMittal Holding”), ArcelorMittal France (“ArcelorMittal France”), ArcelorMittal Luxembourg (“ArcelorMittal Luxembourg”), e ArcelorMittal Belgium (“ArcelorMittal Belgium”) 

> 2 Do grupo Votorantim S.A. 

2 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **2. Base de dados, softwares e informações técnicas** 

Com o objetivo de avaliar os possíveis efeitos anticompetitivos da referida operação de aquisição da Votorantim Siderurgia S.A. pela ArcelorMittal, o Departamento de Estudos Econômicos contou com os dados de preços, quantidades vendidas, custos e margens nos mercados em que as requerentes atuam em sobreposição. Os dados foram solicitados para as empresas nos mercados analisados por meio de ofícios. As empresas enviaram os dados com discriminação de produto e de Unidade da Federação de destino. O intervalo temporal contemplado inicia-se em janeiro de 2011 e vai até dezembro de 2016.  Para as análises, foi utilizado o software R. Além disso, utilizou-se o Excel, com o _add-in_ para o PCAIDS ( _Proportionally-Calibrated AIDS_ ), na versão PC AIDS 2.41, disponibilizado ao Departamento de Estudos Econômicos do Cade por um dos autores do artigo original do PC AIDS, Roy Epstein. 

As análises descritivas apresentam dados agregados em âmbito nacional, em termos anuais (ou mensais) e para cada um dos mercados. No caso das quantidades, o valor considerado foi o total vendido de um produto por empresa mensalmente (ou agregado anualmente), dentro do território nacional. No caso dos preços, foram calculadas médias mensais nacionais ponderadas (pelo volume por UF) para as empresas e deflacionadas mensalmente pelo IPCA **[3]** , de forma a controlar efeitos potenciais da inflação. Após deflacionar a série de preços das empresas, os mesmos foram ponderados pelas quantidades vendidas em cada um dos meses para que, por fim, fosse calculada uma média anual por empresa. Finalmente, as participações de mercado das empresas foram computadas em termos de quantidade vendida e receita auferida em cada ano (2011 a 2016). Aquelas que possuíam um _market share_ inferior a 5% - tanto em relação a volume, quanto em relação a receita - foram classificadas como “outras” nos gráficos da seção 3. 

Ademais, no processo de adequação dos dados e, buscando evitar distorções nas análises descritivas, as informações de preços/quantidades que foram preenchidas pelas 

> 3 No cômputo dos preços médios mensais não foram considerados fretes e impostos. Os preços, neste caso, são denominados preços “ _ex-works_ ”. Além disso, os preços foram deflacionados pelo IPCA, utilizando-se o período base dezembro de 2016. 

3 

_Nota Técnica nº 30/2017/DEE/CADE_ 

empresas com “0” (zero), foram substituídas por NA **[4]** (acrônimo para _not available_ ), de forma que os dados com essa classificação não fossem contabilizados nos cálculos das variáveis utilizadas nas análises. 

Por fim, com o intuito de mostrar robustez dos resultados quantitativos também foram utilizados os cálculos de _market share_ consolidados pela Superintendência Geral (SG)[5] que incluem para alguns mercados uma parcela de importações e/ou parcela de pequenas empresas. A diferença na consolidação dos dados surge, pois, para montar a base com dados tanto de preço quanto de quantidade, o DEE utilizou apenas as informações das empresas que apresentaram os dados em conformidade com a solicitação de preços e quantidades. Assim, foi possível comparar os resultados quantitativos utilizando diferentes consolidações dos bancos de dados e mostrar que, independentemente da base de dados utilizada, os resultados convergem para conclusões similares. 

> 4 Exceto casos em que o “0” indicava quantidade nula e não uma informação faltante. 

> 5 Quando o _market share_ consolidado pela SG é utilizado nesta nota técnica, isto é expressamente salientado. 

4 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **3. Análise descritiva dos dados** 

A análise empreendida por esta nota envolve a indústria de aços longos comuns. Os aços longos comuns são produtos utilizados, majoritariamente, na construção civil, sendo segmentados pelo formato, composição e aplicação dos mesmos. 

Vale salientar que o parecer “ _Consolidação e dinâmica competitiva no segmento de laminados longos comuns_ ” de lavra do professor Germano Mendes De Paula, apresentado pelas requerentes, faz uma ampla análise do referido mercado. Não é objetivo desta seção, revisitar todos os pontos discutidos naquele documento.  O objetivo desta seção será analisar separadamente e de forma descritiva os nove mercados citados abaixo, atentando-se para a evolução dos preços, volumes e _market shares_ das empresas (tanto em termos de volume como de receita). Tal análise é importante para contextualizar as discussões empreendidas nas seções subsequentes desta nota. 

No tocante ao mercado relevante de produto, ao todo, dez mercados são analisados por esta nota técnica. Esses dez mercados foram identificados juntamente com a SG como os potencialmente mais problemáticos, em termos concorrenciais, da presente operação e, por isso, o DEE focou a análise quantitativa destes. Com relação à definição do mercado geográfico, seguiu-se a jurisprudência do CADE, que o delimita como sendo nacional. Assim, temos os seguintes mercados analisados: (i) mercado nacional de barras; (ii) mercado nacional de perfis leves; (iii) mercado nacional de perfis médios/pesados[6] ; (iv) mercado nacional de fio-máquina comum; (v) mercado nacional de trefilados CA-60; (vi) mercado nacional de telas eletrosoldadas; (vii) mercado nacional de treliças; (viii) mercado nacional de arame recozido; (ix) mercado nacional de vergalhões (CA-25 e CA50). O mercado de sucata é foco da seção 7 desta nota. 

Destaca-se da resposta ao “Formulário de Notificação de AC” (Documento SEI n° 0323161), páginas 81-82, o seguinte: 

_“Em termos de qualidades e atributos, em geral, os aços longos comuns, essencialmente destinados à construção civil, são padronizados e normatizados. Há pouquíssimas diferenças técnicas relevantes entre eles,_ 

> 6 Os dados de perfis médios e pesados foram analisados conjuntamente, pois não foram apresentados de forma separada por algumas empresas. 

5 

_Nota Técnica nº 30/2017/DEE/CADE_ 

_assim como diferenciação de marcas. A dinâmica de concorrência no setor envolve fatores mais genéricos e presentes em outros mercados, como a confiabilidade de atendimento e disponibilidade de produtos. Nesse sentido, os aços longos comuns são considerados produtos “commoditizados”, sendo o preço uma das principais determinantes para a escolha do consumidor._ 

_Cumpre reiterar que, diante da homogeneidade dos produtos, não há fidelidade à marca que possa limitar a migração entre fornecedores concorrentes, visto que o principal item observado pelo consumidor é o preço. (_ ...) _[o] fornecimento se dá em modo spot, não exclusivo e independente de processo de homologação de fornecedores, evidenciando que a mudança para novos fornecedores pode ser feita em um curto espaço de tempo e a custos baixos_ .” 

_de tempo e a custos baixos_ .” 

Ademais, no referido parecer do professor Germano Mendes De Paula, ressaltase que: 

_“Embora as companhias desenvolvam esforços mercadológicos, na maioria dos produtos siderúrgicos, a diferenciação é pouco ou nada relevante na dinâmica competitiva. É verdade que existem marcas bem conhecidas, mas é pouco provável que um consumidor esteja disposto a pagar um prêmio considerável por um produto siderúrgico quando existe similar no mercado. Isto ajuda a explicar, inclusive, o considerável volume mundial de exportações de produtos siderúrgicos, muitas das quais intermediadas por trading companies” (págs. 29-30)._ 

Por fim, antes de empreender a análise descritiva, é importante ter em mente o peso relativo de cada mercado relevante em relação ao total, tanto em perspectiva das receitas de cada requerente como em relação à soma de todas as empresas do mercado. A tabela a seguir mostra esses valores. 

## **Tabela 3.1 – Receita por mercado relevante em 2016** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Faturamento em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

Observa-se que do total da receita dos nove produtos analisados, 50,3% advém do vergalhão. Esse percentual é **[ACESSO RESTRITO]** para cada uma das requerentes: vergalhão responde por **[ACESSO RESTRITO]** % das receitas da ArcelorMittal e por **[ACESSO RESTRITO]** % das receitas da Votorantim. Nota-se, também, a importância de ambas as empresas no mercado geral: a ArcelorMittal detém **[ACESSO RESTRITO]** % das receitas totais e a Votorantim por **[ACESSO RESTRITO]** %. 

6 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Com esses números em mente, passa-se à análise dos dados de cada um desses nove mercados relevantes de produto. Como já explicado na seção 2, os dados analisados a seguir não são iguais aos consolidados pela SG, visto que, para montar a base de dados com preço e quantidade, só foram consideradas as informações das empresas que apresentaram os dados em conformidade com a solicitação. Cabe frisar que tal opção na apresentação dos dados nesta seção não prejudicou a mensuração quantitativa dos efeitos unilaterais da operação empreendida na seção 5 visto que, quando daquela análise, também foram utilizadas as informações consolidadas pela SG. Foi possível, dessa forma, comparar os resultados utilizando diferentes consolidações dos bancos de dados. 

## 3.1 Mercado nacional de vergalhões 

Além das Requerentes, as principais empresas que produziram vergalhões (CA25 e CA-50) em 2016 foram: CSN, Gerdau, Silat, Simec e Sinobras. A líder de vendas foi a Gerdau, seguida pela ArcelorMittal e Votorantim, respectivamente. Em 2016, as Requerentes representaram, conjuntamente, cerca de **[ACESSO RESTRITO]** % do volume total vendido (ver Gráfico 3.1). As participações das empresas em relação às receitas auferidas permanecem semelhantes àquelas observadas no caso do volume total vendido (ver Gráfico 3.2). 

## **Gráfico 3.1 - Evolução do** _**market share**_ **no mercado de vergalhões (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.2 - Evolução do** _**market share**_ **no mercado de vergalhões (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Com relação ao movimento dos preços, verifica-se que a Sinobras é a que apresenta os níveis mais elevados, ao passo que os preços praticados pela Simec e CSN estão bem abaixo daqueles observados para o restante do mercado. **[ACESSO RESTRITO]** . Também é possível notar que os preços sofreram um movimento geral de queda a partir de 2014 (ver Gráfico 3.3). Quanto aos volumes vendidos, Gerdau, ArcelorMittal e Votorantim revelaram queda nas vendas, ao passo que Simec, Sinobras e CSN mantiveram patamares mais estáveis de quantidade vendida (ver Gráfico 3.4). 

7 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 3.3 - Evolução dos preços no mercado de vergalhões** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.4 – Evolução do volume no mercado de vergalhões** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. 

## 3.2 Mercado nacional de barras 

Em relação ao volume anual vendido, a Gerdau foi a líder do mercado, seguida pela ArcelorMittal, Cipalam e Ciafal, respectivamente. Em 2016, a Gerdau representou **[ACESSO RESTRITO]** % das vendas de barras, ao passo que a Arcelor e a Cipalam representaram cerca de **[ACESSO RESTRITO]** % e **[ACESSO RESTRITO]** %, nessa ordem (ver Gráfico 3.5). Quanto às receitas auferidas, a Gerdau continuou liderando o mercado, tendo em vista sua considerável participação no total vendido anualmente (ver Gráfico 3.6). Por fim, os Gráficos 3.7 e 3.8 apresentam os movimentos dos preços e quantidades vendidas, respectivamente. 

## **Gráfico 3.5 - Evolução do** _**market share**_ **no mercado de barras (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.6 -  Evolução do** _**market share**_ **no mercado de barras (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.7 - Evolução dos preços no mercado de barras** 

**[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.8 – Evolução do volume no mercado de barras** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. 

## 3.3 Mercado nacional de perfis leves 

Quando são observadas as participações das empresas nas vendas anuais em volume, nota-se que a Gerdau foi a líder do mercado, representando **[ACESSO RESTRITO]** % do total vendido em 2016. As Requerentes, por sua vez, ficaram logo 

8 

_Nota Técnica nº 30/2017/DEE/CADE_ 

atrás com participações **[ACESSO RESTRITO]** . Conjuntamente, as duas representaram **[ACESSO RESTRITO]** % das vendas de perfis leves em 2016. As distribuições das participações permanecem praticamente as mesmas quando são analisadas as receitas auferidas por cada uma das empresas nesse mercado (ver Gráfico 3.10). 

## **Gráfico 3.9 - Evolução do** _**market share**_ **no mercado de perfis leves (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.10 - Evolução do** _**market share**_ **no mercado de perfis leves (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Com relação aos preços praticados pelas empresas, nota-se que aqueles correspondentes à Ciafal estão bem acima daqueles observados para suas rivais. A referida diferença de preços pode ajudar a explicar o fato de a participação da Ciafal sofrer uma leve mudança quando são observadas as receitas auferidas no mercado de perfis leves. Além disso, destaca-se que, em termos reais, os preços caíram a partir de 2014 (ver Gráfico 3.11). Com relação ao volume, a quantidade vendida pela Gerdau vem caindo ao longo do tempo, ao passo que o total vendido pela ArcelorMittal e Votorantim sofreu variação ao longo do tempo. A Ciafal teve leve aumento das vendas (ver Gráfico 3.12). 

## **Gráfico 3.11 - Evolução dos preços no mercado de perfis leves** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.12 – Evolução do volume no mercado de perfis leves** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. 

## 3.4 Mercado nacional de perfis médios/pesados 

A Gerdau foi a que apresentou maior participação em termos das vendas. Em 2016, **[ACESSO RESTRITO]** % do volume vendido era proveniente da mesma. Além disso, as Requerentes apresentaram **[ACESSO RESTRITO]** ao longo do tempo. Se consideradas as participações conjuntas das empresas no ano passado, as mesmas representariam por volta de **[ACESSO RESTRITO]** % das vendas (ver Gráfico 3.13). 

9 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Quando as participações são analisadas em termos de receitas, nota-se que a São Joaquim é a que apresenta a maior variação de _market share_ . Assim, a participação da São Joaquim **[ACESSO RESTRITO]** (ver Gráfico 3.14). 

## **Gráfico 3.13 - Evolução do** _**market share**_ **no mercado de perfis médios/pesados (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.14 - Evolução do** _**market share**_ **no mercado de perfis médios/pesados (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Na análise dos preços, nota-se que os valores cobrados pelas participantes desse mercado sofreram fortes variações. Além disso, observa-se também que, em termos reais, os preços passaram a cair a partir de 2014 (ver Gráfico 3.15).  Em relação ao volume, a quantidade vendida pela Gerdau caiu ao longo dos anos, ao passo que a Arcelor e a Votorantim apresentaram uma estabilidade maior nas vendas (ver Gráfico 3.16). 

## **Gráfico 3.15 - Evolução dos preços no mercado de perfis médios/pesados** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.16 – Evolução do volume no mercado de perfis médios e pesados** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE 

## 3.5 Mercado nacional de fio-máquina comum 

A Gerdau é a líder do mercado de fio-máquina comum, chegando a representar, em 2014, cerca de **[ACESSO RESTRITO]** % do volume de vendas total. Já em 2016, o _market share_ da Gerdau reduziu para **[ACESSO RESTRITO]** %. As Requerentes ficaram logo atrás, com a Votorantim em segundo lugar e a ArcelorMittal em terceiro. Em 2016, a participação conjunta dessas duas últimas empresas foi em torno de **[ACESSO RESTRITO]** %. A Votorantim, foi a empresa que mais ganhou participação 

10 

_Nota Técnica nº 30/2017/DEE/CADE_ 

de mercado a partir de 2014 (ver Gráfico 3.17). A distribuição das participações de mercado quando são analisadas as receitas permanece muito semelhante. 

## **Gráfico 3.17 - Evolução do** _**market share**_ **no mercado de fio-máquina comum (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.18 - Evolução do** _**market share**_ **no mercado de fio-máquina comum (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Com relação aos preços praticados no mercado de fio-máquina comum, **[ACESSO RESTRITO]** . A CSN, por sua vez, praticou preços menores do que o restante de suas rivais, sofrendo grandes variações ao longo do tempo. Além disso, destaca-se também que, em termos reais, os preços caíram a partir do ano de 2014 (ver Gráfico 3.19). Quanto ao volume, nota-se que a quantidade vendida pela Gerdau tem caído consideravelmente nesse mercado, ao passo que as vendas da Votorantim, ArcelorMittal e CSN vêm crescendo (ver Gráfico 3.19). 

## **Gráfico 3.19 - Evolução dos preços no mercado de fio-máquina comum** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.20 – Evolução do volume no mercado de fio-máquina comum** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE 

## 3.6 Mercado nacional de trefilados CA-60 

Em termos de volume de vendas, as três maiores empresas do mercado foram ArcelorMittal, Gerdau e Votorantim. Ao longo dos anos, observa-se que **[ACESSO RESTRITO]** . Nesse mesmo ano, o total das vendas provenientes das Requerentes foi equivalente a **[ACESSO RESTRITO]** % do total. A Sinobras está entre as menores do mercado, mas tem crescido, **[ACESSO RESTRITO]** (ver Gráfico 3.21). O padrão do _market share_ permanece praticamente o mesmo quando analisado em termos de receita em cada um dos anos (ver Gráfico 3.22). 

11 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 3.21 - Evolução do** _**market share**_ **no mercado de trefilados CA-60 (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.22 - Evolução do** _**market share**_ **no mercado de trefilados CA-60 (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Quanto aos preços praticados nesse mercado, **[ACESSO RESTRITO]** . Por outro lado, a Sinobras, é a que pratica os maiores níveis de preços, se descolando consideravelmente dos valores observados para as demais empresas. Assim como em mercados analisados anteriormente, os preços de trefilados CA-60 também revelaram um movimento de queda a partir do final de 2013 (ver Gráfico 3.23). Sobre o volume de vendas, a ArcelorMittal e a Gerdau apresentaram queda no total vendido, ao passo que a Sinobras e Votorantim apresentaram volumes crescentes de vendas (ver Gráfico 3.24). 

## **Gráfico 3.23 - Evolução dos preços no mercado de trefilados CA-60** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.24 – Evolução do volume no mercado trefilados CA-60** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE 

## 3.7 Mercado nacional de telas eletrosoldadas 

No mercado de telas eletrosoldadas a ArcelorMittal foi líder de vendas, **[ACESSO RESTRITO]** . Observa-se que foi justamente após de 2013 que a Gerdau perdeu espaço nas vendas desse mercado, em meio ao crescimento da ArcelorMittal e Votorantim. Em 2016, a participação da ArcelorMittal e Gerdau nas vendas totais foram, respectivamente, **[ACESSO RESTRITO]** % e **[ACESSO RESTRITO]** %. A Votorantim, por sua vez, representou **[ACESSO RESTRITO]** % do total vendido no mesmo ano. Se consideradas as participações conjuntas das Requerentes em 2016, as duas seriam responsáveis por **[ACESSO RESTRITO]** % das vendas (ver Gráfico 3.25). O mesmo padrão pode ser observado em termos de receita (ver Gráfico 3.26). 

12 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 3.25 - Evolução do** _**market share**_ **no mercado de telas eletrosoldadas (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.26- Evolução do** _**market share**_ **no mercado de telas eletrosoldadas (receita) [ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Sobre o movimento de preços, observa-se que, no decorrer do período analisado, os valores cobrados pelas maiores participantes apresentaram um movimento geral de queda, que se acentuou ainda mais ao final de 2013 (ver Gráfico 3.27). Com relação às quantidades vendidas, o volume correspondente à ArcelorMittal e à Gerdau começou a cair ao final de 2014, ao passo que as vendas da Votorantim vêm crescendo ao longo do tempo (ver Gráfico 3.27). 

## **Gráfico 3.27 - Evolução dos preços no mercado de telas eletrosoldadas** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.28 – Evolução do volume no mercado de telas eletrosoldadas** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. 

## 3.8 Mercado nacional de treliças 

A Gerdau liderou o mercado de treliças, sendo responsável por cerca de **[ACESSO RESTRITO]** % das vendas do ano de 2016. Logo atrás ficaram a Arcelor e a Votorantim com, respectivamente, **[ACESSO RESTRITO]** % e **[ACESSO RESTRITO]** % de participação nas vendas do ano passado. Considerando-se a participação conjunta das requerentes nas vendas de 2016, **[ACESSO RESTRITO]** % seriam provenientes das mesmas (ver Gráfico 3.29). Ainda, quanto às participações de mercado em termos da receita auferida, observa-se que a Sinobras ganha maior participação de mercado (ver Gráfico 3.30). 

13 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 3.29 - Evolução do** _**market share**_ **no mercado de treliças (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.30 - Evolução do** _**market share**_ **no mercado de treliças (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

A respeito do movimento de preços, em termos reais, a Sinobras foi a que apresentou os níveis mais elevados. Além disso, nota-se que, em termos reais, houve um movimento generalizado de queda dos preços que se iniciou ao final de 2013 (ver Gráfico 3.31). Quanto às quantidades vendidas, o volume de vendas foi mais expressivo para a ArcelorMittal e Gerdau. Apesar de não ter vendido tal como essas duas últimas empresas, o volume de vendas da Votorantim foi ascendente no decorrer do tempo. Por fim, as vendas da Sinobras ficaram em níveis estáveis (ver Gráfico 3.32). 

## **Gráfico 3.31 - Evolução dos preços no mercado de treliças** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.32 – Evolução do volume no mercado de treliças** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE 

## 3.9 Mercado nacional de arame recozido 

Em termos de volume vendido, a ArcelorMittal e a Gerdau foram as empresas que lideraram o mercado, **[ACESSO RESTRITO]** . Além dessas participantes está a Votorantim que, no decorrer dos anos, vem ganhando maior presença e que, em conjunto com ArcelorMittal, representou cerca de **[ACESSO RESTRITO]** % das vendas, em termos de volume, de 2016 (ver gráfico 3.33). Quando se observam as participações em termos das receitas, a Gerdau também lidera o mercado ao longo de toda a série (ver gráfico 3.34). 

14 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 3.33 - Evolução do** _**market share**_ **no mercado de arame recozido (volume)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

## **Gráfico 3.34 - Evolução do** _**market share**_ **no mercado de arame recozido (receita)** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. As empresas com menos de 5% de _market share_ foram agregadas com o título “outras”. 

Com relação aos preços, nota-se que, em termos reais, houve uma queda nos preços a partir de 2014 das três empresas analisadas (ver Gráfico 3.35). Por sua vez, a queda nas quantidades vendidas foi mais pronunciada para a Gerdau. A Votorantim conseguiu manter seu volume de vendas mesmo durante a crise (ver Gráfico 3.36). 

## **Gráfico 3.35 - Evolução dos preços no mercado de arame recozido** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. Nota: Preço “ _ex-works_ ” em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA. 

## **Gráfico 3.36 - Evolução do volume no mercado de arame recozido** 

## **[ACESSO RESTRITO]** 

Elaboração: DEE. 

3.10. Breves considerações sobre a análise descritiva das informações recebidas 

Na análise de _market share_ nos mercados relevantes analisados, verificou-se que na maioria dos mercados a operação tornaria a empresa combinada líder de mercado. Em especial, verifica-se que no mercado de vergalhões, que representa cerca de 50% (em termos de receita) de todos os nove mercados relevantes analisados, a operação torna as requerentes líderes de mercado com **[ACESSO RESTRITO]** % de _market share_ . 

Ademais, analisando-se a dinâmica dos preços de ArcelorMittal e Votorantim, é possível verificar que a Votoratim apresenta sistematicamente preços inferiores aos praticados pela ArcelorMittal. Isto se verifica para a maioria dos mercados analisados, incluindo o mercado de vergalhões. 

Por fim, vale destacar que, dada a retração econômica dos últimos anos, verificouse uma diminuição da produção nos mercados acima discutidos e, consequentemente, um aumento da capacidade ociosa. Esse aumento também decorreu da entrada de novas firmas, que gerou incremento da capacidade produtiva da indústria. 

15 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Como se sabe, a princípio, a disponibilidade de capacidade ociosa pode ser vista como uma condição necessária para a constatação de rivalidade. Entretanto, como bem destaca o Guia de Análise de Atos de Concentração Horizontal (Guia-H, 2016, pág. 36) do CADE, “ _a existência de capacidade ociosa ou de expansão em empresas rivais não é incentivo suficiente para uma estratégia contestadora do exercício do poder de mercado da firma resultante, já que o uso da capacidade ociosa pode não ser lucrativo e é possível haver mercados com baixa rivalidade (e até colusão tácita e explícita), mesmo na presença de capacidade ociosa_ ”. Ademais, o documento da ICN (2013, pág. 26) argumenta que “ _o fato de as empresas que não se fundiram poderem expandir a produção ou a capacidade não significa necessariamente que elas o fariam: se as empresas tiverem excesso de capacidade e margens positivas, isso significa que, mesmo antes da fusão, elas podiam expandir a produção, mas decidiram não fazê-lo”[7]_ . Assim, a existência de capacidade ociosa é condição necessária, mas não suficiente para a existência de rivalidade. 

> 7 Tradução livre da versão em inglês: “ _the fact that non-merging firms could expand production or capacity does not necessarily mean that they would do so: if firms have excess capacity and positive margins, it means that even before the merger they could expand production but decided not to do so_ ”. 

16 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **4. Métodos quantitativos: GUPPI e PCAIDS** 

## 4.1. GUPPI 

A referência adotada para o GUPPI ( _Gross Upward Pricing Pressure Index)_ é Salop e Moresi (2009)[8] e, também, o _Competition Competence Report_ (2013) e a sua expressão final sintetizada no documento. Trata-se de um teste em que se assume competição em preços e produtos diferenciados, mas não se assume a existência de eficiências na expressão final, tal como na expressão final do UPP ( _Upward Pricing Pressure)_ , além de apresentar o resultado em proporção ao preço para o qual o GUPPI está sendo calculado. 

Assim, a expressão usada para o GUPPI resulta em: 

**==> picture [129 x 30] intentionally omitted <==**

Essa expressão é, por definição, positiva e devolve um valor percentual para o aumento de preços do produto após a fusão. Conforme explicado pela _Competition Competence Report_ (2013), a probabilidade de um aumento de preços após a fusão é influenciada por dois fatores: (i) o primeiro fator é a migração dos consumidores, também chamada taxa de desvio, do produto 1 para o produto 2. A taxa de desvio busca responder a seguinte pergunta: se o preço do produto 1 aumentar, qual parte dos consumidores irá mudar para o produto 2?; (ii) o segundo fator relevante é a margem de lucro bruta definida como a diferença entre o preço (p2) e o custo marginal (mc2). Em suma, a probabilidade de um aumento de preços após a fusão é calculada pela multiplicação da margem de lucro bruta e a taxa de desvio. 

No presente caso, a taxa de desvio foi calculada com base nos _market shares_ conforme segue: 

**==> picture [68 x 27] intentionally omitted <==**

> 8 SALOP, STEVEN. MORESI, SERGE. Updating the Merger Guidelines: Comments. 2009. Disponível em: https://www.ftc.gov/sites/default/files/documents/public_comments/horizontal-merger-guidelinesreview-project-545095-00032/545095-00032.pdf 

17 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Com essa hipótese, o percentual de vendas perdidas pela empresa 1 (ArcelorMittal) que é capturada pela empresa 2 (Votorantim) é representado pela expressão acima, envolvendo apenas os _market shares_ dessas empresas. Ademais, é importante ressaltar que tal hipótese é simplificadora. Entretanto, isso traz maiores preocupações apenas quando os produtos analisados são altamente diferenciados (Epstein e Rubinfeld (2004)). Outro ponto a destacar é que o GUPPI calculado na seção 5.1 considera o desvio de demanda da ArcelorMittal para Votorantim. Ou seja, calcula-se o aumento percentual de preço da ArcelorMittal. No Anexo A, têm-se os resultados de aumento de preço da Votorantim para o ano de 2016. 

## 4.2. _Proportionally-Calibrated_ AIDS (PCAIDS) 

O modelo adotado para o cálculo dos efeitos da presente operação pertence à classe de modelos _AIDS_ ( _Almost Ideal Demand System_ ), com o modelo original criado por Deaton e Muellbauer (1980)[9] . Porém, em razão de sua conveniência, para a presente análise utiliza-se o _PCAIDS_ ( _Proportionally Calibrated Almost Ideal Demand System_ ), criado por Epstein e Rubinfeld (2001)[10] . 

O modelo _AIDS_ necessita de vários parâmetros estimados, como as elasticidades cruzadas dos produtos no mercado definido para análise, o que exige tempo para o teste de diferentes especificações econométricas, se é que será realmente possível a obtenção de elasticidade cruzadas com valores intuitivos e significância estatística. Essas dificuldades favorecem o uso de um modelo que exige menos parâmetros estimados. Segue, no entanto, que há perda de complexidade na análise, pois será necessário assumir relações hipotéticas entre os produtos analisados para definir os parâmetros não estimados. 

A hipótese mais importante do modelo, inovando em relação ao _AIDS_ original, é a proporcionalidade no aumento de preço em relação ao _market share_ da empresa no mercado analisado. Recorre-se aqui ao exemplo de Epstein e Rubinfeld (2001) em uma versão do modelo em que cada empresa produz um único produto e se analisam três 

> 9 DEATON, A., & MUELLBAUER, J. (1980). An Almost Ideal Demand System. _American Economic Review, 70_ , 312-326. 

> 10 EPSTEIN, R. J., & RUBINFELD, D. L. (2001). Merger Simulation: A simplified approach with new applications. _Antitrust Law Journal, 69_ , 883-919. 

18 

_Nota Técnica nº 30/2017/DEE/CADE_ 

produtos (nomeados 1, 2 e 3). Abaixo definiremos as relações de _market shares_ e preços proposta por um modelo _AIDS_ : 

**==> picture [244 x 88] intentionally omitted <==**

onde os _S_ são os _market shares_ das empresas, os coeficientes _b_ com subscritos repetidos são os “coeficientes próprios” e os com subscritos diferentes são os “coeficientes cruzados”; intuitivamente, esses coeficientes possuem uma relação clara com as elasticidades-preço da demanda, ao que o “coeficiente próprio” deve ter um sinal negativo (um aumento de preços, dada a substitubilidade por outros produtos, diminui o _market share_ da empresa) e o “coeficiente cruzado” deve ter, por consequência, um sinal positivo. 

Diferenciando as equações acima, chega-se em parte da dinâmica que se pretende obter, geralmente, com os efeitos de uma fusão. Seguem as equações após a diferenciação total: 

**==> picture [195 x 142] intentionally omitted <==**

O modelo deixa clara a dificuldade e o tempo necessário para estimação dos parâmetros de um modelo _AIDS_ , já que mesmo em um caso hipotético simples compreende-se a necessidade de estimar nove parâmetros diferentes, os coeficientes próprios e cruzados (os coeficientes _b_ ) das três equações. 

A alternativa diante da necessidade de tantos parâmetros, definida por Epstein e Rubinfeld (2001), foi assumir uma relação de proporcionalidade. Em um exemplo usado no artigo, se a firma que produz o produto 2 possui um _market share_ de 40% e a firma 

19 

_Nota Técnica nº 30/2017/DEE/CADE_ 

que produz o 3, um _market share_ de 20%, o _market share_ da firma que produz o produto 2 deve aumentar duas vezes mais que a que produz o produto 3. Essa assunção permite definir uma relação matemática entre o coeficiente próprio e os coeficientes cruzados, de tal maneira que (no presente exemplo): 

**==> picture [147 x 23] intentionally omitted <==**

Essa assunção permite que o número de coeficientes não conhecidos caía de 9 para 3. A adição da hipótese de proporcionalidade, contudo, ainda permite diminuir mais ainda o número de parâmetro necessários para a estimação. O que se precisa, em síntese, para solucionar o sistema de equações são somente estimativas da elasticidade-preço da demanda para o mercado inteiro, a elasticidade-preço da demanda residual de uma das empresas e os _market shares_ das empresas[11] . As equações que resumem estas relações seguem abaixo e conduzem aos principais parâmetros de interesse: 

**==> picture [171 x 77] intentionally omitted <==**

**==> picture [178 x 48] intentionally omitted <==**

**==> picture [151 x 38] intentionally omitted <==**

onde 𝑒, com os subscritos 11, é a elasticidade-preço da demanda própria do produto 1 e 𝑒, sem os subscritos, é a elasticidade-preço da demanda de mercado; no caso dos subscritos distintos, _i_ e _j_ , tem-se a fórmula acima das elasticidades cruzadas. Dessa forma, podemos chegar a todos os parâmetros necessários para a fusão, ao que se comparará os efeitos pós fusão de uma empresa detentora dos novos produtos 

> 11 Os resultados estão provados no apêndice do artigo original de Epstein e Rubinfeld (2001).  Contudo, tenta-se neste documento destacar qual é a lógica principal do modelo. 

20 

_Nota Técnica nº 30/2017/DEE/CADE_ 

diferenciados, comparando a sua solução de maximização de lucro antes e depois da fusão. 

É notório que este modelo, com essas assunções, faz simplificações que limitam a complexidade da análise. Conforme os autores do modelo da simulação alertam, essas assunções podem fazer sentido em um mercado em que há pouca diferenciação entre os produtos. No caso em análise, esta parece uma hipótese válida. 

21 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **5. Análise dos resultados: efeitos unilaterais** 

Esta seção irá analisar os resultados obtidos para os potenciais aumentos de preços unilaterais associados à aquisição da Votorantim pela ArcelorMittal. Estes resultados são apresentados na forma do teste GUPPI e do modelo de simulação PCAIDS. 

## 5.1. GUPPI 

Nas subseções seguintes são apresentados os resultados, entre 2011 e 2016, para cada mercado relevante analisado, utilizando-se valores de _market shares_ calculados de maneira alternativa, como será explicado mais adiante. Os resultados foram calculados usando-se preços ( _ex-works_ ) e custos variáveis médios ponderados agregados anualmente a nível nacional. 

Vale ressaltar que o valor calculado do GUPPI é, por definição, positivo e devolve um valor percentual para o aumento de preços do produto analisado após a fusão. Os referenciais típicos para avaliar esses percentuais são aumentos de preços de 5%. Valores acima desses percentuais seriam mais preocupantes na avaliação da fusão hipotética. Ressalta-se, no entanto, que na existência de valores mais precisos de eficiências advindas da operação, estes devem ser usados como valores limítrofes de preocupações concorrenciais. Assim, o parecer da LCA intitulado “ _Aquisição da Votorantim Siderurgia pela ArcelorMittal Aços Longos: Análise de eficiências_ ” afirma na página 28 que “ _[e]m termos de custos variáveis, a Operação permitirá redução de_ **[ACESSO RESTRITO]** _do custo, explicitando o potencial de repasse das sinergias para o consumidor final_ ”. Em relação as eficiências alegadas, não se está aqui referindo que o DEE deva aceitar ou rejeitar tais eficiências, já que, como será demonstrado a seguir, ainda que eventualmente todas as eficiências alegadas sejam consideradas, as mesmas não são suficientes para impedir efeitos anticompetitivos derivados da presente operação na maior parte dos mercados analisados. 

Foram considerados três conjuntos distintos de _market shares_ implicando no cálculo de três taxas de desvio distintas para cada mercado, em cada ano. São eles: 

22 

_Nota Técnica nº 30/2017/DEE/CADE_ 

1. _Market shares_ baseados em quantidade (volume vendido), calculados com base nos dados de 2011 a 2016 solicitados às empresas, por meio de oficio[12] , pelo DEE. 

2. _Market shares_ baseados em receita (multiplicando preço e quantidade), calculados com base nos dados de 2011 a 2016 solicitados às empresas, por meio de oficio[13] , pelo DEE. 

3. _Market shares_ baseados em quantidade (volume vendido), com base nos dados utilizados na análise da SG que incluiu empresas independentes[14] e as importações como parte de mercado. Observa-se, a SG compilou dados para o período 2012 a 2016. 

A finalidade de se realizar o teste GUPPI em vários anos é avaliar se a pressão por aumento de preço tem ou não natureza circunstancial, levando-se em conta diferentes momentos do ciclo econômico. As tabelas das subseções a seguir compilam os resultados obtidos para cada mercado relevante em análise, de modo a tornar possível a comparação dos diversos anos. Entretanto, é importante ressaltar que o valor dos testes para o ano de 2016 é o mais apropriado para a análise desta operação, tendo em vista que representa o período mais recente disponível para a análise. Como já salientado, o GUPPI calculado a seguir considera o desvio de demanda da ArcelorMittal para Votorantim. Ou seja, calculase o aumento percentual de preço da ArcelorMittal. No Anexo A, são apresentados os resultados de aumento de preço da Votorantim para o ano de 2016. Os resultados do Anexo A corroboram as conclusões apresentadas abaixo. 

## 5.1.1. Vergalhão 

O mercado de vergalhão é o maior mercado relevante relacionado na operação (ver seção 4). O mercado de vergalhão tem claros problemas associados a aumento de preço relacionados à operação entre ArcelorMittal e Votorantim. Em todos os testes, o GUPPI apresenta um aumento de preço igual ou superior a 5,9% (ver Tabela 5.1). 

> 12 Ofícios de 2017 n° 3596, 3597, 3598, 3599, 3601, 3603, 3604, 3605, 3595, 3607 e 3608. 

> 13 Mesmos ofícios da nota de rodapé nº 10. 

> 14 No parecer “Consolidação e dinâmica competitiva no segmento de laminados longos comuns” de lavra do professor Germano Mendes De Paula, descreve-se os trefiladores independentes como sendo “ _empresas que possuem trefilas, sem relação acionária com siderúrgicas. Ou seja, compram fio-máquina no mercado (nacional ou importado) e o transformam em produtos trefilados (arames, principalmente)_ ” (pág. 126). 

23 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Tabela 5.1 – GUPPI para o mercado de vergalhão** 

|Vergalhão|Vergalhão|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|7,0%|7,8%|9,1%|8,3%|9,1%|5,9%|
||_Market share_<br>(Receita)|6,5%|7,2%|8,5%|7,8%|8,8%|5,9%|
||_Market share_<br>(Volume SG)|n.d.|7,2%|8,2%|7,2%|8,0%|6,0%|



Elaboração: DEE. 

Mesmo como uma tendência de queda nas margens das requerentes a partir de 2014, as participações de mercado das requerentes são tão consideráveis que ainda se alcançam significativas pressões por aumento de preços. Para o ano de 2016, tem-se o menor GUPPI calculado com o valor de 5,9%. 

## 5.1.2. Barras 

O mercado relevante de barras apresenta poucas evidências de pressão de preços: o valor mais alto para o GUPPI foi de 2% no ano de 2011 e, em 2016, ficou ao redor de 1%. 

**Tabela 5.2 – GUPPI para o mercado de barras** 

||Barras|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|2,0%|1,7%|1,3%|1,4%|1,2%|1,0%|
||_Market share_<br>(Receita)|1,8%|1,6%|1,2%|1,2%|1,1%|0,9%|
||_Market share_<br>(Volume SG)|n.d.|1,6%|1,2%|1,3%|1,1%|0,9%|



Elaboração: DEE. 

Segundo os dados compilados pelo DEE, o mercado de barras em 2016 conta com oito players, e os indicadores de concentração mostram uma perda de participação contínua da primeira colocada (Gerdau) ao longo dos anos. **[ACESSO RESTRITO]** . São as variações nas margens, que explicam a tendência de queda do GUPPI. De fato, as margens da Votorantim têm caído de forma consistente, de algo em torno de **[ACESSO RESTRITO]** % em 2011, para **[ACESSO RESTRITO]** % em 2016. 

24 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## 5.1.3. Perfis leves 

O mercado para perfis leves apresenta em 2016 um GUPPI entre 3,5% e 3,8%. Apenas em 2013 é possível encontrar valores acima dos 6%. Por sua vez, o Anexo A mostra um potencial de aumento unilateral de preços de até 8% em 2016. 

**Tabela 5.3 – GUPPI para o mercado de perfis leves** 

|Perfis leves|Perfis leves|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|2,8%|4,8%|6,8%|3,9%|4,6%|3,8%|
||_Market share_<br>(Receita)|2,7%|4,5%|6,3%|3,6%|4,2%|3,5%|
||_Market share_<br>(Volume SG)|n.d.|4,1%|6,1%|3,5%|4,2%|3,5%|



Elaboração: DEE. 

**[ACESSO RESTRITO]** é possível explicar variações do GUPPI pela análise das margens. 

## 5.1.4. Perfis médios/pesados 

Deve-se enfatizar que os dados de perfis médios e pesados foram agregados devido às dificuldades de classificação por parte das empresas. Já os _market shares_ consolidados pela SG consideraram perfis médios separadamente, o que pode justificar as discrepâncias de resultados. Conforme Tabela 5.4.1, a inserção dos perfis pesados fez os _market shares_ de ArcelorMittal e Votorantim caírem pela metade. 

**Tabela 5.4.1 –** _**Market shares**_ **para o mercado de perfis médios e pesados** 

|**Ano**|**Arcelor**|**Votorantim**|**Arcelor**|**Votorantim**|
|---|---|---|---|---|
||**SG**|**SG**|**DEE**|**DEE**|
||**Em volume**|**Em volume**|**Em receitas**|**Em receitas**|
|**2012**|**[ACESSO**|<br>**[ACESSO**|<br>**[ACESSO**|**[ACESSO**|
||**RESTRITO]**%|<br>**RESTRITO]**%|<br>**RESTRITO]**%|**RESTRITO]**%|
|**2013**|**[ACESSO**|<br>**[ACESSO**|<br>**[ACESSO**|**[ACESSO**|
||**RESTRITO]**%|<br>**RESTRITO]**%|<br>**RESTRITO]**%|**RESTRITO]**%|
|**2014**|**[ACESSO**|<br>**[ACESSO**|<br>**[ACESSO**|**[ACESSO**|
||**RESTRITO]**%|<br>**RESTRITO]**%|<br>**RESTRITO]**%|**RESTRITO]**%|
|**2015**|**[ACESSO**|<br>**[ACESSO**|<br>**[ACESSO**|**[ACESSO**|
||**RESTRITO]**%|<br>**RESTRITO]**%|<br>**RESTRITO]**%|**RESTRITO]**%|
|**2016**|**[ACESSO**|<br>**[ACESSO**|<br>**[ACESSO**|**[ACESSO**|
||**RESTRITO]**%|<br>**RESTRITO]**%|<br>**RESTRITO]**%|**RESTRITO]**%|



Elaboração: DEE. Nota: _Market share_ da SG consideram apenas perfis médios. 

Não se pode afastar as preocupações com aumentos de preços, já que, pelos resultados da SG, os percentuais de GUPPI estão em torno de 5%. 

25 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Tabela 5.4.2 – GUPPI para o mercado de médios e pesados** 

|Perfis médios|Perfis médios|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)<br>_Market share_<br>(Receita)<br>_Market share_*<br>(Volume SG)|2,5%|2,4%|2,7%|2,7%|2,5%|2,6%|
|||2,5%|2,2%|2,6%|2,6%|2,4%|2,3%|
|||n.d.|4,2%|4,7%|5,4%|4,8%|4,4%|



Elaboração: DEE. Nota: * _Market share_ consolidado pela SG considera apenas perfis médios. 

## 5.1.5. Fio-máquina comum 

Os resultados no mercado de fio-máquina comum também evidenciam problemas associados às pressões unilaterais de preços. O menor valor percentual de aumento de preços para 2016 é de 7,5%. 

**Tabela 5.5.1 – GUPPI para o mercado de fio-máquina comum** 

|Fio-máquina comum|Fio-máquina comum|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|7,6%|7,8%|8,1%|4,7%|7,9%|8,8%|
||_Market share_<br>(Receita)|7,6%|7,9%|8,2%|4,8%|8,0%|9,0%|
||_Market share_<br>(Volume SG)|n.d.|4,8%|4,8%|2,9%|6,2%|7,5%|



Elaboração: DEE. 

## 5.1.6. Trefilados CA-60 

O mercado de trefilados CA-60 apresenta um padrão para potenciais aumentos de preços. O menor GUPPI para o ano de 2016 é 8,7%. 

**Tabela 5.6 – GUPPI para o mercado de trefilado CA-60** 

||CA-60|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|5,9%|7,0%|9,3%|7,6%|9,2%|9,5%|
||_Market share_<br>(Receita)|5,8%|6,7%|8,9%|7,3%|8,6%|8,8%|
||_Market share_<br>(Volume SG)|n.d.|6,4%|8,5%|6,8%|8,4%|8,7%|



Elaboração: DEE. 

Não obstante os preços reais e os indicadores de concentração nesse mercado 

terem caído, a posição relativa da ArcelorMittal frente à Votorantim torna o desvio de demanda associado à operação cada vez mais relevante. 

26 

_Nota Técnica nº 30/2017/DEE/CADE_ 

O fato é que, no período de 2011-2016, a Arcelor tem um pico de _market share_ de **[ACESSO RESTRITO]** % em 2012 e cai para **[ACESSO RESTRITO]** % em 2016, ao mesmo tempo que a Votoratim apresenta um expressivo crescimento de **[ACESSO RESTRITO]** % para **[ACESSO RESTRITO]** % (em volume). Com a presente operação, a ArcelorMittal estará deixando de disputar com um player relevante nesse mercado, que ano após ano tem ganhado participação. 

## 5.1.7. Telas eletrosoldadas 

O mercado de telas apresenta claros problemas associados às pressões por aumentos de preço de forma unilateral. Em 2016, o menor GUPPI é de 6,1%. 

**Tabela 5.7 – GUPPI para o mercado de telas eletrosoldadas** 

|Telas eletrosoldadas|Telas eletrosoldadas|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|7,1%|8,3%|9,8%|9,8%|10,5%|9,6%|
||_Market share_<br>(Receita)|6,7%|7,5%|8,9%|9,0%|9,8%|9,0%|
||_Market share_<br>(Volume SG)|n.d.|5,1%|6,3%|6,2%|6,7%|6,1%|



Elaboração: DEE. 

Em um cenário em que as margens têm caído, o GUPPI passa a ser explicado pelo aumento significativo da participação da Votorantim nesse mercado. De 2011 a 2016, tal participação cresceu de **[ACESSO RESTRITO]** % para **[ACESSO RESTRITO]** % (em volume), enquanto que a Arcelor passou de **[ACESSO RESTRITO]** % para **[ACESSO RESTRITO]** %. 

## 5.1.8. Treliça 

O mercado de treliças não levanta tantas preocupações em termos de pressões de aumento de preços devido à operação. Em 2016, os aumentos variam entre 2,6% e 3,7%. Entretanto, há que se ressaltar que o Anexo A mostra um potencial de aumento unilateral de preço de até 6,4% em 2016, quando se analisam os incentivos da Votorantim em elevar preços. 

27 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Tabela 5.8 – GUPPI para o mercado de treliça** 

||Treliça|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|3,1%|2,2%|4,3%|4,2%|3,9%|3,7%|
||_Market share_<br>(Receita)|3,0%|2,1%|4,0%|3,9%|3,7%|3,5%|
||_Market share_<br>(Volume SG)|n.d.|1,5%|3,0%|2,9%|2,5%|2,6%|



Elaboração: DEE. 

Não obstante, a crescente participação da Votorantim no mercado, o cenário de queda das margens reduz o impacto do aumento do desvio de demanda. Ademais, tal mercado é composto por sete players com mais de 3% de mercado e outros players independentes. 

## 5.1.9. Arame recozido 

Com base nos cenários descritos para o mercado de arame recozido, não houve, em nenhum dos anos, pressão por aumento de preço superior a 3,5% a partir do teste GUPPI. 

**Tabela 5.9 – GUPPI para o mercado de arame recozido** 

|Arame recozido|Arame recozido|2011|2012|2013|2014|2015|2016|
|---|---|---|---|---|---|---|---|
|GUPPI<br>ArcelorMittal|_Market share_<br>(Volume)|2,7%|2,1%|3,1%|3,2%|3,0%|3,5%|
||_Market share_<br>(Receita)|2,5%|1,9%|3,1%|3,1%|2,7%|3,3%|
||_Market share_<br>(Volume SG)|n.d.|1,5%|2,1%|2,4%|2,2%|2,8%|



Elaboração: DEE. 

O que justifica a evolução do GUPPI é o crescimento do _market share_ da Votorantim nesse mercado, o que tem levado a taxas de desvio da demanda cada vez maiores. 

28 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## 5.2. PC-AIDS 

Nesta seção são discutidos os resultados do modelo de simulação PCAIDS para os mercados relevantes apresentados anteriormente. Recorre-se aqui a parâmetros considerados adequados para a análise da operação, o que inclui optar pelo uso dos _market shares_ de 2016 consolidados pela SG, que incluem pequenas empresas independentes e/ou importações como parte dos mercados analisados. Além disso, o modelo PCAIDS foi calibrado com elasticidade da indústria como sendo -1. Por sua vez, foram calibrados diferentes cenários para a elasticidade da ArcelorMittal como sendo: -3, -2 e -1,2.  Para cada mercado relevante, apresentam-se resultados sem e com eficiências de **[ACESSO RESTRITO]** % (conforme estimado no parecer da LCA intitulado “ _Aquisição da Votorantim Siderurgia pela ArcelorMittal Aços Longos: Análise de eficiências_ ”). 

Como exposto anteriormente, em relação as eficiências, não se está aqui referindo que o DEE deva aceitar ou rejeitar tais eficiências, já que, como será demonstrado a seguir, ainda que eventualmente todas as eficiências alegadas sejam consideradas, as mesmas não são suficientes para impedir efeitos anticompetitivos derivados da presente operação. 

Ademais, considera-se “generosa” a adoção do parâmetro de -1 para a elasticidade-preço da indústria. As estimativas encontradas na literatura são bem inferiores (em módulo), a saber: Schmidt e Lima (2006) chegou a uma elasticidade-preço de -0,14 para a demanda por aço no Brasil. Reis et al. (2013) encontraram valor de -0,24 para a elasticidade-preço da demanda de aço como um todo e de -0,10 em vergalhões. Por sua vez, Lovarato (2010)[15] estimou, a partir dos dados agregados da indústria siderúrgica, uma elasticidade-preço de -0,329. Em suma, todas as estimativas indicam que a demanda é inelástica. 

> 15 O autor fez dois exercícios, um com dados mensais agregados de toda indústria de aço, e outro com dados em painel anuais desagregados por produto. No primeiro exercício calculou-se o estimador de mínimos quadrados ordinários em dois estágios (2SLS), o que permitiu o uso de variáveis instrumentais. Para o exercício com o painel, fez-se uso de efeitos fixos e estimação de painel dinâmico e heterogêneo, este capaz de estimar efeitos de curto e longo prazo para as elasticidades. 

29 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Os resultados apresentados são os aumentos de preço ponderados pelos _market shares_ das empresas que formarão a nova companhia (a nova empresa resultante da aquisição da Votorantim pela ArcelorMittal). 

Dos nove mercados analisados, oito ensejam preocupações com aumentos unilaterais de preços: (i) vergalhões, (ii) perfis leves, (iii) perfis médios, (iv) fio-máquina comum, (v) trefilados CA-60, (vi) telas eletrosoldadas, (vii) arame recozido, e (viii) treliças. Os resultados encontrados com as simulações de fusões utilizando o PCAIDS reforçam as preocupações trazidas pela análise do GUPPI. 

Como é possível observar no Gráfico 5.10, para o mercado de vergalhão, com a assunção de eficiências para ambas requerentes da ordem de **[ACESSO RESTRITO]** % e a premissa de elasticidade própria de -3 para a ArcelorMittal, tem-se um aumento de preço de 4,4%. Em outros cenários, o aumento de preço é superior a 5%, deixando evidentes as preocupações associadas a aumentos de preços. 

Nos mercados de CA-60 (Gráfico 5.11) e telas eletrosoldadas (Gráfico 5.12), o que se observa, com o mesmo cenário descrito no parágrafo anterior, são altíssimas pressões de aumento de preço, chegando-se a valores de 11,5% e 7,5%, respectivamente. Ademais, neste mesmo cenário, para os mercados de perfis leves (Gráfico 5.13) e arame recozido (Gráfico 5.14) ficam evidentes as pressões de aumento de preços da ordem de 6,8% e 4,5%, respectivamente. É importante ressaltar que as pressões de aumento de preços nos mercados discutidos até aqui podem superar o valor de 20%, a depender dos parâmetros escolhidos. 

Já nos mercados de perfis médios (Gráfico 5.15) e fio-máquina (Gráfico 5.16) basta supor uma elasticidade própria de -2 para a ArcelorMittal, para se observarem resultados mais preocupantes. Nesse cenário, supondo as eficiências alegadas, chega-se a aumentos de preços da ordem de 4,7% e 5,1%, respectivamente. Entretanto, tais valores podem alcançar o valor de 15%, a depender dos parâmetros selecionados. 

Em relação ao mercado de treliças (Gráfico 5.17), este ainda revela alguma preocupação. No cenário de elasticidade em -2, por exemplo, apresenta potencial para aumento de preços de 5,9%. Quanto ao mercado de barras (Gráfico 5.18), o resultado é bastante compatível com o que foi atingido no GUPPI: apenas com a elasticidade mais baixa (-1,2) e sem eficiências é que se calcula um aumento superior a 5%. 

30 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 5.10 – PCAIDS para o mercado de vergalhão** 

**==> picture [426 x 278] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

**Gráfico 5.11 – PCAIDS para o mercado de trefilado CA-60** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

31 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Gráfico 5.12 – PCAIDS para o mercado de telas eletrosoldadas** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

**Gráfico 5.13 – PCAIDS para o mercado de perfil leve** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

32 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Gráfico 5.14 – PCAIDS para o mercado de arame recozido** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

**Gráfico 5.15 – PCAIDS para o mercado de perfil médio** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

33 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Gráfico 5.16 – PCAIDS para o mercado de fio-máquina** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

**Gráfico 5.17 – PCAIDS para o mercado de treliças** 

**==> picture [72 x 17] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

34 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **Gráfico 5.18 – PCAIDS para o mercado de barras** 

**==> picture [428 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
[ACESSO RESTRITO]<br>**----- End of picture text -----**<br>


Elaboração: DEE. 

35 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **6. Análise de poder coordenado** 

Além de exercício unilateral de poder de mercado, outra possível consequência negativa de um ato de concentração é o aumento dos incentivos à coordenação de empresas em um mercado. Quando empresas rivais atuam coordenadamente, pode ocorrer dano à rivalidade com impacto no bem-estar dos consumidores. O exemplo clássico de coordenação é a formação de cartel, situação em que existe um acordo entre as empresas para a fixação de preço ou a limitação da quantidade ofertada que seria observada sob concorrência. 

A coordenação, porém, não precisa ocorrer de forma explícita pela comunicação. É possível que agentes de mercado atuem fora do equilíbrio concorrencial, sem que necessariamente haja um ilícito.  É possível que firmas de um mercado mantenham preços acima dos níveis de concorrência competitiva, sem que necessariamente haja coordenação explícita. Esse tipo de coordenação é denominado coordenação tácita. 

Diversas características de mercado indicam se determinado mercado possui maior ou menor probabilidade de coordenação. Esses fatores foram mapeados pela literatura econômica e pelas agências antitruste com base em sua experiência. 

Em casos de atos de concentração, existe a preocupação se a aquisição elevaria os incentivos de determinadas empresas de um mercado a coordenar. Um método de avalição da probabilidade de poder coordenado consiste em verificar a existência no mercado de características que favorecem a coordenação.  O Guia de Análise de Atos de Concentração Horizontais do Cade indica quais características devem ser verificadas em casos de atos de concentração. 

No presente caso, além de verificar as características inerentes ao mercado em questão, é necessário ponderar que o setor de aços longos no Brasil passou por recentes mudanças que modificaram a estrutura dos mercados. Primeiramente, ocorreu a entrada de novas firmas que passaram a operar em alguns mercados do setor. Em segundo lugar, houve retração da demanda como consequência da recessão econômica brasileira. 

Nos últimos cinco anos, empresas como a Simec e a CSN passaram a ofertar alguns produtos como vergalhões. O efeito desse acontecimento pode ser observado na queda de participação de mercado das maiores empresas do setor e na redução dos índices de concentração do mercado, conforme apresentado na seção 3. 

36 

_Nota Técnica nº 30/2017/DEE/CADE_ 

A queda na demanda pode ser observada com os dados de volume e receita abaixo. 

|**Tabela 6.1 -**|**Evolução da Receita e Volume Comercializado (2011 -2016)**|**Evolução da Receita e Volume Comercializado (2011 -2016)**|**Evolução da Receita e Volume Comercializado (2011 -2016)**|**Evolução da Receita e Volume Comercializado (2011 -2016)**|**Evolução da Receita e Volume Comercializado (2011 -2016)**|
|---|---|---|---|---|---|
|**Produto**|**Ano**|**Receita**<br>**(R$**<br>**constantes**<br>**de**<br>**dez/2016)**|**Variação da**<br>**Receita 2011**<br>**-2016**|**Volume**<br>**(toneladas)**|**Variação do**<br>**Volume**<br>**2011 -2016**|
|Arame Recozido|2011|**[ACESSO RESTRITO]**||||
|Arame Recozido|2016|||||
|Barra|2011|||||
|Barra|2016|||||
|CA 60|2011|||||
|CA 60|2016|||||
|Fio-Máquina Comum|2011|||||
|Fio-Máquina Comum|2016|||||
|Perfis Leves|2011|||||
|Perfis Leves|2016|||||
|Perfis Médios|2011|||||
|Perfis Médios|2016|||||
|Telas Eletrosoldadas|2011|||||
|Telas Eletrosoldadas|2016|||||
|Treliça|2011|||||
|Treliça|2016|||||
|Vergalhão|2011|||||
|Vergalhão|2016|||||



Elaboração: DEE. Faturamento em R$ a preços constantes de dezembro de 2016 deflacionados pelo IPCA 

Comparando os anos de 2011 com 2016, fica claro que os mercados se contraíram. A receita se reduziu em todos os mercados e houve queda expressiva dos volumes comercializados para a maioria dos mercados analisados. 

Esse cenário de contração aliado à presença de novos _players_ torna improvável a entrada de novas empresas no curto prazo, visto que há capacidade ociosa proveniente dos investimentos das firmas entrantes e da queda do volume comercializado das firmas incumbentes. 

Apesar de a entrada de novos _players_ ter reduzido a concentração dos mercados, os níveis de concentração permaneceram elevados, conforme evidenciam os índices de concentração C3 e C4 apresentados na Tabela 6.2: 

37 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Tabela 6.2 - Indicadores de Concentração C3 e C4 pré-operação** 

|**Produto**|**C3**|**C4 **|
|---|---|---|
|Arame Recozido|89%|95%|
|Barra|75%|86%|
|CA-60|84%|90%|
|Fio-Máquina Comum|86%|95%|
|Perfis Leves|84%|95%|
|Perfis Médio|100%|100%|
|Telas Eletrosoldadas|78%|86%|
|Treliça|73%|85%|
|Vergalhão|73%|84%|



Elaboração: DEE. 

Nota: C3 e C4 calculados com base em dados de volume de 2016 consolidados pela SG. 

Com a aquisição, os indicadores de concentração aumentariam ainda mais, conforme mostra a Tabela 6.3. 

**Tabela 6.3 - Indicadores de Concentração C3 e C4 pós-operação** 

|**Produto**|**C3**|**C4 **|
|---|---|---|
|Arame Recozido|95%|97%|
|Barra|79%|89%|
|CA-60|90%|93%|
|Fio-Máquina Comum|95%|100%|
|Perfis Leves|95%|100%|
|Perfis Médio|100%|100%|
|Telas Eletrosoldadas|86%|91%|
|Treliça|85%|89%|
|Vergalhão|84%|90%|



Elaboração: DEE. 

Nota: C3 e C4 calculados com base em dados de volume de 2016 consolidados pela SG. 

38 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Portanto, mesmo com os movimentos recentes, o mercado ainda é caracterizado por uma concentração excessiva com uma quantidade reduzida de firmas dominantes. Os índices de concentração apresentados exigem análise mais criteriosa. Deve-se, então, verificar como as características de mercado afetaram a probabilidade de coordenação, ponderando para o fato de que esse mercado passou por mudanças recentes. 

Seguindo o modelo apresentado em Tirole (1989)[ 16] , as empresas de um mercado possuem duas estratégias viáveis: cobrar um preço competitivo ou um preço de colusão que é maior. A coordenação ocorre quando as firmas decidem cobrar preços de colusão em todos os períodos em que elas interagem. Porém, se em algum momento uma empresa decide cobrar um preço competitivo quando a outra cobra o preço de colusão, temos que a empresa que desviou da colusão ganha participação e eleva a sua receita de mercado no período do desvio. Esse evento desencadeia uma guerra de preços competitivos em todos os períodos seguintes. 

A escolha de coordenação ou não entre empresas de um mercado é então uma decisão que pondera os benefícios de curto prazo do desvio com os ganhos de coordenação. Analisando um caso simples de coordenação com produto homogêneo e empresas iguais descrito por  Ivaldi et al (2003), se duas firmas produzem o mesmo bem e possuem o mesmo custo marginal, a competição em preço leva essas firmas a fazer preço igual a custo marginal. Isto é, o preço seria 𝑝= 𝑐 e não há possibilidade de qualquer lucro supra competitivo. No entanto, se as firmas decidem trabalhar em conluio e colocar preço 𝑝[𝑐] > 𝑐, elas podem dividir o mercado de modo que cada firma domine metade e tenha, assim, metade do lucro dado por  𝜋[𝑐] = (𝑝[𝑐] −𝑐)𝐷(𝑝[𝑐] ). Caso alguma das firmas desvie do conluio, o resultado é uma guerra de preços que leva à situação de  𝑝= 𝑐. 

Se as firmas possuem o mesmo desconto intertemporal dado por 𝛿, na situação de 𝜋[𝑐] 𝜋[𝑐] 𝜋[𝑐] conluio, cada firma obterá + 𝛿 + 𝛿[2 𝜋][𝑐] + ⋯= (1 + 𝛿+ 𝛿[2] + ⋯). Porém, se 2 2 2 2 uma das firmas desvia, ela domina todo o mercado e obtém 𝜋[𝑐] , mas elimina a possibilidade de lucros futuros. Por conseguinte, uma firma estará disposta a manter-se 𝜋[𝑐] 1 no conluio se (1 + 𝛿+ 𝛿[2] + ⋯) ≥𝜋[𝑐] + 𝛿× 0, ou seja, se 𝛿≥𝛿[∗] ≡ , onde 𝛿[∗] é a 2 2 1 taxa de desconto de equilíbrio. Isso ocorre, pois (1 + 𝛿+ 𝛿[2] + ⋯)= . 1−𝛿 

> 16 O modelo tradicional de interação estratégica foi proposto por Friedman (1971) e pode ser aplicado para a interação estratégia entre empresas de um mercado. 

39 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Nesse exemplo simplificado, temos que todas as firmas são iguais e o fator de desconto intertemporal 𝛿 é a única característica que determina se as firmas entram em coordenação ou não. Na sequência, são apresentadas diversas características de mercado e como a presença delas permite que a coordenação em um mercado seja mais provável ou não. 

A primeira característica analisada é a quantidade de firmas de um mercado. Quanto mais empresas operam em um determinado mercado, mais improvável é a coordenação. Primeiramente, temos que quanto mais empresas operam em um mercado, mais difícil é determinar qual seria o preço e participação de mercado que satisfariam todas as empresas para uma coordenação. A dificuldade em determinar o preço de equilíbrio das empresas seria então um impedimento à coordenação tácita em que não há comunicação. 

O segundo impedimento é que quanto mais empresas operam no mercado, menor é a participação de cada empresa do acordo em colusão. Isso significa que uma empresa que adota preços competitivos, enquanto as outras operam sob colusão,  adquire parcela maior de participação de mercado desviado de todas as outras concorrentes. Quando as firmas entram em coordenação, menor é a participação de mercado de cada firma restante. Assim, o aumento do número de firmas eleva os incentivos a traição e reduz os benefícios de longo prazo da colusão. 

Utilizando o exemplo de Ivaldi et al (2003), considere o caso em que há 𝑛 firmas que produzem um mesmo bem com custos marginais idênticos. No caso em que há 𝜋[𝑐] 𝜋[𝑐] 𝜋[𝑐] conluio no preço 𝑝[𝑐] , cada firma obtém + 𝛿 + 𝛿[2 𝜋][𝑐] + ⋯= (1 + 𝛿+ 𝛿[2] + ⋯). 𝑛 𝑛 𝑛 𝑛 Se há desvio por parte de uma firma, ela obtém lucro 𝜋[𝑐] , mas gera uma guerra de preços que levará 𝑝= 𝑐 e impedirá a possibilidade de lucros futuros. Assim, uma firma estará 𝜋[𝑐] disposta a manter o preço de conluio se (1 + 𝛿+ 𝛿[2] + ⋯) ≥𝜋[𝑐] +δ× 0, ou seja, se 𝑛 1 𝛿≥𝛿[∗] (𝑛) ≡1 − ~~.~~ 𝑛 

1 Quando 𝑛= 2, temos o caso anterior  em que 𝛿≥𝛿[∗] (𝑛) ≡ . Porém se 𝑛= 3, 2 2 tem-se 𝛿≥𝛿[∗] (𝑛) ≡ .  Ou seja, quando há três empresas, as empresas têm que ser mais 3 pacientes para que a coordenação seja viável do que se só houvesse duas empresas. 

40 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Quanto mais assimétricas as empresas do mercado, mais difícil é a coordenação. As empresas que detém menor participação de mercado possuem mais incentivos a desviar demanda pois quanto menor a participação das empresas da franja, maiores os incentivos que elas possuem para desviar, já que podem obter maior participação de mercado. 

Utilizando novamente um exemplo de Ivaldi et al (2003), suponha que há duas 1 1 firmas competidoras com _market shares_ dados por 𝑠≤ e 1 −𝑠≥ de modo que a firma 2 2 com menor _market share_ vai estar disposta a manter o preço de conluio desde que 𝛿 𝑠𝜋[𝑐] (1 + 𝛿+ 𝛿[2] + ⋯) ≥𝜋[𝑐] + 𝛿× 0, ou, equivalentemente, (1 −𝑠)𝜋[𝑐] ≤ (𝑠𝜋[𝑐] − (1−𝛿) 0), ou ainda, 𝛿≥𝛿[∗] (𝑠) ≡1 −𝑠. A ideia do modelo é indicar que o conluio se torna mais difícil quando o _market share_ das duas firmas é mais assimétrico. 

Os autores ressaltam, porém, que a participação de mercado é uma variável endógena dependendo, então, de outros fatores como diferencial de estrutura de custo ou diferenciação de produto. De forma geral, assimetrias entre os participantes de mercado reduzem a probabilidade de coordenação. Porém, no caso em questão, a assimetria de participação de mercado é consequência da recente entrada de empresas no mercado. Temos então que, por esse fator, a recente entrada de empresas no mercado reduziu a probabilidade de coordenação intrínseca desse mercado. 

A colusão é difícil de ser sustentada se não existirem barreiras à entrada. A coordenação implica em preços de mercado acima do competitivo. Dessa forma, sem barreiras relevantes, novas firmas tenderiam a entrar nesse mercado. Assim, a probabilidade de coordenação cresce à medida que existam maiores barreiras de entrada no mercado. 

O mercado analisado em questão é peculiar pois, conforme discutido anteriormente, as entradas recentes, a capacidade ociosa e a queda da demanda são fatores que reduzem a probabilidade de entrada no curto prazo. Assim a questão de barreiras à entrada não é crucial para a análise de poder coordenado no cenário atual. 

A coordenação de mercado é facilitada se o mercado apresenta transparência.  Para que uma firma decida punir a outra, ela precisa determinar se essa firma desviou da coordenação. Desse modo, informações sobre a atuação dos outros participantes do mercado devem estar disponíveis para que a colusão se sustente. Note-se que não é 

41 

_Nota Técnica nº 30/2017/DEE/CADE_ 

essencial que os preços sejam diretamente observados. Basta que, com as informações disponíveis, as concorrentes consigam inferir se elas estão perdendo participação de mercado. 

O setor de siderurgia é um setor maduro, de modo que a tecnologia de produção não difere significativamente entre as empresas de mercado. Isso permite que as empresas consigam inferir fatores como capacidade de produção e custos sem necessariamente precisar observar os preços. 

O setor siderúrgico passou por um período de queda de demanda que levou a uma redução da demanda de aços. Como discutido por Rotenberg and Saloner (1986), em momentos em que o mercado passa por um _boom_ , ou seja, quando a demanda está acima da média do mercado, a colusão é mais difícil. A decisão da firma é se os ganhos de receita de curto prazo compensariam uma guerra de preços futura, quando a demanda estará no seu ponto mais elevado e os benefícios do desvio serão maiores. 

O caso brasileiro é o inverso. O mercado está em um momento de baixa demanda, de modo que os benefícios de uma competição acirrada não são tão interessantes hoje quanto seriam em situações normais de mercado. 

Por outro lado, a crise econômica por que o Brasil passa atualmente é uma das maiores da história e criou desequilíbrios na economia de forma geral.  Não há garantia para os agentes econômicos sobre quando e como a recuperação ocorrerá. Esse ambiente de incertezas reduz a previsibilidade dos agentes de mercado, reduzindo a probabilidade de colusão. 

Temos então que os efeitos da crise econômica são ambíguos, indicando que não é possível afirmar com certeza quais seus impactos sobre a probabilidade de coordenação. 

Outra característica que deve ser analisada é a frequência com que as firmas interagem. Se as firmas estão constantemente ofertando os seus produtos, fica mais fácil determinar e consequentemente punir as empresas que desviam da interação. 

Considere o duopólio simples utilizado no primeiro modelo, mas, assuma agora que as firmas só interagem entre si a cada 𝑇 períodos. Isto é, as firmas só competem no período 1, 𝑇+ 1, 2𝑇+ 1 e assim por diante de modo que uma frequência maior de 𝜋[𝑐] interação indica um menor 𝑇. O conluio será sustentável se (1 + 𝛿[𝑇] + 𝛿[2𝑇] + ⋯) ≥ 2 

42 

_Nota Técnica nº 30/2017/DEE/CADE_ 

1 𝜋[𝑐] + 𝛿[𝑇] × 0, isto é, se 𝛿≥ 𝛿[∗] (𝑇) ≡ 1 ~~.~~ A conclusão fundamental desse modelo é que, 2 ⁄𝑇 quando as firmas interagem com menor frequência, o conluio é mais difícil de se manter, porque o custo de desvio se torna menor. 

Argumento análogo pode ser feito para a capacidade das firmas de reajustar seus preços. Quanto mais rígidos forem os preços, mais tempo demorará para uma firma punir a outras. Observando a evolução de preços desse mercado nas seções de descrição de dados, foi observado reajuste frequente de preços, indicando que, por esse fator, esse mercado pode ser problemático. 

Outra característica relevante é o fato de que as empresas atuam em diversos mercados diferentes do setor de aços longos. Ou seja, elas possuem uma interação multimercado, conforme pode ser verificado na tabela 6.4, que indica os mercados em que cada empresa atua. 

**Tabela 6.4 – Atuação das Empresas nos Mercados Relevantes em 2016** 

|**Firma**|Arame<br>recozido|Barras|CA-<br>60|Fio-<br>máquina<br>comum|Perfis<br>Leves|Perfis<br>médios|Telas<br>eletrosoldadas|Treliça|Vergalhão|
|---|---|---|---|---|---|---|---|---|---|
|**Arcelor**|1|1|1|1|1|1|1|1|1|
|**Ciafal**|0|1|0|0|1|0|0|0|0|
|**Cipalam**|0|1|0|0|0|0|0|0|0|
|**Cosmetal**|0|1|0|0|0|0|0|0|0|
|**CSN**|0|0|1|1|0|0|0|0|1|
|**Gerdau**|1|1|1|1|1|1|1|1|1|
|**São**<br>**Joaquim**|0|0|0|0|0|1|0|0|0|
|**Silat**|0|0|1|0|0|0|1|1|1|
|**Simec-GV**|0|0|0|0|0|0|0|0|1|
|**Sinobrás**|0|1|1|1|0|0|1|1|1|
|**Spillere**|0|1|0|0|0|0|0|0|0|
|**Votorantim**|1|1|1|1|1|1|1|1|1|
|**Total**|3|8|6|5|4|4|5|5|7|



Elaboração: DEE Nota: “1” denota participação no mercado e “0” denota não participação. 

43 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Apesar de cada um dos produtos acima ser um mercado relevante separado, as empresas atuantes nesses mercados são similares. Os efeitos da atuação multimercado na probabilidade de interação são diversos. Esse fato foi reconhecido pela teoria econômica - ver Bernheim e Whinston (1990) - e corroborado pela evidência empírica: Evans e Kessides (1994) analisaram o mercado de transporte aéreo e Parker e Röller (1997) analisaram o setor de telecomunicações. 

O primeiro efeito da atuação multimercado é que ela aumenta a interação entre as mesmas empresas e, como já visto, quanto mais frequente a interação, maior é a probabilidade de coordenação. Outro efeito é que a atuação multimercado permite suavizar assimetrias existentes em cada mercado específico. Por exemplo, uma firma que tem baixa participação em um mercado -  que teria a princípio baixo incentivo de coordenação -  pode entrar em um acordo que englobe outro mercado em que ela possui uma participação mais elevada. Essa lógica é similar para os outros tipos de assimetria como diferencial de custos e capacidade. 

Firmas podem, estão, sacrificar participação em alguns mercados como forma de chegar ao equilíbrio cooperativo que componha diversos mercados, sendo que em cada mercado individualmente a coordenação não seria necessariamente alcançada. 

Seguindo Ivaldi de et al (2003), suponha que há duas firmas em duopólio em um mercado e que, em outro mercado, essas duas firmas enfrentam um outro competidor. Conforme os modelos anteriores, no primeiro mercado, as duas firmas devem sustentar o 1 conluio se a taxa de desconto intertemporal dessas firmas é superior a ~~,~~ mas, a priori, não 2 podem sustentar o conluio no segundo mercado se o desconto intertemporal for inferior 2 a 3 ~~.~~ 

No entanto, mesmo nessa situação, pode ser possível sustentar o conluio. A intuição é que as duas firmas que interagem em duopólio no primeiro mercado podem dar um _market share_ maior para o competidor no segundo mercado para que ele tenha incentivos suficientes para manter o conluio nesse mercado. Entre as duas firmas, a confiança de manutenção do conluio dependerá da interação entre elas no primeiro mercado. 

Formalmente, as duas firmas que atuam em duopólio no primeiro mercado podem deixar o _market share_ de 𝛼= 1 −𝛿 para o competidor no segundo mercado e, assim, 

44 

_Nota Técnica nº 30/2017/DEE/CADE_ 

ainda podem dividir a remanescente parte do mercado, que é dada por 𝛿. Por conseguinte, 1 𝛿 o conluio entre essas duas firmas deve-se manter se 𝜋[𝑐] + 𝜋[𝑐] + ⋯) ≥ (2 2 ) (1 + 𝛿+ 𝛿[2] 3 𝜋[𝑐] + 𝜋[𝑐] + 𝛿× 0, ou seja, se 𝛿≥ . 5 

Dessa forma, a taxa de desconto intertemporal de limite para a manutenção do 1 2 conluio é maior do que e menor do que de modo que, se as firmas possuem desconto 2 3 5 2 intertemporal entre e ~~,~~ elas podem sustentar o conluio em ambos os mercados, muito 12 3 embora não pudessem sustentar o conluio se estivessem presentes apenas no segundo mercado. 

Os fatores discutidos acima são consequência da literatura econômica que se debruçou sobre a questão de coordenação estratégica. Porém, não só a academia analisou a questão de poder coordenado. As agências antitruste na sua experiência de atuação também identificaram características que julgam importantes para a análise de coordenação. 

Entre essas características, destaca-se a baixa elasticidade da demanda de mercado.  Quanto mais inelástica é a demanda de mercado, maiores são os lucros cooperativos e, por consequência, maiores são os prejuízos causados aso consumidores finais pela coordenação. 

Conforme já discutido na seção 5.2, as estimativas de demanda do mercado de aço no Brasil indicam que a demanda do aço é inelástica. Schmidt e Lima (2006) encontraram uma elasticidade de -0,14, enquanto Reis et al. (2013) encontraram valor de -0,24 para a elasticidade-preço da demanda de aço como um todo e de -0,10 em vergalhões. 

Uma ressalva precisa ser feita em relação à elasticidade-preço da demanda, conforme argumenta Ivaldi (2003). A elasticidade-preço da demanda não indica se a colusão é mais provável ou não, mas sinaliza qual o impacto da coordenação no bemestar, sendo, dessa forma, um fator de interesse. 

Outro fator que está no próprio guia de Atos de Concentração Horizontal do Cade é o histórico de coordenação do mercado. Em 2005, as maiores empresas desse mercado foram condenadas por cartel. Ou seja, já existe exemplo de que esse mercado apresentou não só problemas de coordenação tácita, mas também de infração concorrencial. Um argumento apresentado pelas Requerentes no parecer “Mercados de Aços Longos 

45 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Comuns: considerações sobre os potenciais efeitos coordenados” diz que não se pode tomar a existência de condenação prévia como evidência de que é possível coordenar no mercado em questão. Assim, o referido parecer contextualiza a conduta ocorrida, discutindo a evolução do mercado nas últimas décadas. 

Em suma, a possibilidade de que uma fusão implique em aumento da probabilidade de coordenação depende de diversos fatores estruturais ou comportamentais descritos pela literatura econômica ou apontados pela experiência das agências antitruste. Tais fatores não devem ser analisados isoladamente, mas sob o contexto do mercado em questão. O setor de aços longos foi afetado por dois eventos recentes: a entrada de diversas empresas nesse setor, tais como a Silat e a CSN, e a queda da demanda. Esses dois eventos tornaram improvável a entrada de novos agentes nesse mercado, gerando um cenário em que as incumbentes possuem expressiva participação de mercado em alguns produtos, enquanto as entrantes possuem baixa participação. Como a assimetria de participação de mercado entre as empresas constitui um fator inibidor de coordenação, a entrada recente de novos agentes reduziu a probabilidade de coordenação. 

Se esses movimentos recentes de mercado indicam queda na probabilidade de coordenação, eles não necessariamente compensam os fatores que favorecem a coordenação. Em relação à queda da demanda, as incertezas advindas da retração do mercado dificultaram a coordenação entre as empresas, pois a previsibilidade de mercado é um fator importante para a coordenação. Porém, o fato de que a demanda esteja em um ponto de baixa é um fator de incentivo à coordenação, já que, ao coordenarem, as empresas sacrificam os benefícios imediatos de preços competitivos por lucros futuros. Como hoje a demanda de mercado está deprimida, o lucro de uma competição acirrada é menor do que em situações futuras de aumento da demanda. 

Além disso, a alta frequência de interação entre consumidores e empresas favorece a coordenação. A oferta de aço longo é feita de forma frequente para diversos consumidores e não de modo esporádico como em casos de leilão. Assim, as empresas interagem com os clientes e entre si de forma contínua, aumentando a previsibilidade de atuação e facilitando a coordenação. 

Ademais, as empresas desse setor atuam em diversos mercados ao mesmo tempo (vergalhão, barra, etc.). Esse fato também eleva a interação entre as empresas (pelo fato 

46 

_Nota Técnica nº 30/2017/DEE/CADE_ 

de serem vários mercados no setor) e contribui para reduzir a incerteza de atuação. A atuação multimercado ainda permite que estratégias de coordenação que não eram viáveis em somente um mercado passem a ser, se forem incluídos mais mercados. Desse modo, acordos que eram mais difíceis com empresas assimétricas podem se tornar viáveis. 

Outro fator que facilita a coordenação se dá pelo fato de que o setor é maduro, de forma que as empresas conseguem inferir custos, preços e capacidade das concorrentes com maior facilidade em comparação a empresas de setores mais dinâmicos. 

Pode-se ainda mencionar outros fatores de preocupação para a coordenação, tais como a existência de histórico de ilícito condenado e julgado pelo Cade e a não previsão de entrada de concorrentes no curto prazo. 

Tem-se, então, que mesmo que a entrada de novos agentes nesse mercado seja inibidora de coordenação, foram observadas diversas outras características próprias do setor de aços longos que favorecem a coordenação. O aumento da concentração gerado pela operação e indicado pelos índices C3 e C4 ainda intensificaria tal situação. Assim, não se pode descartar a hipótese de que o risco de coordenação se elevaria com a aquisição da Votorantim Siderurgia pela ArcelorMittal. 

47 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **7. Análise do mercado de sucata** 

A aquisição da Votorantim pela ArcelorMittal pode gerar prejuízos à concorrência não só na produção de aços longos já discutida, mas também em etapas de produção à montante, em que as empresas requerentes atuam adquirindo insumos. Esta seção analisará os prováveis impactos esperados da operação no mercado de sucata ferrosa. 

A sucata ferrosa é um importante insumo na produção do aço, sendo utilizada como insumo complementar e/ou substituto ao ferro gusa. O uso da sucata na produção de aço possui algumas vantagens produtivas como, por exemplo, a baixa necessidade energética, se comparada ao ferro gusa. A ArcelorMittal alega que 30% do seu aço produzido utilizou sucata como insumo.[17] Tem-se, então, que a sucata é um insumo importante para a cadeia produtiva da siderurgia, afetando diretamente o setor. 

O setor de aços longos é caracterizado por elevada concentração de mercado com um número reduzido de empresas, especificamente as requerentes e a Gerdau. Desse modo, a operação pode elevar o poder de barganha que as siderúrgicas possuem em relação aos sucateiros, gerando o risco de que o possível aumento do poder de compra da siderurgia implique em disrupção no mercado de sucata com possíveis impactos também para os consumidores de aço. 

O poder de compra, como descrito por Chen (2007), consiste na capacidade de um comprador de reduzir o preço cobrado por um fornecedor para valores abaixo do que ele normalmente cobraria. Os efeitos desse poder em termos de bem-estar e eficiência econômica dependem, porém, das características do fornecedor, de modo que os efeitos do aumento do poder de compra não são necessariamente negativos. É possível que, no processo de barganha entre fornecedores e produtores, ocorra um aumento de eficiência econômica com benefícios aos consumidores finais. 

Quando um aumento do poder de compra implica em efeitos negativos à concorrência, esse poder pode ser denominado de poder de monopsônio e quando os efeitos do aumento de poder são positivos, o poder pode ser denominado de poder compensatório. O que determina cada situação é a natureza da relação entre os agentes 

> 17 http://blog.arcelormittal.com.br/aco-material-reciclavel-por-excelencia/. Acessado em 18/08/2017. 

48 

_Nota Técnica nº 30/2017/DEE/CADE_ 

no mercado à montante. Então, para checar quais os prováveis impactos do poder de compra em fusões, deve-se checar como o mercado opera atualmente. 

Se os fornecedores do mercado à montante operam em um mercado competitivo, então o poder de compra resulta em poder de monopsônio. Se, por outro lado, os fornecedores são em número reduzido, possuindo algum poder de mercado, o poder de compra é poder compensatório. 

O monopsônio é uma característica de mercado análoga ao monopólio, onde somente um comprador opera no mercado. Assim como no monopólio, a quantidade que o monopsonista decide comprar é inferior à quantidade de competição, levando a preços de compra de insumos deprimidos. O mercado de sucata ferrosa brasileiro possui características de um oligopsônio, em que há um número reduzido de compradores com poder de mercado e uma grande quantidade de fornecedores com pouco poder. 

Utilizando dados compilados pela SG referentes a 2016, tem-se que o setor siderúrgico adquiriu cerca de **[ACESSO RESTRITO]** % do volume de sucata disponível no Brasil. As requerentes foram responsáveis pela aquisição de **[ACESSO RESTRITO]** % desse volume (ou **[ACESSO RESTRITO]** % do total). A única outra compradora com participação similar é a Gerdau, que adquiriu **[ACESSO RESTRITO]** % do volume do setor siderúrgico (ou **[ACESSO RESTRITO]** % do total). Temos, então, que três empresas adquirem **[ACESSO RESTRITO]** % da produção de sucata do Brasil. 

Resultados similares foram encontrados utilizando dados de gastos com a compra de sucata requisitados pelo DEE às siderúrgicas. Eles indicaram participação de **[ACESSO RESTRITO]** % das requerentes em 2016 e **[ACESSO RESTRITO]** % para a Gerdau, corroborando a hipótese de que efetivamente esse mercado é concentrado nas requerentes e Gerdau. 

Situação inversa é observada para as sucateiras no Brasil. Utilizando dados da RAIS, temos 4.373 estabelecimentos que possuem a atividade econômica de comércio atacadista de sucata metálica no Brasil em 2015. Além da quantidade elevada de estabelecimentos, temos que eles são em sua maioria microempresas. 

49 

_Nota Técnica nº 30/2017/DEE/CADE_ 

**Tabela 7.1 - Sucateiros no Brasil** 

|**Ano**|**Número de**<br>**estabelecimentos**|**% de estabelecimentos**<br>**que não empregam**|**% de estabelecimentos que**<br>**são microempresa (< 10**<br>**vínculos empregatícios)**|
|---|---|---|---|
|2006|3.691|37%|84%|
|2007|4.029|37%|85%|
|2008|4.435|39%|86%|
|2009|4.330|40%|87%|
|2010|4.417|40%|86%|
|2011|4.462|37%|86%|
|2012|4.537|37%|86%|
|2013|4.631|37%|87%|
|2014|4.444|35%|86%|
|2015|4.373|35%|87%|



Elaboração DEE com dados da RAIS/MTE. 

Do total de empresas que operam no Brasil, mais de um terço declaram não empregar nenhuma pessoa e mais de 80% são enquadradas na categoria de microempresa, pois possuem menos de dez vínculos empregatícios. 

Dada a estrutura característica desse mercado, como baixa necessidade de capital para operar, espera-se que os ajustes de mercado ocorram por meio de entrada e saída de firmas do mercado. Nos períodos em que a economia estava em expansão (2006-2008), houve entrada de firmas nesse setor. Porém, com a crise de financeira de 2008, a quantidade de firmas do mercado caiu. Comportamento similar ocorreu com a recente crise econômica, o que se reflete no número de 2015. 

A caracterização de que as firmas operam segundo os ciclos econômicos possui respaldo na literatura econômica. Estimativas de demanda indicam que a elasticidadepreço, tanto dos fornecedores quanto dos compradores, é inelástica. Analisando o mercado de sucata ferrosa dos EUA e Europa, Söderholm & Ejdemo (2008) observaram: 

_“A combinação de elasticidades-preço baixas para a oferta e demanda, por um lado, e a elasticidade-renda alta da demanda por metal, por outro lado, implica que os preços da sucata geralmente tendem a flutuar muito ao longo do tempo de acordo_ 

50 

_Nota Técnica nº 30/2017/DEE/CADE_ 

_com o ciclo econômico e as variações resultantes na demanda por metal.”_ (tradução livre) _[18]_ 

Ou seja, o mercado de sucata é composto por uma quantidade elevada de pequenos agentes, que têm a sua dinâmica de crescimento atrelada ao mercado à jusante que, no caso dessa operação, é a siderurgia. Assim, é possível afirmar que os sucateiros não possuem poder de mercado e que as siderurgias já detém poder de compra. Hoje, o mercado de sucata possui três compradores relevantes, de modo que a união da ArceloMittal com a Votorantim tende a aumentar o poder de compra e esse poder é poder de monopsônio. 

A consequência do poder de monopsônio em um mercado são descritas por Kirkwood (2012). Temos que fornecedores submetidos a um monopsônio ficam com suas receitas e lucros reduzidos, visto que o monopsonista demanda quantidades inferiores aos insumos de concorrência. Essa redução na quantidade vem acompanhada de preços de mercado inferiores aos que ocorreriam sob concorrência, levando a transferência do excedente dos produtores de insumo aos compradores. 

A princípio, o poder de mercado do monopsonista poderia ser benéfico para os consumidores finais, visto que haveria redução nos custos do insumo cobrado. Porém, como discutido por Blair & Harrison (1991), não necessariamente a redução de preço obtida pelo monopsonista será repassada para os consumidores do produto final. 

O efeito esperado do poder de monopsônio é a redução da quantidade de insumo adquirida. Essa redução pode implicar em uma menor oferta de produto final para o consumidor final. Se o mercado a jusante for competitivo, a queda na oferta da firma monopsonista é absorvida pelos outros concorrentes no mercado final. 

Porém, se a firma detiver poder de mercado também no mercado à jusante, a redução de produto final implicará em preços mais elevados ao consumidor final. Esse é o caso das siderurgias no Brasil. As participações de mercado calculadas e simulações realizadas em seções anteriores indicam que as siderúrgicas detêm poder de mercado na produção de aço. 

> 18 “ _The combination of low own-price elasticities for demand and supply, on the one hand, and the high income elasticity of metal demand, on the other, implies that scrap prices often tend to fluctuate a lot over time in line with the business cycle and the resulting variations in metal demand_ .” 

51 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Os impactos da aquisição da Votorantim pela AcerloMittal tendem, portanto, a ser contrários à eficiência de mercado. O mercado de sucata se caracteriza por um oligopsônio no qual operam um número reduzido de consumidores e uma grande quantidade de pequenos fornecedores. Com a operação, é previsto um aumento do poder de barganha das siderúrgicas com consequente redução do excedente dos produtores de sucata. Dado que as siderúrgicas também possuem poder de mercado na produção de aço, a redução potencial de preço obtida não beneficiaria os consumidores finais. 

52 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **8. Conclusões** 

A presente nota do Departamento de Estudos Econômicos do Cade (DEE/Cade) realizou estudo quantitativo a respeito de impactos concorrenciais decorrentes da operação de que trata o AC nº 08700.002165/2017-97 (“AC ArcelorMittal/Votorantim”). Especificamente, analisaram-se descritivamente os dados recebidos sobre quantidades e preços para, em seguida, realizar testes quantitativos para mensuração das potenciais pressões de aumento de preços decorrentes da operação. Ademais, efetuou-se a uma discussão sobre poder coordenado e sobre o efeito da operação no mercado de sucata. 

Para a primeira parte do estudo, procedeu-se uma análise descritiva das informações recebidas. Na análise de _market share_ nos mercados relevantes analisados, verificou-se que, na maioria dos mercados, a operação tornaria a empresa combinada líder de mercado. Em especial, verifica-se que no mercado de vergalhões, que representa cerca de 50% (em termos de receita) de todos os nove mercados relevantes analisados, a operação torna as requerentes líderes de mercado com **[ACESSO RESTRITO]** % de _market share_ . Ademais, analisando-se a dinâmica dos preços de ArcelorMittal e Votorantim, é possível verificar que a Votorantim apresenta sistematicamente preços inferiores aos praticados pela ArcelorMittal. Isso se verifica para maioria dos mercados analisados, incluindo o mercado de vergalhões. 

As análises, com o teste quantitativo de efeito unilaterais chamado GUPPI, ressaltam preocupações de pressões de aumento de preços em oito dos nove mercados analisados. Utilizando dados de 2016, os aumentos de preços podem alcançar valores superiores às eficiências alegadas nos seguintes mercados: (i) vergalhões, (ii) perfis leves, (iii) perfis médios, (iv) fio-máquina comum, (v) trefilados CA-60, (vi) telas eletrosoldadas, (vii) arame recozido, e (viii) treliças. Apenas o mercado nacional de barras não traz preocupações em relação a efeitos unilaterais resultantes da Operação. 

Ademais, os resultados encontrados com as simulações de fusões utilizando o PCAIDS reforçam as preocupações trazidas pela análise do GUPPI. As simulações mostraram que, a depender dos parâmetros selecionados (elasticidades da empresa e eficiências) os aumentos de preços podem alcançar, e até superar, o valor de 15% naqueles oito mercados: (i) vergalhões, (ii) perfis leves, (iii) perfis médios, (iv) fiomáquina comum, (v) trefilados CA-60, (vi) telas eletrosoldadas, (vii) arame recozido, e (viii) treliças. 

53 

_Nota Técnica nº 30/2017/DEE/CADE_ 

Tendo em vista os testes e simulações realizadas, esta nota sugere que a presente operação não apresenta efeitos anticompetitivos no mercado de barras. Entretanto, existem consideráveis efeitos anticompetitivos nos demais oito mercados analisados. 

A análise de poder coordenado não permitiu descartar a hipótese de que o risco de coordenação se elevaria com a operação. Contribuiu para tal conclusão a existência de várias características do setor de aços longos que favorecem a coordenação, tais como a alta frequência de interação entre as firmas, a previsibilidade do setor decorrente de sua maturidade, o histórico de conduta no setor, além da intensificação da concentração no mercado. 

Por fim, a avaliação dos efeitos da operação sobre o mercado de sucata indicou impactos contrários à eficiência de mercado, com aumento do poder de barganha das siderúrgicas e diminuição do excedente dos produtores de sucata. Ademais, dado o poder de mercado das siderúrgicas na produção de aço, eventuais reduções de preços não beneficiariam os consumidores finais. 

Brasília, 05 de setembro de 2017. 

[assinado eletronicamente] 

**Guilherme Mendes Resende** Economista-chefe 

[assinado eletronicamente] 

**Patrícia A. Morita Sakowski** Economista-chefe adjunta 

[assinado eletronicamente] 

**Felipe Costa Bispo** Coordenador 

[assinado eletronicamente] 

**João Isídio Freitas Martins** Economista 

54 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **9. Referências** 

BLAIR, ROGER  & HARRISON, JEFFREY L. (1991) Antitrust Policy and Monopsony, 76 CORNELL L.REV. 297, 306 (1991) 

CHEN, ZHIQI (2007)  Buyer Power,  Economic Theory and Antitrust Policy. Research in Law and Economics, Vol. 22, 17-40. 

DEATON, A., & MUELLBAUER, J. (1980). An Almost Ideal Demand System. American Economic Review, 70, 312-326. 

EPSTEIN, R. J., & RUBINFELD, D. L. (2001). Merger Simulation: A simplified approach with new applications. Antitrust Law Journal, 69, 883919. Acesso em 22 de Agosto de 2017, disponível em **http://scholarship.law.berkeley.edu/cgi/viewcontent.cgi?article=2362&context=fac pubs** 

EPSTEIN, R., & RUBINFELD, D. (2004). Effects of Mergers Involving Differentiated Products. Technical Report COMP/B1/2003/07. Comissão Europeia. Bruxelas: Departamento Antitruste  Mergers. Acesso em 22 de Agosto de 2017, disponível em **http://ec.europa.eu/competition/mergers/studies_reports/effects_mergers_involvin g_differentiated_products.pdf** 

European E&M Consultants. Competition Competence Report. 2013. O documento se encontra disponível no seguinte endereço eletrônico: **http://www.eemc.com/uploads/media/Merger_Screening_Tools.pdf** 

EVANS, W.N. & KESSIDES, I.N. (1994), “Living by the ‘Golden Rule’: Multimarket Contact in the U.S. Airline Industry,” Quarterly Journal ofEconomics, 109:341-366. 

FRIEDMAN, JAMES W., (1971), A Non-cooperative Equilibrium for Supergames, _Review of Economic Studies_ , 38, issue 1, p. 1-12. 

GUIA-H (2016). Guia de Análise de Atos de Concentração. CADE, Brasília, 2016. 

ICN (2013). The Role of Economists and Economic Evidence in Merger Analysis. Updated Chapter 4 of the ICN Investigative Techniques Handbook for Merger Review. Presented at the 12th Annual Conference of the ICN, Warsaw, Poland. 

IVALDI, MARC, JULLIEN, BRUNO, REY, PATRICK, SEABRIGHT, PAUL & TIROLE, JEAN, (2003), The Economics of Tacit Collusion, No 186, IDEI Working Papers, Institut d'Économie Industrielle (IDEI), Toulouse. 

KIRKWOOD, JOHN (2012) Powerful Buyers and Merger Enforcement, 92 B.U.L.REV. 1485-1544 . 

LOVARATO, M. V. L. (2010). Estimativas para a Elasticidade-Preço da Demanda por Produtos Siderúrgicos no Brasil. Rio de Janeiro. Tese de Mestrado em Finanças e Economia Empresarial da EPGE/FVG. Maio. 

55 

_Nota Técnica nº 30/2017/DEE/CADE_ 

PARKER, P.M. & L.-H. RÖLLER (1997), “Parker, Philip M. and Röller, Lars-Hendrik, Collusive Conduct in Duopolies: Multi-Market Contact and Cross-Ownership in the Mobile Telephone Industry. RAND JOURNAL OF ECONOMICS, Vol. 28, No. 2 

REIS JD, DE MORAES MA, BACCHI MR. (2013) A demanda do aço brasileiro e a perda de bem-estar ocasionada pelo exercício do poder de mercado no período de 2006 a 2008. Revista de Defesa da Concorrência.  Maio, 15;1(1):170-96. 

ROTEMBERG, J., & G. SALONER (1986), “A Supergame-Theoretic Model of Business Cycles and Price Wars during Booms,” American Economic Review, 76:390-407. 

SALOP, STEVEN & MORESI, SERGE. Updating the Merger Guidelines: Comments. 2009. Disponível em: **- https://www.ftc.gov/sites/default/files/documents/public_comments/horizontal mergerguidelinesreviewproject54509500032/54509500032.pdf** 

SCHMIDT, C. A. J. & LIMA, M. A. M., (2006). A Perda do Peso Morto e a ElasticidadePreço da Demanda do Setor Siderúrgico no Brasil, Revista de Estudos Econômicos, São Paulo, V. 36, N. 1, P. 127-147, Janeiro-Março. 

SÖDERHOLM,  P,  &  EJDEMO, T. (2008)  Steel  scrap  markets  in  Europe  and  the USA, Minerals and Energy - Raw Materials Report 23,  57–73. 

TIROLE, J. (1988). _The theory of industrial organization_ . Cambridge, Mass: MIT Press 

56 

_Nota Técnica nº 30/2017/DEE/CADE_ 

## **ANEXO A** 

Seguem abaixo os aumentos de preços unilaterais associados aos produtos da Votorantim. 

## **Tabela A.1 – GUPPI 2016 - Votorantim** 

|**2016**|**Mercado**|**_Market share_**<br>**(Volume)**|**_Market share_**<br>**(Receita)**|**_Market share_**<br>**(Volume SG)**|
|---|---|---|---|---|
|GUPPI<br>(Votorantim)|Vergalhão|8,1%|8,1%|8,2%|
||Barras|5,0%|4,9%|4,9%|
||Perfis leves*|8,3%|8,1%|7,9%|
||Perfis médios/pesados|2,6%|2,4%|4,5%|
||Fio-máquina comum|3,5%|3,5%|2,8%|
||Trefilado CA-60|9,9%|9,7%|9,3%|
||Telas eletrosoldadas|14,0%|14,0%|9,9%|
||Treliça|6,2%|6,4%|4,6%|
||Arame recozido|13,5%|13,4%|12,2%|



Elaboração: DEE. Nota: * _Market share_ consolidado pela SG considera apenas perfis médios. 

57 

