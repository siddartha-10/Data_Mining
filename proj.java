import java.util.LinkedList;
import java.util.Queue;

public class proj {

    private static final int WINDOW_SIZE = 32;

    public static void main(String[] args) {
        String dataStream = "In the 1990’s “data mining” was an exciting and popular new concept. Around 2010, people\n" +
                "instead started to speak of “big data.” Today, the popular term is “data science.” However,\n" +
                "during all this time, the concept remained the same: use the most powerful hardware, the most\n" +
                "powerful programming systems, and the most efficient algorithms to solve problems in science,\n" +
                "commerce, healthcare, government, the humanities, and many other fields of human endeavor.\n" +
                "To many, data mining is the process of creating a model from data, often by the process of\n" +
                "machine learning, which we mention in Section 1.1.3 and discuss more fully in Chapter 12.\n" +
                "However, more generally, the objective of data mining is an algorithm. For instance, we discuss\n" +
                "locality-sensitive hashing in Chapter 3 and a number of stream-mining algorithms in Chapter 4,\n" +
                "none of which involve a model. Yet in many important applications, the hard part is creating the\n" +
                "model, and once the model is available, the algorithm to use the model is straightforward.";
        Queue<Integer> bitQueue = new LinkedList<Integer>();
        int oneCountEstimate = 0;

        for (int i = 0; i < dataStream.length(); i++) {
            char c = dataStream.charAt(i);
            if (Character.isLetter(c)) {
                int code = (int) c;
                if (code % 2 == 1) {
                    bitQueue.add(1);
                } else {
                    bitQueue.add(0);
                }

                // If bitQueue exceeds window size, remove oldest bit(s)
                while (bitQueue.size() > WINDOW_SIZE) {
                    int oldestBit = bitQueue.remove();
                    if (oldestBit == 1) {
                        oneCountEstimate--;
                    }
                }

                // Update oneCountEstimate using DGIM algorithm
                int j = 0;
                int sum = 0;
                int oldestBucketSize = 0;
                while (!bitQueue.isEmpty()) {
                    int bit = bitQueue.remove();
                    if (bit == 1) {
                        sum += (int) Math.pow(2, j);
                    }
                    j++;
                    if (j > oldestBucketSize) {
                        oldestBucketSize++;
                        oneCountEstimate += sum;
                        sum -= (int) Math.pow(2, oldestBucketSize-1);
                    }
                }
            }
        }

        System.out.println("DGIM representation of data stream: " + bitQueue.toString());
        System.out.println("Estimated count of 1's in the last " + WINDOW_SIZE + " bits: " + oneCountEstimate);
    }
}
