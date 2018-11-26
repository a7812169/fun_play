from app import get_connection
import datetime
import random
def get_all_news():
	conn = get_connection()
	cur = conn.cursor()
	sql = 'select * from article'
	data=[]
	content={}
	try:
		cur.execute(sql)
		res=cur.fetchall()
		for i in res:
			content={"id":i[0],"title":i[1],"url_address":i[2],"content":i[3],"collection":i[4]}
			data.append(content)
	except Exception as e:
		conn.rollback()
	finally:
		conn.close()
		cur.close()
	return data
def get_top10_funplay():
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
def get_new_by_type(type):
	conn = get_connection()
	cur = conn.cursor()
	sql='select * from article where tag_id={}'.format(type)
	cur.execute(sql)
	res = cur.fetchall()
	data = []
	for i in res:
		content = {"id": i[0], "title": i[1], "url_address": i[2], "content": i[3], "collection": i[5]}
		data.append(content)
	return data
def get_order(name):
	conn = get_connection()
	cur = conn.cursor()
	sql = 'select * from amusement_project where name=%s'
	time_list = []
	cur.execute(sql,name)
	res = cur.fetchone()
	print(res)
	time=res[2]
	max_man=res[6]
	for i in range(1,5):
		wait_people=random.randint(1,max_man)
		content={"back_time":back_time(time,i),"wait_people":wait_people}
		time_list.append(content)
	conn.close()
	cur.close()
	this_data={"id":res[0],"name":res[1],"back_time":time_list}
	return this_data
def back_time(time,num):
	the_time=(datetime.datetime.now() + datetime.timedelta(minutes=int(time)*num)).strftime('%H:%M')
	return the_time
