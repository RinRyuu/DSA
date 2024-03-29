import java.util.ArrayList;
import java.util.Scanner;

class Item {
    private int itemNo;
    private String itemName;
    private double price;

    public Item(int itemNo, String itemName, double price) {
        this.itemNo = itemNo;
        this.itemName = itemName;
        this.price = price;
    }

    public int getItemNo() {
        return itemNo;
    }

    public String getItemName() {
        return itemName;
    }

    public double getPrice() {
        return price;
    }
}

public class ShoppingCart {
    private ArrayList<Item> cartItems;

    public ShoppingCart() {
        cartItems = new ArrayList<>();
    }

    public void addItems(int itemNo, String itemName, double price) {
        Item item = new Item(itemNo, itemName, price);
        cartItems.add(item);
        System.out.println("Item added to the cart successfully.");
    }

    public void showItems() {
        System.out.println("Items in the cart:");
        for (Item item : cartItems) {
            System.out.println("Item No: " + item.getItemNo() + ", Item Name: " + item.getItemName() + ", Price: $" + item.getPrice());
        }
    }

    public void deleteItems(int itemNo) {
        for (int i = 0; i < cartItems.size(); i++) {
            if (cartItems.get(i).getItemNo() == itemNo) {
                cartItems.remove(i);
                System.out.println("Item deleted from the cart successfully.");
                return;
            }
        }
        System.out.println("Item with Item No " + itemNo + " not found in the cart.");
    }

    public void updateItems(int itemNo, String newItemName, double newPrice) {
        for (Item item : cartItems) {
            if (item.getItemNo() == itemNo) {
                item.itemName = newItemName;
                item.price = newPrice;
                System.out.println("Item updated successfully.");
                return;
            }
        }
        System.out.println("Item with Item No " + itemNo + " not found in the cart.");
    }

    public void orderItems() {
        double totalAmount = 0;
        System.out.println("Order Details:");
        for (Item item : cartItems) {
            System.out.println("Item Name: " + item.getItemName() + ", Price: $" + item.getPrice());
            totalAmount += item.getPrice();
        }
        System.out.println("Total Amount: $" + totalAmount);
    }

    public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\nMenu:");
            System.out.println("1. Add Item");
            System.out.println("2. Show Items");
            System.out.println("3. Delete Item");
            System.out.println("4. Update Item");
            System.out.println("5. Order Items");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter Item No: ");
                    int itemNo = scanner.nextInt();
                    System.out.print("Enter Item Name: ");
                    String itemName = scanner.next();
                    System.out.print("Enter Price: ");
                    double price = scanner.nextDouble();
                    cart.addItems(itemNo, itemName, price);
                    break;
                case 2:
                    cart.showItems();
                    break;
                case 3:
                    System.out.print("Enter Item No to delete: ");
                    int deleteItemNo = scanner.nextInt();
                    cart.deleteItems(deleteItemNo);
                    break;
                case 4:
                    System.out.print("Enter Item No to update: ");
                    int updateItemNo = scanner.nextInt();
                    System.out.print("Enter new Item Name: ");
                    String newItemName = scanner.next();
                    System.out.print("Enter new Price: ");
                    double newPrice = scanner.nextDouble();
                    cart.updateItems(updateItemNo, newItemName, newPrice);
                    break;
                case 5:
                    cart.orderItems();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 6);
        scanner.close();
    }
}
