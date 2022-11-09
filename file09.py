def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    for i in data:
        if i.isdigit():
            s.append(int(i))
    return min(s)
print(main(open('txt_file/data09.txt').read()))
# Read data from file