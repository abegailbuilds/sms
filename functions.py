#a block of code that performs a certain action

#parameters-named variables with values
#arguments=actual values supplied to a fn
#return value-value that is returned after a function is executed
#**kwargs, *args
#defining functions
"""
def main(**kwargs):

    print("overloading 1")


#return type
def add(num1=8, num2=8):

    print(num1+num2)

    return num1+num2

add()
def square(num1=90):

    squarenum=num1*num1
    return squarenum
#int main() void main()


num1=int(input("enter num1"))
num2=int(input("enter num2"))

add(num1=num1,num2=num2)



print(square(num1))



#print(result)
"""

count =0

def incrementCounter(countnum):
    global count

    count+=countnum

    return count

def fn2(function, value):
    return incrementCounter(value)


def mean(sub1,subj2,sub3):

    return (sub3+subj2+sub1)/3

def grade(mean, values):

    result=mean(values[0],values[1],values[2])

    if 80 <result <100:
        return "A"
    elif 70 <result<80:
        return "B"
    elif result <=70:
        return "F"
    else:
        return None



result=grade(mean,[3,89,89])

print(result)

def add(num1,num2):
    return  num1+num2


print(add(2,5))
print(add(3,78))
print(add(90,89))