#Retornar as URLs de (Subcategoria) - nivel 2, que estão dentro da (Categoria) Home page - nivel 1

import urllib.request
import re


def get_subcat():
	urlhome = 'https://www.zonasul.com.br/'
	sourcecode = urllib.request.urlopen(urlhome)
	strsourcecode = str(sourcecode.read())
	re_get_subcat_url =  re.compile('_linkMenuPrincipal" href=".*?"')
	subcat_url = re_get_subcat_url.findall(strsourcecode)
	url_subcat = []
	for i in subcat_url:
		temp_url = i.split('href="')[1][1:-1]
		url_subcat.append('https://www.zonasul.com.br/'+temp_url)
	return url_subcat


global_url_subcat = get_subcat()



#Funcao recebe como input um vetor com todas as URLs da home page (nivel 1) e retorna um vetor com todas as URLs da subcategoria (nivel 2)
def get_dentro_subcat(string):
	urlsubcat = string
	sourcecode = urllib.request.urlopen(urlsubcat)
	strsourcecode = str(sourcecode.read())
	re_get_dentro_subcat_url =  re.compile('_lnkSubsecao" href=".*?"')
	dentro_subcat_url = re_get_dentro_subcat_url.findall(strsourcecode)
	url_dentro_subcat = []
	for i in dentro_subcat_url:
		temp_url = i.split('href="')[1][1:-1]
		url_dentro_subcat.append('https://www.zonasul.com.br/'+temp_url)
	return url_dentro_subcat

#Funcao chama a funcao acima (get_dentro_subcat(string)) e organiza/limpa o vetor de URLs de subcategoria gerado na funcao (get_dentro_subcat(string)).
#Output desta funcao é um vetor com todas as URLs das subcategorias limpo e organizado
def get_value_dentro_subcat():
	temp_dentro_subcat = []
	url_dentro_subcat_final = []
	for i in global_url_subcat:
		temp_dentro_subcat.append(get_dentro_subcat(i))
	for i in temp_dentro_subcat: #daqui em diante ele tira os valores do vetor para colocar em um único
		for j in i:
			url_dentro_subcat_final.append(j)
	return url_dentro_subcat_final


global_url_dentro_subcat = get_value_dentro_subcat()




#Funcao recebe como input um vetor com todas as URLs da de subcategoria (nivel 2) e retorna um vetor com todas as URLs da dentro_subcategoria (nivel 3)
def get_nome_preco(string):
	vetorlimpo = []
	temp_vetor = []
	f_vetor = []
	final_vetor = []
	url_nome_preco = string
	sourcecode = urllib.request.urlopen(url_nome_preco)
	strsourcecode = str(sourcecode.read())
	re_get_nome_preco =  re.compile('title=".*?"|R[$] [0-9],[0-9][0-9]|R[$] [0-9][0-9],[0-9][0-9]')
	title = re_get_nome_preco.findall(strsourcecode)
	for i in title:
		if i not in vetorlimpo:
			vetorlimpo.append(i)
	for i in vetorlimpo:
		temp_vetor.append(i.replace('title="', 'R$ '))
	for i in temp_vetor:
		f_vetor.append(i.replace('R$ ',''))
	for i in f_vetor:
		final_vetor.append(i.replace('"',''))
	return final_vetor

#Funcao chama a funcao acima (get_nome_preco(string)) e organiza/limpa o vetor de URLs de dentro_subcategoria gerado na funcao (get_nome_preco(string)).
#Output desta funcao é um vetor com todas os nomes e precos dos produtos
def get_value_nome_preco():
	temp_nome_preco = []
	url_nome_preco_final = []
	for i in global_url_dentro_subcat:
		temp_nome_preco.append(get_nome_preco(i))# PEGAR DAQUI
	return temp_nome_preco



global_url_nome_preco = get_value_nome_preco()
