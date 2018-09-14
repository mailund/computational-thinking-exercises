
n = 100
numbers = list(range(2,n))
p = 1
while numbers != []:
	fmt = "#numbers = {:>2}, n/p = {:>3.2f}"
	print(fmt.format(len(numbers), n/p))
	p = numbers[0]
	numbers = [n for n in numbers if n % p != 0]
