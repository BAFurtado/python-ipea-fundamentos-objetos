

def is_even(num: int) -> bool:
    # your code here
    return num % 2 == 0


if __name__ == '__main__':
    valor_teste = 4
    print(f"{valor_teste} is even: {is_even(valor_teste)}:")

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print('Testes passed!')
