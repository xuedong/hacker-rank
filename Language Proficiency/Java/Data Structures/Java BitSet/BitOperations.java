import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        BitSet b1 = new BitSet(n);
        BitSet b2 = new BitSet(n);
        BitSet[] arr = new BitSet[3];
        arr[1] = b1;
        arr[2] = b2;
        
        for (int i = 1; i <= m; i++) {
            String op = sc.next();
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            switch (op) {
                case "AND":
                    arr[x].and(arr[y]);
                    break;
                case "OR":
                    arr[x].or(arr[y]);
                    break;
                case "XOR":
                    arr[x].xor(arr[y]);
                    break;
                case "FLIP":
                    arr[x].flip(y);
                    break;
                case "SET":
                    arr[x].set(y);
                    break;
                default:
                    throw new IllegalArgumentException();
            }
            
            System.out.printf("%d %d%n", b1.cardinality(), b2.cardinality());
        }
    }
}

