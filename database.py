import pymysql
from pymysql.cursors import DictCursor

def savedata(val1,val2):

	connection = pymysql.connect(
    		host='localhost',
		user='bot',
		password='testbot!54',
   		db='Databasebot',
    		charset='utf8mb4',
)
	mycursor = connection.cursor()

	sql = "INSERT INTO Save (UserID, PathToSound) VALUES (%s, %s)"
	val = (val1,val2)
	mycursor.execute(sql, val)

	connection.commit()
	connection.close()



