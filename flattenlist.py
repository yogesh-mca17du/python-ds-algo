lst = [10, 20, [25, 30], 40, [50, 70], 80]
flat_list = []


def flatten(nested_list, index=0):
    """
      Objective : To flat a nested list
      Input Parameter : nested_list - A nested list to be flattened
                        index - index of list element
      Approach : using recursion and type() function
    """
    if index == len(nested_list):
        return flat_list
    elif type(nested_list[index]) == list:
        n = len(nested_list[index])
        for i in range(n):
            flat_list.append(nested_list[index][i])
        return flatten(nested_list, index + 1)
    else:
        flat_list.append(nested_list[index])
        return flatten(nested_list, index + 1)


if __name__ == "__main__":
    print("flattened list is", flatten(lst, 0))
