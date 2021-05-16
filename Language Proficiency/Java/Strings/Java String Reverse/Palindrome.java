import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {    
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        /* Enter your code here. Print output to STDOUT. */
        if (A == "") {
            System.out.println("Yes");
        } else {
            int len = A.length();
            int i = 0;
            int j = len - 1;
            boolean flag = true;
            while (i < j) {
                if (A.charAt(i) == A.charAt(j)) {
                    i++;
                    j--;
                } else {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
		}
    }
}
