def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list_int = []
    for i in data.split(','):
        list_int.append(int(i))
    return list_int
    
print(main(open('txt_file/data01.txt').read()))
# Read data from file