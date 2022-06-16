# Project House Predict Price
Imagine que você é um comprador de imóveis e que está negociando com algum potencial cliente e durante a conversa ele diz que o imóvel está com um otímo preço e que você vai ter sorte de comprar por esse preço, como você não e bobo em nem nada, você começa a pensar em todos os negocios que fez, começa a fazer os calculos de cabeça ou até em uma folha de papel até que percebe que sim e um bom negócio e compra aquele imóvel, dias depois procurando por mais imóveis você encontra um que e semelhante ao imóvel que você comprou so que esse está pela metade do preço, e você descobre que foi engano e que perdeu dinheiro.
Buscando uma forma de resolver esse problema, você contrata uma consutoria de Ciência de dados, você nem sabe muito bem o que é, porém ouviu falar que pode ajudar você no seu negocio pois eles trabalham com uma tal de Inteligencia artificial, então você resolve
tentar e pede pra essa pessoa que ela crie algo que lhe diga o preço aproximado que aquele imóvel deveria está, que o erro não fosse muito grande mais também não precisa ser perfeito pois o preço de casas varia muito, o Cientista aceita e começa o projeto...

### Questão de Negócio
Como podemos analisar na pequena historia criada, o problema de negocio e a precificação dos imóveis na hora  da compra, então e isso que vamos tentar resolver aqui, achar o melhor preço na hora de  **Precifica o Preço do Imóvel**

### Premissas
Caso eu não tivesse a historia do comprador e o do cliente, eu diria que o comprador de imóveis está pedindo o projeto, para que saiba quando está fazendo um bom negócio na compra de um ímovel ou não, ou seja, se na hora que o cliente der o preço do imóvel, se ele realmente condiz com a realidade, pois caso não o comprador vai está perdendo dinheiro e caso contrario que o cliente de o preço menor do que deveria estar esse vai ser um bom negócio para o comprador, pois vai comprar mais barato e mais tarde vender mais caro, fazendo assim a empresa ganhar mais dinheiro.

### Planejamento da Solução:
Para resolver esse projeto eu vou seguir os passos e usar as seguintes ferramentas

1.O que será entregue no final?
No fim Projeto vamos ter
    1. Um modelo com mais de 80% de precisão já que os preços das casas variam muito.
    2. WebApp
        - Para deploy vamos ter um Webapp que vai funcionar assim:
            - input: Informações sobre o imóvel
            - output: Preço mais adequado para aquele imóvel ou mais proximo que deveria estar.
2.Ferramentas
    Python 3
        - Vou usar Python para Coletar, limpar e fazer os modelos de Machine Learning.
    GitHub
        - Vou usar o Git para versionamento de codigo, ir salvando o projeto a cada etapa.
    Streamlit
        - Vou usar o streamlit para fazer o deploy do modelo e um Webapp
    Heroku
        - Vou usar o heroku para colocar esse webapp criado pelo streamlit na nuvem

3.Como será feito a solução do problema?
    - Para solucionar esse problema eu vou criar um modelo de machine learning que dado os parametros me retorne o preço, para fazer isso eu vou realizar o projeto em ciclos e ir analisando a melhora do modelo passo a passo, o projeto vai levar em média 10 ciclos e no fim de cada ciclo vai ter uma miní-conclusão do projeto, para saber os proximos passos e o resumo que foi feito naquela etapa.


### Validação de hipoteses:
Depois de fazer analise exploratoria de dados eu fiz 5 descobetas que vieram da validação de hipoteses.
Abaixo vamos ter a Hipotese | Se ele e verdadeira ou não

H1: O crescimento de vendas YoY e de 10%.
FALSA: O crescimento YoY não cresce ao passar dos anos ele DECAI

H2: Imóveis com data de construção menor que 1960, são 40% mais baratos, na média.
FALSA Imoveis com data de contrução menor que 1960 são 41 % mais baratos na média.

H3: A região com mais imóveis possui o preço 10% maior do que as outras regiões, na média.
FALSA: Mesmo a região RL possuindo mais imóveis o preço médio dela e 12% menor do que a região FV que possui menos imóveis.

H4: Imóveis com preço abaixo da média representam 45% ou mais da minhas vendas.
VERDADEIRA: Minhas vendas com os imóveis com preço abaixo da média REPRESENTAM 76% DAS MINHAS VENDAS

H5:O crescimento de vendas dos imóveis aumenta 10% a cada mes (MoM), na média.
FALSA: O crescimento a cada mes não é de 10% e tendem até a diminuir com o tempo, com uma queda de 10% no mês 10.



### Resultados Financeiros
Quanto a empresa vai ganhar caso siga o que o modelo prediz?
E caso ele erre quanto a empresa vai faturar?
Abaixo tempos uma Tabela com essas respostas.




### Conclusão Final.
Agora vamos imaginar a mesma historia do comprador, com o mesmo cliente so que agora ele tem um WebApp com um modelo de Machine Learning rodando por trás, depois que o cliente da o preço do imóvel, aquele acima do preço o comprador agora vai no WebbApp pede as informações para o cliente e tem como retorno um valor que e a metade do preço que o cliente passou, e agora ao inves de comprar o imóvel, você fala para o cliente que está muito acima do preço e que não quer o imóvel, dias depois você encontra aquele imóvel com o preço semelhante ao preço que o modelo te passou, compra o imóvel e dias consegue vender mais caro, fazendo assim a receita da sua empresa aumentar.

Como podemos notar na pequena historia criada por mim, feita apenas a fim de contextualização do problema, agora o comprador vai saber o quanto os imoveis deveriam custar e quando e uma boa oportunidade ou não, fazendo assim ele se livrar de negócios que geriam mais prejuizos do que lucro e conseguindo aproveitar melhor as oportunidades de comprar algum imóvel com o preço menor do que deveria está.

Por isso me sinto sadisfeito com o projeto pois cheguei até onde eu queria.




### Próximos Passos
Existem muitos passos no projeto que poderiam ser refeitos de uma melhor forma, quem sabe numa segunda onda do ciclo de desenvolvimento do projeto eu conseguisse uma precisão maior, so que para isso e para melhorar o projeto o ponto mais crucial seria coletar mais dados, pois com mais dados com certeza teriamos um projeto mais preciso, mas como não e possivel já que e um projeto do Keggle então estou sadisfeito por agora, porém vou lista alguns passos que poderiam ser feitos de uma melhor forma
    - Coletar mais dados.
    - Realizar outros tipos de Preenchimento de NA
    - Dependendo da quantidade de dados até usar uma Rede Neural
    - Mudar o tipo de enconder das variaveis
    - Realizar um Feature Engienner melhor
    - etc...
o ponto e que projeto pode ser melhorado, podendo chegar até em uma precisão melhor, mas isso seria praticamente outro projeto e que no final quem iria descidir seria o "Comprador" ficticio da nossa historia, mas como não tenho esse Feedback de que precisa melhorar mais, eu vou parar por aqui, obrigado por ler, tenha um bom dia!.
