import java.util.Scanner;

public class array2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            String s = sc.next();
            sc.close();
            String ans = "";
            for(int i =0;i<n;i+=2){
                if(s.charAt(i)=='0' && s.charAt(i+1)=='0' ){
                    ans+='A';
                }else if(s.charAt(i)=='0' && s.charAt(i+1)=='1' ){
                    ans+='T';
                }else if(s.charAt(i)=='1' && s.charAt(i+1)=='0' ){
                    ans+='C';
                }else{
                    ans+='G';
                }
            }
            System.out.println(ans);
        }
    }
}
