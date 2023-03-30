#class Bucket stores no of 1's as its size and the rightmost 1 as its timestamp
class Bucket:
    def __init__(self, size, time_stamp):
        self.size = size
        self.time_stamp = time_stamp

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

def intial_buckets(bin_stream):
    output_file = open("Final_Output.txt", "w")
    a_c_file = open("Actual_count.txt", "w")
    bucketList = []

    
    oc = 0  # one count
    c = 0
    n = 0
    bucket_counter = 0
    for x in bin_stream:
        if (x == 1):
            c = c + 1
            oc = oc + 1
            if (c == 8 or c == 12 or c == 16 or c == 18 or c == 19):
                bucketList.append(Bucket(oc, n + 1))  # creating intial buckets for first 32 bits
                oc = 0
                bucket_counter = bucket_counter + 1

            output_file.write("%i " % c)
            a_c_file.write("%i " % c)
        else:
            output_file.write("%i " % c)
            a_c_file.write("%i " % c)

        n = n + 1
        if (n == 32):
            output_file.write("\n")
            a_c_file.write("\n")
            break
    merge_and_estimate(bucketList, bin_stream, bucket_counter, output_file)
    actual_count(bin_stream, a_c_file)

#counts the actual no of 1's for every bit entering into the last 32 bits
def actual_count(bin_stream, a_c_file):
    ac = 0
    d = 0
    j = 1
    for x in range(32, len(bin_stream)):
        for y in range(j, x + 1):
            if (bin_stream[y] == 1):
                ac = ac + 1
        a_c_file.write("%i " % ac)
        ac = 0
        d = d + 1
        j = j + 1
        if (d == 32):
            a_c_file.write("\n")
            d = 0

#counts no of 1's for every bit entering into the last 32 bit stream using buckets
def merge_and_estimate(bucketList, bin_stream, bucket_counter, output_file):
    z = 32  # sliding window size
    d = 0
    for x in range(32, len(bin_stream)):
        sum = 0
        if (bin_stream[x] == 1):
            bucketList.append(Bucket(1, x + 1))
            bucket_counter = bucket_counter + 1
            bc = bucket_counter
            while (bc != 0):
                if (bc - 3 >= 0):
                    if (bucketList[bc - 3].size == bucketList[bc - 1].size): #checks if the size appears 3rd time
                        size = bucketList[bc - 2].size
                        bucketList[bc - 2].size = size * 2
                        del bucketList[bc - 3]
                        bucket_counter = bucket_counter - 1
                bc = bc - 1
        b_s = bucket_counter
        while (b_s > 0): #estimate for every new bit into the last 32 bit stream
            l = bucketList[bucket_counter - 1].time_stamp - z
            k = bucketList[b_s - 1].time_stamp
            if (k > l):
                sum += bucketList[b_s - 1].size
            else:
                sum += int(bucketList[b_s - 1].size / 2)
                break
            b_s = b_s - 1
        d = d + 1
        output_file.write("%i " % sum)
        if (d == 32):
            output_file.write("\n")
            d = 0



text = """In the 1990’s “data mining” was an exciting and popular new concept. Around 2010, people
instead started to speak of “big data.” Today, the popular term is “data science.” However,
during all this time, the concept remained the same: use the most powerful hardware, the most
powerful programming systems, and the most efficient algorithms to solve problems in science,
commerce, healthcare, government, the humanities, and many other fields of human endeavor.
To many, data mining is the process of creating a model from data, often by the process of
machine learning, which we mention in Section 1.1.3 and discuss more fully in Chapter 12.
However, more generally, the objective of data mining is an algorithm. For instance, we discuss
locality-sensitive hashing in Chapter 3 and a number of stream-mining algorithms in Chapter 4,
none of which involve a model. Yet in many important applications, the hard part is creating the
model, and once the model is available, the algorithm to use the model is straightforward."""

bin_stream = input_bin_stream(text)
intial_buckets(bin_stream)