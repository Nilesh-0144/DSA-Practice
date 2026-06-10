n=[1,2,3,1,43,13,41,4,2,3]
m=[23,1,4,56,3,2,55]

freq={}

for num in n:
    freq[num]=freq.get(num,0)+1

for num in m:
    print(num,"->",freq.get(num,0))