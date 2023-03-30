import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Created by michiline on 17/05/2017.
 */
public class dgim {

    private static class Bucket {
        public int timestamp;
        public int size;

        public Bucket(int timestamp, int size) {
            this.timestamp = timestamp;
            this.size = size;
        }
    }

    private static class Buckets {
        // window length
        private int N;
        private ArrayList<Bucket> items;

        public Buckets(int N) {
            this.N = N;
            this.items = new ArrayList<>();
        }

        public void checkWindow(int currentTime) {
            int difference = currentTime - N;
            items = items.stream().filter(i -> i.timestamp > difference).collect(Collectors.toCollection(ArrayList::new));
        }

        public void addNewBucket(Bucket b, int currentTime) {
            ArrayList<Bucket> temp = new ArrayList<>();
            int length = items.size();
            for (int i = 0; i < length; i++) {
                if (items.get(i).size == b.size) {
                    temp.add(items.get(i));
                    if (temp.size() == 2) {
                        break;
                    }
                }
            }
            items.add(b);
            if (temp.size() != 0 && temp.size() != 1) {
                items.remove(temp.get(0));
                items.remove(temp.get(1));
                int timestamp = Math.max(temp.get(0).timestamp, temp.get(1).timestamp);
                int size = temp.get(0).size * 2;
                Bucket newBucket = new Bucket(timestamp, size);
                addNewBucket(newBucket, currentTime);
            }
        }

        public int estimateOnes(int k, int currentTime) {
            int difference = currentTime - k;
            int length = items.size();
            int sum = 0;
            int max = 0;
            for (int i = 0; i < length; i++) {
                Bucket b = items.get(i);
                if (b.timestamp >= difference) {
                    sum += b.size;
                    if (b.size > max) {
                        max = b.size;
                    }
                }
            }
            if (max == 1) {
                max++;
            }
            return sum - max / 2;
        }
    }

    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new FileReader("examples/1.in"));
//        BufferedWriter bw = new BufferedWriter(new FileWriter("examples/my.out"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String line;
        Buckets buckets = new Buckets(N);
        int time = 0;


        while ((line = br.readLine()) != null) {
            if (line.startsWith("q")) {
                int k = Integer.parseInt(line.split(" ")[1]);
                int est = buckets.estimateOnes(k, time);
                System.out.println(est);
//                bw.write(est + "\n");
//                bw.flush();
            } else {
                int length = line.length();
                for (int i = 0; i < length; i++) {
                    char c = line.charAt(i);
                    buckets.checkWindow(time);
                    if (c == 49) {
                        buckets.addNewBucket(new Bucket(time, 1), time);
                    }
                    time++;
                }
            }
        }
        br.close();
//        bw.close();
    }
}
