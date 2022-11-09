def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    i=0
    while i<len(data):
        if data[i].isdigit():
            s.append(int(data[i]))
        i+=1
    return sum(s)
print(main(open('txt_file/data07.txt').read()))
# Read data from file