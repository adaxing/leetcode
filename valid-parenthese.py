from pythonds.basic.stack import Stack

def isValid(s):
	dic = {
		'(':')',
		'{':'}',
		'[':']',
	}
	st = Stack()
	balanced = True
	index = 0
	print(len(s))
	while index < len(s) and balanced:
		symbol = s[index]
		if symbol == dic.keys():
			st.push(symbol)
		else:
			print(st.isEmpty())
			if st.isEmpty():
				balanced = False
			else:
				print("!!!")
				match = dic[symbol]=st.pop()
		index = index + 1
	if balanced and st.isEmpty():
		return True
	else: 
		return False

   
input_value = input("Input:")
print(isValid(input_value))