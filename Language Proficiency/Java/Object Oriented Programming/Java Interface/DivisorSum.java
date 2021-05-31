import java.util.*;

interface AdvancedArithmetic{
  int divisorSum(int n);
}

//Write your code here
class MyCalculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        int sum = 0;
        int sqrt = (int) Math.sqrt(n);
        
        for (int i = 1; i <= sqrt; i++) {
            if (n % i == 0) sum += i + n/i;
        }
        
        if (n == sqrt * sqrt) sum -= sqrt;
        
        return sum;
    }
}

class Solution{
    public static void main(String []args) {
        MyCalculator myCalculator = new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(myCalculator);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(myCalculator.divisorSum(n) + "\n");
      	sc.close();
    }

    /*
     *  ImplementedInterfaceNames method takes an object and prints the name of the interfaces it implemented
     */
    static void ImplementedInterfaceNames(Object o) {
        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++){
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}

