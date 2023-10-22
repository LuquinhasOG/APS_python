from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd, mkdir
from os.path import exists
from time import sleep

id_ano = {
    "2003": "cphBody_lkAno3",
    "2004": "cphBody_lkAno4",
    "2005": "cphBody_lkAno5",
    "2006": "cphBody_lkAno6",
    "2007": "cphBody_lkAno7",
    "2008": "cphBody_lkAno8",
    "2009": "cphBody_lkAno9",
    "2010": "cphBody_lkAno10",
    "2011": "cphBody_lkAno11",
    "2012": "cphBody_lkAno12",
    "2013": "cphBody_lkAno13",
    "2014": "cphBody_lkAno14",
    "2015": "cphBody_lkAno15",
    "2016": "cphBody_lkAno16",
    "2017": "cphBody_lkAno17",
    "2018": "cphBody_lkAno18",
    "2019": "cphBody_lkAno19",
    "2020": "cphBody_lkAno20",
    "2021": "cphBody_lkAno21",
    "2022": "cphBody_lkAno22"
}
id_mes = ["cphBody_lkMes1", "cphBody_lkMes2", "cphBody_lkMes3", "cphBody_lkMes4", "cphBody_lkMes5", "cphBody_lkMes6", "cphBody_lkMes7", "cphBody_lkMes8", "cphBody_lkMes9", "cphBody_lkMes10", "cphBody_lkMes11", "cphBody_lkMes12", ]
diretorio_atual = getcwd()

def criar_pastas():
    if(not exists(diretorio_atual+"/tabelas/xls") or not exists(diretorio_atual+"/tabelas/csv")):
        mkdir(diretorio_atual+"/tabelas")
        mkdir(diretorio_atual+"/tabelas/xls")
        mkdir(diretorio_atual+"/tabelas/csv")

def iniciar_navegador():
    print("Abrindo o navegador")
    configuracoes_nav = Options()
    configuracoes_nav.add_argument("--headless=new")
    configuracoes_nav.add_experimental_option("detach", True)
    configuracoes_nav.add_experimental_option("prefs", {"download.default_directory": diretorio_atual + "\\tabelas\\xls"})

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=configuracoes_nav)
    print("Acessando portal de transparência")
    driver.get("https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx")
    driver.find_element(By.ID, "cphBody_btnFurtoVeiculo").click()
    return driver

def clicar_ano(ano, driver):
    print(f"Acessando dados do ano {ano}")
    driver.find_element(By.ID, id_ano[str(ano)]).click()
    sleep(1)

def clicar_mes(mes, driver):
    print(f"Acessando dados do mês {mes}")
    driver.find_element(By.ID, id_mes[int(mes)-1]).click()
    sleep(1)

def baixar(driver):
    print("Baixando a tabela")
    driver.find_element(By.ID, "cphBody_ExportarBOLink").click()
    print("Tabela baixada com sucesso!\n")
    sleep(3)

def etapa_baixar_tabelas(anos, meses):
    navegador = iniciar_navegador()

    for ano in anos:
        clicar_ano(ano, navegador)
        for mes in meses:
            clicar_mes(mes, navegador)
            baixar(navegador)

    navegador.close()
    print("Navegador fechado\n")

def converter_xls_para_csv(ano, mes):
    print(f"Convertendo DadosBO_{ano}_{mes}(FURTO DE VEÍCULOS).xls para .csv")
    arquivo = open(diretorio_atual + f"/tabelas/xls/DadosBO_{ano}_{mes}(FURTO DE VEÍCULOS).xls", "r", errors="ignore")
    convertido = open(diretorio_atual + f"/tabelas/csv/furto_de_veiculos_{ano}_{mes}.csv", "w", encoding='utf_8')
    while True:
        linha_lida = arquivo.readline().replace("\x00", "").replace("ÿþ", "").replace("\t", ",")
        if not linha_lida:
            break

        convertido.write(linha_lida)

    arquivo.close()
    convertido.close()
    print("Tabela convertida com sucesso!\n")
    sleep(2)

def etapa_converter_tabelas(anos, meses):
    for ano in anos:
        for mes in meses:
            converter_xls_para_csv(ano, mes)

if __name__ == "__main__":
    criar_pastas()

    print("Digite os anos das tabelas que quer baixar:",end=' ')
    anos_selecionados = [i for i in input().split()]
    print("Digite os meses das tabelas que quer baixar:",end=' ')
    meses_selecionados = [i for i in input().split()]

    etapa_baixar_tabelas(anos_selecionados, meses_selecionados)
    etapa_converter_tabelas(anos_selecionados, meses_selecionados)

    print("Fim da execução!")