from collections import OrderedDict

def no_dups(s):
    new_list = OrderedDict().fromkeys(s.split())
    return " ".join(new_list)    

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))