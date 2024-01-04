import java.util.*;

public class taxcal {

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        Float Incom = sc.nextFloat();
        if (Incom<500000){
            System.out.println("tax is 0rs");
        }else if (500000 <= Incom && Incom <= 1000000){
            Float tax = Incom*0.20f;
            System.out.println("tax is "+tax+"rs");
        }else {
            Float tax = Incom*0.30f;
            System.out.println("your tax is"+tax+"rs");
        }
    }
}