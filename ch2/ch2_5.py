class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        resize_self_string = ""
        for alphabet in self.string:
            if alphabet.isupper():
                resize_self_string += alphabet.lower()
            elif alphabet.islower():
                resize_self_string += alphabet.upper()

        return resize_self_string

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        result = []
        for alphabet in self.string:
            if alphabet not in result:
                result.append(alphabet)
        self.string = ''.join(result)
        return self.string

str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :   print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())