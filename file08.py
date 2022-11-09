def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    for i in data:
        if i.isdigit():
            s.append(int(i))
    return max(s)
print(main(open('txt_file/data08.txt').read()))
# Read data from file