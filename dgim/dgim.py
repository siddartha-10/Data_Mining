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