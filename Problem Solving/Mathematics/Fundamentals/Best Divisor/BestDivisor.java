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
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        
        int best = 0; int res = 0;
        for (int i = 1; i <= n; i++) {
            int sum = 0;
            if (n % i == 0) {
                int value = i;
                while (value != 0) {
                    sum += value % 10;
                    value = value/10;
                }
                if (sum > best) {
                    best = sum;
                    res = i;
                }
            }
        }
        
        bufferedWriter.write(String.valueOf(res));

        bufferedReader.close();
        bufferedWriter.close();
    }
}

