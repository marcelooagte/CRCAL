# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:50:19 2023
Checar dois documentos em pdf os quais possuem listas de cpf (contadores que deram baixa e contadores em atividade), e caso de estes possuam o mesmo cpf nas duas planilhas, retornar os CPFs que foram localizados. 

realizar procedimentos abaixo :


@author: Marcelo Oliveira
"""

import PyPDF4
import re

mascaraCpf=r'\d{3}\.\d{3}\.\d{3}-\d{2}'; 

#------------------------------------------------------------------------------------------------------------------]
print('Primeira parte:')
cpfs_encontrados = [];


#LINK DO PRIMEIRO ARQUIVO 
pdf_file = open("C:/Users/SUPORTE/Desktop/CRCAL/Programação/Cristiano - 04.09.2023/documentos/BAIXADOS_2020_A_2023-assinado.pdf","rb")

pdf = PyPDF4.PdfFileReader(pdf_file)
#extrair conteudo do pdf: 

#lê a primeira página completa
for c in range(pdf.getNumPages()):
    page = pdf.getPage(c)
    
    #extrai apenas o texto
    texto_da_pagina = page.extractText()
    
    #tirar espaços e quebras
    texto_da_pagina = re.sub(r'\s', '', texto_da_pagina)
   

    cpfs = re.findall(mascaraCpf, texto_da_pagina)
    cpfs_encontrados.extend(cpfs)


#array cpfs_encontrados carregado

print('Fim primeira parte')
#------------------------------------------------------------------------------------------------------------------

print('Segunda parte:')
cpfs_encontrados2 = [];


#LINK DO SEGUNDO ARQUIVO 
pdf_file2 = open("C:/Users/SUPORTE/Desktop/CRCAL/Programação/Cristiano - 04.09.2023/documentos/Maceio-fiscalizacao.pdf","rb")
pdf2 = PyPDF4.PdfFileReader(pdf_file2)


#lê página por página
for d in range(pdf2.getNumPages()):
    page2 = pdf2.getPage(d)    
            
    #extrai apenas o texto
    texto_da_pagina2 = page2.extractText() 
    texto_da_pagina2 = re.sub(r'\s', '', texto_da_pagina2)
    cpfs2 = re.findall(mascaraCpf, texto_da_pagina2)
    cpfs_encontrados2.extend(cpfs2)
   
print('Fim Segunda parte:')
#------------------------------------------------------------------------------------------------------------------

#sem elementos duplicados 
primeiro_conjunto = set(cpfs_encontrados);
segundo_conjunto = set(cpfs_encontrados2);


#Interseção
valores_comuns = primeiro_conjunto.intersection(segundo_conjunto)

array_final = list(valores_comuns)

# Imprimir o Array 
print(array_final)















