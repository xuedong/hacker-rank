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

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int n = Integer.parseInt(firstMultipleInput[0]);

                int m = Integer.parseInt(firstMultipleInput[1]);

                double p = Double.parseDouble(firstMultipleInput[2]);

                // Write your code here
                double e1 = 0;
                double e2 = 0;
                double e3 = 0;
                double el = 0;
                
                if (m > 3 && n > 3) {
                    e1 = 4 * Math.pow(1-p, 2) + 2 * (m+n-4) * Math.pow(1-p, 3) + (m-2) * (n-2) * Math.pow(1-p, 4);
                    e2 = 8 * p * Math.pow(1-p, 3) + 2 * (m+n-6) * p * Math.pow(1-p, 4) + 2 * (m+n-4) * p * Math.pow(1-p, 5) + ((m-3)*(n-2) + (m-2)*(n-3)) * p * Math.pow(1-p, 6);
                    e3 = 8 * p * p * Math.pow(1-p, 4) + 2 * (m+n-8) * p * p * Math.pow(1-p, 5) + 2 * (m+n-4) * p * p * Math.pow(1-p, 7) + ((m-4)*(n-2) + (m-2)*(n-4)) * p * p * Math.pow(1-p, 8);  
                    el = 4 * p * p * Math.pow(1-p, 4) + 8 * p * p * Math.pow(1-p, 5) + 4 * p * p * Math.pow(1-p, 6) + 4 * (m+n-6) * p * p * Math.pow(1-p, 6) + 4 * (m+n-6) * p * p * Math.pow(1-p, 7) + 4 * (m-3) * (n-3) * p * p * Math.pow(1-p, 8);
                } else if (m == 1 && n == 1) {
                    e1 = 1;
                    e2 = 0;
                    e3 = 0;
                    el = 0;
                } else if ((m == 1 && n == 2) || (m == 2 && n == 1)) {
                    e1 = 2 * (1-p);
                    e2 = p;
                    e3 = 0;
                    el = 0;
                } else if ((m == 1 && n == 3) || (m == 3 && n == 1)) {
                    e1 = 2 * (1-p) + Math.pow(1-p, 2);
                    e2 = 2 * p * (1-p);
                    e3 = p * p;
                    el = 0;
                } else if ((m == 1 && n >= 4) || (m >= 4 && n == 1)) {
                    int l = Math.max(m, n);
                    e1 = 2 * (1-p) + (l-2) * Math.pow(1-p, 2);
                    e2 = 2 * p * (1-p) + (l-3) * p * Math.pow(1-p, 2);
                    e3 = 2 * p * p * (1-p) + (l-4) * p * p * Math.pow(1-p, 2);
                    el = 0;
                } else if (m == 2 && n == 2) {
                    e1 = 4 * Math.pow(1-p, 2);
                    e2 = 4 * p * Math.pow(1-p, 2);
                    e3 = 0;
                    el = 4 * p * p * Math.pow(1-p, 2);
                } else if ((m == 2 && n == 3) || (m == 3 && n == 2)) {
                    e1 = 4 * Math.pow(1-p, 2) + 2 * Math.pow(1-p, 3);
                    e2 = 2 * p * Math.pow(1-p, 2) + 4 * p * Math.pow(1-p, 3) + p * Math.pow(1-p, 4);
                    e3 = 2 * p * p * Math.pow(1-p, 3);
                    el = 4 * p * p * Math.pow(1-p, 3) + 4 * p * p * Math.pow(1-p, 4);
                } else if ((m == 2 && n >= 4) || (m >= 4 && n == 2)) {
                    int l = Math.max(m, n);
                    e1 = 4 * Math.pow(1-p, 2) + 2 * (l-2) * Math.pow(1-p, 3);
                    e2 = 2 * p * Math.pow(1-p, 2) + 4 * p * Math.pow(1-p, 3) + (l-2) * p * Math.pow(1-p, 4) + 2 * (l-3) * p * Math.pow(1-p, 4);
                    e3 = 4 * p * p * Math.pow(1-p, 4) + 2 * (l-4) * p * p * Math.pow(1-p, 5);
                    el = 4 * p * p * Math.pow(1-p, 3) + 4 * p * p * Math.pow(1-p, 4) + 4 * (l-3) * p * p * Math.pow(1-p, 5);
                } else if (m == 3 && n == 3) {
                    e1 = 4 * Math.pow(1-p, 2) + 4 * Math.pow(1-p, 3) + Math.pow(1-p, 4);
                    e2 = 8 * p * Math.pow(1-p, 3) + 4 * p * Math.pow(1-p, 5);
                    e3 = 4 * p * p * Math.pow(1-p, 3) + 2 * p * p * Math.pow(1-p, 6);
                    el = 4 * p * p * Math.pow(1-p, 4) + 8 * p * p * Math.pow(1-p, 5) + 4 * p * p * Math.pow(1-p, 6);
                } else {
                    int l = Math.max(m, n);
                    e1 = 4 * Math.pow(1-p, 2) + (2 + 2*(l-2)) * Math.pow(1-p, 3) + (l-2) * Math.pow(1-p, 4);
                    e2 = 8 * p * Math.pow(1-p, 3) + 2 * (l-3) * p * Math.pow(1-p, 4) + (2 + 2*(l-2)) * p * Math.pow(1-p, 5) + (l-3) * p * Math.pow(1-p, 6);
                    e3 = 2 * p * p * Math.pow(1-p, 3) + 4 * p * p * Math.pow(1-p, 4) + 2 * (l-4) * p * p * Math.pow(1-p, 5) + (l-2) * p * p * Math.pow(1-p, 6) + 2 * p * p * Math.pow(1-p, 7) + (l-4) * p * p * Math.pow(1-p, 8);
                    el = 4 * p * p * Math.pow(1-p, 4) + 8 * p * p * Math.pow(1-p, 5) + 4 * p * p * Math.pow(1-p, 6) + 4 * (l-3) * p * p * Math.pow(1-p, 6) + 4 * (l-3) * p * p * Math.pow(1-p, 7);
                }
                
                double total = e1 + e2 + e3 + el;
                double score = total / (n*m);
                System.out.printf("%.9g%n", score);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}

