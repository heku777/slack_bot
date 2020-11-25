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

def today_todo(today):
	if str(today) == "0":
		return 'お風呂掃除'
	elif str(today) == "1":
		return '資源ゴミ'
	elif str(today) == "2":
		return '燃えるゴミ'
	elif str(today) == "3":
		return "トイレ掃除"
	elif str(today) == "4":
		return "洗面所と台所"
	elif str(today) == "5":
		return "燃えるゴミ"
	else:
		return "掃除機"


def main():
	#曜日を取得
	today = what_today()

	todo = today_todo(today)

	client = slack.WebClient(token=os.environ['API_TOKEN'])

	client.chat_postMessage(channel='#second_floor_bot', text=todo)


if __name__ == '__main__':
	main()
