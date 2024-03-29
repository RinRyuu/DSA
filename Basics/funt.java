import java.util.Scanner;
class maxer {

public static int subs(int a,int b){
            return a+b;
        }
    
}
public class funt {

        public static int add(int a,int b){
            return a+b;
        }
    public static void main(String[] args) {
        System.out.println("huhd");
        maxer d = new maxer();
        System.out.println(d.subs(2,3));
        int arry[] = {2,3,456,677,7};
        System.out.println(arry[3]);
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = add(a, b);
        System.out.println(c);
    }
}