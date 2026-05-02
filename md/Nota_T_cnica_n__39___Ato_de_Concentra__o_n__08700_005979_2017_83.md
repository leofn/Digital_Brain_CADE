Ministério da Justiça – MJ
Conselho Administrativo de Defesa Econômica – CADE

SEPN 515 Conjunto D, Lote 4 Ed. Carlos Taurisano, 4º andar - Bairro Asa Norte, Brasília/DF, CEP 70770-504
Telefone: (61) 3221-8409 e Fax: (61) 3326-9733 – www.cade.gov.br

NOTA TÉCNICA Nº 39/2018/DEE/CADE

Referência: Ato de Concentração nº 08700.005979/2017-83

Requerentes:  União  Transporte  Interestadual  de  Luxo  S.A.  ("UTIL")  e  Expresso
Gardênia Ltda. ("Gardênia")

Ementa: Ato de concentração referente à operação de transferência de autorização para
prestação  de  serviços  de  transporte  interestadual  de  passageiros  da  Gardênia  para  a
UTIL. Análise de diferença de médias de linhas, passageiros e descontos dos períodos
pré  e  pós-operação  por  mínimos  quadrados  ordinários.  Não  se  encontrou,  de  forma
consistente, qualquer mudança de padrão de atuação que possa ter decorrido da referida
operação.

Versão: Pública.

1.  Introdução

Este  Departamento  de  Estudos  Econômicos  do  Cade (DEE/Cade),  em  atendimento  ao
memorando nº 2384/2018 (SEI 0537567) da Superintendência Geral do Cade (SG/Cade),
avalia, por meio desta nota técnica, os efeitos decorrentes da operação de transferência de
autorização  (o  “ato  de  concentração”)  para  prestação  de  serviços  de  transporte
interestadual  de  passageiros  da  Expresso  Gardênia  Ltda.  ("Gardênia")  para  a  União
Transporte Interestadual de Luxo S.A. ("UTIL").

Em temos mais específicos, a referida autorização diz respeito ao seguinte conjunto de
serviços  (linhas)  em  regime  de  autorização  especial  para  transporte  rodoviário
interestadual coletivo de passageiros:

  06.0848-00 São João Del Rei (MG) - São Paulo (SP) via BR 381;

  06.1090-00 Barbacena (MG) - São Paulo (SP);

  06.1090-01 Barbacena (MG) - Campinas (SP);

  06.0100-00 Lavras (MG) - São Paulo (SP); e

  06.0100-01 Bom Sucesso (MG) - São Paulo (SP)

A operação consumou-se no primeiro trimestre de 2015 mediante o estabelecimento das
resoluções  da  Agência  Nacional  de  Transportes  Terrestres  –  ANTT,  a  saber,  as  de  n°
4.517, de 19 de dezembro de 2014,  e n° 4.635,  de 5 de março de 2015,  tratadas mais
detalhadamente adiante.

O ato de concentração foi notificado pela UTIL ao CADE por meio da “Notificação de
Ato de Concentração” (SEI 0390515). Segundo a parte, ad cautelam, pois para esta as
competências para a análise do caso se encerrariam na ANTT. A ANTT normatiza sobre
a transferência de serviço operado sob o regime de autorização especial em sua Resolução
nº 3076, de 26 de março de 2009.

Este documento restringe-se a avaliar os impactos econômicos associados ao bem-estar
do consumidor. Para tal, compõe esta nota técnica por esta introdução, seguida por uma
contextualização  de  como  foi  a  avaliação  do  processo  na  ANTT  e  das  mudanças
institucionais contemporâneas, seguida por uma descrição das bases de dados utilizadas
para  então  avaliar,  tanto  de  forma  descritiva  quanto  por  meio  de  testes  estatísticos  de
diferenças de médias, a evolução de variáveis como o número de linhas, o número de
passageiros pagantes e os descontos.

2.  Aspectos sobre o ato de concentração

Aqui  são  elencadas  algumas  características  essenciais  do  serviço  de  transporte
interestadual  de  passageiros,  permitindo  descrever com  mais  precisão  a  operação  e  os
critérios  considerados  no  processo  administrativo  que  correu  na  ANTT.  Por  fim,  são
discutidas as mudanças no marco legal para possibilitar uma avaliação ceteris paribus
dos efeitos do ato de concentração.

2.1.  Características do serviço

Para se entender a natureza das sobreposições que podem ser observadas na operação,
primeiro  há  de  se  entender  o  que  é  o  serviço  em  questão.  Para  as  finalidades  deste
documento, uma linha pode ser entendida como  um  conjunto contíguo de origens que
seguem para um conjunto de destinos. A cada par origem-destino dá-se o nome de seção.
Por simplicidade, convém apresentar um exemplo específico de março de 20151. Trata-
se  do  serviço  de  prefixo  06.0848-00  (um  dos  transferidos  no  ato  de  concentração),
operado à época pela Gardênia. Eis a descrição geral do serviço:

Fonte: Dados Cadastrais – ANTT. Elaboração DEE.

1 Dados disponíveis no arquivo compactado em “cadastro operacional do Serviço Regular (rodoviário e
semiurbano)”  no  link:  http://portal.antt.gov.br/index.php/content/view/46223/2015.html,  na  data  de
29/08/2018.

2

Este serviço (assim como outros) subdivide-se em outras operações menores, suas seções.
Eis a descrição das seções para o serviço em questão:

Fonte: Dados Cadastrais – ANTT. Elaboração DEE.

Apenas para ilustrar2, eis o mapa com as cidades de origem e o destino destas seções:

Figura 1: Direções de São João Del Rei (MG) para São Paulo (SP)

Fonte: Map data 2018 Google. Elaboração DEE.

O usuário só pagará pela seção que pretende contratar. A tarifa teto de cada seção é uma
função dos coeficientes tarifários por pavimento estabelecidos pela ANTT3 e da distância
em quilômetros por tipo de pavimento entre a origem e destino da seção.

(cid:2871)
(cid:3046) = (cid:3533) 𝐷(cid:3036)
𝑝(cid:3021)
(cid:3036)(cid:2880)(cid:2869)

(cid:3046)𝑐(cid:3036)

Onde:

2 A rota apresentada pode não ser necessariamente aquela que é a adotada pela empresa.

3 Disponíveis em:
http://www.antt.gov.br/perguntas_frequentes/passageiros.html?diretorio=reajuste_tarifario&titulo=Reajus
te%20Tarif%C3%A1rio&categoria=passageiros

3

(cid:3046) : Preço teto de uma seção.
(cid:3046): Distância percorrida na seção no pavimento do tipo “𝑖”.

𝑝(cid:3021)
𝐷(cid:3036)
𝑐(cid:3036): Coeficiente tarifário teto estabelecido pela ANTT para o pavimento do tipo “𝑖”.
Ademais,  existem  coeficientes  tarifários  distintos  para  serviços  prestados  com  ônibus
convencional  com  sanitário,  convencional  sem  sanitário,  executivo,  leito  com  ar,  leito
sem ar, semi-leito e cama.

2.2.  A operação e o processo administrativo

Na NT 58/SEREG/ANTT/2014 da Superintendência de Marcos Regulatórios – SUREG,
a  nota  que  primeiro  avaliou  os  aspectos  concorrenciais  do  caso,  ainda  no  âmbito  da
ANTT, tem-se, em sua página 8, que: “a dimensão geográfica do mercado em questão é
configurada  pelos  pares  de  cidade  origem-destino,  ou  seja,  as  diversas  seções  de  uma
linha”.

