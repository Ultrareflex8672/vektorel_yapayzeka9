# belli kritere uyan kayıtlar DEĞİŞKEN ile
import mysql.connector

xxx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="deneme1"
)

secilen = xxx.cursor()

sql = "SELECT * FROM ogretmen" 

secilen.execute(sql)
okunan = secilen.fetchall()

for x in okunan:
  print(x)
