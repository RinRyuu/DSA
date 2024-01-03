import java.util.*;

public class tester2 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        Float pencil =  sc.nextFloat();
        Float pen =  sc.nextFloat();
        Float eraser =  sc.nextFloat();
        Float GST = ((pen+pencil+eraser)*18)/100;
        Float Total = pen+pencil+eraser;
        System.out.println(Total-GST);
        
    }
}
