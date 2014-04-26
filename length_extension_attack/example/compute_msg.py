#!/usr/bin/env python

from sys import argv, stdout

# 64 is for the full padding
# minus 8 to be able to store data length
BLOC_SIZE = 56

if __name__ == "__main__" :

    if len(argv) != 4 :
        print ('Usage: {} <message> <extension> <key_size>'.format(argv[0]))
        exit()

    message = argv[1]
    extension = argv[2]
    key_size = int(argv[3])

    pad_len = BLOC_SIZE - key_size - len(message) - 1

    padding = '\\x80' + '\\x00' * pad_len + '\\' + hex((len(message) + key_size) * 8)[1:] + '\\x00' * 7
    final_msg = message + padding + extension

    stdout.write(final_msg)


