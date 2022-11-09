def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list_data = open(data).read()
    list_str = list_data.split(',')
    list_int = []
    for i in list_str:
        list_int.append(int(i))
    
    return list_int
    
print(main('txt_file/data01.txt'))
# Read data from file