# Given a list arr of N integers, print sums of all subsets in it.
#
# Note: Return all the element is increasing order.

def sums(lst,c,sum):
    if(c>len(lst)-1):
        print(sum)
        return
    else:
        sums(lst,c+1,sum+lst[c])
        sums(lst,c+1,sum)

lst=list(map(int,input().split()))
sums(lst,0,0)