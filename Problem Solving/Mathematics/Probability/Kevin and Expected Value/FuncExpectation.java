import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {
    
    public static void main(String[] args) throws IOException {
        int maxLength = 5000001;
        double[] precompute = new double[maxLength];
        double cumsum = 0.0;
        for (int i = 1; i < maxLength; i++) {
            cumsum += (1+Math.sqrt(1+4*i)) / 2.;
            precompute[i] = cumsum/(i+1);
        }
        
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                long n = Long.parseLong(bufferedReader.readLine().trim());

                double result = 0.;
                if (n < maxLength) {
                    result = precompute[(int) (n-1)];
                } else {
                    result = Math.sqrt(n-1) * (2./3.) + 0.5;
                }

                bufferedWriter.write(String.valueOf(result));
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

