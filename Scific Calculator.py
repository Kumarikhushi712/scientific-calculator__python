def sum(a,b):
    return a+b
def sub(a,b):
    return a-b

def div(a,b):
    return a/b
def mul(a,b):
    return a*b


print('SCIENTIFIC CALCULATOR')

print('THE FOLLOWING OPERATIONS YOU CAN PERFORM')
while True:

    print('''
    BASIC MATHS OPERATION

    1) ADDITION
    2) SUBTRACTION
    3) MULTIPY
    4) DIVIDE

    ADVANCE MATHS OPERATION
    5) MOD
    6) SQUARE ROOT 
    7) EXPONENT

    TRIGONOMETRY OPERATIONS
    8) SIN
    9) COS
    10) TANGENT

    CONVERSION OPERATIONS
    11) RADIAN TO DEGREE
    12) DEGREE TO RADIAN''')

    flag='''1) ADDITION
    2) SUBTRACTION
    3) MULTIPY
    4) DIVIDE'''

    choice=int(input('Which operation do you want to perform: '))
    if choice==1:
        user=int(input('how many numbers you want to add: '))

        sum=0
        for i in range (user):
            
            a=int(input('Enter number:'))
            sum+=a
        print('result:',sum)
        
    if choice==2:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a-b)
    if choice==3:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a*b)
    if choice==4:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',a/b)

    if choice==5:
        a=int(input('Enter first number:'))
        b=int(input('Enter second number: '))
        print('result:',abs(a+b))

    if choice==6:
        import math
        a=int(input('Enter number: '))
        print('result:',math.sqrt(a))

    if choice==7:
        import math
        a=int(input('Enter number: '))
        b=int(input('Enter power/exponent: '))
        print('result:',math.pow(a,b))

    if choice==8:
        import math
        a=int(input('Enter number: '))
        b=int(input('Enter second number:'))
        print(flag)
        cc=int(input('what action do you want to perform?:'))
        
        if cc==1:
            print(sum(math.sin(a),math.sin(b)))
        elif cc==2:
            print(sub(math.sin(a),math.sin(b)))
        elif cc==3:
            print(mul(math.sin(a),math.sin(b)))
        elif cc==4:
            print(div(math.sin(a),math.sin(b)))

    if choice==9:
        import math
        a=int(input('Enter number: '))
        b=int(input('Enter second number:'))
        print(flag)
        cc=int(input('what action do you want to perform?:'))
       
        if cc==1:
            print(sum(math.cos(a),math.cos(b)))
        elif cc==2:
            print(sub(math.cos(a),math.cos(b)))
        elif cc==3:
            print(mul(math.cos(a),math.cos(b)))
        elif cc==4:
            print(div(math.cos(a),math.cos(b)))

    if choice==10:
        import math
        a=int(input('Enter number: '))
        b=int(input('Enter second number:'))
        cc=int(input('what action do you want to perform?:'))
        print(flag)
        if cc==1:
            print(sum(math.tan(a),math.tan(b)))
        elif cc==2:
            print(sub(math.tan(a),math.tan(b)))
        elif cc==3:
            print(mul(math.tan(a),math.tan(b)))
        elif cc==4:
            print(div(math.tan(a),math.tan(b)))

    if choice==11:
        import math
        a=int(input('Enter number in radian: '))
        print('result:',math.degrees(a))

    if choice==12:
        import math
        a=int(input('Enter number in degrees: '))
        print('result:',math.radians(a))
    cont=input('Do you want to perform more calculations???(Y/N): ')
    if cont=='Y' or cont=='y':
        continue
    else:
        break