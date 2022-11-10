def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    d=data.split('\n')
    s=[]
    for i in d:
        if i.isalpha():
            s.append(len(i))
        else:
            not(i.isalpha())
            s.append(len(i))
    return max(s)
print(main(open('txt_file/data10.txt').read()))