De  fato,  não  parece  interessar  ao  consumidor  o  traçado  que  faz  uma  linha  para  além
daquele da seção que o mesmo pretende contratar. Outro fato interessante é que diferentes
linhas, com diferentes rotas, podem ter em comum seções especificas.

Sendo assim, parece intuitivo, até este ponto, adotar, assim considerado pela ANTT, as
seções como padrão para o mercado relevante.

Eis  então  as  trinta  seções  atendidas  pelas  cinco  linhas  envolvidas  na  operação,  com
destaque para as seis seções com a atuação simultânea de ambas as empresas antes do ato
de concentração.

4

Fonte: Dados Operacionais - ANTT. Elaboração DEE.

A  respeito  dessas  sobreposições,  a  SUREG,  por  meio  da  NT  58/SEREG/ANTT/2014,
alertou  que  alguns  mercados  seriam  monopolizados  pela  UTIL,  propondo  então  o
indeferimento da transferência das linhas 06.0848-00, 06.1090-00 e 06.1090-01, o que
foi prontamente atendido na forma da Resolução n° 4.517 de 19 de dezembro de 2014,
que só autorizou a transferência das duas outras linhas.

Em  janeiro  de  2015  a  UTIL  apresentou  na  agência  um  pedido  de  “Reconsideração
Especial”,  ali  alertava  para  a  impossibilidade  de  se  transferir  apenas  uma  parcela  dos
serviços, já que, aparentemente, ainda existiriam custos fixos com os quais a Gardênia
não conseguiria lidar.

Em  resposta ao pedido de reconsideração, por meio da NT 11/SUREG/ANTT/2015, a
SUREG  considera  que  a  resolução  “apenas  autoriza  a  transferência,  sendo  que  as
empresas  não  ficam  obrigadas  a  realizar  a  transferência  dos  serviços”,  portanto,  num
cenário de inviabilidade operacional, a Gardênia poderia optar por desistir do negócio.
Dessa forma, a SUREG manteve a recomendação inicial.

Mas  dessa  vez,  devido  a  possibilidade  de  paralisação  dos  serviços  da  Gardênia,  foi
admitida, na forma da resolução n° 4.635, de 5 de março de 2015, a transferência das
demais linhas que outrora fora negada.

5

2.3.  O contexto de mudança no marco legal

Ao se avaliar um conjunto de variáveis que no tempo possam indicar uma mudança em
desfavor  do  consumidor  e  que,  além  disso,  tenham  derivado  de  uma  decisão
anticompetitiva da adquirente, faz-se necessário, antes de tudo, isolar (controlar) outros
fatores que possam ter afetado a evolução das séries.

Logo,  outras  mudanças  importantes  que  possam  ser  contemporâneas  ao  ato  de
concentração  devem  ter  seus  efeitos  destacados  para  que  não  se  confundam  com  da
operação.

Quando se fala do Transporte Interestadual e Internacional de Passageiros (TRIIP), o que
se observou nos últimos anos foram mudanças profundas no regramento. Convertendo
um modelo de sistema de transporte cuja característica principal era o controle do estado,
para um modelo mais adaptado à livre iniciativa.

O Art. 13 da lei n° 10.233, de 5 de junho de 2001, alterado pela lei nº 12.815, de 5 de
junho de 2013, muda o regime de outorga do TRIIP de permissão para autorização. Para
este setor isso implicou, especificamente, no abandono do ProPass, que era a proposta de
licitação de todos os serviços, caracterizado, principalmente, pela venda de pacotes de
serviços  numa  estratégia  de  subsídios  cruzados,  e  na  adoção  recente  do  regime  de
autorização por meio da resolução n° 4.770/ANTT, de 25 de junho de 2015.

Grosso modo, num regime de permissão o estado definiria a maioria dos parâmetros do
negócio, a saber: a linha e suas seções, o número de viagens de ida e volta, os padrões de
qualidade, os preços teto, o número de operadores e quem são por meio de licitação, e
etc.

Quanto ao regime de autorização, idealiza-se que todo agente privado que seja capaz de
preencher  um  conjunto  mínimo  de  requisitos  tenha  a  possibilidade  de  prestar  aquele
serviço público. Diz-se ideal, pois mesmo no novo modelo de outorga persistem regras
como  a  de  inviabilidade  operacional4,  que  possibilita  ao  estado  limitar  o  número  de
operadores em um dado mercado em situações que configurassem “concorrência ruinosa
ou restrição de infraestrutura”.

No novo regime, o operador habilitado determina os mercados que quer atender, a relação
das linhas pretendidas com suas respectivas seções e o itinerário, bem como a frequência
da linha, respeitada a frequência mínima de, ao menos, uma viagem semanal por sentido,
por empresa.

O  operador  determina  também  o  esquema  operacional  (ex:  infraestrutura  de  apoio  e
rodovias utilizadas em seu percurso), o quadro de horários (registro da programação das
viagens previstas em cada sentido, dia da semana e meses do ano, com os horários de
partida dos pontos terminais da linha), conforme a frequência solicitada.

Outra mudança importante é a liberdade para definir os preços dos serviços ofertados,
com previsão na norma para entrar em vigor em 19 de junho de 2019.

O mais importe é: quando observadas as séries, há de se ter em mente que o operador tem,
depois da mudança do regime de outorga, a possibilidade de deslocar seus recursos dos
mercados menos lucrativos para os mais lucrativos, podendo gerar, ao menos no curto
prazo, uma redução na oferta em alguns mercados. Sendo assim, serão aqui consideradas

4  Há  uma  tomada  de  subsidio  em  discussão  na  agência  na  data  deste  parecer.  Disponível  em:
http://portal.antt.gov.br/index.php/content/view/54017.html

6

nas análises relativas à avaliação dos impactos da operação as mudanças no regime de
outorga.

3.  Base de dados, softwares e informações técnicas

Todos  os  dados  utilizados  nesta  nota,  bem  como  outras  informações  técnicas,  são  de
natureza  pública,
eletrônico  da  ANTT:
e
http://www.antt.gov.br/.

estão  disponíveis  no

sítio

Nomeadamente,  foram  utilizados  os  dados  de  Estatísticas  e  Estudos  do  transporte
rodoviário, que estão divididos em:

  Dados cadastrais

  Dados operacionais

Dos  dados  cadastrais,  nas  planilhas  que  dizem  respeito  ao  “cadastro  operacional  do
serviço regular (rodoviário e semiurbano)”, foi possível verificar as seções de cada linha
envolvida  na  operação,  bem  como  obter  a  quilometragem  por  pavimento  em  alguns
pontos do tempo para tornar possível o cálculo das tarifas teto.

Quanto  aos  coeficientes  tarifários,  existe  um  conjunto  de resoluções  da  ANTT  que  as
definem,  a  saber:  5.826/2018,  5.368/2017,  5.123/2016,  4.765/2015,  4.351/2014,
4.166/2013, 3.852/2012, 3.687/2011, 3.538/2010, 3.173/2009 e 2.772/2008.

Ainda em relação aos dados cadastrais, das planilhas que tratam do “cadastro de quadro
de  horários  e  tarifas  promocionais  do  serviço  regular  (rodoviário  e  semiurbano)”  foi
possível retirar os descontos promocionais com seus respectivos períodos de validade.

Os dados cadastrais das linhas consideradas são de março de 2009 a julho de 2016.

