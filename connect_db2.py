import mysql.connector
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': '8889',
  'database': 'Test_DB',
  'raise_on_warnings': True,
}

def insert_db (nome, preco_de, preco_por):
	link = mysql.connector.connect(**config)
	insert_query = ("INSERT INTO page_data (page_name,page_title,page_description) VALUES (%s,%s,%s)")
	page_name = nome
	page_title = preco_de
	page_description = preco_por
	empname = (page_name,page_title,page_description)
	cursor = link.cursor()
	cursor.execute(insert_query,empname)
	link.commit()
	cursor.close()
	link.close()

insert_db ('novo','teste','run')
#for que chama a funcao acima e passa como input cada valor do vetor

#test_vect = ['jabba','test','vect']

#insert_db('aula','2,99','chata demais')

vetor_test = [['jabba','1','a'],['joe','2','b'],['joseph','3','c']]
vetor_teste_zs = ['', 'P\\xc3\\xa1gina inicial Zona Sul', 'Manteiga com Sal Itamb\\xc3\\xa9 Tablete  200 g ', '9,79', 'Manteiga com Sal Eleg\\xc3\\xaa Tablete  200 g ', '8,90', 'Manteiga com Sal Avia\\xc3\\xa7\\xc3\\xa3o Tablete  200 g ', '11,49', 'Manteiga sem Sal Itamb\\xc3\\xa9 Tablete  200 g ', 'Manteiga com Sal Boa Nata Pote  200 g ', '10,98', 'Manteiga com Sal Da Matina   Caixa 200 g ', '8,99', '7,79', 'Manteiga com Sal Pr\\xc3\\xa9sident Tablete  199 g', '13,99', 'Manteiga sem Sal Eleg\\xc3\\xaa Tablete  200 g ', 'Manteiga com Sal Itamb\\xc3\\xa9 Pote  500 g ', '22,90', 'Manteiga sem Sal Avia\\xc3\\xa7\\xc3\\xa3o Tablete  200 g ', 'Manteiga com Sal Pr\\xc3\\xa9sident La Motte Pote  250 g', '19,90', 'Manteiga sem Sal Da Matina   Caixa 200 g ', 'Manteiga com Sal Avia\\xc3\\xa7\\xc3\\xa3o Lata  200 g ', '12,99', 'Manteiga sem Sal Pr\\xc3\\xa9sident Tablete  199 g', 'Manteiga com Sal Gran Mestri  Lata 200 g ', '14,90', 'Zona Sul']

j = 0
for i in temp_nome_preco:
    j = j+3
    if j < len(i):
        insert_db(i[j],i[j+1],i[j+2])





for i in temp_nome_preco:
    #desmontar o vetor i e colocar dentro de uma string - adicionar essa string no db
    insert_db(i,'26','09/2017')

for i in vetor_test:
    insert_db(i[0],i[1],i[2])
