import mysql.connector
import database_info

db = mysql.connector.connect(
    host=database_info.host,
    port=database_info.port,#Который указывали при установке
    user=database_info.user,
    password=database_info.password,#Пароль который указывали при установке
    database = database_info.database #Название которое сделали в sql workbench
)

db.autocommit = True #Свойство автоотправки запросов insert
cursor = db.cursor() #С помощью этой переменной будем делать запросы к бд

#Получить 1 запись по id
def get_one_by_id(table:str,id:int):
    query = f'''SELECT * FROM {table} WHERE id = {id}'''
    cursor.execute(query)
    record = cursor.fetchone() #Получение результатов запроса
    return record

#Сохранить 1 запись
def save_one(table:str,record:str,values:str):
    query = f'''INSERT INTO {table}({record}) VALUES({values})'''
    cursor.execute(query)
#Удалить 1 запись по id
def delete_one_by_id(table:str,id:int):
    query = f'''DELETE FROM {table} WHERE id = {id}'''
    cursor.execute(query)

# cursor.execute('SELECT * FROM users;') #Сам запрос
# result = cursor.fetchone() #Обработка запроса
# print(result)
