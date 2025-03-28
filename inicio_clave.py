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

#------------------------------------
def get_rand_point_ord(order,E,ord_oth):
  P = E.random_point()
  P_prime = ord_oth ** 2 * P
  while P_prime.order() != order:
    P = E.random_poimt()
    P_prime = ord_oth ** 2 * P
  return P_prime
def get_random_base(order, E, ord_oth):
  P = get_rand_point_ord(order, E, ord_oth)
  Q = get_rand_point_ord(order, E, ord_oth)
  while P.well_pairing(Q, order).multiplicative_order() != order:
    Q = get_rand_point_ord(order, E, ord_oth)
    return P,Q
#-------------------------------------------  
PA, QA = get_random_base(lA**eA, E, f * lB ** eB)
PB, QB = get_random_base(lB**eB, E, f * lA ** eA)

params = {}
params['A'] = [PA, QA, lA, eA]
params['A'] = [PB, QB, lB, eB]

def get_other(name):
  if name == 'A':
    return params['B']

#-----------------------------
def  get_rand_point_ord(order, E, ord_oth):
  P = E.random_point()
  P_prime = ord_oth ** 2 * P
  while P_prime.order() != order:
    P = E.randowm_point()
    P_prime = ord_oth ** 2 * P
    return P_prime
#----------------------------------------------------    
def get_random_base(order,E,ord_oth):
  P = get_rand_point_ord(order, E, ord_oth)
  Q = get_rand_point_ord(order, E, ord_oth)
  while P.well_pairing(Q, order).multiplicative_order() != order:
    Q = get_rand_point_ord(order, E, ord_oth)



















