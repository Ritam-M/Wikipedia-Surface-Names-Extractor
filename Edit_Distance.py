import json

with open('Correct_List_gr1.json') as file:
    CL = json.load(file)
    file.close()

with open('Dict_ru.json') as file:
    Dict = json.load(file)
    file.close()

def editDistDP(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return(dp[m][n])

c = 0

count=0
ED = {}
j = len(Dict)
for k,v in Dict.items():
    '''
    if(len(v)==1):
        c+=1
        print(c/j)
        ED1[k]={}
        L= list(v.keys())
        if(k==L[0]):
            ED1[k][L[0]]=0
            count+=1
        else:
            ED1[k][L[0]]=editDistDP(k,L[0])
    '''
    if(len(v)>1):
        c+=1
        print(c/j)
        L = list(v.keys())
        ED[k] = {}

        for l in L:
            min_dist = 1000000000
            if(l in CL[k]):
                ED[k][l]=0
            else:
                for m in list(CL[k].keys())[:5]:
                    min_dist = min(min_dist, editDistDP(l,m))
                ED[k][l] = min_dist

    if(c%50000000==0):
       with open('ED_gr1.json','w') as file:
           json.dump(ED,file)
           file.close()

with open('ED_gr1.json','w') as file:
    json.dump(ED,file)
    file.close()
