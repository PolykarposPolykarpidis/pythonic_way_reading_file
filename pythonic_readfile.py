def read_a_line_from_file(path):
    file_obj = open(path, "r")
    file_obj_iter = iter(file_obj)
    while True:
        try:
            n =  next(file_obj_iter)
            yield n
        except StopIteration:
            file_obj.close()
            break


def main_function(filepath):
    for line in read_a_line_from_file(filepath):
            print(line)


if '__main__' == __name__:
    # Lets see an example. 
    filepath = 'file.txt'
    main_function(filepath)
    
