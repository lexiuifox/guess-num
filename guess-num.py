#產生隨機整數1~100 (不要印出來)
#讓使用者重複輸入去猜
#猜對的話印出“終於猜對了！”
#猜錯的話 要告訴他比答案大/小

import random
start = input('請決定隨機數字範圍開始值')
end = input('請決定隨機數字範圍結束值')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	num = input('請猜數字：')
	num = int(num)
	if num > r:
		count += 1 #count = count + 1
		print('小一點	～')
	elif num < r:
		count += 1
		print('大一點～')
	elif num == r:
		print('你猜中了！')
		print('總共猜了', count,'次')
		break
	print('這是你猜的第', count,'次')

