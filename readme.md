# Stack Overflow Developer Survey - 2023

![Logo](/assets/logo.png)

O projeto consiste na análise das respostas feitas por programadores na pesquisa anual do site **[Stack Overflow](https://stackoverflow.com)**.

Para realizar o projeto respondendo as perguntas de negócio, utilizei o Python para tratamento dos dados e para fazer a análise exploratória por meio da biblioteca SQLAlchemy que possibilitou a execução de queries nativas SQL dentro do Python e Power BI para visualização e interação com os dados existentes.

## Sobre os dados

A análise foi realizada utilizando a base de dados contendo as respostas de pesquisa, os dados foram retirados do site **[Stack Overflow Survey](https://survey.stackoverflow.co)**

### Dashboard:

No dashboard, pode-se conferir quais os indicadores existem para um melhor entendimento e existe a possibilidade de aplicar filtros para diferentes visões.

![Dashboard_Indicadores](/assets/dashboard_indicadores.png)

![Dashboard_Lista](/assets/dashboard_listas.png)

**[Clique para ver o dashboard](https://app.powerbi.com/view?r=eyJrIjoiNDIwYzM1MDgtNDg3Mi00YmQ5LWI1N2QtNzk4YmU2Yzg1NTg0IiwidCI6ImE5NjgwMmM4LTA0OTAtNDI3NC1iZDVmLTA5NzIxYWQzOWRjNiJ9)**

## Ferramentas

Utilizei as seguintes ferramentas:

- **Python**: Foi utilizado para realizar a análise exploratória dos dados, criação e manipulação da base.
- **SQL**: Foi utilizado como forma de realizar as consultas para base utilizando dentro do python por meio da biblioteca SQLAlchemy.
- **Power BI**: Foi utilizado para construção do dashboard.

## Perguntas respondidas

### O público da pesquisa

#### **Distribuição do nível educacional:**

41,72% dos entrevistados possuem um diploma de bacharel, seguidos por 23,35% possuindo um mestrado.

![Distribuição por nível educacional](/assets/Distribuição_por_nível_educacional.png)

#### **Qual a distribuição da idade?**

37,28% dos entrevistados estão na faixa etária dos 25 até os 34 anos, 23,02% na faixa etária dos 35 até os 44 anos e 20,11% na faixa dos 18 até os 24 anos.

![Distribuição por idade](/assets/Distribuição_por_idade.png)

#### **Qual a distribuição por status de empregabilidade?**

59,75% dos entrevistados estão empregados e trabalhando uma jornada de trabalho completa, 13,72% como freelancer ou consultores e 11,55% como estudantes em período integral.

![Distribuição por empregabilidade](/assets/Distribuição_por_empregabilidade.png)

#### **Qual a distribuição por modalidade de emprego?**

42,18% dos entrevistados trabalham no modelo híbrido, 41,41% no modelo remoto e apenas 16,41% no modelo presencial.

![Distribuição por nível modalidade de emprego](/assets/Distribuição_por_modalidade_de_emprego.png)

### Estudo, trabalho e carreira

#### **Qual a forma mais utilizada para estudar?**

78,76% dos entrevistados prefere recursos online para estudar como vídeos, blog, etc. 50,91% preferem estudar com mídias físicas, 49,29% preferem estudar em faculdades e 48,44% preferem fazer cursos ou certificações.

![Distribuição por formas de estudo](/assets/Distribuição_por_formas_de_estudo.png)

#### **Quais cursos ou certificações online foram mais utilizadas?**

33,42% dos entrevistados fizeram certificações pela Udemy, 17,66% pela Coursera e 12,40% pela Codeacademy.

![Distribuição por certificações realizadas](/assets/Distribuição_por_certificações_realizadas.png)

#### **Qual a quantidade por senoridade? (Dividir em júnior, pleno e sênior)**

61,13% dos entrevistados são sêniors, 20,10% são júniors e 18,77% são considerados plenos.

![Distribuição por senioridade](/assets/Distribuição_por_senioridade.png)

#### **Quais os cargos mais populares?**

A maior parte dos entrevistados são desenvolvedores web divididos em:

- Fullstack: 33,48%
- Backend: 17,88%
- Frontend: 6,60%

![Distribuição por cargo](/assets/Distribuição_por_cargo.png)

#### **Qual o salário médio por cargo? Existe correlação com a idade, escolaridade, modalidade e senioridade? Verifique todos os pontos no Brasil**

**Por Cargo**

O cargo que melhor está pagando é engenheiro que garante o funcionamento de uma empresa inteira, porém, a amostragem é muito baixa. Com a amostragem mais alta, Desenvolvedor backend em média está pagando quase 19 mil reais e o fullstack em média está ganhando cerca de 18 mil e 800 reais por mês.

![Cargo x Salário Médio](/assets/CargoxSalário_Médio.png)

**Por Idade**

Podemos afirmar que existe uma correlação entre idade e o salário médio mensal, uma vez que pessoas no auge da carreira estão ganhando mais do aquelas que estão começando ainda.

![Idade x Salário Médio](/assets/IdadexSalário_Médio.png)

**Por Escolaridade**

Não existe uma correlação clara entre estudo e o salário médio, já que em primeiro lugar está aqueles que possuem o tecnólogo acima de quem possue mestrado por exemplo.

![Escolaridade x Salário Médio](/assets/EscolaridadexSalário_Médio.png)

**Por Senioridade**

Podemos afirmar que existe uma correlação com a senioridade, já que o sênior ganha mais em média, seguido do pleno e do júnior.

![Senioridade x Salário Médio](/assets/SenioridadexSalário_Médio.png)

**Por Modalidade**

As modalidades que mais paga é a híbrida, já a presencial é a que menos paga.

![Modalidade x Salário Médio](/assets/ModalidadexSalário_Médio.png)

### Tecnologias

#### **Quais as linguagens mais utilizadas?**

O top 5 linguagens utilizadas foram:

- Javascript: 62,47%
- HTML/CSS: 52,02%
- Python: 48,38%
- SQL: 47,79%
- Typescript: 38,17%

São principalmente linguagens focadas no desenvolvimento web fullstack (JS, HTML, CSS e TS) e para dados/automações (Python e SQL).

![Distribuição por linguagem](/assets/Distribuição_por_linguagem.png)

#### **Quais os frameworks mais utilizados?**

O top 5 frameworks utilizados foram:

- Node.js: 34,34%
- React: 32,67%
- JQuery: 17,70%
- Express: 15,52%
- Angular: 14,06%

Todos frameworks javascript para desenvolvimento web fullstack.

![Distribuição por framework](/assets/Distribuição_por_Framework.png)

#### **Quais os bancos de dados mais utilizados?**

O top 5 bancos de dados utilizados é:

- Postgres: 39,14%
- MySQL: 35,31%
- SQLite: 26,55%
- MongoDB: 21,93%
- Microsoft SQL Server: 21,87%

![Distribuição por Banco de dados](/assets/Distribuição_por_Banco_de_dados.png)

#### **Quais as clouds mais utilizadas?**

O Top 5 clouds são:

- AWS: 37,92%
- Azure: 20,30%
- Google Cloud: 18,60%
- Firebase: 12,07%
- Cloudflare: 11,88%

![Distribuição por cloud](/assets/Distribuição_por_Cloud.png)

#### **Quais os editores de código preferidos?**

O Top 5 IDEs utilizadas são:

- Visual Studio Code: 71,53%
- Visual Studio: 27,59%
- IntelliJ IDEA: 26,02%
- Notepad++: 23,82%
- Vim: 21,63%

![Distribuição por Editor de código](/assets/Distribuição_por_Editor_de_código.png)

#### **Qual a média de salário por linguagem?**

O Top 5 salários médios por linguagem é:

- Cobol: R$71764,05
- Swift: R$60423,42
- Delphi: R$37991,44
- Ruby: R$31195,56
- Java: R$29357,56

![Salário Médio por linguagem](/assets/Salário_Médio_por_linguagem.png)

#### **Qual a média de salário por framework?**

O Top 5 frameworks em salário médio são:

- Phoenix: R$44637,83
- AngularJS: R$38734,50
- ASP.NET: R$38192,90
- WordPress: R$33270,67
- jQuery: R$32457,94

![Salário Médio por framework](/assets/Salário_Médio_por_framework.png)
