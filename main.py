# começo imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
from time import sleep
# fim imports

id_botao_ano = {
    '2003': 'cphBody_lkAno3',
    '2004': 'cphBody_lkAno4',
    '2005': 'cphBody_lkAno5',
    '2006': 'cphBody_lkAno6',
    '2007': 'cphBody_lkAno7',
    '2008': 'cphBody_lkAno8',
    '2009': 'cphBody_lkAno9',
    '2010': 'cphBody_lkAno10',
    '2011': 'cphBody_lkAno11',
    '2012': 'cphBody_lkAno12',
    '2013': 'cphBody_lkAno13',
    '2014': 'cphBody_lkAno14',
    '2015': 'cphBody_lkAno15',
    '2016': 'cphBody_lkAno16',
    '2017': 'cphBody_lkAno17',
    '2018': 'cphBody_lkAno18',
    '2019': 'cphBody_lkAno19',
    '2020': 'cphBody_lkAno20',
    '2021': 'cphBody_lkAno21',
    '2022': 'cphBody_lkAno22'
}
id_botao_mes = ['cphBody_lkMes1','cphBody_lkMes2','cphBody_lkMes3','cphBody_lkMes4','cphBody_lkMes5','cphBody_lkMes6','cphBody_lkMes7','cphBody_lkMes8','cphBody_lkMes9','cphBody_lkMes10','cphBody_lkMes11','cphBody_lkMes12']

# começo declaração de funções
def abrir_navegador():
    opcoes = Options()
    opcoes.add_argument("--headless=new")
    opcoes.add_experimental_option('detach', True)
    opcoes.add_experimental_option('prefs', {'download.default_directory': getcwd() + '\\tabelas\\xls'}) # local de download das tabelas

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opcoes)
    driver.get('https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx')

    driver.find_element(By.ID, "cphBody_btnFurtoVeiculo").click()

    return driver

def clicar_mes(driver, mes: int):
    driver.find_element(By.ID, id_botao_mes[int(mes)-1]).click()

def clicar_ano(driver, ano: str):
    driver.find_element(By.ID, id_botao_ano[str(ano)]).click()

def baixar(driver):
    driver.find_element(By.ID, 'cphBody_ExportarBOLink').click()

def iniciar(driver):
    for i in anos_selecionados:
        sleep(1)
        print(f'Acessando dados do ano {i}')
        clicar_ano(driver, i)

        for j in meses_selecionados:
            sleep(2)
            print(f'Acessando dados do mes {j}')
            clicar_mes(driver, j)
            print(f'Baixando tabela {j}/{i}')
            baixar(driver)
            print(f'Tabela {j}/{i} baixada com sucesso! \n')
            sleep(2)
# fim declaração de funções

# começo da execução do código
if __name__ == '__main__':
    print("Digite os anos que deseja baixar os dados:", end=' ')
    anos_selecionados = input().split()
    print("Digite os meses que deseja baixar os dados:", end=' ')
    meses_selecionados = input().split()
    print()

    print('Abrindo navegador')
    navegador = abrir_navegador()

    iniciar(navegador)

    sleep(5)
    print('Fim!')

# fim da execução do código