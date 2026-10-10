import sympy as s
m=s.symbols('m')
T=s.Matrix([[1,0],[-m/s.Integer(3),-s.Rational(1,3)]])
S=s.Matrix([[s.Rational(2,3),s.Rational(1,3)],[1,0]])
from itertools import product
for L in range(1,9):
 found=[]
 for w in product('ST', repeat=L):
  M=s.eye(2)
  for c in w:M=(T if c=='T' else S)*M
  # normalized ratio entries polynomial
  if s.simplify(M[1,0])==0 or s.simplify(M[0,1])==0:
   found.append((w,s.simplify(M)))
 print('L',L,'found',len(found))
 for w,M in found[:10]:print(''.join(w),M)
