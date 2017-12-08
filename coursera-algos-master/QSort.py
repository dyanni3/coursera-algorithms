# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 21:51:18 2016
QuickSort as taught in Tim Roughgarden algorithms course
@author: dyanni3
"""

def QSort(A,method):
    #takes an unsorted array input A. Returns a sorted *numpy* array
    
    import numpy as np
    
    #base case
    if len(A)<3:
        if len(A)==2 and A[0]>A[1]:
            return 1, np.array([A[1],A[0]])
        elif len(A)==2 and A[0]<A[1]:
            return 1,np.array(A)
        return 0,A
        
    #define subroutines--------------------
    def Partition(A,p):
        #partitions a list into [..<A[p]....A[p]....>A[p]..] 
        #given an unsorted list and an index p returns partitioned list and the true index of A[p]
    
        # initially the data is [..some >A[p] and some less than A[p] all mixed ]
    
        i=1; #index of first known element greater than A[p]
        j=1; #index of first undiscovered element
        slot=None
        
        #swap A[p] with A[0]
        slot=A[0]
        A[0]=A[p]
        A[p]=slot    
        
        # now data looks like [A[p], len(A)-1 mixed data entries]
        
        #primary loop of Partition
        while(j<len(A)):
            """if A[j]>A[p]: #great, do nothing
                pass"""
            if A[j]<A[0]: #swap A[i] and A[j]
                slot=A[i]
                A[i]=A[j]
                A[j]=slot
                i+=1
            j+=1
            
        # now the data looks like [A[p],<A[p],<A[p],...,>A[p],>A[p],...]
        
        #swap A[]
        slot=A[0]
        A[0]=A[i-1]
        A[i-1]=slot
        
        # now the data looks like [<A[p],<A[p],...,A[p],>A[p],>A[p],...]
        return A,i-1
     

    def ChoosePivot(A,method='random'): #chooses a pivot, using 'method'
        """method='random' chooses pivots at random
        """
        if method=='random':
            return np.random.randint(0,len(A)-1)
        elif method=='first':
            return 0
        elif method=='last':
            return len(A)-1
        elif method=='median':
            if len(A)%2==1:
                first=A[0]
                middle=A[int(len(A)/2)]
                last=A[-1]
            else:
                first=A[0]
                middle=A[int(len(A)/2)-1]
                last=A[-1]
            _,Q=QSort([first,middle,last],'random')
            if Q[1]==first:
                return 0
            elif Q[1]==middle:
                if len(A)%2==1:
                    return int(len(A)/2)
                else:
                    return int((int(len(A))/2)-1)
            else:
                return len(A)-1
                
        
    
    #main
    n=len(A)-1 #number of comparisons made at "level 0"
    p=ChoosePivot(A,method) # O(1)
    A,p=Partition(A,p) # O(len(A))
    n_left, A_left=QSort(A[:p],method); A[:p]=A_left; #recursive call O(len(A_left)*log(len(A_left)))
    n+=n_left #add number of comparisons made at all subsquent levels to the left
    n_right,A_right=QSort(A[p+1:],method); A[p+1:]=A_right;
    n+=n_right #add number of comparisons made at all subsequent levels to the right
    
    return n,np.array(A)
    
results = []
with open('QSort.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split('\n'))
results=[int(x[0]) for x in results]