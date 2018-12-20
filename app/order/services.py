from app import get_connection
import datetime
import random
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
def get_order(name):
	conn = get_connection()
	cur = conn.cursor()
	sql = 'select * from amusement_project where name=%s'
	time_list = []
	cur.execute(sql,name)
	res = cur.fetchall()
	time=res[2]
	max_man=res[6]
	for i in range(1,5):
		wait_people=random.randint(1,max_man)
		content={"back_time":back_time(time,i)}
		time_list.append(content)
	conn.close()
	cur.close()
	this_data={"id":res[0],"name":res[1],"back_time":time_list}
	return this_data
def back_time(time,num):
	the_time=(datetime.datetime.now() + datetime.timedelta(minutes=int(time)*num)).strftime('%H:%M')
	return the_time
