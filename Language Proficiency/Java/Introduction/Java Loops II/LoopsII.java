import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int curr = a;
            int pow = 1;
            for (int j = 0; j < n; j++) {
                curr += pow * b;
                pow *= 2;
                System.out.printf("%d ", curr);
            }
            System.out.println();
        }
        in.close();
    }
}

