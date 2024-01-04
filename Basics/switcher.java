import java.util.*;

public class switcher {
    public static void main (String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        switch (N) {
            case 1:
                System.out.println("maker of case 1");
                break;
            
            case 2:
              System.out.println("case 2");
              break;
            default:
                System.out.println("maker of default");
                break;
        }
    }
}