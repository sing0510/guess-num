import random
r = random.randint(1, 100)
while True:
	num = input(' 請輸入數字: ')
	num = int(num)
	if r == num:
		print('你猜對了')
		break
	elif num > r :
		print('太大了,請再猜')
	elif num < r :
		print('太小了,再猜')