No que diz respeito aos dados operacionais, para fim de aferição do número mensal de
linhas que atendiam as seções e número de passageiros pagantes, foram considerados os
dados disponíveis nas planilhas que tratavam dos dados mensais do serviço regular. Os
dados avaliados são do período que vai de janeiro de 2013 a março de 2018.

Quanto  aos  softwares  estatísticos,  foram  utilizados  na  análise  o  R,  versão  3.4.1,  e  o
RStudio, versão 1.1.383.

4.  Análise descritiva, metodologia e avaliação dos impactos da operação

Este tópico analisa seis das trinta seções transferidas da Gardênia para UTIL. Tratam-se
das  seções  aonde  havia  atuação  de  ambas  as  empresas  antes  de  concretizado  o  ato  de
concentração.

Neste  sentido,  este  parecer  segue  o  mesmo  curso  do  apresentado  pela  NT
58/SEREG/ANTT/2014.  Diferencia-se  pela  possibilidade  de  avaliar  ex-post  o  ato  de
concentração, verificando suas possíveis decorrências, e pelo uso de bases de informações
distintas  das  usadas  naquela  nota,  bem  como  pela  aplicação  de  outros  métodos  de
avaliação.

Portanto, intenta esta nota aprofundar e complementar as conclusões observadas outrora
pelas NT 58/SEREG/ANTT/2014 e NT 11/SUREG/ANTT/2015.

7

Primeiro, realiza-se para cada uma das seis seções uma análise descritiva da evolução das
variáveis  número  de  linhas  e  número  de  passageiros  pagantes  (proxies  para
oferta/demanda). Num segundo momento avalia-se a diferença de médias destas mesmas
variáveis  antes  e  depois  do  ato  de  concentração  por  meio  de  mínimos  quadrados
ordinários.

No tópico seguinte,  aplica-se a mesma estratégia, mas agora para avaliar os descontos
promocionais oferecidos pela UTIL.

Como a atuação das empresas era fortemente regulada antes do regime de autorização, a
possibilidade de oferecer descontos era a forma viável de se competir em preços com as
demais concorrentes. Observando a evolução no tempo dos descontos oferecidos, é que
se  verificará  ou  não  uma  mudança  de  comportamento  da  UTIL,  atenuado  ou  não  sua
política de descontos.

4.1.  Análise descritiva

Os gráficos a seguir destacam nas linhas verticais, continua e tracejada, o início de dois
períodos importantes para a análise, respectivamente, o mês em que a agência reguladora
autoriza o início da operação da UTIL nas linhas cedidas pela Gardênia e o mês em que
a  ANTT  emite  a  licença  operacional5  do  Consórcio  Guanabara,  o  qual,  salvo  melhor
fonte,  detém  o  controle  acionário  da  UTIL  desde  20036,  para  a  prestação  do  serviço
regular de TRIIP, já sob o novo regime de autorização. A saber, a data da emissão da
licença operacional do Consórcio Guanabara representa o efetivo momento em que houve
a  mudança  de  regime  para  os  seis  mercados  aqui  destacados  pelas  sobreposições  pré-
operação7.

Mais especificamente, para a operação dos serviços transferidos por meio da Resolução
n° 4.517: 06.0100-00 - Lavras (MG) – São Paulo (SP) e 06.0100-01 - Bom Sucesso (MG)
- São Paulo (SP), estava a UTIL autorizada a operar a partir de 07 de janeiro de 2015,
conforme a Ordem de Serviço n° 001/SUPAS/ANTT/2015, de 24 de dezembro de 2014.
Porém, como nenhuma dessas linhas operam nas seções com sobreposição, não haverá
menção a data nos gráficos.

Quanto à operação dos serviços transferidos por meio da Resolução n° 4.635: 06.0848-
00 - São João Del Rei (MG) - São Paulo (SP), 06.1090-00 - Barbacena (MG) - São Paulo
(SP) e 06.1090-01 - Barbacena (MG) - Campinas (SP), só a partir de 31 de março de

5 Portaria SUPAS/ANTT/MT 76/2016 de 29/04/2016, disponível em:
https://anttlegis.antt.gov.br/action/UrlPublicasAction.php?acao=abrirAtoPublico&cod_modulo=161&cod
_menu=5414&num_ato=00000076&sgl_tipo=POR&sgl_orgao=SUPAS/ANTT/MT&vlr_ano=2016&seq
_ato=000
6 “A União Transporte Interestadual de Luxo S/A – UTIL foi fundada em 1950 e operava a linha de ônibus
entre  Petrópolis  e  o  Rio  de  Janeiro.  O  Grupo  Guanabara,  de  Jacob  Barata,  assumiu  a  UTIL  em  2003”.
Disponível  em  17.08.2018,  em:  https://diariodotransporte.com.br/2016/02/23/util-de-jacob-barata-e-
autorizada-pelo-governo-do-estado-de-sao-paulo-a-operar-na-area-3-da-emtu/.

7 É possível verificar as seções por meio do link:
http://www.antt.gov.br/passageiros/Publicacoes_Licencas_Operacionais__LOP.html.

8

2015 estava a UTIL autorizada a operar, conforme se verifica na Ordem de Serviço n°
005/SUPAS/ANTT/2015, de 27 de março de 2015.

Quanto  à  licença  operacional  do  Consórcio  Guanabara,  esta  que  trouxe  as  seções  em
análise para o novo regime de autorização, a Portaria 76 SUPAS/ANTT/MT/2016 data
do dia 29/04/2016 e teve efeitos imediatos já em sua publicação.

4.1.1.  Barbacena/MG - São Paulo/SP

Segundo o IBGE, a população estimada de Barbacena era de 136.6898 pessoas em 2017.
O gráfico a seguir (Figura 2) mostra o número de linhas (prefixos) que atenderam mês a
mês  este  mercado,  por  razão  social.  No  subtítulo  identificam-se  também  as  linhas
envolvidas na operação e que, em algum momento, atenderam essa seção.

Sobre o que o número de linhas é capaz de informar, salienta-se que tanto no novo quanto
no  antigo  regime  de  outorga  existiram  regras  de  número  mínimo  de viagens  que  uma
empresa tem de realizar para uma linha a ela incumbida. Portanto, um aumento do número
de  linhas  em  uma  mesma  seção  pode  representar  um  aumento  no  número  mínimo  de
viagens a serem feitas naquela seção.

Figura 2: Número de linhas na seção Barbacena (MG) - São Paulo (SP)

Grosso modo, percebe-se que, na média, há uma manutenção, quando não um pequeno
aumento,  no  número  de  linhas  que  atenderam  aquela  seção.  A  priori,  não  é  possível
reconhecer  uma  mudança  de  padrão  imediatamente  depois  da  data  da  operação.  No

8 https://cidades.ibge.gov.br/brasil/mg/barbacena/panorama.

9

entanto, pode ser que exista um aumento no número de linhas associado à mudança no
regime  de  outorga,  o  que  será  testado  mais  adiante  por  meio  do  método  de  mínimos
quadrados ordinários.

Outro  ponto  é  a  aparição  do  Consócio  Guanabara  ao  final  da  série.  Mas,  como  esse
consórcio aparentemente detém o controle acionário da UTIL, , não se está a observar um
novo ato de concentração.

Quanto ao período de maio a junho de 2014, não se conseguiu identificar, até o momento,
uma razão específica para a quebra/ausência de dados. No entanto, umas das possíveis
razões  podem  ser  os  erros  de  preenchimento  dos  formulários  disponibilizados  pela  a
ANTT (cuja responsabilidade de preenchimento é do operador).

