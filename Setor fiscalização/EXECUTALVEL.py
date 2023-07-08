# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:07:39 2023

Descrição: 

Sistema para ajudar no setor de fiscalização do CRCAL, por meio do cruzamento de planilhas, relacionando as pessoas que passaram no exame do CFC com as pessoas que trabalham na área de contabilidade, com o objetivo de identificar quem foi aprovado e mesmo assim está trabalhando na área sem o registro.

@author: Marcelo T.I 
"""
#importação da biblioteca pandas, a qual permite trabalhar com planilhas em excel
import pandas as pd 
#baixando as planilhas para o sistema  
df_01 = pd.read_excel('PLANILHA_ANALISE/PLANILHAS_RAIS.CAGED/AL_BAIX_SUSP_REPETIDOS.xlsx');
df_02 = pd.read_excel('PLANILHA_ANALISE/PLANILHAS_RAIS.CAGED/AL_BAIXADOS_SUSPENSOS_NOVOS.xlsx');
df_03 = pd.read_excel('PLANILHA_ANALISE/PLANILHAS_RAIS.CAGED/AL_NAOREGISTRADOS_NOVOS.xlsx');
df_04 = pd.read_excel('PLANILHA_ANALISE/PLANILHAS_RAIS.CAGED/AL_NAOREGISTRADOS_REPETIDOS_PF.xlsx');

#pegando as colunas em comum existentes nas planilhas armazenadas 
df_selecao_01 = df_01[['CPF','Nome Trabalhador','CNPJ Trabalho','Razao Social/Nome Fantasia','CBO','Descricao CBO','Data Admissao','CNAE','Descricao CNAE','Logradouro','Tipo_Logradouro','Numero','Complemento','CEP','Bairro','UF','Email','DDD1','Telefone1']]
df_selecao_02 = df_02[['CPF','Nome Trabalhador','CNPJ Trabalho','Razao Social/Nome Fantasia','CBO','Descricao CBO','Data Admissao','CNAE','Descricao CNAE','Logradouro','Tipo_Logradouro','Numero','Complemento','CEP','Bairro','UF','Email','DDD1','Telefone1']]
df_selecao_03 = df_03[['CPF','Nome Trabalhador','CNPJ Trabalho','Razao Social/Nome Fantasia','CBO','Descricao CBO','Data Admissao','CNAE','Descricao CNAE','Logradouro','Tipo_Logradouro','Numero','Complemento','CEP','Bairro','UF','Email','DDD1','Telefone1']]
df_selecao_04 = df_04[['CPF','Nome Trabalhador','CNPJ Trabalho','Razao Social/Nome Fantasia','CBO','Descricao CBO','Data Admissao','CNAE','Descricao CNAE','Logradouro','Tipo_Logradouro','Numero','Complemento','CEP','Bairro','UF','Email','DDD1','Telefone1']]

#concatenado as planilhas
df_concatenacao = pd.concat([df_selecao_01, df_selecao_02,df_selecao_03, df_selecao_04], ignore_index=True)

#transformar números em strings( texto e não número) 
df_concatenacao['CPF'] = df_concatenacao['CPF'].astype(str) 
df_concatenacao['CNPJ Trabalho'] = df_concatenacao['CNPJ Trabalho'].astype(str)

#Colocando zeros a esquerda para o cpf ter 11 numeros 
df_concatenacao['CPF'] = df_concatenacao['CPF'].apply(lambda x: x.zfill(11))

#Colocando traços e pontos:
df_concatenacao['CPF'] = df_concatenacao['CPF'].apply(lambda x: f'{x[:3]}.{x[3:6]}.{x[6:9]}-{x[9:11]}');

#Exportando planilha juntadas 
novaplanilha = df_concatenacao.to_excel('PLANILHA_ANALISE/PLANILHAS_RAIS.CAGED/PLANILHAS_RAIS.CAGED_JUNTADAS/COMBINADAS.xlsx')


#leitura da planilha aprovados e da combinada 
df_combinada = pd.read_excel('PLANILHA_ANALISE/PLANILHAS_RAIS.CAGED/PLANILHAS_RAIS.CAGED_JUNTADAS/COMBINADAS.xlsx');
df_avaliar = pd.read_excel('PLANILHA_ANALISE/APROVADOS/APROVADOS_2022.xlsx');

#comparação do cpf: 
cpf_comum = pd.merge(df_combinada, df_avaliar, on='CPF', how='inner')

final = cpf_comum.to_excel('PLANILHA_ANALISE/RESULTADO/resultado_final.xlsx')


print("Planilha gerada com sucesso!")