import random
r = random.randint(1, 2)
print(r)
while True:
	a = input('請輸入')
	a = int(a)
	if r == a:
		print('你猜對了')
		break
	else:
		print('再猜')

