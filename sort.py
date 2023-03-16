def sort_dictionary(dict):
    try: 
        dict = sorted(dict.items(),key=lambda dict: dict[1][1])
        l = []
        for i in dict:
            l.append((i[0],i[1][0]))
        return l
    except:
        return {}
