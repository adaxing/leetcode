from pythonds.basic.stack import Stack

def isValid(s):
	# dic = {
	# 	'(':')',
	# 	'{':'}',
	# 	'[':']',
	# }
	# st = Stack()
	# match = True
	# for para in s:
	# 	if para in dic.keys():
	# 		st.push(dic[para])
	# 	else:
	# 		if para != st.pop():
	# 			match = False

	# if st.isEmpty() and match:
	# 	return True
	# else:
	# 	return False
	dic = {
		'(':')',
		'{':'}',
		'[':']',
        }
        stack = []
        match = True
        for para in s:
            if para in dic.keys():
                stack.append(dic[para])
            else:
                if len(stack) == 0:
                    return False
                elif len(stack) != 0 and para != stack.pop():
                    match = False

        if len(stack) == 0 and match:
            return True
        else:
            return False

   
input_value = input("Input:")
print(isValid(input_value))