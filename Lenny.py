def make_sentence(p, f):
    return p + "is" + f
sentence = make_sentence("power" , "fab")
print(sentence)

def check_even_odd():
    a = int(input("What's a? "))
    b = int(input("What's b? "))
    if a % 2 == 0:
        print(str(a) + " is even ")
    else:
         print(str(a) + " is odd")   
    if b % 2 != 0:
        print(str(b) + " is odd") 
    else:
        print(str(b) + " is even")
check_even_odd()




