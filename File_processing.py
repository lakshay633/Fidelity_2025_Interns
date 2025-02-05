# convert only dictionaries from a text file to binary
import re
import pickle
with open("Fidelity_2025_Interns\\text1.txt","r") as i:
    l=i.readlines()

a=[]
for x in l:
    if re.match(r"^\{.*:", x):
        a.append(x)
        
with open("binary1.dat","wb") as file:
    pickle.dump(a,file)
with open("binary1.dat","rb") as file:
    print(pickle.load(file))