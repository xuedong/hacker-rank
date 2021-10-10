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

class Result {

    /*
     * Complete the 'solve' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER k
     *  3. STRING s
     */

    public static String solve(long n, long k, String s) {
    // Write your code here
        long x = 0;
        long ans = 0;
        for (long i = 0; i < n; i++) ans += s.charAt((int) i)-48;
        for (long i = 0; i < k; i++) x += s.charAt((int) i)-48;
        if (k > 1) ans += x * (x-1);
            
        for (long i = k; i < n; i++) {
            ans += x * (s.charAt((int) i)-48) * 2;
            x = x + (s.charAt((int) i)-48) - (s.charAt((int) (i-k))-48);
        }
        
        long denom = n * n;
        long g = gcd(denom, ans);
        String output = String.valueOf(ans/g) + "/" + String.valueOf(denom/g);
        return output;
    }
    
    public static long gcd(long a, long b) {
        if (b == 0) return a;
        return gcd(b, a%b);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                long n = Integer.parseInt(firstMultipleInput[0]);

                long k = Integer.parseInt(firstMultipleInput[1]);

                String s = bufferedReader.readLine();

                String result = Result.solve(n, k, s);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

