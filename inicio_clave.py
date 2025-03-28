Python  
f = 1
lA = 2
lB = 3
eA = 216
eB = 137

p = f * lA**eA * lB ** eB - 1 
assert p.is_prime()

Fp = GF(p)
Fp2 = GF(p ** 2, 'i' , modulus = x **2 + 1 )

E = ElliptiCurve(Fp2,[1,0])

assert E.is_supersingular()
