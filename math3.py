from itertools import combinations


def TestIndepEVENT( a,b, c): #a and b are probs .03 #c ==  P(A and B)
    hold=a*b
    if(hold == c):
        return True
    else:
        return False

print(TestIndepEVENT(.36,.25,.085))


#If two events A and B are mutually exclusive, the events are called disjoint events.

def OR2indepEvent(a,b):
    hold = a+b
    print(hold)
OR2indepEvent(.3,.6)


def AGiveBexclu(a,b): #(A|B)
   return None
def AGiveB(a, b):  # (A|B)
    hold = a
    print(hold/b)


l= [0,3,3,3]
hold=combinations(l,4)
print(hold)