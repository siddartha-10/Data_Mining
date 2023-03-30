
# DGIM ALGORITHM

Suppose we have a window of length N on a binary stream. We want at all times to be able to answer queries of the form “how many 1’s are there in the last k bits?” for any k≤ N. For this purpose we use the DGIM algorithm.

The dgim.py first takes the input paragraph and converts all letters to their ASCII representation and then their binary form. Once the paragraph has converted to 0/1 stream, the algorithm creates buckets for the first 32 bits in the stream. When a new bit enters, it slides the window (N=32) so that the window only contains 32 bits. For every new bit 1, it creates the bucket with size 1 and merges the other buckets if any of the buckets sizes appear 3 times. Lastly, after the merge, it estimates the no of 1's by adding all the buckets size and adds the only the half the size of a bucket that overlaps with the window (N=32).




# Requirements

Python 3.0
 
Any Python IDE / Google Colab
## Running Tests

To run tests, run the following command if you are using and IDE

```bash
  python dgim.py
```




## Authors

### I worked together on this project with :-
- Eshwar
- Rohith

