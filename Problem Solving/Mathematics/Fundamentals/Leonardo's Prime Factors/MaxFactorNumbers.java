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

    public static boolean isPrime(long n) {
        if (n == 2) return true;
        boolean flag = true;
        for (long i = 2; i <= n / 2; ++i) {
            if (n % i == 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }

    /*
     * Complete the 'primeCount' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts LONG_INTEGER n as parameter.
     */

    public static int primeCount(long n) {
        // Write your code here
        if (n == 1) return 0;

        long product = 1;
        long i = 2;
        int count = 0;
        while (i <= n) {
            if (isPrime(i)) {
                product *= i;
                if (product <= n) {
                    count++;
                } else {
                    break;
                }
                i++;
            } else {
                i++;
            }
        }
        // if (count > 15) count = 15;
        return count;
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                long n = Long.parseLong(bufferedReader.readLine().trim());

                int result = Result.primeCount(n);

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

