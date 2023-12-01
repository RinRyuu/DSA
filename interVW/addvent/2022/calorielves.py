import os


def main():
    with open('inputofday1.txt', 'r') as file:
        for i in range(20): #2253
            list = []
            line = file.readline()
            if line.isnumeric():
                list.append(line)
            elif line.startswith('\n'):
                print(line, end='')
        

    

if __name__ == "__main__":
    main()