import java.util.*;

public class oddeven{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        if (N%2==0){
            System.out.println("it is even");
        }else{
            System.out.println("its odd");
        }
    }
}