import zsbot
import db_input




global_url_subcat = zsbot.get_subcat()
global_url_dentro_subcat = zsbot.get_value_dentro_subcat()
global_url_nome_preco = zsbot.get_value_nome_preco()

db_input.populating_db(global_url_nome_preco)
