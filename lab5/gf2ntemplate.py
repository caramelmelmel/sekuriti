# 50.042 FCS Lab 5 Modular Arithmetics
# Year 2021
#Completed by:
# Leong Yun Qin Melody 1004489

import copy
from helper import (xor, and_gate)
from itertools import zip_longest
class Polynomial2:
    def __init__(self,coeffs):
        self.coeffs = coeffs
        

    def add(self,p2):
        added_ls = []
        #check if the len of what is lesser than what then add the 0s to the front
        for i,j in zip_longest(self.coeffs, p2.coeffs,fillvalue=0):
            added_ls.append(xor(i,j))
        #remove the trailing zero as some do not match 
        while len(added_ls) > 0 and added_ls[-1] == 0:
            added_ls.pop(-1)
        return Polynomial2(added_ls)
                

    def sub(self,p2):
        return self.add(p2)

    def mul(self,p2,modp=None):
        # L-> R LSB to MSB in the list
        mod_list = []
        mod_list.append(p2)

        for i in range(1,len(self.coeffs)):
            prev_res = mod_list[-1]

            #Shift regardless of 0 or 1
            shifted_prev_result = prev_res.shift()

            #use the modp value
            if modp != None:
                mod_list.append(shifted_prev_result.modp(modp))

            else:
                mod_list.append(shifted_prev_result)

        #return the class object
        res = Polynomial2([0])

        for index, coeff in enumerate(self.coeffs):
            if coeff == 1:
                res = res.add(mod_list[index])

        return res  
    
    #lc 
    def lc(self):
        return self.coeffs[-1]
    
    def deg(self):
        return len(self.coeffs) - 1

    def div(self,p2):
        q = Polynomial2([0])
        r = copy.deepcopy(self)
        d = p2.deg()
        c = p2.lc()
        s = []

        while r.deg() >= d:
            s= Polynomial2([0 for i in range(r.deg()-d)] + [1])
            q = s.add(q)
            r = r.sub(s.mul(p2))

        return q, r
    

    def shift(self):
        #shift to the right 
        #adds to the MSB
        return Polynomial2([0] + self.coeffs)
    
    def modp(self, modp):

        #check for coincidence 
        if len(self.coeffs) >= len(modp.coeffs):

            #XOR self using the add method and modp without the msb
            return Polynomial2(self.coeffs[:-1]).add(Polynomial2(modp.coeffs[:-1]))

        else:
            return self

    def __str__(self):
        output = ""
        for order, coeff in enumerate(self.coeffs[::-1]):
            if coeff == 1:
                output += f' x^{len(self.coeffs)-order-1} +'
        return output.rstrip(output[-1])

    def getInt(p):
        res = 0 
        # do the comp struct method 
        for order,coeff in enumerate(p.coeffs):
            res += (2** order) * coeff
        return res


class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        pass


    def add(self,g2):
        pass
    def sub(self,g2):
        pass
    
    def mul(self,g2):
        pass

    def div(self,g2):
        pass

    def getPolynomial2(self):
        pass

    def __str__(self):
        pass

    def getInt(self):
        pass

    def mulInv(self):
        pass

    def affineMap(self):
        pass

print('\nTest 1')
print('======')
print('p1=x^5+x^2+x')
print('p2=x^3+x^2+1')
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
#print(type(p3))
print(f'p3= p1+p2 = {p3}')


print('\nTest 2')
print('======')
print('p4=x^7+x^4+x^3+x^2+x')
print('modp=x^8+x^7+x^5+x^4+1')
p4=Polynomial2([0,1,1,1,1,0,0,1])
# modp=Polynomial2([1,1,0,1,1,0,0,0,1])
modp=Polynomial2([1,0,0,0,1,1,0,1,1])
p5=p1.mul(p4,modp)
print('p5=p1*p4 mod (modp)=',p5)

print('\nTest 3')
print('======')
print('p6=x^12+x^7+x^2')
print('p7=x^8+x^4+x^3+x+1')
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])    
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print('q for p6/p7=',p8q)
print('r for p6/p7=',p8r)

####
print('\nTest 4')
print('======')
g1=GF2N(100)
g2=GF2N(5)
print('g1 = ',g1.getPolynomial2())
print('g2 = ',g2.getPolynomial2())
g3=g1.add(g2)
print('g1+g2 = ',g3)

print('\nTest 5')
print('======')
ip=Polynomial2([1,1,0,0,1])
print('irreducible polynomial',ip)
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print('g4 = ',g4.getPolynomial2())
print('g5 = ',g5.getPolynomial2())
g6=g4.mul(g5)
print('g4 x g5 = ',g6.p)

print('\nTest 6')
print('======')
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print('g7 = ',g7.getPolynomial2())
print('g8 = ',g8.getPolynomial2())
q,r=g7.div(g8)
print('g7/g8 =')
print('q = ',q.getPolynomial2())
print('r = ',r.getPolynomial2())

print('\nTest 7')
print('======')
ip=Polynomial2([1,1,0,0,1])
print('irreducible polynomial',ip)
g9=GF2N(0b101,4,ip)
print('g9 = ',g9.getPolynomial2())
print('inverse of g9 =',g9.mulInv().getPolynomial2())

print('\nTest 8')
print('======')
ip=Polynomial2([1,1,0,1,1,0,0,0,1])
print('irreducible polynomial',ip)
g10=GF2N(0xc2,8,ip)
print('g10 = 0xc2')
g11=g10.mulInv()
print('inverse of g10 = g11 =', hex(g11.getInt()))
g12=g11.affineMap()
print('affine map of g11 =',hex(g12.getInt()))