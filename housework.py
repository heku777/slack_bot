# -*- coding: utf-8 -*-
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#曜日を取得する関数
def what_today():
	weekday = datetime.date.today().weekday()
	return weekday

def what_time():
	time = datetime.datetime.now().time()
	hour = str(time).split(':')[0]
	return hour

def today_todo(today, hour):
	todo_list = []
	if str(today) == "0":
		todo_list.append('今日はお風呂掃除')
		todo_list.append("トイレふき")
		if int(hour) >= 20:
			todo_list.append('明日は資源ゴミ')

	elif str(today) == "1":
		todo_list.append('台所掃除と流しのネットを変える')
		if int(hour) < 9:
			todo_list.append('資源ゴミ')
		if int(hour) >= 20:
			todo_list.append('明日は燃えるゴミ')

	elif str(today) == "2":
		if int(hour) < 9:
			todo_list.append('燃えるゴミ')

	elif str(today) == "3":
		todo_list.append("トイレ掃除とトイレふき")

	elif str(today) == "4":
		todo_list.append("洗面所掃除")
		if int(hour) >= 20:
			todo_list.append('明日は燃えるゴミ')

	elif str(today) == "5":
		todo_list.append("トイレふき")
		if int(hour) < 9:
			todo_list.append('燃えるゴミ')
	else:
		todo_list.append("掃除機")
		todo_list.append("洗濯機のフィルターの掃除")

	return todo_list

def file_upload(today):
	if str(today) == "0":
		return './bath.txt'

	elif str(today) == "1":
		return './kichen.txt'

	elif str(today) == "2":
		return 'none'

	elif str(today) == "3":
		return './toilet.txt'

	elif str(today) == "4":
		return './fc.txt'

	elif str(today) == "5":
		return 'none'

	else:
		return 'none'




def main():
	#曜日を取得
	today = what_today()

	hour = what_time()

	todo = today_todo(today, hour)

	file = file_upload(today)

	client = slack.WebClient(token=os.environ['API_TOKEN'])

	for td in todo:
		client.chat_postMessage(channel='#second_floor_bot', text=td)

	if file != 'none':
		client.files_upload(channels='#second_floor_bot', file=file)


if __name__ == '__main__':
	main()
