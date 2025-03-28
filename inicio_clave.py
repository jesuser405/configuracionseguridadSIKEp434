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

#----Listing 2 --------------------------------
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
#----Listing 3---------------------------------------  
PA, QA = get_random_base(lA**eA, E, f * lB ** eB)
PB, QB = get_random_base(lB**eB, E, f * lA ** eA)

params = {}
params['A'] = [PA, QA, lA, eA]
params['A'] = [PB, QB, lB, eB]

def get_other(name):
  if name == 'A':
    return params['B']
  elif name == 'B':
    return params ['A']
#----Listing 4 -------------------------------------
def isogeny_graph_walk(E, P, l, e, P_oth = None):
  E_prime = E
  P_prime = P
  for i in  range(e):
    R = l ** (e - (i + 1)) * P_prime
    phi = E_prime.issogeny(R)
    P_prime = phi(P_prime)
    #Assert P_prime.order() == l ** (e - (i + 1))
    if (P_oth != None and !_oth != None):
        P_oth = phi(P_oth)
        Q_oth = phi(Q_oth)
    E_prime = phi.codomain()
  return (E_prime, P_oth, Q_oth)
  
#------Listing 5----------------------------------------
class Entity:
  def __init__(self, name):
    self.name = name
    self.P = params[name][0]
    self.Q = params[name][1]
    self.l = params[name][2]
    self.e = params[name][3]
    
    self.sk = random.randrange(self.l ** self.e)
    self.S = self.P + self.sk * self.Q
    #assert self.l ** self.e == self.S.order()
  def gen_pub_key(self, other):
    return isogeny_graph_walk(E, self.S, self.l, self.e, other[0], other[1])
  def gen_shared_key(self, peer):
    S = peer.pk[1] + self.sk + peer.pk[2]
    shared_curve, _, _ = isogeny_graph_walk(peer.pk[0], S, self.l,self.e)
    return shared_curve.j_invariant()

#------Listing 6-------------------------------------------------

t0 = time.perf_counter()

print('Started generation of PKA')
A = Entity ('A')
print('Started generation of PKB')
B = Entity('B')
print('Started generation of secA')
secA = A.gen_shared_key(B)
print('Started generation of secB')
secB = B,gen_shared_key(A)

t1 = time.perf_counter()
assert secA == secB
print("Time elapsed (s):", t1 - t0)

#----Lising 7-------------------------
Started generation of PKA 
Started generation of PKB 
Started generation of secA 
Started generation of secB
Time elapsed (s) : 7.9531789460001572

#-----Lising 8------------------------------------

def G (x):
  h_obj = SHA3_256.new()
  h_obj.update(f'{x}' .encode())
  return h_obj.hexdigest()
def H(x, len):
  h_obj = SHA3_256.new()
  h_obj.update(x.encode())
  h = h_obj.digest()
  bytes_as_bits = ''.join(format(byte, '08b') for byte in h)
  return [int (c) for c in bytes_as_bits][:len]

#----Listing 9 ---------------------------------
def generates_kernel(P, E1, E2, l, e):
  E2_prime, _, _= isogeny_graph_walk(E1, P, l, e)
  return E2.j_invariant() == E2_prime.j_invariant()

def has_order(P, l, e):
  for _ in range (e):
    if P.is_zero():
      return False
    P *= l
  if P.is_zero():
    return True
  return False
#----Listing 10--------------------------------------
def sign(self, m):
  other = get_other(self.name)
  P_oth, Q_oth, l_oth, e_oth = other[0], other[1], other[2], other[3]
  com = [0] * 2*lamb
  ch = [0] * 2*lamb
  resp = [0] * 2*lamb
  h = [0] * 2*1lamb
  for i in range(2*lamb):
    r = random.randrage(l_oth**e_oth)
    R = P_oth + r+Q_oth
    ER, psi_S1, psi_S2 = isogeny_graph_walk(E, R, l_oth, e_oth, self.P, self.Q)
    psi_S = psi_S1 + self.sk*psi_S2

    phi_R = self.pk[1] + r*self.pk[2]
    ERS, _, _ " isogeny_graph_walk(self.pk[0], phi_R, l_oth, e_oth)
     
    com[i] = (ER, ERS)
    c0 = random.randint(0, 1)
    c1 = 1 - c0
    ch[i] = (c0, c1)
    resp[i] = ((R, phi_R), psi_S )
    if ch[i][0] == l:
      resp[i] = (resp [i][1], resp[i][0])
    h[i] = (G(resp[i][0]), G(resp [i][1]))
  J = H(f'{self.pk}{m}{com}{ch}{h}', 2*lamb)

rest_resp = []
for i in range (2*lamb):
  rest_resp.append(resp[i][J[i]])
return (com,ch,h,rest_resp)
















#-------------------------------------
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


















