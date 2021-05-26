import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        LinkedList<Integer> L = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            L.add(sc.nextInt());
        }
        
        int Q = sc.nextInt();
        for (int query = 0; query < Q; query++) {
            String action = sc.next();
            if (action.equals("Insert")) {
                int index = sc.nextInt();
                int value = sc.nextInt();
                L.add(index, value);
            } else if (action.equals("Delete")) {
                int index = sc.nextInt();
                L.remove(index);
            }
        }
        
        sc.close();
        
        for (Integer value : L) {
            System.out.print(value+" ");
        }
    }
}

