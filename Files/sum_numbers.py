import sys


def main():
    with open(sys.argv[1], 'r') as f:
        result = 0
        data = str(f.read()).split(" ")
        for x in data:
            if x != '\n':
                result += int(x)
        print(result)

if __name__ == '__main__':
    main()
