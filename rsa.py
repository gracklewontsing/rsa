#get lcm
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

#get gcd
def gcd (x,y):
    while y != 0:
        x,y = y, x % y
    return x

#get coprimes
def coprime (x, y):
    return gcd (x,y) == 1

#get p
p = int(input("Enter prime number value for p: "))

if p > 1:
    for i in range (2,p):
        if (p % i) == 0:
            print ("please use prime numbers")
            exit()                

#get q
q = int(input("Enter prime number value for q: "))

#q must be distinct form p
if p == q:
    print("please use distinct values")
    exit()

if q > 1:
    for i in range (2,q):
        if (q % i) == 0:
            print ("please use prime numbers")
            exit()

#n is pq
n = p*q

#get lcm of p-1 and q-1
x = lcm(p-1,q-1)

#choose e
e = int(input("Enter a number between 1 and {}: ".format(x)))

#e must be coprime with the lcm of p-1 and q-1
while coprime(e,x) == 0:
    e = int(input("Enter a valid number between 1 and {}".format(x)))
#e is now the public key exponent

#testing e^-1
#print(pow(e, -1))

#get d, where d = (1+k(lcm(p-1,q-1))/e), and it needs the extended euclidean algorithm to get

