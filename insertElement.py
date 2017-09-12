def insertElement(lst,element,indx=0):
    '''
       Objective : Insert an elemnt in sorted list
       Input Parameter : lst - Our sorted list
                         indx - Represents index of list elements
                         element -


    '''
    if(element<lst[indx]):
        lst.insert(indx,element)
    elif(lst[indx]<= element and lst[indx+1] > element):
        lst.insert(indx+1,element)
    elif(element >lst[len(lst)-1]):
        lst.insert(len(lst),element)      
    else:
        insertElement(lst,element,indx+1)
