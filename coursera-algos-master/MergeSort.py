# -*- coding: utf-8 -*-
"""
Sorting using mergesort for Coursera Algorithms course part 1

@author: dyanni3
"""

#%%
#import the txt file...
results = []
with open('C:\\Users\\dyanni3\\Desktop\\list.txt') as inputfile:
    for line in inputfile:
        results.append(int(line.strip().split('\n')[0]))

#%%
def sort(A):
#inputs: an array A of length n
#returns: sorted A by mergeSort algorithm
    
    #base case
    if len(A)<2:
        return A
    
    #merge subroutine
    def merge(B,C):
    #inputs two sorted arrays and merges them together- return a big sorted array
    
        #preallocate for the return array
        n=len(B)+len(C);
        D=[0 for index in range(n)];
        
        #walk through B and C in parallel, putting elements into D in the appropriate order...  
        #introduce indices to keep track of where we are in array B and array C
        B_index=0; C_index=0;
        
        for k in range(n):
            
            #check whether we've exhausted either of the small arrays
            if B_index>=len(B): #then finish copying from C without further thought
                D[k]=C[C_index];
                C_index+=1;
            elif C_index>=len(C): #then finish copying from B without further thought
                D[k]=B[B_index];
                B_index+=1;
             
            #otherwise compare which small array has the lesser value at current indices, put that value into D 
            elif (B[B_index]<C[C_index]):
                D[k]=B[B_index];
                B_index+=1;
            else:
                D[k]=C[C_index];
                C_index+=1;
                
        return D
        
    #divide into subproblems     
    leftArray=A[:int(len(A)/2)]; 
    rightArray=A[int(len(A)/2):]; 
    
    #conquer subproblems
    leftArray=sort(leftArray)#,left_length);
    rightArray=sort(rightArray)#,right_length);
    
    #return stitched together solution
    return merge(leftArray,rightArray)
    
#%%    
def sort_and_count(A):
    #inputs an array A of length n and returns sorted A by mergeSort algorithm and number of inversions
    
    #base case
    if len(A)<2:
        return A,0
    
    #merge_and_count subroutine
    def merge_and_count(B,C):
        #inputs two sorted arrays and merges them together while counting the number of inversions
        #returns a big sorted array and number of inversions
        
        #initialization type stuff
        n=len(B)+len(C);
        D=[0 for index in range(n)];
        i=0; j=0;
        num_inversions=0;
        
        #main merging loop: walking through two half-lists in parallel comparing elements and pasting them into output array
        for k in range(n):
            
            if i>=len(B): #finish copying from C, have already exhausted elements in B
                D[k]=C[j];
                j+=1;
                
            elif j>=len(C): #finish copying from B, have already exhausted elements in C
                D[k]=B[i];
                i+=1;
                
            elif (B[i]<C[j]):
                D[k]=B[i];
                i+=1;
            else:
                D[k]=C[j];
                j+=1;
                num_inversions+=len(B)-i
                
        return D,num_inversions
        
    #divide into subproblems     
    leftArray=A[:int(len(A)/2)]; 
    rightArray=A[int(len(A)/2):]; 
    
    #conquer subproblems
    leftArray,x=sort_and_count(leftArray)
    rightArray,y=sort_and_count(rightArray)

    #stitch together solutions to subproblems and return result
    merged,num_inversions=merge_and_count(leftArray,rightArray)
    num_inversions=x+y+num_inversions;
    return merged,num_inversions