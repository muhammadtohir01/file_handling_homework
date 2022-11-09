def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list_data = open('txt_file/'+data).read()
    list_str = list_data.split(',')
    list_int = []
    for i in list_str:
        list_int.append(int(i))
    
    return list_int
    
print(main('data01.txt'))