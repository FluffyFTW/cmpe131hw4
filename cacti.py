def cacti_number(arr):
    maxlength = len(arr)
    maxheight = len(arr[0])
    valid_spaces = 0
    for y in range(maxheight):
        for x in range(maxlength):
            if (_is_available(arr,x,y)):
                valid_spaces += 1
    return valid_spaces


def _is_available(arr,x,y):
    if(arr[x][y] == 1 ):
        return False
    else:
        try:
            if(arr[x + 1][y] == 1):
                return False
        except IndexError:
            pass
        try:
            if(arr[x][y + 1] == 1):
                return False
        except IndexError:
            pass
        if(x and arr[x - 1][y] == 1):
            return False
        if(y and arr[x][y - 1] == 1):
            return False
        arr[x][y] = 1
        return True