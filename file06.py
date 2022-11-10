def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    d = data.split('\n')
    s = []
    for i in d:
        s.append(len(i))
        
    return s
print(main(open('txt_file/data06.txt').read()))
# Read data from file