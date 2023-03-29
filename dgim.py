# WINDOW_SIZE = 32

# class Bucket:
#     def __init__(self, count, timestamp, bucket_id):
#         self.count = count
#         self.timestamp = timestamp
#         self.bucket_id = bucket_id

# def dgim(stream):
#     # Initialize buckets with size decreasing by powers of 2
#     buckets = []
#     count = 0
#     for i, bit in enumerate(stream):
#         if bit == 0:
#             continue
#         count += 1
#         timestamp = i
#         # Merge buckets with the same size
#         while len(buckets) > 1 and buckets[-1].count == buckets[-2].count:
#             buckets.pop()
#             buckets[-1].timestamp = timestamp
#         # Remove buckets that are outside the window
#         while buckets and i - buckets[0].timestamp > WINDOW_SIZE:
#             buckets.pop(0)
#         # Add new bucket
#         if len(buckets) == 0 or buckets[0].count != 1:
#             buckets.insert(0, Bucket(1, timestamp, len(buckets)))
#         else:
#             buckets[0].timestamp = timestamp
#         # Update counts
#         for i in range(len(buckets)):
#             buckets[i].count *= 2
#         # Merge buckets with the same size
#         while len(buckets) > 1 and buckets[-1].count == buckets[-2].count:
#             buckets.pop()
#             buckets[-1].timestamp = timestamp
#         # Compute estimate
#         total_count = sum(bucket.count for bucket in buckets)
#         estimate = (total_count - 1) - (total_count - 1) % WINDOW_SIZE
#         print(estimate, end=' ')
# input_stream = "1010001010100010010101000100101010001001010100010010101000100101010001001010100010010101000100101010001001010100010010101000100101010001001010100010010101000100101010001001010100010010101000100"
# dgim(input_stream)




# import sys

# def add_timestamp(bucket_timestamps, bucket_counts, timestamp, bucket):
#     if bucket not in bucket_timestamps:
#         bucket_timestamps[bucket] = (0, 0)

#     timestamp_next_bucket = bucket_timestamps[bucket][1]
#     if (bucket_timestamps[bucket][0] == 0 and bucket_timestamps[bucket][1] == 0) or \
#         (bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] != 0):
#         bucket_timestamps[bucket] = (timestamp, 0)
#     elif bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] == 0:
#         bucket_timestamps[bucket] = (bucket_timestamps[bucket][0], timestamp)

#     if timestamp_next_bucket != 0:
#         bucket_counts.setdefault(bucket*2, 0)
#         bucket_counts[bucket*2] += 1


#     return timestamp_next_bucket


# def remove_bucket_timestamp(bucket_timestamps, bucket):
#     if bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] != 0:
#         bucket_timestamps[bucket] = (bucket_timestamps[bucket][1], 0)
#     elif bucket_timestamps[bucket][0] != 0 and bucket_timestamps[bucket][1] == 0:
#         del bucket_timestamps[bucket]

# s = "In the 1990s data mining was an exciting and popular new concept. Around 2010, peopleinstead started to speak of “big data.” Today, the popular term is “data science.” However,during all this time, the concept remained the same: use the most powerful hardware, the mostpowerful programming systems, and the most efficient algorithms to solve problems in science,commerce, healthcare, government, the humanities, and many other fields of human endeavor.To many, data mining is the process of creating a model from data, often by the process ofmachine learning, which we mention in Section 1.1.3 and discuss more fully in Chapter 12.However, more generally, the objective of data mining is an algorithm. For instance, we discusslocality-sensitive hashing in Chapter 3 and a number of stream-mining algorithms in Chapter 4,none of which involve a model. Yet in many important applications, the hard part is creating themodel, and once the model is available, the algorithm to use the model is straightforward."
# n = len(s)
# N = int(input())
# a = []
# for i in range(n):
#     if s[i].isalpha():
#         if (ord(s[i])-ord('0')) & 1:
#             a.append(1)
#         else:
#             a.append(0)

# timestamp = 1
# bucket_counts = {}  # <bucket, count>
# bucket_timestamps = {}  # <bucket, <timestamp1, timestamp2>>
# bucket_index_merge = 0
# siz = len(a)
# bucket_counts[1] = 0
# for i in range(siz):
#     # check if bucket_timestamp is empty
#     # remove two timestamps from bucket_timestamps if present for bucket 1, and add timestamp.
#     if bucket_timestamps:
#         end_bucket = max(bucket_timestamps.keys())
#         end_timestamp = bucket_timestamps[end_bucket][0]
#         if timestamp - end_timestamp >= N:  # remove the last element from list and bucket_timestamps if its timestamp is greater than N
#             bucket_counts[end_bucket] -= 1
#             if bucket_counts[end_bucket] == 0:
#                 del bucket_counts[end_bucket]
#             remove_bucket_timestamp(bucket_timestamps, end_bucket)