O gráfico seguinte apresenta a soma do número de passageiros pagantes no trajeto de ida
e no trajeto de volta para a seção em questão.

Figura 3: Número de pagantes na seção Barbacena (MG) - São Paulo (SP)

Aparentemente, há uma redução na média de pagantes no período que se inicia com a
entrada em operação do Consórcio Guanabara. Quanto à operação, é possível que número
de pagantes médio tenha até aumentado. No entanto, fatores como a sazonalidade devem
ser considerados como futuros controles em uma regressão, afinal, são notáveis os picos
associados aos meses de dezembro.

4.1.2.  Barroso/MG - São Paulo/SP

O padrão de análise descritiva para os demais mercados pouco diferirá do realizado até
aqui, de forma que as análises serão mais sucintas.

10

O  município  de  Barroso  detém  uma  população,  segundo  o  IBGE,  de  20.8829  pessoas.
Está localizado entre Barbacena e São João Del Rei (origens de duas das seções analisadas
aqui). Eis a evolução do número de linhas na seção:

Figura 4: Número de linhas na seção Barroso (MG) - São Paulo (SP)

Tendo por referência os períodos antes e depois da data da operação é possível identificar
uma pequena redução no número de linhas, no entanto, não é claro que essa redução tenha
ocorrido por causa da operação, afinal, esse movimento é percebido pelo menos um ano
antes. Quanto ao período posterior à mudança no regime de outorga, essa queda é radical.

Como o Consórcio Guanabara pode ter optado por outra forma de organização, como, por
exemplo,  menos  linhas  com  viagens  mais  frequentes,  é válido  observar  o  que  ocorreu
com o número de passageiros pagantes:

9 População estimada em 2017, disponível em: https://cidades.ibge.gov.br/brasil/mg/barroso/panorama

11

Figura 5: Número de pagantes na seção Barroso (MG) - São Paulo (SP)

O que se observa é uma redução no número de passageiros pagantes consistente no tempo.
Neste  ponto  é  tentador  supor  que  as  consecutivas  mudanças  tenham  prejudicado  o
mercado de transporte de passageiros na seção. No entanto, fatores como a evolução da
renda no município de Barroso ou mesmo uma mudança na forma como o usuário acessa
o  sistema  de  transporte  interestadual,  como,  por  exemplo,  com  o  uso  de  linhas
intermunicipais para acessar o terminal rodoviário (característica patente de sistemas com
linhas  tronco  alimentadas),  bem  como  pelo  uso  de  aplicativos  de  carona,  como
mencionado no Formulário de Notificação de AC (Documento SEI n° 0390517), podem
conceder melhor explanação ao padrão observado. Infelizmente, não se dispõem aqui de
dados para testar todas estas hipóteses.

4.1.3.  Itumirim/MG - São Paulo/SP

Com uma população estimada pelo IBGE de 6.213 habitantes10, o município de Itumirim
localiza-se  entre Barbacena  e  a  BR-381  (via importante  no  trajeto  até  São  Paulo).  No
período analisado, assim foi atendida de serviços (linhas) a seção:

10 População estimada em 2017, disponível em: https://cidades.ibge.gov.br/brasil/mg/itumirim/panorama

12

Figura 6: Número de linhas na seção Itumirim (MG) - São Paulo (SP)

O  gráfico  apresenta  um  padrão  muito  similar ao  observado  na  seção  que  se  inicia  em
Barroso, o que não é surpreendente na medida em que muitas vezes ambas as seções são
atendidas pelas mesmas linhas. Não obstante, é possível observar as pequenas diferenças
de nível.

A operação parece ter um efeito positivo sobre o número de linhas que atendem a seção,
enquanto que a mudança de regime é seguida por uma queda brusca neste número.

Quanto ao número de pagantes, é possível observar uma tendência de queda um ano antes
da  efetivação  da  operação.  Em  relação  ao  período  do  novo  regime  de  autorização,  a
tendência foi de queda acentuada.

13

Figura 7: Número de pagantes na seção Itumirim (MG) - São Paulo (SP)

4.1.4.  Itutinga/MG - São Paulo/SP

Figura 8: Número de linhas na seção Itutinga (MG) - São Paulo (SP)

14

Itutinga também está no trajeto que vai de Barbacena à BR-381, sua população é de 3.926
pessoas11 segundo o IBGE. No que diz respeito às linhas, seu gráfico é idêntico ao de
Itumirim. Tratam-se de cidades contíguas e que, neste caso, foram atendidas exatamente
pelo mesmo conjunto de linhas.

Quanto ao número de passageiros pagantes, o aspecto do gráfico também é similar.

Figura 9: Número de pagantes na seção Itutinga (MG) - São Paulo (SP)

Itutinga  tinha  a  maior  parte  de  sua  da  demanda  atendida  pela  Expresso  Gardênia,  no
entanto, a queda que é observada um ano antes da operação torna improvável uma relação
casuística com o ato de concentração. No mais, os padrões são exatamente os mesmos.

4.1.5.  Nazareno/MG - São Paulo/SP

O  município  entre  São  João  Del  Rei  e  Itutinga  tem  população  estimada  de  8.583
pessoas12,  conforme  dados  do  IBGE.  Essa seção  foi  atendida  exatamente  pelo  mesmo
conjunto de linhas que atendeu Itumirim e Itutinga com o passar do tempo. Mais uma vez,
tem-se um gráfico idêntico ao das demais seções.

11 População estimada em 2017, disponível em: https://cidades.ibge.gov.br/brasil/mg/itutinga/panorama

12 População estimada em 2017, disponível em: https://cidades.ibge.gov.br/brasil/mg/nazareno/panorama

15

Figura 10: Número de linhas na seção Nazareno (MG) - São Paulo (SP)

Quanto aos pagantes, uma tendência distinta do que vem sendo observado. No período
pré-operação houve um aumento no número de pagantes. A maior parte da demanda era
atendida pela UTIL, até que no último ano antes da operação inicia-se uma queda.

Figura 11: Número de pagantes na seção Nazareno (MG) - São Paulo (SP)

16

No período posterior ao ato de concentração a série se estabiliza, até que se inicia o regime
de outorga com uma súbita queda que tende a nulidade.

4.1.6.  São João Del Rei/MG - São Paulo/SP

São João Del Rei é a segunda cidade de maior população dentre as que estão nas seções
analisadas  (claro  que  aqui  se  ignora  São  Paulo,  destino  final  de  todas  as  seções
analisadas), com uma população de 90.263 habitantes13, apresenta estatísticas que mais
se assemelham às de Barbacena que as das demais cidades consideradas.

No caso desta seção, fica um pouco mais evidente que o número de linhas que a atendeu
aumentou com o passar do tempo. No ano que se sucede a operação, vê-se um imediato
aumento subsequente, já em relação à mudança no regime de outorga o que se observa é
uma estabilização em níveis acima dos níveis históricos.

Figura 12: Número de linhas na seção São João Del Rei (MG) - São Paulo (SP)

Quanto ao número de passageiros pagantes, em média os níveis pré e pós-fusão parecem
similares. O mesmo pode ser dito em relação ao período do novo regime de outorga.

13  População  estimada  em  2017,  disponível  em:  https://cidades.ibge.gov.br/brasil/mg/sao-joao-del-
rei/panorama

17

