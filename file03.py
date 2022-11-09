def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1=[]
    for i in data:
        if i.isdigit():
            list1.append(i)
    return list1
print(main(open('txt_file/data03.txt').read()))
