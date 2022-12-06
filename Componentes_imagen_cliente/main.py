import pyorient
import os

#PASO 1: CONEXIÓN A LA BASE DE DATOS
print("connection to the server...")
client=pyorient.OrientDB("orientdb",2424)	#Inicialización del cliente, 'orientdb' 
#indica el conetenedor de la base de datos y 2424 es el puerto binario al que se accede
client.set_session_token(True)		
session_id=client.connect("root","password") #Conexión a la base de datos
print("OK - sessionID: ",session_id,"\n")


#PASO 2: CREACIÓN O ACCESO A LA BASE DE DATOS 'capitals'

db_name='capitals' #Nombre de la base de datos

if client.db_exists(db_name): #Si la base de datos 'capitals' ya existe
   print("Database already exist. Opening ", db_name, " database")
   client.db_open( db_name, "root", "password" ) #Se conecta a la base de datos
   
else: #Si la base de datos 'capitals' no existe
   print("Creating database", db_name)
   client.db_create(
      db_name,
      pyorient.DB_TYPE_GRAPH,
      pyorient.STORAGE_TYPE_PLOCAL) #Creamos la base de datos 'capitals'

   cluster_id = client.command( "create class capitals" ) #Creamos clase 'capitals'
   #Definimos 'country' como un atributo que tiene formato String
   cluster_id = client.command( "create property capitals.country String" ) 
   #Definimos 'city' como otro atributo que tiene formato String
   cluster_id = client.command( "create property capitals.city String" ) 
   
   #Lista de datos a introducir en la base de datos 'capitals'
   countryCity = [('Warsaw','Poland'),('Madrid','Spain'),('Bucharest','Romania'),('Berlin','Germany'),('Rome','Italy')] 
   
   for data in countryCity: #Para cada posición en la lista de datos
       #Insertamos los datos en la base de datos 'capitals'
      comando = "INSERT INTO capitals (country, city) VALUES ('" + data[0] + "','" + data[1] + "')"
      client.command(comando)
      linea = 'City:' + data[0] + ', Country:' + data[1] + '\n' #Creación de un String con los datos
      with open('/db/data.txt', 'a') as the_file: #Escritura de los datos en un arichivo .txt
         the_file.write(linea)

client.db_close() #Cierre de la base de datos 'capitals'


