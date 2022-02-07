def top_n(items,n):
    """ Returns top n items in an array in descending order

    Args:
    items(array): list or array like object
    n(int): number of items to return

    Return:
    array:top_n items in desc oorder

    Egs:
    top_n([1,4,5,7], 2)
    [7,5]
    
    """
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j]> items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    top_n=items[-n:]

    return top_n[::-1]
