import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        int[] frequencyA = new int[26];
        int[] frequencyB = new int[26];
        
        int lenA = a.length();
        int lenB = b.length();
        if (lenA != lenB) return false;
    
        for (int i = 0; i < lenA; i++) {
            int asciiA = (int) a.charAt(i);
            int asciiB = (int) b.charAt(i);
            
            if (asciiA > 90) {
                frequencyA[asciiA-97]++;
            } else {
                frequencyA[asciiA-65]++;
            }
            
            if (asciiB > 90) {
                frequencyB[asciiB-97]++;
            } else {
                frequencyB[asciiB-65]++;
            }
        }
        
        for (int j = 0; j <= 25; j++) {
            if (frequencyA[j] != frequencyB[j]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}

