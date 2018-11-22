from app import get_connection

def get_all_news():
	conn = None
	cur = None
	conn = get_connection()
	cur = conn.cursor()
	sql = 'select * from article'
	data=[]
	content={}
	try:
		cur.execute(sql)
		res=cur.fetchall()
		for i in res:
			print(i)
			content={"id":i[0],"title":i[1],"url_address":i[2],"content":i[3]}
			data.append(content)
	except Exception as e:
		conn.rollback()
	finally:
		conn.close()
		cur.close()
	return data




