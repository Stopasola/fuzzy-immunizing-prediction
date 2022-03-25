# Distribuição de imunizantes em um cenário epidêmico de covid-19

![image](https://img.shields.io/github/languages/top/stopasola/minimum-cost-graph)
 
## Introdução

   No ano de 2020 a humanidade enfrentou um de seus maiores desafios em décadas, uma pandemia de alcance global assolou o planeta todo e trouxe consigo
milhares de mortes, desinformações, crise financeira e muitas dúvidas quanto aofuturo. 
   Neste cenário a comunidade científica ficou encarregada de encontrar uma solução para o coronavírus, solução esta que veio por meio de vacinas desenvolvidas em tempo recorde e capazes de devolver à sociedade uma vida normal.
  A partir do momento em que o desenvolvimento das vacinas chegaram às fases finais de testes, houve uma preocupação de países e instituições como a OMS
na maneira em que esse recurso finito seria distribuído, uma vez que países com maior poder econômico tem maior poder de barganha e, como resultado, vão
conseguir vacinar sua população em ritmo acelerado, enquanto países subdesenvolvidos não serão capazes de adquirir imunizantes em quantia necessária
para reduzir significantemente o número de infecções e consequentemente de mortes diárias devido a COVID-19.

   
   A COVAX (COVID-19 Vaccines Global Access) é uma iniciativa global criada com o objetivo de proporcionar acesso igualitário à vacina para países de médio e baixo poder econômico. A distribuição irá consistir em uma divisão igualitária entre todos
os países membros da aliança proporcionalmente a sua população, ressaltando que
nenhum país receberá doses que correspondam a mais de 20% de seus habitantes
enquanto todos os membros não tiverem a mesma oferta.

   Dentro do contexto supracitado este trabalho se propoẽ, dentro de suas
limitações, a desenvolver um algoritmo de lógica fuzzy capaz de atribuir valores
dentro de um range específico para cada país, imputando variáveis de entrada como
densidade populacional, população com mais de 70 anos, PIB per capita, população
com doenças respiratórias crônicas e leitos de hospitais disponíveis. De acordo com o
valor obtido pelo país, este irá figurar em uma lista com todos os participantes
ordenados por seu score, e receberá proporcionalmente a sua colocação uma
porcentagem da amostra total.
Desenvolvimento:
Neste relatório são validados modelos que representam abstrações lógicas do
cenário real, ou seja para representar a amostra populacional, ao invés de considerar
todos os países destinatários do consórcio Covax Facility consideramos apenas 21
países selecionados aleatoriamente em cada continente.
Quanto ao número de vacinas, consideramos uma quantidade de 500 milhões
de doses para distribuição do consórcio. Nossas variáveis de entrada foram escolhidas
com base nos dados apresentados no trabalho Explaining among-country variation in
COVID-19 case fatality rate [15]. Nele são apresentados diversos fatores possíveis que
podem ser considerados de risco, e que podem potencializar o número de mortes no
país. No apêndice A são listados todos os países usados na pesquisa, suas variáveis
de entrada, e seus respectivos valores para cada.
Os dados usados neste trabalho provêm do repositório de dados Our World in
Data [1], utilizado por diversas instituições de renome internacional, inclusive para
pesquisas de distribuição e análise de dados da OMS. Para o desenvolvimento do
projeto, usamos a ferramenta de cálculo numérico MATLAB[16] utilizando o pacote
Fuzzy Logic Toolbox[17].
Usamos trapézios como nossas funções de pertinência a fim de representar os
intervalos das variáveis de entrada, uma vez que melhor representou os dados usados
devido a seus platôs.
Uma vez que tínhamos nossas variáveis de entradas, funções de pertinência,
modelamos um score de 1 a 100, onde quanto maior o valor, mais o país precisa de
vacinas. Por fim estipulamos qual seria a distribuição da COVAX e de nosso sistema
fuzzy, atribuindo porcentagens maiores de acordo com as posições no ranking. Nosso
objetivo principal é evitar que o sistema de saúde fique sobrecarregado e
consequentemente cause um número maior de óbitos.
Variáveis de entrada:

Variáveis de entrada:
Variáveis Faixa de valor Função de
pertinência
Densidade
populacional
[0, 25] baixa
[50, 100] média
[200,>] alta
Trapézio
Porcentagem da
população com
mais de 70 anos
[0, 5] baixa
[7, 14] média
[16, >] alta
Trapézio
PIB per capita [0, 2.000] muito baixa
[3000, 8.000] baixa
[10.000, 30.000] média
Trapézio
[35.000, >] alta
Porcentagem de
pessoas com
doenças
respiratórias
crônicas
[0, 30] baixa
[40,70] média
[80, >] alta
Trapézio
Número de leitos [0, 2] baixa baixa
[3, 5] média
[7, >] alta
Trapézio
Variáveis de saída
Variáveis Faixa de valor Função de
pertinência
Score [0, 20] baixa
[21, 40] média baixa
[41, 60] média
[61, 80] média alta
[81,100] alta
Trapézio
Saída esperada
Dado o número de vacinas disponíveis para distribuição no consórcio COVAX,
consideramos com base nas nossas variáveis de entrada o percentual (quantidade) de
vacinas que os países receberão com base no score calculado através das variáveis de
entrada.

Regras implementadas
Implementamos 324 regras e distribuímos pesos para cada entrada e seu
respectivo range, tal estratégia foi usada para calcular o range da saída obtida, uma
vez que nessa etapa seria esperado que um infectologista especialista na área
auxiliasse na criação das regras e suas respectivas saídas. Podemos observar algumas
de nossas regras na Figura 1.
Figura 1 - Exemplo regras Matlab
Sintaxe das regras:
If (DensidadePopulacional is baixa) and (MaisQue70Anos is baixa) and (PIBPerCapita
is muitobaixa) and (DoencasCronicas is baixa) and (NumeroLeitos is baixa) then (Score
is baixa) (1)
If (DensidadePopulacional is baixa) and (MaisQue70Anos is baixa) and (PIBPerCapita
is muitobaixa) and (DoencasCronicas is baixa) and (NumeroLeitos is media) then
(Score is baixa) (1)
If (DensidadePopulacional is baixa) and (MaisQue70Anos is baixa) and (PIBPerCapita
is muitobaixa) and (DoencasCronicas is baixa) and (NumeroLeitos is alta) then (Score
is muitobaixa) (1)
Controlador
Mamdani
Método de defuzzificação utilizado
Centróide
Resultado da implementação:
Foi testado um modelo utilizando um valor de 500.000.000 de doses de
vacinas, fizemos uma distribuição proporcional ao número de habitantes como é
realizado pela COVAX, e utilizamos nosso modelo para realizar a mesma tarefa. Na
distribuição proporcional à população, países grandes como a China tomam uma
parcela muito grande do estoque, enquanto países menores como Israel acabam
recebendo uma parcela menor das doses, mais detalhes nos anexos B e C.
Observamos que nosso modelo fornece uma distribuição mais justa das doses,
proporcional a sua necessidade estimada pelo nosso sistema, o que pode ser
fundamental no auxílio dos países no que tange a sobrecarga dos sistemas de saúde,
o qual era nosso objetivo inicial.
Já a métrica do número de vidas salvas, não é confiável ou possível de se
transpor para o mundo real pois poucos países realizaram um estudo que estima o
número de vidas salvas graças à vacinação. Ainda faltam dados para compararmos
nossos resultados de maneira mais assertiva, considerando que ainda não temos a
redução de mortes e infectados para cada país analisado, dificultando maiores
conclusões.
Infelizmente, acabamos não encontrando informações correspondentes à
queda do número de mortes para cada país estudado a fim de validar nossos dados.
Obtivemos apenas parâmetros do números de pessoas salvas pela vacinação nos
Estados Unidos [2] e Inglaterra[12], não sendo suficiente para validar a saída do
sistema.

Referências bibliográficas


[1] GLOBAL CHANGE DATA LAB. Our world in data, 2021. Página inicial. Disponível em:
<https://ourworldindata.org/>. Acesso em: 20/07/2021.
[2] GALVANI, Alison; MOGHADAS, Seyed M.; SCHNEIDER, Eric C. Deaths and
Hospitalizations Averted by Rapid U.S. Vaccin
