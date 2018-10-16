num = int(input("enter total number: "))
dic = {}

for i in range(num):
	key, value = input("enter key and value: ").split()
	dic[key] = value

coded_result = input("your coded text: ")

print(dic)

s, e = 0, 1
while True:
	if coded_result[s:e] in dic.keys():
		print(dic[coded_result[s:e]])
		s = e
		e += 1
	else:
		e += 1
	if s >= len(coded_result) - 1:
		break




