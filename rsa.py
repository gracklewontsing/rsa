# get lcm
from pip._vendor.distlib.compat import raw_input


def lcm(x, y):
    # get greater
    if x > y:
        g = x
    else:
        g = y

    while (True):
        # brute find
        g += 1
        if (g % x == 0) and (g % y == 0):
            lcm = g
            break
        # try again
    return lcm


# get gcd
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


# get coprimes
def coprime(x, y):
    return gcd(x, y) == 1


def prime(x):
    if p > 1:
        for i in range(2, p):
            if (p % i) == 0:
                return True
    return False


def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


# get p
p = int(input("Enter prime number value for p: "))

if prime(p):
    print("please use prime numbers")
    exit()

# get q
q = int(input("Enter prime number value for q: "))

# q must be distinct form p
if p == q:
    print("please use distinct values")
    exit()

if prime(q):
    print("please use prime numbers")
    exit()

# n is pq
n = p * q

# get lcm of p-1 and q-1
phi = lcm(p - 1, q - 1)

# get e
e = 0
for aux in range(2, phi - 1):
    if coprime(aux, n) != 0 and coprime(aux, phi):
        e = aux

# e is now the public key exponent

# define  k=e^−1(mod λ(n))
# k = (e ** -1) % phi
# print('k is ', k)

# loop i until i mod λ(n) == k
# for i in range(0, n):  # possibly change range to a bigger number
# if i % phi == k:
# var d now equals i because i satisfies congruency with e^-1
#   d = i
#  print('d is ', d)


d = modInverse(e, phi)

print('e is ', e)
print('d is ', d)

# take input and transform to numbers
def letterstonumbers(str):
    inpu = raw_input(str)
    inpu = inpu.lower()
    outpu = []
    for character in inpu:
        number = ord(character) - 96
        outpu.append(number)
    return outpu


def encryption(plain):
    return (plain ** e) % n


def decryption(cipher):
    return (cipher ** d) % n


selected = False
select = 0

while not selected:
    select = int(input("Enter 1 for encryption or 2 for decryption: "))
    if select == 1 or 2:
        break

if select == 1:
    text = letterstonumbers('Enter plain text: ')
    for w in text:
        print(encryption(w))

if select == 2:
    text = letterstonumbers('Enter cipher text: ')
    for w in text:
        print(decryption(w))
