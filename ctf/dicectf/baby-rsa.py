from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

N = 57996511214023134147551927572747727074259762800050285360155793732008227782157
e = 17
c = 19441066986971115501070184268860318480501957407683654861466353590162062492971



p = 172036442175296373253148927105725488217
q = 337117592532677714973555912658569668821

from math import gcd

def getModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

phi = (p-1)*(q-1)
priv_key = pow(N,-1,phi)

d = getModInverse(N, phi)
print(long_to_bytes(pow(c, d, N)))
