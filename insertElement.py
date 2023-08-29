def insert_element(lst, element, index=0):
    """
       Objective : Insert an element in sorted list
       Input Parameter : lst - Our sorted list
                         index - Represents index of list elements
                         element -


    """
    if element < lst[index]:
        lst.insert(index, element)
    elif lst[index] <= element < lst[index + 1]:
        lst.insert(index + 1, element)
    elif element > lst[len(lst) - 1]:
        lst.insert(len(lst), element)
    else:
        insert_element(lst, element, index + 1)
