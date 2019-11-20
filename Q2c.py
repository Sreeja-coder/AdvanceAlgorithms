import random


values = [1,-1]
crossorigin_1 = []
crossorigin_2 = []
crossorigin_3 = []

#for range t = 4*10**4
for i in range(50):
    x = 0
    for t in range(4*10**4):
        y=random.choice(values)
        x = x+y

        if x==0:
            crossorigin_1.append(x)



print(crossorigin_1.count(0))
print(" for t = 4*10**4",crossorigin_1.count(0)/50);

#for range t = 9*10**4

for i in range(50):
    x = 0
    for t in range(9*10**4):
        y=random.choice(values)
        x = x+y
        if x==0:
            crossorigin_2.append(x)

print(crossorigin_2.count(0))
print("for t = 9*10**4", crossorigin_2.count(0)/50);

#for range t = 9*10**4

for i in range(50):
    x = 0
    for t in range(16*10**4):
        y=random.choice(values)
        x = x+y
        if x==0:
            crossorigin_3.append(x)

print(crossorigin_3.count(0))
print("for t = 16*10**4"crossorigin_3.count(0)/50);







