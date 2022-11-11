def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1=[]
    for i in data:
        if i.isalpha():
            list1.append(i)
        if i==('\n'):
            list1.append(i)
    return list1
print(main(open('txt_file/data04.txt').read()))
