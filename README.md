# Documentação 

O objetivo do projeto é fazer a automação de download das planilhas de furto de veiculos do [Portal de Transparência do SSP SP](https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx), através de um script em python.

---

### Tecnologias usadas
O projeto foi inteiramente desenvolvido na linguagem de programação python, fazendo uso das IDEs [Visual Studio Code](https://code.visualstudio.com) e [Replit](https://replit.com), e, do gerenciador de pacotes [Anaconda](https://www.anaconda.com). As bibliotecas em python usadas foram Selenium, Webdriver-Manager, Pandas, time e OS. O navegador utilizado na executação do código é o Google Chrome.

---

### Dependências
- [Google Chrome](https://www.google.pt/intl/pt-PT/chrome/?brand=FHFK&gclid=EAIaIQobChMI4rmvs8_GggMVjF9IAB3MZAplEAAYASAAEgIHdvD_BwE&gclsrc=aw.ds)
- [selenium 4.14](https://pypi.org/project/selenium/4.14.0/)
- [webdriver-manager 4.0.1](https://pypi.org/project/webdriver-manager/4.0.1/)
- [pandas 2.1.1](https://pypi.org/project/pandas/2.1.1/)

---

### Scripts
O repositório apresenta dois arquivos python, o arquivo "main.py", e, o arquivo "aps.py".

#### main.py
quando executado, pergunta os anos e meses das tabelas que deseja e realiza o download

##### funções:
- criar_pastas() - Cria os diretórios onde as planilhas serão armazenadas.
- deletar_tabelas() - Deleta tabelas baixadas e criadas no processamento anterior.
- iniciar_navegador() - Esta função inicia o Chrome no site do SSP SP em segundo plano e retorna o driver, que será utilizado para controlar o navegador.
- clicar_ano(ano: int, driver) - Recebe de parâmetros o ano da tabela e o driver do navegador. A função realiza o clique na aba que apresenta os dados do ano escolhido.
- clicar_mes(mes: int, driver) - Recebe de parâmetros o mês da tabela e o driver do navegador. A função realiza o clique na aba que apresenta os dados do mês escolhido.
- baixar(driver) - Recebe de parâmetro o driver do navegador. Realiza o download da tabela no diretório "./tabelas/xls/".
- atapa_baixar_tabelas(anos: list, meses: list) - Recebe de parâmetros as listas dos anos e meses das tabelas. Faz o download de todas as tabelas escolhidas automaticamente.
- etapa_converter_tabelas() - Faz a conversão de todas as tabelas de extenção .xls para arquivos .csv, que podem ser encontrados no diretório "./tabelas/csv/".
- etapa_juntar_tabelas(anos: list) - Recebe de parâmetro a lista dos anos das tabelas. Esta função junta os dados das tabelas dos meses em uma tabela de seus respectivos anos, que podem ser encontradas em "./tabelas/final".
- iniciar(anos: list, meses: list) - Recebe de parâmetros as listas dos anos e meses das tabelas. Esta função organiza e executa todos as funções em ordem que devem ser executadas para o funcionamento do script.

##### variáveis globais:
- id_ano - É um dicionário que relaciona o ano da tabela com o atributo id dos botões que permitem acessar as informações das tabelas de cada ano no site do SSP SP.
- id_mes - É uma lista que apresenta os atributos id dos botões que permitem acessar as informações de cada mês no site do SSP SP.
- diretorio_atual - Armazena o diretório em que o código está sendo executado

#### aps.py
Este arquivo importa as funções e variáveis de main.py, e, quando executado, realiza o download apenas das tabelas pedidas no documento de orientação da APS
