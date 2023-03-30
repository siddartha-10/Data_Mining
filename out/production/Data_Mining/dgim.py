def input_bin_stream(Input):
    binary_file = open("Binary_Input.txt", "w") #this file stores the 0/1 stream
    bin_stream = []

    # converting the letters to 0/1 stream
    for i in Input:
        if (ord(i) in range(65, 91) or ord(i) in range(97, 123)):
            if (ord(i) % 2 == 0):
                bin_stream.append(0)
            else:
                bin_stream.append(1)

    # storing the binary stream into the Binary_Input file
    count = 0
    for x in bin_stream:
        binary_file.write("%i" % x)
        count = count + 1
        if (count == 32):
            binary_file.write("\n")
            count = 0

    binary_file.close()
    print(len(bin_stream))
    return bin_stream
string_input = input("Hey please enter the string \n")
print(string_input)
