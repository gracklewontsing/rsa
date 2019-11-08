def lcm(x,y):
    #get greater
    if x>y:
        g=x
    else:
        g=y
    
    while(True):
        #brute find
        g+=1
        if((g % x == 0) and (g % y == 0)):
            lcm = g
            break
        #try again
    return lcm

def gcd (x,y):
    while y != 0:
        x,y = y, x % y
    return x

def coprime (x, y):
    return gcd (x,y) == 1

p = int(input("Enter prime number value for p: "))

if p > 1:
    for i in range (2,p):
        if (p % i) == 0:
            print ("please use prime numbers")
            exit()                


q = int(input("Enter prime number value for q: "))

if p == q:
    print("please use distinct values")
    exit()

if q > 1:
    for i in range (2,q):
        if (q % i) == 0:
            print ("please use prime numbers")
            exit()
        
n = p*q
q = lcm(p-1,q-1)

e = int(input("Enter a number between 1 and {}: ".format(q)))
while coprime(e,q) == 0:
    e = int(input("Enter a valid number between 1 and {}".format(q)))

print(pow(e, -1))


