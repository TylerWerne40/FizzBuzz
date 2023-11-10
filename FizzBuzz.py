

words = {       # words to be used. keys are the values to says the words on multiples of the key.
    '3': "Fizz",
    '5': "Buzz",
    '7': "Bazz"
}

def fizz_buzz(datum: int) -> str:
    """
    Run fizz buzz on an integer

    Args:
        datum (int): data to run fizz buzz on

    Returns:
        str: string to return
    """    
    string = ''
    for i in words.keys():
        if datum%int(i) == 0:
            string += words[i]
    if string == '':
        string = str(datum)

    return string


def main():
    """
    Main function : starts here.
    """    
    data = range(1,100)
    for i in data:
        print(fizz_buzz(i))


if __name__ == '__main__':
    main()