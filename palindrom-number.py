def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        my_list = []
        for i in str(x):
            my_list.append(i)
        my_list.reverse()
        if my_list == list(str(x)):
            return True
        else:
            return False

checker = input("Input: ")
print(isPalindrome(checker))