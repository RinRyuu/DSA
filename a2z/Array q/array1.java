import java.util.Scanner;

public class array1{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[2][2];
        for(int i = 0;i<2;i++){
            for(int j = 0;j<2;j++){
                matrix[i][j]=sc.nextInt();
            }    
        }
        sc.close();
        System.out.println();
        for (int i=0;i<2;i++){
            for(int j=0;j<2;j++){
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
    }
}