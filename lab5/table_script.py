#done by Leong Yun Qin Melody 1004489

from gf2ntemplate import GF2N, Polynomial2


file = open('table1.txt','w')

ip = Polynomial2([1,0,0,1,1])

output = ""

for i in range(2**4):
    for j in range(2**4):
        g1 = GF2N(i,4,ip)
        g2 = GF2N(j,4,ip)
        output += f'g1: {g1} \n'
        output += f'g2: {g2} \n'
        output += f'add: {g1.add(g2)} \n'
        output += f'mul: {g1.mul(g2)} \n'
        output += '\n'
file.write(output)
