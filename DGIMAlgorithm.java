//public class DGIMAlgorithm {
//
//    public static void main(String[] args) {
//        String text = "In the 1990’s “data mining” was an exciting and popular new concept. "
//                + "Around 2010, people instead started to speak of “big data.” "
//                + "Today, the popular term is “data science.” "
//                + "However, during all this time, the concept remained the same:";
//        int N = 32; // window size
//        int[] buckets = new int[N];
//        int currentBucketSize = 0;
//
//        for (int i = 0; i < text.length(); i++) {
//            char c = text.charAt(i);
//            if (Character.isLetter(c)) { // ignore non-letter characters
//                int ascii = (int) c;
//                int bit = (ascii % 2 == 1) ? 1 : 0; // convert to bit
//                currentBucketSize++;
//                for (int j = N - 1; j >= 1; j--) {
//                    buckets[j] = buckets[j-1];
//                }
//                buckets[0] = bit;
//                if (currentBucketSize > N) {
//                    currentBucketSize--;
//                    int lastBucketSize = 0;
//                    for (int j = N-1; j >= 0; j--) {
//                        if (buckets[j] == 1) {
//                            lastBucketSize = j + 1;
//                            break;
//                        }
//                    }
//                    int sum = lastBucketSize;
//                    int k = 1;
//                    while (k <= lastBucketSize) {
//                        int powerOf2 = (int) Math.pow(2, k-1);
//                        int count = 0;
//                        for (int j = 0; j < N; j++) {
//                            if (buckets[j] == 1 && j < lastBucketSize && (lastBucketSize-j) <= powerOf2) {
//                                count++;
//                            } else if (buckets[j] == 1 && j >= lastBucketSize && (N-j+lastBucketSize) <= powerOf2) {
//                                count++;
//                            }
//                        }
//                        sum += (int) Math.floor(count / 2) * powerOf2;
//                        k++;
//                    }
//                    System.out.println("Estimated number of 1's in last " + N + " bits: " + sum);
//                }
//            }
//        }
//    }
//}

import java.sql.SQLOutput;

public class DGIMAlgorithm {
    public static void main(String[] args) {
        String text = "In the 1990’s “data mining” was an exciting and popular new concept. "
                + "Around 2010, people instead started to speak of “big data.” "
                + "Today, the popular term is “data science.” "
                + "However, during all this time, the concept remained the same:";

        StringBuilder binaryStream = new StringBuilder(); // Initialize a StringBuilder to store the binary stream

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (Character.isLetter(c)) { // Ignore non-letter characters
                int asciiCode = (int) c; // Convert letter to its ASCII code
                if (asciiCode % 2 == 1) { // If odd, append 1; otherwise, append 0
                    binaryStream.append("1");
                } else {
                    binaryStream.append("0");
                }
            }
        }

        System.out.println(binaryStream.length()); // Print the binary stream
        // the length of the binary stream is 172 and
        // now you have to do in sunch a way that each of the letter is skipped

        for (int i = 0; i < binaryStream.length()-32; i++) {
            
        }
    }
}

