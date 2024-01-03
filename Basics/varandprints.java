// public class varandprints {
//     public static void main(String[] args) {
//         System.out.println("Hello World!");
//     }
// }
import java.util.*;

public class varandprints {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            System.out.print(a+a);
        }
    }
}   