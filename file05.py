def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    s=0
    d=0
    list1=[s,d]
    for i in data:
        if i.isdigit():
            s+=1
    for i in data:
        if not(i.isdigit()):
            d+=1
        list1=[s,d]
    return list1
print(main(open('txt_file/data05.txt','r').read()))


# Read data from file