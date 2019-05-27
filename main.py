from hello import hello
from calculator import calc

def main():
    hello.hello_world("pveronezi")
    print('sum 2 numbers: {}'.format(calc.sum(3, 4)))


if __name__ == '__main__':
    main()

# TODO: commit to master, then publish again. 
