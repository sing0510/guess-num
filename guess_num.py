import random
start = input('請決定開始數字')
end = input('請決定結尾數字')
start = int(start)
end = int(end)


r = random.randint(start, end)
count = 0
while True:
	count += 1 #等於 count = count + 1 (簡化)
	num = input(' 請輸入數字: ')
	num = int(num)
	if r == num:
		print('你猜對了')
		print('你在第', count, '次猜對了!')
		break
	elif num > r :
		print('太大了,請再猜')
	elif num < r :
		print('太小了,再猜')
	print('這是你第', count, '次猜了!')



