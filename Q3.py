import random

mylist = [None]*10**6
#print(len(mylist))
count =1;
for i in range(len(mylist)):
    if count<= (0.52*len(mylist)):
        mylist[i]=(1)
        count +=1
    else:
        mylist[i]=(-1)
        count +=1

#print(mylist.count(1))
print(len(mylist))

list_of_random_items_20 = random.sample(mylist, 20)

list_of_random_items_400 = random.sample(mylist, 400)
print(len(list_of_random_items_400))

#sample size 20
average_20= []
for j in range(100):
    list_of_random_items_20 = random.sample(mylist, 20)
    count_1 = list_of_random_items_20.count(1)
    #print("1",count_1)
    count_not1 = list_of_random_items_20.count(-1)
    #print("-1",count_not1)
    if count_1 > count_not1:
        average_20.append(1)
    else:
        average_20.append(-1)

print("average probability ",average_20.count(1)/100)


#sample size 100
average_100= []
for j in range(100):
    list_of_random_items_100 = random.sample(mylist, 100)
    count_1 = list_of_random_items_100.count(1)
    #print("1",count_1)
    count_not1 = list_of_random_items_100.count(-1)
    #print("-1",count_not1)
    if count_1 > count_not1:
        average_100.append(1)
    else:
        average_100.append(-1)

print("average probability  100", average_100.count(1)/100)

#sample size 400
average_400= []
for j in range(100):
    list_of_random_items_400 = random.sample(mylist, 400)
    count_1 = list_of_random_items_400.count(1)
    #print("1",count_1)
    count_not1 = list_of_random_items_400.count(-1)
    #print("-1",count_not1)
    if count_1 > count_not1:
        average_400.append(1)
    else:
        average_400.append(-1)

print("average probability  400", average_400.count(1)/100)

#searching for sample size so that the probability becomes 0.9
average_950= []
for j in range(100):
    list_of_random_items_950 = random.sample(mylist, 950)
    count_1 = list_of_random_items_950.count(1)
    #print("1",count_1)
    count_not1 = list_of_random_items_950.count(-1)
    #print("-1",count_not1)
    if count_1 > count_not1:
        average_950.append(1)
    else:
        average_950.append(-1)

print("average probability 950", average_950.count(1)/100)
