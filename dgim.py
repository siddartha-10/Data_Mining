# input1 = list(map(int,input("Please input the data stream separated by spaces ").split()))
# print(len(input1))
# print("Input is ", input1)
# k = int(input("Enter the value of k : "))
# bucket_list = []
# count_bucketsize = {}

# start_ind =0
# end_ind = 0
# pair = 0

# for i in range(len(input1)):
#     binary_bit = input1[i]
#     if(binary_bit == 1):
#         if(pair == 1):
#             end_ind = i
#             pair = 0
#             bucket_list.append((start_ind,end_ind,2))
#             if 2 in count_bucketsize:
#                 count_bucketsize[2]+=1
#             else:
#                 count_bucketsize[2] = 1
#             for ct in count_bucketsize.keys():
#                 if(count_bucketsize[ct]>2):
#                     s2,e2,size2 = bucket_list.pop(-2)
#                     s1,e1,size1 = bucket_list.pop(-2)
#                     bucket_list.insert(-1,(s1,e2,size1*2))
#                     count_bucketsize[ct]-=2
#         else:
#             start_ind = i
#             pair = 1


# print ("List of Bucket Indexes Are : ",bucket_list)
# starts = []
# ends = []
# for s,e,size in bucket_list:
#     starts.append(s)
#     ends.append(e)

# print ("Buckets are ",end="")

# for i in range(len(input1)):
#     binary_bit = input1[i]
#     if(i in starts):
#         print (" " ,binary_bit,end="")
#     elif(i in ends):
#         print (binary_bit,end= " ")
#     else:
#         print (binary_bit,end = " ")

# print("")


# length = len(input1)

# bound1 = length-1-k
# bound2 = length-1

# count_1 = 0

# for s,e,size in bucket_list[::-1]:
#     if(s<bound1 and e < bound1):
#         break
#     elif(s<=bound1 and e >= bound1):
#         count_1 +=int(size/2)
#     elif(s>=bound1 and e >= bound1):
#         count_1 += size
#     else:
#         continue



# print("Last",k,"binary bits have",count_1,"Ones")



from collections import defaultdict

def add_timestamp(bucket_timestamps, bucket_counts, timestamp, bucket):
    timestamp_next_bucket = bucket_timestamps[bucket][1]
    if (bucket_timestamps[bucket][0] == 0 and bucket_timestamps[bucket][1] == 0) or \
            (bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] != 0):
        bucket_timestamps[bucket][0] = timestamp
        bucket_timestamps[bucket][1] = 0
    elif bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] == 0:
        bucket_timestamps[bucket][1] = timestamp
    if timestamp_next_bucket != 0:
        bucket_counts[bucket*2] += 1
        bucket_counts[bucket] = 1
    return timestamp_next_bucket

def remove_bucket_timestamp(bucket_timestamps, bucket):
    if bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] != 0:
        bucket_timestamps[bucket][0] = bucket_timestamps[bucket][1]
        bucket_timestamps[bucket][1] = 0
    elif bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] == 0:
        del bucket_timestamps[bucket]

if __name__ == '__main__':
    N = int(input().strip())
    s = input().strip()
    while s == "":
        s = input().strip()
    a = []
    n = len(s)
    for i in range(n):
        if s[i].isalpha():
            if (ord(s[i]) - ord('0')) & 1:
                a.append(1)
            else:
                a.append(0)
    timestamp = 1
    bucket_counts = defaultdict(int)
    bucket_timestamps = defaultdict(lambda: [0, 0])
    bucket_index_merge = 0
    siz = len(a)
    for i in range(siz):
        if bucket_timestamps:
            end_bucket = max(bucket_timestamps.items())
            end_timestamp = end_bucket[1][0]
            if timestamp - end_timestamp >= N:
                bucket_counts[end_bucket[0]] -= 1
                if bucket_counts[end_bucket[0]] == 0:
                    del bucket_counts[end_bucket[0]]
                remove_bucket_timestamp(bucket_timestamps, end_bucket[0])
        if a[i] == 1:
            bucket_counts[1] += 1
            for bucket, count in bucket_counts.copy().items():
                if bucket == 1:
                    bucket_index_merge = add_timestamp(bucket_timestamps, bucket_counts, timestamp, bucket)
                elif bucket != 1 and bucket_index_merge != 0:
                    bucket_index_merge = add_timestamp(bucket_timestamps, bucket_counts, bucket_index_merge, bucket)
                else:
                    break
        count_print_check = 0
        if i > siz - len("straightforward") - 1:
            count = 0
            for bucket, bucket_count in bucket_counts.items():
                if bucket == max(bucket_counts):
                    count += bucket // 2
                    count_print_check += 1
                    break
                count += bucket * bucket_count
            if count_print_check == 1:
                print(count)
        timestamp += 1
