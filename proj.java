import java.util.LinkedList;
import java.util.Queue;

public class proj {

    private static final int WINDOW_SIZE = 32;

    public static void main(String[] args) {
        String dataStream = "Hello World! This is a sample data stream.";
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
