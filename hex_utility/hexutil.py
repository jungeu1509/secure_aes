import binascii
import sys

def hexlify(mode, input_file, output=''):
    if mode=='0':
        try:
            data_f = open(input_file, 'rb')
            data = data_f.read()
            data_f.close()
            print("hexlify with input data")
        except FileNotFoundError:
            data = input_file
            print("hexlify with data")

        if output == "":
            print(binascii.hexlify(data))
            return binascii.hexlify(data)
        else:
            print(binascii.hexlify(data))
            output_f = open(output, 'wb+')
            output_f.write(binascii.hexlify(data))
            print("write success")
            return

    elif mode=='1':
        try:
            data_f = open(input_file, 'r')
            data = data_f.read()
            data_f.close()
            print("unhexlify with input data file")
        except FileNotFoundError:
            data = input_file
            print("unhexlify with input data")

        if output == "":
            print(binascii.unhexlify(data))
            return binascii.unhexlify(data)
        else:
            print(binascii.unhexlify(data))
            output_f = open(output, 'wb+')
            output_f.write(binascii.unhexlify(data))
            print("write success")
            return

    else:
        usage()
        print("mode : " + mode + " / input_file : " + input_file + " / output : " + output)

def usage():
    print("how to use")
    print("hexlify.py mode data (output)")
    print("--------------------------------------------------------")
    print("mode : 0(Hex to String(ASCII)), 1(String to Hex)")
    print("data : Input data or data file")
    print("output : If you input filename")
    print("--------------------------------------------------------")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
    else:
        hexlify(*sys.argv[1:])