Figura 13: Número de pagantes na seção São João Del Rei (MG) - São Paulo (SP)

Cabe esclarecer, mais uma vez, que essa análise visual não dispensa uma análise mais
específica dessas médias, no entanto, este ponto será tratado adiante com as ferramentas
adequadas.

4.2.  Diferença de médias

O  uso  de  econometria  para  comparar  as  médias,  a  saber,  do  número  de  linhas  que
atendem dada seção e de passageiros pagantes em uma dada seção, para cada um dos
três períodos da análise (pré-operação, pós-operação e o da vigência do novo regime de
outorga) permite avaliar o quão distintas essas médias são. Inclusive, se as médias são
distintas do ponto de vista estatístico.

Os betas associados a cada período de análise também revelam uma possível direção do
impacto dessas mudanças. Para tal, realiza-se um conjunto de regressões para cada seção,
composto pelas seguintes formas funcionais:

𝑦(cid:3036) = 𝛽(cid:4632)
𝑦(cid:3036) = 𝛽(cid:4632)

(cid:2868) + 𝛽(cid:4632)
(cid:2868) + 𝛽(cid:4632)

(cid:2869)𝑑(cid:3007) + 𝑒̂(cid:3036) (1)
(cid:2869)𝑑(cid:3007) + 𝛽(cid:4632)

(cid:2870)𝑑(cid:3016) + 𝑒̂(cid:3036) (2)

𝑦(cid:3036) = 𝛽(cid:4632)

(cid:2868) + 𝛽(cid:4632)

(cid:2869)𝑑(cid:3007) + 𝛽(cid:4632)

(cid:2870)𝑑(cid:3016) + ∑ 𝛽(cid:4632)

(cid:2869)(cid:2870)
(cid:3036)(cid:2880)(cid:2869)

(cid:3036)𝑑(cid:3036)

+ 𝑒̂(cid:3036) (3)

Onde:

𝑦(cid:3036):  Ou,  número  de  linhas  que  atendem  a  seção  no  mês  𝑖;  Ou,  número  de  passageiros
pagantes no mês 𝑖.

18

𝑑(cid:3007): Dummy da operação UTIL-Gardênia. Assume o valor “1” a partir de março de 2015.

𝑑(cid:3016): Dummy para a entrada em vigor do novo regime de outorga naquela seção. Assume
o valor “1” a partir de abril de 2016.

𝑑(cid:3036): Dummies dos meses para controle de sazonalidade.

𝛽(cid:4632)
(cid:2868): Constante.

𝛽(cid:4632)
(cid:2869): Estimador do acréscimo/decréscimo na média decorrente da operação.

𝛽(cid:4632)
(cid:2870): Estimador do acréscimo/decréscimo na média decorrente da mudança do regime de
outorga.

𝛽(cid:4632)
(cid:3036): Estimador do acréscimo/decréscimo na média associado ao i-ésimo mês.

𝑒̂(cid:3036): Resíduo

A Tabela 4 a seguir estabelece o padrão de apresentação das regressões. No título, tem-
se a seção considerada. Para cada seção foram realizadas seis regressões, nas colunas (1),
(2) e (3) as regressões com o número de linhas como variável dependente, enquanto que
nas colunas (4), (5) e (6) têm-se as regressões com o número de passageiros pagantes
como variável dependente.

Para  cada  variável  dependente,  são  testadas  as  três  formas  funcionais  elencadas.  Nas
regressões (3) e (6), onde são consideradas as dummies mensais, os resultados de seus
betas são omitidos. A respeito dos valores nulos na amostra, estes foram excluídos, o que
reduz o grau de liberdade de algumas regressões.

Em  relação  à  Tabela  4,  têm-se  os  resultados  dessas  regressões  para  a  seção
Barbacena/MG - São Paulo/SP.

No que diz respeito ao número de linhas, os resultados para a dummy da operação para as
três formas funcionais são positivos e estatisticamente significantes. A inserção da dummy
de  outorga  reduz  a  significância  da  dummy  da  operação.  A  dummy  de  outorga  não  é
estatisticamente significante.

Tomando por referência esse resultado, o que se teria observado é um aumento no número
de linhas depois do ato de concentração.

Quanto ao número de passageiros pagantes, a regressão (4) da Tabela 4, apenas com a
dummy  da  operação,  apresenta  estimativas  indistintas  de  zero  para  essa  variável.  Na
medida em que se passa a controlar pelo período do regime de autorização, como se vê
nas  regressões  (5)  e  (6),  as  estatísticas  se  tornam  significantes  para  todas  as  variáveis
explicativas.  O  resultado  indica  um  acréscimo  na  média  associado  à  operação  e  um
posterior decréscimo associado à mudança no regime de outorga.

Sendo  assim,  não  há  evidencia  de  que  o  referido  ato  de  concentração  gerou  qualquer
prejuízo àquela seção.

19

Elaboração: DEE/CADE.

20

A Tabela 5 apresenta o conjunto de resultados das regressões para a seção Barroso/MG -
São Paulo/SP.  Tendo em vista o número de linhas, a regressão somente com a dummy da
operação apresenta resultados significativos que indicam um choque negativo associado
ao período. No entanto, a adição da dummy de outorga faz com que a dummy da operação
se torne estatisticamente não diferente de zero. Como a regressão com a adição da variável
outorga apresenta 𝑅(cid:2870) ajustado significativamente maior (0,614 contra 0,254), entende-se
que seja esse o modelo mais capaz de explicar as mudanças no período. Portanto, não há
evidência  de  que  a  operação  alterou  o  patamar  dessa  variável.  De  fato,  as  mudanças
parecem ser mais bem explicadas pela mudança no regime de outorga.

Quanto aos passageiros pagos, os resultados mostram que os modelos (5) e (6) são os
mais apropriados (com a inclusão da dummy de outorga em ambos e dummies mensais no
segundo), verifica-se que o coeficiente da operação é estatisticamente não diferente de
zero (a um nível de significância de 5%). Portanto, neste caso também, não há evidência
de que a operação alterou o patamar dessa variável.

Não obstante, aqui valem todas as ressalvas sobre a ausência da renda dos municípios
envolvidos  na  regressão,  bem  como  da  oferta  de  serviços  por  aplicativos  naqueles
municípios  e o  desconhecimento  de como  tem  evoluído  os  arranjos  com  o  sistema  de
transporte intermunicipal.

Na  mesma  linha,  a  Tabela  6  e  a  Tabela  7  apresentam,  respectivamente,  as  seções
Itumirim/MG  -  São  Paulo/SP,  Itutinga/MG  -  São  Paulo/SP  e  seus  resultados.  Aqui  as
conclusões  se  distinguem  um  pouco  das  obtidas  para  Barroso.  Não  há  alterações  no
número de linhas associado ao período pós-operação. Basta recordar que os gráficos de
número de linhas das seções que envolviam estas duas cidades eram idênticos. Por sua
vez,  ocorre,  nestas  duas  seções,  uma  redução  do  número  de  passageiros  associada  à
operação.

Já  na seção Nazareno/MG - São Paulo/SP, cujos resultados  estão na Tabela 8, não há
alterações no número de linhas associado ao período pós-operação, nem, uma redução do
número de passageiros associada à operação.

Enfim,  a  seção  de  São  João  Del  Rei/MG  -  São  Paulo/SP,  Tabela  9,  apresenta  valores
positivos  e  significantes  associados  ao  número  de  linhas  na  seção  com  a  referida
operação. Já para o número de passageiros, não há indícios de efeitos da operação.