#     if a[i] == 1:
#         bucket_counts[1] += 1
#         # loop over bucket_counts and merge buckets if count is greater than 2
#         for bucket, count in bucket_counts.items():
#             if bucket == 1:
#                 bucket_index_merge = add_timestamp(bucket_timestamps, bucket_counts, timestamp, bucket)
#             elif bucket != 1 and bucket_index_merge != 0:
#                 bucket_index_merge = add_timestamp(bucket_timestamps, bucket_counts, bucket_index_merge, bucket)
#             else:
#                 break

#     if i > siz - 15:
#         count = 0
#         # loop over a copy of bucket_counts and merge buckets if count is greater than 2
# for bucket, count in bucket_counts.copy().items():
#     if bucket == 1:
#         bucket_index_merge = add_timestamp(bucket_timestamps, bucket_counts, timestamp, bucket)
#     elif bucket != 1 and bucket_index_merge != 0:
#         bucket_index_merge = add_timestamp(bucket_timestamps, bucket_counts, bucket_index_merge, bucket)
#     else:
#         break


from collections import defaultdict

import re

def process_stream(stream):
    # Step 1: ignore non-letter characters
    stream = re.sub(r'[^a-zA-Z]', '', stream)
    
    # Step 2: convert letters to ASCII code
    ascii_codes = [ord(c) for c in stream]
    
    # Step 3: convert ASCII codes to binary
    binary_codes = [int(bin(code)[2:]) for code in ascii_codes]
    binary_stream = ''.join([str(b) for b in binary_codes])
    
    # Step 4: return the binary stream
    return binary_stream

def dgim_last_chars(stream, N, last_chars):
    buckets = {1: [], 2: [], 4: [], 8: [], 16: [], 32: []}
    window = []
    counts = defaultdict(int)
    
    for bit in stream:
        if len(window) == N:
            oldest = window.pop(0)
            for size in buckets:
                if len(buckets[size]) > 0 and buckets[size][0][0] <= oldest:
                    counts[last_chars[int(stream[oldest])]] -= buckets[size][0][1]
                    buckets[size].pop(0)
        window.append(int(ord(bit) % 2 == 1))
        for size in buckets:
            if len(buckets[size]) > 1 and buckets[size][0][0] < window[-1] - N:
                counts[last_chars[int(stream[buckets[size][0][0]])]] -= buckets[size][0][1]
                buckets[size].pop(0)
            if len(buckets[size]) == 0 or buckets[size][-1][0] != window[-1]:
                counts[last_chars[int(bit)]] += 1
                buckets[size].append((len(window) - 1, 1))
            else:
                buckets[size][-1] = (buckets[size][-1][0], buckets[size][-1][1] + 1)
        total = 0
        estimate = None
        for size in sorted(buckets.keys(), reverse=True):
            for i in range(len(buckets[size])):
                total += buckets[size][i][1]
                if total > N:
                    estimate = buckets[size][i-1][1] // 2
                    break
            if estimate is not None:
                break
        if len(window) >= len(last_chars):
            counts[last_chars[int(stream[window[-len(last_chars)]])]] -= int(ord(stream[window[-len(last_chars)]]))
        counts[last_chars[int(bit)]] += int(ord(bit) % 2 == 1)
    return counts


stream = "In the 1990’s “data mining” was an exciting and popular new concept. Around 2010, peopleinstead started to speak of “big data.” Today, the popular term is “data science.” However,during all this time, the concept remained the same: use the most powerful hardware, the mostpowerful programming systems, and the most efficient algorithms to solve problems in science,commerce, healthcare, government, the humanities, and many other fields of human endeavor.To many, data mining is the process of creating a model from data, often by the process ofmachine learning, which we mention in Section 1.1.3 and discuss more fully in Chapter 12.Howevermoregenerally, the objective of data mining is an algorithm. For instance, we discusslocality-sensitive hashing in Chapter 3 and a number of stream-mining algorithms in Chapter 4,none of which involve a model. Yet in many important applications, the hard part is creating themodel, and once the model is available, the algorithm to use the model is straightforward."

last_chars = "straightforward"
for value in dgim_last_chars(process_stream(stream),32,last_chars).values():
    print(value)




