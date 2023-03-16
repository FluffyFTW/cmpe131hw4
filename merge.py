def merge(arr1, arr2):
    sorted(arr1)
    sorted(arr2)
    out = []
    while(len(arr1) and len(arr2)):
        try:
            if(arr1[0] < arr2[0]):
                out.append(arr1[0])
                arr1.pop(0)
            else:
                out.append(arr2[0])
                arr2.pop(0)
        except:
            return TypeError
    if(len(arr1)):
        out.extend(arr1)
        arr1.clear()
    elif(len(arr2)):
        out.extend(arr2)
        arr2.clear()
    return out