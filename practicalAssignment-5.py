import random, math
a = random.randint(2, 10)

def power(x, y, p) :
    res = 1    
    x = x % p
    if (x == 0) :
        return 0
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y >> 1      
        x = (x * x) % p    
    return res

def gen_key(q):
  temp = math.pow(10,20)
  key = random.randint(temp, q)
  while math.gcd(q, key) != 1:
	  key = random.randint(temp, q)
  return key

def encrypt(msg, q, h, g):
	en_msg = []
	k = gen_key(q)
	s = power(h, k, q)
	p = power(g, k, q)
	for i in range(0, len(msg)):
		en_msg.append(msg[i])
	print("g^k used : ", p)
	print("g^ak used : ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])
	return en_msg, p

def decrypt(en_msg, p, key, q):
	dr_msg = []
	h = power(p, key, q)
	for i in range(0, len(en_msg)):
		dr_msg.append(chr(int(en_msg[i]/h)))
	return dr_msg

msg = 'Jinesh'
print("Original Message :", msg)
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)
h = power(g, key, q)
print("g used : ", g)
print("g^a used : ", h)
en_msg, p = encrypt(msg, q, h, g)
dr_msg = decrypt(en_msg, p, key, q)
dmsg = ''.join(dr_msg)
print("Decrypted Message :", dmsg);
