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
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER d
     *  2. INTEGER p
     */

    public static int solve(long d, long p) {
    // Write your code here
        if (d < 0) {
            return 0;
        } else if (d == 0 && p == 0) {
            return 1;
        } else if (d == 0 && p < 0) {
            return 0;
        } else if (d == 0 && p > 0) {
            double root = Math.sqrt(p);
            if (Math.abs(Math.floor(root) - root) <= 1e-9) {
                return 2;
            } else {
                return 0;
            }
        } else {
            if (p == 0) {
                return 4;
            } else {
                double det = Math.sqrt(d * d + 4 * p);
                if (det < 0) {
                    return 0;
                } else if (det == 0) {
                    return d % 2 == 0 ? 2 : 0;
                } else {
                    if (Math.abs(Math.floor(det) - det) <= 1e-9 && (-d + Math.floor(det)) % 2 == 0) {
                        return 4;
                    } else {
                        return 0;
                    }
                }
            }
        }
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

                int d = Integer.parseInt(firstMultipleInput[0]);

                int p = Integer.parseInt(firstMultipleInput[1]);

                int result = Result.solve(d, p);

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
