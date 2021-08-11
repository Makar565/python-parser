#!/usr/bin/env python3
import vk_api
import time
import datetime
login="login"
password="password"
vk_session = vk_api.VkApi(login,password)

import sys
n =int( sys.argv[1])
method=int(sys.argv[2])
url=sys.argv[3]
id_group=url.replace("https://vk.com/","")
try:
	
	vk_session.auth(token_only=True)
	vk = vk_session.get_api()
	vk.account.getAppPermissions()

	info_members=vk.groups.getMembers(group_id=id_group,count=1)
	info_group=vk.groups.getById(group_id=id_group)
	gr_id=info_group[0]["id"]
	wall_get_gr=vk.wall.get(owner_id="-"+str(gr_id),domain=url,count=n,filter="owner")
	count_members=info_members["count"]
	sum_views=0
	sum_likes=0
	pop=0
	nopop=0
	count_likes=wall_get_gr["items"][0]["likes"]["count"]
	count_views=wall_get_gr["items"][0]["views"]["count"]
	count_reposts=wall_get_gr["items"][0]["reposts"]["count"]
	pop_count=int(count_views)+int(count_likes)+int(count_reposts)
	nopop_count=pop_count
	sum_act=0
	if(method==0):
		print(count_members)
	if(method==1):
		for i in range(n):
			count_views=wall_get_gr["items"][i]["views"]["count"]
			sum_views+=int(count_views)
			
		ratio_mem_views=count_members//(sum_views//n)#отношение кол.подписчиков к ср.кол.просмотров
		print(ratio_mem_views)
	if(method==2):
		for i in range(n):
			count_likes=wall_get_gr["items"][i]["likes"]["count"]
			count_views=wall_get_gr["items"][i]["views"]["count"]
			count_reposts=wall_get_gr["items"][i]["reposts"]["count"]
			sum_act+=int(count_views)+int(count_likes)+int(count_reposts)
			sum_views+=int(count_views)
		col_act_mem=count_members//(sum_views//(3*n))
		print(col_act_mem)
	if(method==3):
		for i in range(n):
			count_likes=wall_get_gr["items"][i]["likes"]["count"]
			count_views=wall_get_gr["items"][i]["views"]["count"]
			count_reposts=wall_get_gr["items"][i]["reposts"]["count"]
			sum_views+=int(count_views)
			sum_likes+=int(count_likes)
		print(sum_views,sum_likes)
	if(method==4):
		for i in range(n):
			count_likes=wall_get_gr["items"][i]["likes"]["count"]
			
			
			sum_likes+=int(count_likes)
		print(count_members,sum_likes)
	if(method==5):
		for i in range(n):
			t=wall_get_gr["items"][i]["date"]
			a = datetime.datetime.today()
			b=time.ctime(int(t))
			b=datetime.datetime(b)
			print(b)
	if(method==61):
		for i in range(n):
			count_likes=wall_get_gr["items"][i]["likes"]["count"]
			count_views=wall_get_gr["items"][i]["views"]["count"]
			count_reposts=wall_get_gr["items"][i]["reposts"]["count"]
			sum_views+=int(count_views)
			sum_act+=int(count_views)+int(count_likes)+int(count_reposts)
			sum_likes+=int(count_likes)
			if((int(count_views)+int(count_likes)+int(count_reposts))>=pop_count):
				pop=i
				pop_count=int(count_views)+int(count_likes)+int(count_reposts)
			elif((int(count_views)+int(count_likes)+int(count_reposts))<=nopop_count):
				nopop=i
				nopop_count=int(count_views)+int(count_likes)+int(count_reposts)
		print(url+"?w=wall-"+str(gr_id)+"_"+str(wall_get_gr["items"][pop]["id"]))
	if(method==62):
		for i in range(n):
			count_likes=wall_get_gr["items"][i]["likes"]["count"]
			count_views=wall_get_gr["items"][i]["views"]["count"]
			count_reposts=wall_get_gr["items"][i]["reposts"]["count"]
			sum_views+=int(count_views)
			sum_act+=int(count_views)+int(count_likes)+int(count_reposts)
			sum_likes+=int(count_likes)
			if((int(count_views)+int(count_likes)+int(count_reposts))>=pop_count):
				pop=i
				pop_count=int(count_views)+int(count_likes)+int(count_reposts)
			elif((int(count_views)+int(count_likes)+int(count_reposts))<=nopop_count):
				nopop=i
				nopop_count=int(count_views)+int(count_likes)+int(count_reposts)
		print(url+"?w=wall-"+str(gr_id)+"_"+str(wall_get_gr["items"][nopop]["id"]))
	
except vk_api.AuthError as er:
	print(er)
