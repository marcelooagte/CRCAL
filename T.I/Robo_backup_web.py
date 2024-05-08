#Robô criado para fazer login no sistema de backup e executar a rotina de backup. Após a geração do arquivo, ele será baixado em seguida. O serviço é realizado diariamente.
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime

# Função para extrair a data de um nome de arquivo
def extrair_data(nome_arquivo):
    partes = nome_arquivo.split('_')
    if len(partes) >= 3:
        return partes[1]
    return None

# Inicializa o navegador Chrome
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Insira o caminho para o chrome.exe em seu sistema
browser = webdriver.Chrome(options=options)

# URL da página
url = 'https://web.crcal.org.br/spw/ListarBackup/Index.aspx'
browser.get(url)

# Aguarda até que os campos de usuário e senha estejam presentes
wait = WebDriverWait(browser, 10)
usuario_field = wait.until(EC.presence_of_element_located((By.ID, 'MainContent_ASPxRoundPanel1_txtUsuario_I')))
senha_field = wait.until(EC.presence_of_element_located((By.ID, 'MainContent_ASPxRoundPanel1_txtSenha_I')))

# Preenche os campos de usuário e senha
usuario_field.send_keys('*******')
senha_field.send_keys('*******')

# Clica no botão "Entrar"
entrar_button = wait.until(EC.element_to_be_clickable((By.ID, 'MainContent_ASPxRoundPanel1_btnEntrar')))
entrar_button.click()

# Espera um pouco para a página carregar completamente
time.sleep(5)

# Clicar no botão "Executar Backup"
executar_backup_button = wait.until(EC.element_to_be_clickable((By.ID, 'MainContent_btnExecutarBackup')))
executar_backup_button.click()

# Espera até que o arquivo seja gerado 
time.sleep(3600)  

# Extrai a data atual
data_atual = datetime.datetime.now().strftime('%d-%m-%Y')

# Coleta todos os links na página
links = browser.find_elements(By.XPATH, "//a[contains(@class, 'dxbButton dxbButtonSys')]")

# Itera sobre os links para encontrar o link com a data atual
link_encontrado = None
for link in links:
    nome_arquivo = link.text
    if data_atual in nome_arquivo:
        link_encontrado = link
        break

# Se um link com a data atual for encontrado, clicar nele
if link_encontrado:
    link_encontrado.click()
else:
    print("Nenhum arquivo encontrado com a data de hoje.")


# Espera até que o arquivo seja Baixado
time.sleep(3600)  

# Fecha o navegador
browser.quit()