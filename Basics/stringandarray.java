import java.util.Scanner;

public class stringandarray {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
        //swap
    //   String x = sc.nextLine();
    //   String y = sc.nextLine();
    //   String temp;

    //   temp =x;
    //   x=y;
    //   y=temp;

    //   System.out.println(x);
    //   System.out.println(y);

    //switch

    // int a = sc.nextInt();
    // switch (a){
    //     case 1:
    //     System.out.println(a);
    //     break;
    //     case 2:
    //     System.out.println(a);
    //     break;
    //     case 3:
    //     System.out.println(a);
    //     break;
    //     case 4:
    //     System.out.println(a);
    //     break;
    //     case 5:
    //     System.out.println(a);
    //     break;
    //     default :
    //     System.out.println("wrong input");
    //     break;
    // }

    //while loop
        // String x = "";
        // while (x.isBlank()) {
        //     x = sc.nextLine();
        // }

        // System.out.println(x);

        // for (int i =0;i<=5;i++){
        //     System.out.println();
        //     for (int j=i;j>=i;j--){
        //         System.out.print("x");
        //     }
        // }

        
        int number = 7;
 
        int m = 1;
 
        int n;
 
        do {n = 1;
            do {
                System.out.print(" ");
            }
            while (++n <= number - m + 1);
            n = 1;
            do {
                System.out.print("*");
            }
            while (++n <= m * 2 - 1);
            System.out.println();
        }
        while (++m <= number);
        m = number - 1; 
        do {
            n = 1;
            do {
                System.out.print(" "); 
            } while (++n <= number - m + 1); 
            n = 1;
            do {
                System.out.print("*");
            } while (++n <= m * 2 - 1);
            System.out.println();
        }
        while (--m > 0);

    }
}