21

Elaboração: DEE/CADE.

Elaboração: DEE/CADE.

Elaboração: DEE/CADE.

22

Elaboração: DEE/CADE.

Elaboração: DEE/CADE.

23

Em resumo, adotando um nível de significância estatística de 5%, que é o comum neste
tipo de análise, tem-se:

Elaboração: DEE/CADE.

Os municípios de maior população não parecerem ter sido afetados negativamente pela
operação,  talvez  essa  fosse  uma  possibilidade  nos  municípios  menores.  Não  obstante,
Nazareno, que é também um município pequeno, não apresenta qualquer redução em suas
médias associadas ao período pós-operação.

Em  suma,  não  há  um  padrão  generalizado  de  queda  nas  médias,  para  as  variáveis
analisadas, associados à realização do ato de concentração. Já a mudança no regime de
outorga pode ter mudado os incentivos do operador na maioria dos casos. Uma hipótese
é que na medida em que no novo regime o operador pode escolher as rotas e horários que
deve cumprir, é provável que este desloque capital para outras seções que considere mais
lucrativas (trata-se apenas de uma hipótese).

4.3.  Descontos

Nos dados de cadastro disponibilizados pela ANTT encontram-se os registros das tarifas
promocionais oferecidas no serviço regular. A saber, cada linha da planilha representa
uma  promoção,  aqui  entendida  como  um  par  ordenado  formado  pelo  número  de
poltronas oferecidas com desconto promocional e o percentual de desconto aplicado.

Em  uma  mesma  viagem  pode  haver  não  só  uma,  mas  um  conjunto  de  promoções
disponíveis. Segue um exemplo real:

Elaboração: DEE/CADE.

24

Eis as promoções disponíveis na data da viagem:

Elaboração: DEE/CADE.

Neste  documento  dá-se  o  nome  de  viagem  à  combinação  formada  por  uma  empresa
atuando em uma dada linha, em certo sentido (ida/volta), dia e horário.

As conclusões aqui baseiam-se na hipótese de que uma empresa, operando em uma dada
linha, não libera, de maneira regular, dois ônibus num mesmo dia, horário e sentido.

Hipótese 1: Em regra dois ônibus não realizam uma mesma viagem.

A ideia por trás é que ao diferenciar os horários uma empresa tem mais chances de “lotar”
seus  ônibus.  Nota-se,  no  entanto,  que  é  até  provável  que  dois  ônibus  de  uma  mesma
empresa tenham partido em uma mesma viagem em algum momento. Porém, a hipótese
aqui restringe-se ao fato de que isso não deve ocorrer de maneira regular, mas, talvez,
esporádica e não prevista pelo operador.

A resolução nº 1.928/ANTT/2007 dispunha sobre as tarifas promocionais para o TRIIP e
teve vigência de 28 de março de 2007 a 3 de março de 2017, ou seja, contemplou todo o
período de análise aqui considerado. Destacam-se alguns trechos:

Art.  1º  As  empresas  permissionárias  poderão  estabelecer  tarifas  promocionais
diferenciadas em função das características técnicas e dos custos específicos provenientes
do atendimento aos usuários.

§  1º  Observado  o  disposto  no  caput  deste  artigo,  as  empresas  poderão  ofertar  tarifas
promocionais  em  horários  específicos,  não  sendo  obrigatório  o  oferecimento  de  igual
promoção em todas as poltronas disponibilizadas na mesma viagem.

§ 2º A promoção deve ser oferecida, nas mesmas condições, em todas as seções da linha.
É de se supor que passageiros mais adiantados contratassem as melhores tarifas, assim
como  acontece  no  setor  aéreo,  em  regra.  Isso  não  quer  dizer  que  a  flexibilidade  para
estabelecer preço é comparável (não no regime de permissão). O fato dos descontos terem
de ser estabelecidos por linha, ignorando concorrências pontuais que poderiam acontecer
no  nível  de  seção,  retira  graus  de  liberdade  do  operador,  que  sobreprecifica  alguns
mercados para não prejudicar o ajuste em outros.

Ainda  quanto  à  flexibilidade  para  se  estabelecer  descontos,  extrai-se  da  referida
resolução:

Art. 3º As permissionárias deverão comunicar à ANTT o período de vigência das tarifas
promocionais,  a  linha,  os  horários,  a  quantidade  de  assentos  ofertados  e  os  respectivos
percentuais de desconto:

I - com antecedência mínima de cinco dias:

a) no caso de descontos superiores a 50% da tarifa máxima autorizada pela

ANTT; ou

b) no caso de descontos com período de vigência maior que 30 dias contínuos.

II - em até 48 horas após o início da promoção:

25

a) no caso de descontos iguais ou inferiores a 50% da tarifa máxima autorizada pela

ANTT; ou

b) no caso de descontos com período de vigência menor que 30 dias contínuos.

Ou seja, existe um desconto teto para o caso do operador querer adotar uma postura mais
agressiva no curto prazo.

Para  calcular  as  tarifas  teto  dispôs-se,  mais  uma  vez,  dos  dados  operacionais,  onde
encontravam-se  as  distâncias  das  seções  em  cada  ponto  do  tempo  e  os  respectivos
coeficientes tarifários aplicáveis à época, por tipo de pavimento.

Tendo-se calculado as tarifas teto em alguns pontos do tempo, usou-se destas para validar
as demais que foram calculadas com base nos coeficientes tarifários14 de cada ano15 e nas
distâncias já citadas que foram extrapoladas para os demais anos.

Com os dados disponíveis torna-se possível calcular os valores, mínimos, que a empresa
UTIL  abriu  mão,  por  viagem,  por  ter  oferecido  um  conjunto  de  promoções  aos  seus
consumidores.

A saber, a receita máxima de que abre mão uma empresa na forma de descontos para
uma  dada  linha,  num  determinado  sentido  (ida/volta),  para  um  determinado  dia  e
horário16, é a seguinte:

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021) (cid:3428)∑𝑛(cid:3036)

𝑑(cid:3036)
100

(cid:3432)

Onde:

𝑅𝑇(cid:3002)(cid:3003): Máxima receita potencial de que abre mão, por viagem, um operador que adota
uma política de descontos.

𝑝(cid:3021): Preço teto de uma linha (o preço da seção que vai do início ao fim da linha).
𝑖: i-ésima promoção da viagem, a saber, par ordenado (𝑛(cid:3036), 𝑑(cid:3036)).
𝑛(cid:3036): Número de poltronas ofertadas para a i-ésima promoção de uma viagem.
𝑑(cid:3036): Desconto percentual da i-ésima promoção de uma viagem.

Essa simplificação da fórmula permite que o cálculo seja realizado com os dados públicos
disponíveis e sua demonstração é apresentada no apêndice deste documento.

Enfatiza-se que a receita abdicada aqui diz respeito apenas à receita de que abre mão o
operador com a adoção de um conjunto de descontos. Os efeitos de outras circunstancias
que possam gerar redução de receita não são aqui mensurados.

De fato, o operador pode ter uma redução na sua receita efetiva associada a clientes que
adquirem o serviço de transporte para outras seções da linha que não a maior (lembrando
que a tarifa cobrada é função da distância percorrida).

14 Ônibus convencional com sanitário, com base nos dados operacionais da ANTT.

15Disponíveis em:
http://www.antt.gov.br/perguntas_frequentes/passageiros.html?diretorio=reajuste_tarifario&titulo=Reajus
te%20Tarif%C3%A1rio&categoria=passageiros

