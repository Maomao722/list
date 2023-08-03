

products = []
while True:
	n = input('輸入名稱: ')
	if n == 'q':
		break
	p = int(input('請輸入價格: '))
	products.append([n, p])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

