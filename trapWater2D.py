
def trapWater(nlist):
    lmax=rmax=0
    lkey,rkey=0,len(nlist)-1
    res=0

    while lkey<rkey:
        lmax=max(lmax,nlist[lkey])
        rmax=max(rmax,nlist[rkey])

        if (lmax<rmax):
            res+= lmax-nlist[lkey]
            lkey+=1
        else:
            res+= rmax-nlist[rkey]
            rkey-=1
    return res
nlist=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trapWater(nlist))