16 Aqui se supõe que uma mesma empresa não dê início a duas viagens no mesmo sentido, dia e horário
para uma mesma linha.

26

É  muito  provável  que  descontos  influenciem  a  demanda  em  cada  uma  das  seções.  Se
mesmo com a adoção de descontos houver situações onde a oferta de lugares em uma
viagem  é  superior  à  demanda por  lugares  da  maior das  seções  da  viagem,  haverá  sim
aumento  da  receita  abdicada  total.  Afinal,  serão  menores  as  tarifas  pagas  pelos
passageiros que contratam o serviço para seções menores, onde ocuparão, ou não, todos
os lugares restantes.

Num  cenário  onde  não  é  possível  restringir  a  oferta,  com  parâmetros  mínimos
estabelecidos pela ANTT (antigo regime de outorga), e tendo em vista a incapacidade do
operador de evitar possíveis desvios de demanda, muitas vezes associados à presença de
outro operador, se justifica uma empresa adotar um conjunto de descontos.

Portanto, espera-se que num ambiente de maior concorrência sejam mais frequentes os
descontos dados aos consumidores. Observa-se, então, o que aconteceu nos mercados de
interesse.

4.3.1.  Análise descritiva das receitas abdicadas

Das  linhas  transferidas,  apenas  as  linhas  São  João  Del  Rei  (MG)  –  São  Paulo  (SP)
(06.0848-00),  Barbacena  (MG)  –  São  Paulo  (SP)  (06.1090-00)  e  Barbacena  (MG)  –
Campinas (SP) (06.1090-00) tinham seções com sobreposição. Sendo assim, ignoram-se
os descontos históricos das demais linhas transferidas.

Com  relação  ao  serviço  São  João  Del  Rei  (MG)  –  São  Paulo  (SP)  (06.0848-00),  não
houve,  em  momento  algum,  qualquer  registro  de  promoção  na  base  de  tarifas
promocionais. Sendo assim, procede-se a análise das linhas restantes.

Como os dados de receita abdicada foram calculados por viagem, foi possível agregar por
mês as receitas das linhas da empresa UTIL.

27

Figura 14: Receita abdicada mensal da UTIL com as linhas 06.1090-00 e 06.1090-01

Em relação às linhas 06.1090-00 e 06.1090-01, o que se percebe é que os descontos se
dão com frequência irregular. Nota-se também que a receita abdicada de ambas alcança
seu  ápice  em  meados  de  junho  de  2013.  Existe  sim  uma  diferença  de  médias  para  os
períodos pré e pós-operação, mas muito influenciada por esse pico.

A diferença notável para a linha 06.1090-01 é que os descontos se tornaram bem mais
frequentes a partir do final de 2015.

Para além do que se pode intuir visualmente, procede-se às regressões para comparar as
receitas abdicadas médias antes e depois da operação. Mesmo sem saber da sua real razão
buscar-se-á, ao realizar as regressões, controlar as médias por uma dummy para o mês de
junho de 2013.

Em todas as regressões da Tabela 13 a seguir foi inserida a dummy “Outorga” que indica
o início do novo regime de autorização vigente, no entanto, a série da linha 06.1090-00
não apresenta dados para esse período. Utilizou-se a série mensal, atribuindo valor zero
aos  meses  em  que  não  houve  a  disposição  de  qualquer  tarifa  promocional.  Quanto  à
operação, as regressões sem o controle do pico de junho de 2013, para ambas as séries,
apresentam coeficientes não diferentes de zero.

Com  a  inserção  dos  controles  de  pico,  observam-se  resultados  distintos.  Para  a  linha
06.1090-00 a operação  continua a apresentar efeito não diferente de zero na média da
série, mas para a linha 06.1090-01, o resultando, mesmo isolando-se os efeitos do período
de pico, é de aumento da média das receitas abdicadas mensais. Dessa forma, para a linha
06.1090-01, observa-se que depois da operação os descontos se tornaram mais frequentes
para a empresa UTIL.

28

5.  Conclusões

Este parecer se ateve a avaliar as diferenças de médias de um conjunto de séries para os
períodos antes e depois da operação. Utilizou como controles outras dummies especificas
associadas  a  mudanças  institucionais.  Ademais,  não  considerou  possíveis  impactos  de
rede que podem ser observados em operações dessa natureza.

Este parecer, limitado às suas hipóteses, restrições e métodos, não encontrou, de forma
consistente, qualquer mudança de padrão que possa indicar uma queda de frequência ou
diminuição dos descontos decorrentes da referida operação.

DEE/Cade

Assinado eletronicamente no DOC SEI 0555894 [versão pública]

29

6.  Referências

ANTT.  Dados  Cadastrais.  http://portal.antt.gov.br/index.php/content/view/46095.html
(acesso em 6 de Setembro de 2018).

—.
Operacionais.
http://portal.antt.gov.br/index.php/content/view/46098/Dados_operacionais.html (acesso
em 6 de Setembro de 2018).

Dados

—.  Licitação  de  serviços  de  transporte  rodoviário  interestadual  semiurbano  de
passageiros.  2016.  http://www.antt.gov.br/backend/galeria/arquivos/pgo_pos_ap.pdf
(acesso em 6 de Setembro de 2018).

—.  Resolução  n  1.928,  de  28  de  março  de  2007.  Mar  de  2007.
http://portal.antt.gov.br/index.php/content/view/2928/Resolucao_1928.html  (acesso  em
6 de Setembro de 2018).

Jun  de  2008.
—.  Resolução  n  2.772,  de  25  de
http://portal.antt.gov.br/index.php/content/view/3772/Resolucao_2772.html  (acesso  em
6 de Setembro de 2018).

junho  de  2008.

—.  Resolução  n  3.076,  de  26  de  março  de  2009.  Mar  de  2009.
http://portal.antt.gov.br/index.php/content/view/4076/Resolucao_3076.html  (acesso  em
6 de Setembro de 2018).

—.  Resolução  n  3.173,  de  25  de
http://portal.antt.gov.br/index.php/content/view/4173/RESOLUCAO_N__3173.html
(acesso em 6 de Setembro de 2018).

junho  de  2009.

Jun  de  2009.

—.  Resolução  n  3.538,  de  16  de
Jun  de  2010.
http://portal.antt.gov.br/index.php/content/view/4538/Resolucao_3538.html  (acesso  em
6 de Setembro de 2018).

junho  de  2010.

—.  Resolução  n  3.687,  de  15  de
Jun  de  2011.
http://portal.antt.gov.br/index.php/content/view/4687/Resolucao_3687.html  (acesso  em
6 de Setembro de 2018).

junho  de  2011.

—.  Resolução  n  3.852,  de  20  de
http://portal.antt.gov.br/index.php/content/view/16836/RESOLUCAO_N__3852.html
(acesso em 6 de Setembro de 2018).

junho  de  2012.

Jun  de  2012.

setembro  de  2013.  Set  de  2013.
—.  Resolução  n  4.166,  de  26  de
http://portal.antt.gov.br/index.php/content/view/25995/Resolucao_n__4166.html (acesso
em 6 de Setembro de 2018).

Jun  de  2014.
—.  Resolução  n  4.351,  de  25  de
http://portal.antt.gov.br/index.php/content/view/32685/Resolucao_n__4351.html (acesso
em 6 de Setembro de 2018).

junho  de  2014.

30

