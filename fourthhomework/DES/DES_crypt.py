from DES.DESSET import *
import re


# IP置换
def IPchange(inputstr):
    newstr = ""
    for i in IP:
        newstr += inputstr[i - 1]
    return newstr


# 逆IP置换
def REIPchange(inputstr):
    newstr = ""
    for i in ReIP:
        newstr += inputstr[i - 1]
    return newstr


def e_change(inputstr):
    newstr = ""
    for i in E:
        newstr += inputstr[i - 1]
    return newstr


def PC1_change(inputstr):
    newstr = ""
    for i in PC1:
        newstr += inputstr[i - 1]
    return newstr


def PC2_change(inputstr):
    newstr = ""
    for i in PC2:
        newstr += inputstr[i - 1]
    return newstr


def P_change(inputstr):
    newstr = ""
    for i in P:
        newstr += inputstr[i - 1]
    return newstr


def strXOR(str1, str2):
    newstr = ""
    for i in range(0, len(str1)):
        xor_str = int(str1[i], 10) ^ int(str2[i], 10)
        if xor_str == 1:
            newstr += '1'
        if xor_str == 0:
            newstr += '0'
    return newstr


def left_move(str1, num):
    left_str = str1[num:len(str1)]
    left_str = str1[0:num] + left_str
    return left_str


def S_box(str1):
    newstr = ""
    c = 0
    for i in range(0, len(str1), 6):
        now_str = str1[i:i + 6]
        row = int(now_str[0] + now_str[5], 2)
        col = int(now_str[1:5], 2)
        num = bin(S[c][row * 16 + col])[2:]
        for gz in range(0, 4 - len(num)):
            num = '0' + num
        newstr += num
        c += 1
    return newstr


def function_F(inputstr, key):
    first = e_change(inputstr)
    second = strXOR(first, key)
    third = S_box(second)
    fourth = P_change(third)
    return fourth


def genKey(key):
    keylist = []
    divide_output = PC1_change(key)
    Key_CO = divide_output[0:28]
    Key_D0 = divide_output[28:]
    for i in LeftMove:
        key_c = left_move(Key_CO, i)
        key_d = left_move(Key_D0, i)
        key_output = PC2_change(key_c + key_d)
        keylist.append(key_output)
    return keylist


def write_in_file(str2write):
    try:
        f = open('DES.txt', 'w', encoding='utf-8')
        f.write(str2write)
        f.close()
        print("output success:)")
    except IOError:
        print('something wrong:(')


def read_out_file():
    try:
        f = open('DES.txt', 'r', encoding='utf-8')
        str2read = f.read()
        f.close()
        print("read file success:)")
        return str2read
    except IOError:
        print('something wrong:(')


def str2bin(message):
    res = ""
    for i in message:
        tmp = bin(ord(i))[2:]
        for j in range(0, 8 - len(tmp)):
            tmp = '0' + tmp  # 把输出的b给去掉
        res += tmp
    return res


def bin2str(inputstr):
    res = ""
    tmp = re.findall(r'.{8}', inputstr)
    for i in tmp:
        res += chr(int(i, 2))
    return res


def des_encrypt_one(bin_message, bin_key):
    mes_ip_bin = IPchange(bin_message)
    key_lst = genKey(bin_key)
    mes_left = mes_ip_bin[0:32]
    mes_right = mes_ip_bin[32:]
    for i in range(0, 15):
        mes_tmp = mes_right
        f_result = function_F(mes_tmp, key_lst[i])
        mes_right = strXOR(f_result, mes_left)
        mes_left = mes_tmp
    f_result = function_F(mes_right, key_lst[15])
    mes_fin_left = strXOR(mes_left, f_result)
    mes_fin_right = mes_right
    fin_message = REIPchange(mes_fin_left + mes_fin_right)
    return fin_message


def des_decrypt_one(bin_mess, bin_key):
    mes_ip_bin = IPchange(bin_mess)
    key_lst = genKey(bin_key)
    lst = range(1, 16)
    cipher_left = mes_ip_bin[0:32]
    cipher_right = mes_ip_bin[32:]
    for i in lst[::-1]:
        mes_tmp = cipher_right
        cipher_right = strXOR(cipher_left, function_F(cipher_right, key_lst[i]))
        cipher_left = mes_tmp
    fin_left = strXOR(cipher_left, function_F(cipher_right, key_lst[0]))
    fin_right = cipher_right
    fin_output = fin_left + fin_right
    bin_plain = REIPchange(fin_output)
    res = bin2str(bin_plain)
    return res


# 简单判断以及处理信息分组
def deal_mess(bin_mess):
    ans = len(bin_mess)
    if ans % 64 != 0:
        for i in range(64 - (ans % 64)):
            bin_mess += '0'  # 补0
    return bin_mess


# 查看秘钥是否为64位,如不是则补0
def input_key_judge(bin_key):
    ans = len(bin_key)
    if len(bin_key) < 64:
        if ans % 64 != 0:
            for i in range(64 - (ans % 64)):
                bin_key += '0'
    return bin_key


def all_message_encrypt(message, key):
    bin_mess = deal_mess(str2bin(message))
    res = ""
    bin_key = input_key_judge(str2bin(key))
    tmp = re.findall(r'.{64}', bin_mess)
    for i in tmp:
        res += des_encrypt_one(i, bin_key)
    return res


def all_message_decrypt(message, key):
    bin_mess = deal_mess(str2bin(message))
    res = ""
    bin_key = input_key_judge(str2bin(key))
    tmp = re.findall(r'.{64}', bin_mess)
    for i in tmp:
        res += des_decrypt_one(i, bin_key)
    return res


def get_mode():
    print("1.Encrypt")
    print("2.Decrypt")
    mode = input()
    if mode == '1':
        print("Please input the message which you want to encrypt：")
        message = input().replace(' ', '')
        print("Please input your key：")
        key = input().replace(' ', '')
        s = all_message_encrypt(message, key)
        out_mess = bin2str(s)
        print("Encrypted:" + out_mess)
        write_in_file(out_mess)
    elif mode == '2':
        print("Please input your key：")
        key = input().replace(' ', '')
        message = read_out_file()
        s = all_message_decrypt(message, key)
        print("Decrypted：" + s)
    else:
        print("Please input correct mode.")


if __name__ == '__main__':
    while True:
        get_mode()
