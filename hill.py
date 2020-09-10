import math
import numpy
from sympy import Matrix

print("Note - while specifying key, ensure that its inverse exists otherwise message can't be encrypted or decrypted")

while 1:
    message = input("Message:- ")
    str = message.lower().replace(" ", "")
    key = input("key:- ")
    key = key.lower().replace(" ", "")

    alphabets = list(map(chr, range(97, 123)))
    message_list = list(str)
    last_ele = str[-1]
    ele_add = chr(ord(last_ele) + 1)
    new_list_add = []
    len_msg = len(message_list)
    pos_msg = []
    key_list = list(key)
    len_key = len(key_list)
    pos_key = []

    root = math.sqrt(len_key)
    # extending the list of key such that it total elements equals n*n
    if root > int(root):
        root = int(root) + 1
        new_len_key = int(math.pow(int(root), 2))
        l_add = new_len_key - len_key
        key_list.extend(map(chr, range(97, 97 + l_add)))
    else:
        root = int(root)
        new_len_key = len_key

    for l in range(0, new_len_key):
        pos_key.append(alphabets.index(key_list[l]))

    key_mat = numpy.array(pos_key).reshape(int(root), int(root))  # nice one - key matrix shaped in n*n

    # extending the list of message till it's total elements are completely divisible by n
    if (len_msg % root) != 0:
        l_add_msg = root - (len_msg % root)
        new_len_msg = len_msg + l_add_msg
        for i in range(0, l_add_msg):
            new_list_add.append(ele_add)
        message_list.extend(new_list_add)
        new_message_list = message_list
    else:
        new_len_msg = len_msg
        new_message_list = message_list

    for l in range(0, new_len_msg):
        pos_msg.append(alphabets.index(new_message_list[l]))

    pos_msg = [pos_msg[i:i + int(root)] for i in range(0, len(pos_msg), int(root))]  # list converted to sublist

    pos_msg = numpy.array(pos_msg)
    pos_msg_transpose = pos_msg.transpose()

    def hill_encrypt():
        cipher_mat = numpy.dot(key_mat, pos_msg_transpose) % 26

        cipher_mat = numpy.array(cipher_mat)
        cipher_mat_transpose = cipher_mat.transpose()

        encrypted_list = []
        for elem in cipher_mat_transpose:
            encrypted_list.extend(elem)

        en = []
        for i in range(0, new_len_msg):
            en.append(alphabets[encrypted_list[i]])
        print("encrypted text - " + "".join(en))

    def hill_decrypt():
        key_mat_adj = Matrix(key_mat).inv_mod(26)
        numpy.key_mat_adj = numpy.array(key_mat_adj)

        decrypted_mat = numpy.dot(key_mat_adj, pos_msg_transpose) % 26

        decrypted_mat = numpy.array(decrypted_mat)
        decrypted_mat_transpose = decrypted_mat.transpose()

        decrypted_list = []
        for elem in decrypted_mat_transpose:
            decrypted_list.extend(elem)

        de = []
        for i in range(0, new_len_msg):
            de.append(alphabets[decrypted_list[i]])
        print("decrypted text - " + "".join(de))

    print("To Encrypt message - 1\n"
          "To Decrypt message - 2")

    def default():
        print("invalid option!")

    x = int(input("Specify Option:- "))
    if x == 1:
        hill_encrypt()
    elif x == 2:
        hill_decrypt()
    else:
        default()