—.  Resolução  n  4.517,  de  19  de  dezembro  de  2014.  Dez  de  2014.
http://portal.antt.gov.br/index.php/content/view/37152/Resolucao_n___4517.html
(acesso em 6 de Setembro de 2018).

—.  Resolução  n  4.635,  de  05  de  março  de  2015.  Mar  de  2015.
http://portal.antt.gov.br/index.php/content/view/38707/Resolucao_n__4635.html (acesso
em 6 de Setembro de 2018).

—.  Resolução  n  4.765,  de  25  de
Jun  de  2015.
http://portal.antt.gov.br/index.php/content/view/40035/Resolucao_n__4765.html (acesso
em 6 de Setembro de 2018).

junho  de  2015.

—.  Resolução  n  4.770,  de  25  de
Jun  de  2015.
http://portal.antt.gov.br/index.php/content/view/40115/Resolucao_n__4770.html (acesso
em 6 de Setembro de 2018).

junho  de  2015.

—.  Resolução  n  5.123,  de  22  de
Jun  de  2016.
http://portal.antt.gov.br/index.php/content/view/47796/Resolucao_n__5123.html (acesso
em 6 de Setembro de 2018).

junho  de  2016.

—.  Resolução  n  5.368,  de  29  de
Jun  de  2017.
http://portal.antt.gov.br/index.php/content/view/51913/Resolucao_n__5368.html (acesso
em 6 de Setembro de 2018).

junho  de  2017.

Jun  de  2018.
—.  Resolução  n  5.826,  de  29  de
http://portal.antt.gov.br/index.php/content/view/53820/Resolucao_n__5826.html (acesso
em 6 de Setembro de 2018).

junho  de  2018.

Tomada

2018.
nº
—.
http://portal.antt.gov.br/index.php/content/view/54017.html (acesso em 6 de Setembro de
2018).

010/2018.

Subsídio

Ago

de

de

ANTT, SUPAS. “Ordem de Serviço n 001/2015.” Dez de 2014.

—. “Ordem de Serviço n 005/2015.” Mar de 2015.

n

de

76,

—.  Portaria
2016.
https://anttlegis.antt.gov.br/action/UrlPublicasAction.php?acao=abrirAtoPublico&sgl_ti
po=POR&num_ato=00000076&seq_ato=000&vlr_ano=2016&sgl_orgao=SUPAS/ANT
T/MT&cod_modulo=161&cod_menu=5414 (acesso em 6 de Setembro de 2018).

2016.  Abr

de  Abril

28

de

de

ANTT, SUREG. “Nota Técnica n 058/SUREG/2014.” Anuência para a transferência de
serviços operados no regime de autorização especial., Dez de 2014.

—. “Nota Técnica n 011/SUREG/2015.” Pedido de Reconsideração Especial. Anuência
para a transferência de serviços operados no regime de autorização especial., Fev de
2015.

31

a

operar

Bazani, Adamo. UTIL, de Jacob Barata, é autorizada pelo Governo do Estado de São
Paulo
2016.
3
https://diariodotransporte.com.br/2016/02/23/util-de-jacob-barata-e-autorizada-pelo-
governo-do-estado-de-sao-paulo-a-operar-na-area-3-da-emtu/ (acesso em 6 de Setembro
de 2018).

EMTU.

área

Fev

na

da

de

n

Brasil.  Lei
2001.
http://www.planalto.gov.br/ccivil_03/LEIS/LEIS_2001/L10233.htm  (acesso  em  6  de
Setembro de 2018).

10.233,

junho

2001.

Jun

de

de

de

de

5

n

Lei

12.815,

2013.
—.
http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2013/Lei/L12815.htm  (acesso  em
6 de Setembro de 2018).

junho

2013.

Jun

de

de

de

de

5

Cascione, Pulino, Boulos & Santos. “Formulário de Notificação de AC (SEI 0390517).”
Set de 2017.

—. “Notificação de Ato de Concentração (SEI 0390515).” Set de 2017.

IBGE. Cidades. https://cidades.ibge.gov.br/ (acesso em 6 de Setembro de 2018).

32

Apêndice

Demonstração do cálculo da receita abdicada

A saber, a máxima receita que uma empresa de ônibus pode realizar numa dada linha,
num determinado sentido (ida/volta), para um determinado dia e horário17, é a seguinte:

Onde:

𝑅𝑇(cid:3014) = 𝑝(cid:3021)𝑁

𝑅𝑇(cid:3014): Máximo potencial de receita por viagem.
𝑝(cid:3021): Preço teto de uma linha (o preço da seção que vai do início ao fim da linha).
𝑁: Número de poltronas ofertadas no ônibus.

Já  a  máxima  receita  que  uma  empresa  pode  obter  quando  oferece  um  conjunto  de
promoções para uma dada viagem é a seguinte:

𝑅𝑇(cid:3017) = 𝑝(cid:3021)(𝑁 − ∑𝑛(cid:3036)) + ∑𝑝(cid:3021) (cid:3436)1 −

𝑑(cid:3036)
100

(cid:3440) 𝑛(cid:3036)

Onde:

𝑅𝑇(cid:3017): Máximo potencial de receita por viagem, com descontos.
𝑖: i-ésima promoção da viagem, a saber, par ordenado (𝑛(cid:3036), 𝑑(cid:3036)).
𝑛(cid:3036): Número de poltronas ofertadas para a i-ésima promoção de uma viagem.
𝑑(cid:3036): Desconto percentual da i-ésima promoção de uma viagem.
Para calcular a receita potencial da qual a empresa abre mão quando adota uma política
de descontos, basta realizar a seguinte subtração:

𝑅𝑇(cid:3002)(cid:3003) = 𝑅𝑇(cid:3014) − 𝑅𝑇(cid:3017)

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021)𝑁 − (cid:3436)𝑝(cid:3021)(𝑁 − ∑𝑛(cid:3036)) + ∑𝑝(cid:3021) (cid:3436)1 −

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021)𝑁 − 𝑝(cid:3021)(𝑁 − ∑𝑛(cid:3036)) − ∑𝑝(cid:3021) (cid:3436)1 −

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021)𝑁 − 𝑝(cid:3021)𝑁 + 𝑝(cid:3021)∑𝑛(cid:3036) − 𝑝(cid:3021)∑ (cid:3436)1 −

𝑑(cid:3036)
100
𝑑(cid:3036)
100
𝑑(cid:3036)
100

(cid:3440) 𝑛(cid:3036)(cid:3440)

(cid:3440) 𝑛(cid:3036)

(cid:3440) 𝑛(cid:3036)

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021) (cid:3428)∑𝑛(cid:3036) − ∑ (cid:3436)1 −

𝑑(cid:3036)
100

(cid:3440) 𝑛(cid:3036)(cid:3432)

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021) (cid:3429)∑𝑛(cid:3036) (cid:3437)1 − (cid:3436)1 −

𝑑(cid:3036)
100

(cid:3440)(cid:3441)(cid:3433)

Que pode ser assim resumido:

17 Aqui se supõe que uma mesma empresa não dê início a duas viagens no mesmo sentido, dia e horário
para uma mesma linha.

33

𝑅𝑇(cid:3002)(cid:3003) = 𝑝(cid:3021) (cid:3428)∑𝑛(cid:3036)

𝑑(cid:3036)
100

(cid:3432)

Onde:

𝑅𝑇(cid:3002)(cid:3003): Máxima receita potencial de que abre mão, por viagem, um operador que adota
uma política de descontos.

34

