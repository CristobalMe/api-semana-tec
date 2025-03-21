import math
message: str
p: int
q: int
e: int
cifer = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}



def manage_message(message):
    message = message.lower()
    reversed_message = message[::-1]
    divided_message = [reversed_message[i:i+4][::-1] for i in range(0, len(message), 4)][::-1]
    return divided_message

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
def phi(p,q):
    return (p-1)*(q-1)

def generar_d(e, p,q):
    phi_n = phi(p, q)
    g, x, y = extended_gcd(e, phi_n)
    d = 0
    if g != 1:
        raise Exception('Modular inverse does not exist')
        return null
    else:
        d = x % phi_n
    if d < 0:
        d += phi_n
    return d

def cifer_message(message):
    divided_message = manage_message(message)
    cifered_message = []
    for sub_message in divided_message:
        cifered_sub_mesage = 0
        count = len(sub_message) - 1
        for char in sub_message:
            cifered_sub_mesage += (cifer[char]*27**count)
            count -= 1
            cifered_message.append((cifered_sub_mesage))
    return cifered_message

def encrypt(message, e, p, q):
    n = p*q
    cifered_message = cifer_message(message)
    encrypted_message = []
    for num in cifered_message:
        encrypted_message.append(pow(num, e, n))
    return encrypted_message

