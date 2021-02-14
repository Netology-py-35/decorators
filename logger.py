from datetime import datetime


def logger(function):
    def wrapper(*args):
        result = function(*args)
        with open('function.log', 'a') as f:
            f.write(f'{datetime.now().strftime("%c")} | {function.__name__} |  {args} | {result}' + '\n')
        return result
    return wrapper


def logger2(log_path):
    def logger(function):
        def wrapper(*args):
            result = function(*args)
            with open(log_path, 'a') as f:
                f.write(f'{datetime.now().strftime("%c")} | {function.__name__} |  {args} | {result}' + '\n')
            return result

        return wrapper

    return logger


@logger2('example.log')
def new_hello(s):
    return s


@logger
def hello(a):
    return a


if __name__ == '__main__':
    print(hello('asdfg'))
    print(new_hello('Hello Logger'))
