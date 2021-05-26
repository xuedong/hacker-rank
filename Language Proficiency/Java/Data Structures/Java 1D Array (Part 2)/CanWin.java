import java.util.*;

public class Solution {

    private static boolean aux(int leap, int[] game, int i) {
        int n = game.length;
        if (i < 0 || game[i] != 0) return false;
        if (i == n-1 || i+leap > n-1) return true;
        
        game[i] = 1;
        return aux(leap, game, i-1) || aux(leap, game, i+1) || aux(leap, game, i+leap);
    }

    public static boolean canWin(int leap, int[] game) {
        // Return true if you can win the game; otherwise, return false.
        return aux(leap, game, 0);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}

