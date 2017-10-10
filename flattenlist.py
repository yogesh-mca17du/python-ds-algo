lst=[10,20,[25,30],40,[50,70],80]
flatlist=[]
def flatten(lst,index=0):
    '''
      Objective : To flat a nested list
      Input Parameter : lst - A nested list to be flattened
                        index - index of list element
      Approch : using recursion and type() functioon
    '''
    if index==len(lst):
        return flatlist
    elif type(lst[index])==list:
         n=len(lst[index])
         for i in range(n):
             flatlist.append(lst[index][i])
         return flatten(lst,index+1)
    else:
         flatlist.append(lst[index])
         return flatten(lst,index+1)

print("flattened list is",flatten(lst,0))
