from hello import hello
from calculator import calc
import argparse

print("START")
parser = argparse.ArgumentParser(description = "For Cloud ML Engine")

parser.add_argument('--train_data_paths', action = 'store',dest = 'train_data_paths', required=True)
parser.add_argument('--train_steps')
args = parser.parse_args()
print(type(args))
def main():
    print(args.train_data_paths)
    # hello.hello_world(args['train_data_paths'])
    print('sum 2 numbers: {}'.format(calc.sum(3, 4)))


if __name__ == '__main__':
    main()

# TODO: commit to master, then publish again.
