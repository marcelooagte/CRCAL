#Robô para compactar os arquivos .bak, que são os arquivos de backup gerados diariamente. Após a compactação dos arquivos gerados, os arquivos .baks são excluídos.  

import os
import subprocess
import datetime

# Caminho da unidade mapeada
unidade_w = 'W:\\'

# Obter a data 
data_atual = datetime.datetime.now().strftime('%Y%m%d')

# Nome do arquivo .rar a ser criado
nome_arquivo_rar = f"{data_atual}.rar"
caminho_arquivo_rar = os.path.join(unidade_w, nome_arquivo_rar)

# Criação de uma lista para armazenar os arquivos .bak
arquivos_bak = []

# Percorrer todos os arquivos na unidade mapeada
for root, dirs, files in os.walk(unidade_w):
    for file in files:
        if file.endswith('.bak'):
            caminho_completo_arquivo = os.path.join(root, file)
            arquivos_bak.append(caminho_completo_arquivo)

# Verificar se há arquivos .bak para compactar
if arquivos_bak:
    # Caminho completo para o rar.exe
    caminho_rar = r"C:\Program Files\WinRAR\rar.exe"
    comando = [caminho_rar, 'a', caminho_arquivo_rar] + arquivos_bak
    subprocess.run(comando, check=True)

    # Remover os arquivos .bak após a compactação
    for arquivo in arquivos_bak:
        os.remove(arquivo)

    print(f"Arquivos .bak compactados em {nome_arquivo_rar} e removidos.")
else:
    print("Nenhum arquivo .bak encontrado para compactar.")
