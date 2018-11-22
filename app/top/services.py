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
def get_top10_funplay():
	conn = None
	cur = None
	conn = get_connection()
	cur = conn.cursor()
	sql='select id,rank,name,pic_url from amusement_project order by rank DESC '
	cur.execute(sql)
	res=cur.fetchall()
	data=[]
	for i in res:
		content={"id":i[0],"rank":i[1],"name":i[2],"pic_url":i[3]}
		data.append(content)
	return data

