import os # operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			n, p = line.strip().split(',')
			products.append([n, p])

#使用者輸入
while True:
	n = input('輸入名稱: ')
	if n == 'q':
		break
	p = int(input('請輸入價格: '))
	products.append([n, p])

#印出所有紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

