import pandas 
import numpy

f=pandas.read_csv("./test.csv",header=None)
f=f[:-1]
with open("./contact cdi.txt","w",encoding="utf-8") as o:
    for i in f.values.tolist()[1:]:
        #print(i[2],i[3],i[0])
        o.write("{0};{1};{2}".format(i[2],i[3],i[0]))
        o.write("\n")
o.close()