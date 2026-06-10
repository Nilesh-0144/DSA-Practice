# arr = [2, 7, 4, 5, 3, 4]
# target = 9
# new = {}

# for i in range(len(arr)):
#     com = target - arr[i]

#     if com in new:
#         print([new[com], i])
#         break

#     new[arr[i]] = i
s="absabsghlkj"

ans={}
for i in range(len(s)) :
    ans[s[i]]=ans.get(s[i],0)+1
    
string=input("Enter a character if you want the frequency:")
print(f"the frequency  of '{string}' is {ans.get(string,0)}")
print(ans)