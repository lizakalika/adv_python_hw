def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    data = '\n'.join(array)
    
    with open('file_name','w') as ouf:
        ouf.write(data)
    pass
