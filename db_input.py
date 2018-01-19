import mysql.connector
import zsbot

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

def populating_db (vetor):
    day = input('What DAY is today? (Use two digits / Example: 01 - 09 - 12) ')
    month = input('What MONTH are we? (Use two digits / Example: 01 - 09 - 12) ')
    j=''
    for i in vetor:
        j = ' '.join(i)
        insert_db(j,day,month)
    print('Congratulations! You got all data from Zona Sul. And dont forget, WACKEN RULES!')


#calling the populating_db function with the vector created at the zsbot2file (the final vector with all the info about products and prices)
