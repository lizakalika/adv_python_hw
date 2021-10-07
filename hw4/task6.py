import time

def logging(file_path):
    def actual_logging(func):
        @wraps(func)
        def log(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            stop = time()
            write_res = result if result else '-'
            with open(file_path, 'a') as f:
                f.writelines([
                        func.__name__ + '\n',
                        str(start) + '\n',
                        (''.join(map(str, args)) + 
                        ' '.join(map(lambda k: str(k[0]) + ' = ' + str(k[1]), kwargs.items())) + '\n'),
                        str(write_res) + '\n',
                        str(stop) + '\n',
                        str(stop - start) + '\n',
                        '\n'
                    ])
            return result
        return log
    return actual_logging
