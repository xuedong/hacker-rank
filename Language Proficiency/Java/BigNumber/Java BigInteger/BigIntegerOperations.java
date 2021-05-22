import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String n1 = sc.next();
        String n2 = sc.next();
        sc.close();
        
        BigInteger a1 = new BigInteger(n1);
        BigInteger a2 = new BigInteger(n2);
        System.out.println(a1.add(a2).toString());
        System.out.println(a1.multiply(a2).toString());
    }
}

