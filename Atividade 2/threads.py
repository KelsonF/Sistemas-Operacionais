import threading

def print_numbers():
    for i in range(10):
        print(i)

def print_letters():
    letters = 'abcdefghij'
    for letter in letters:
        print(letter)

if __name__ == '__main__':
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
