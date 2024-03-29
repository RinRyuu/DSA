package collection;
import java.util.*;
 


public class Shopingcarter {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        boolean flag =true;
        ArrayList menu = new ArrayList<>(); 
        menu.add("1 fry 100");
        menu.add("2 fryrice 100");
        menu.add("3 frywater 100");
        menu.add("4 fryfire 100");
        menu.add("5 fryice 100");
        while (flag) {
            System.out.println("------------menu---------------");
            System.out.println("1 Add Items ");
            System.out.println("2 Show Items ");
            System.out.println("3 Delete Items ");
            System.out.println("4 Update Items ");
            System.out.println("5 Order Menu ");
            System.out.println("6 Exit");
            System.out.println("--------------------------------");
            System.out.println("Enter value for using function : ");
            int key = sc.nextInt();
            switch (key) {
                case 1:
                    System.out.println("adding items");
                    break;
                case 2:
                    System.out.println("adding items");
                    break;
                case 3:
                    System.out.println("adding items");
                    break;
                case 4:
                    System.out.println("adding items");
                    break;
                case 5:
                for (int i =0;i<menu.size();i++){
                    System.out.println(menu.get(i).toString());
                }
                    break;

                case 6:
                    System.out.println("Thanks for using");
                    flag=false;
                    break;
            
                default:
                    System.out.println("Wrong input try agin");
                    break;
            }
        }
    }    
}


