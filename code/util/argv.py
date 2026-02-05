import sys

def main(argv):
    print(argv)

if __name__ == "__main__":
    main(sys.argv)

def dealing_with_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

dealing_with_args(1, 2, 3, a=4, b=5)

def add(a, b):
    print(a + b)

def wrapper(*args, **kwargs):
    print("Before function call")
    add(*args, **kwargs)
    print("After function call")

wrapper(1, 2)




    