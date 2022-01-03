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
    
    static BigInteger mod = BigInteger.TEN.pow(9).add(BigInteger.valueOf(7));

    /*
     * Complete the 'solve' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER a
     *  2. INTEGER b
     *  3. INTEGER n
     */

    public static int solve(int a, int b, int n) {
    // Write your code here
        BigInteger num = BigInteger.valueOf(n-1);
        BigInteger aRes = BigInteger.ZERO;
        BigInteger bRes = BigInteger.ONE;
        BigInteger cRes = BigInteger.ONE;
        BigInteger aBase = BigInteger.ZERO;
        BigInteger bBase = BigInteger.ONE;
        BigInteger cBase = BigInteger.ONE;
        while (num.compareTo(BigInteger.ZERO) > 0) {
            if (num.mod(BigInteger.valueOf(2)).compareTo(BigInteger.ONE) == 0) {
                BigInteger temp1 = aRes.multiply(aBase).add(bRes.multiply(bBase)).mod(mod);
                BigInteger temp2 = aBase.multiply(bRes).add(bBase.multiply(cRes)).mod(mod);
                BigInteger temp3 = bBase.multiply(bRes).add(cBase.multiply(cRes)).mod(mod);
                aRes = temp1;
                bRes = temp2;
                cRes = temp3;
            }
            num = num.shiftRight(1);
            BigInteger temp1 = aBase.multiply(aBase).add(bBase.multiply(bBase)).mod(mod);
            BigInteger temp2 = aBase.multiply(bBase).add(bBase.multiply(cBase)).mod(mod);
            BigInteger temp3 = bBase.multiply(bBase).add(cBase.multiply(cBase)).mod(mod);
            aBase = temp1;
            bBase = temp2;
            cBase = temp3;
        }
        aRes = bRes.multiply(BigInteger.valueOf(b)).add(aRes.multiply(BigInteger.valueOf(a))).mod(mod);
        return aRes.mod(mod).intValue();
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

                int a = Integer.parseInt(firstMultipleInput[0]);

                int b = Integer.parseInt(firstMultipleInput[1]);

                int n = Integer.parseInt(firstMultipleInput[2]);

                int result = Result.solve(a, b, n);

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

