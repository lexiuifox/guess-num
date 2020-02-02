#產生隨機整數1~100 (不要印出來)
#讓使用者重複輸入去猜
#猜對的話印出“終於猜對了！”
#猜錯的話 要告訴他比答案大/小


import random

r = random.randint(1,100)

while True:
	num = input('猜一個號碼：')
	num = int(num)
	if num > r:
		print('小一點	～')
	elif num < r:
		print('大一點～')
	elif num == r:
		print('猜對了！')
		break
