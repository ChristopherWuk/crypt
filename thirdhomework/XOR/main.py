import re


def encode(text1, keys):
    lentext = len(text1)
    lenkeys = len(keys)
    keys = lentext // lenkeys * keys + keys[0:lentext % lenkeys]
    code1 = []
    for i in range(len(keys)):
        code1.append(chr(ord(text1[i]) ^ ord(keys[i])))
    print(''.join(code1))


def decode(text2, keys):
    lentext = len(text2)
    lenkeys = len(keys)
    keys = lentext // lenkeys * keys + keys[0:lentext % lenkeys]
    code2 = []
    for i in range(len(keys)):
        code2.append(chr(ord(text2[i]) ^ ord(keys[i])))
    print(''.join(code2))


def main():
    input_str = input('What you wanna do? 1:encode 2:decode 3:quit\n')

    if input_str == '1':
        text1 = input('Please input your message which you want to encrypt it:\n')
        keys = input('Please input your keys:\n')
        encode(text1, keys)
        main()
    elif input_str == '2':
        text2 = input('Please input the ciphertext:\n')
        keys = input('Please input your keys:\n')
        decode(text2, keys)
        main()
    elif input_str == '3':
        quit()
    else:
        print('Please choose a correct number.\n')
        main()


if __name__ == '__main__':
    main()
