import os
file=open("cars",'r')
for line in file:
        l=line.split()
        os.system("wget -O {0} {1}".format(l[0],l[1]))
