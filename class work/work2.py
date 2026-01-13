def merl(l1,l2):
    i=0
    j=0
    r=[]
    while i<len(l1) and j<len(l2):
        if l2[j]<l1[i]:
            r.append(l2[j])
            j+=1
        else:
            r.append(l1[i])
            i+=1
    while i<len(l1):
        r.append(l1[i])
        i+=1
    while j<len(l2):
        r.append(l2[j])
        j+=1
    return r
def sor(l1):
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[j]<l1[i]:
                l1[i],l1[j]=l1[j],l1[i]
    return l1
def sore(l2):
    for i in range(len(l2)):
        for j in range(i+1,len(l2)):
            if l2[j]<l2[i]:
                l2[i],l2[j]=l2[j],l2[i]
    return l2
l1=[1,2,9]
l1=sor(l1)
l2=[3,1,4,2,9]
l2=sore(l2)
merl(l1,l2)