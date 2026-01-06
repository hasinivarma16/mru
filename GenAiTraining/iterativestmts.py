#iterative statements:-if you want to execute a group statements multiple times we have to use for or while
#we use for loop to iterating over a sequence(list,tuple,set,dict)
#range(start,stop,step)
for i in range(6):
    print(i)#from 0-5
sum=0
for i in range(1,11):
    sum+=i
print(sum)#sum of 10 nums
#reverse order
for i in range(10,0,-1):
    print(i)
#seperate negative nums and positive nums
li=[10,4,-5,-3,2,20,-50]
p=[]
n=[]
p_sum=0
n_sum=0
for i in li:
    if i>0:
        p.append(i)
        p_sum+=i
    else:
        n.append(i)
        n_sum+=i
print(p,p_sum)
print(n,n_sum)

#for loop with dictionaries:-
person={
    "name":"mokshi",
    "age":19,
    "dream":"arts and crafts"
}
print(person.keys())
print(person.values())
print(person.items())
#list
d=[('name','luffy'),('age',21),('dream','king of pirates')]
print(d[0][1])

for i in person.values():
    print(i)
for k,v in person.items():
    print(k,v)

#WHILE LOOP:-
n=int(input("enter n value: "))
i=0
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)