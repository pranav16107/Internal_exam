import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<String> list = new ArrayList<>();

        list.add("Apple");
        list.add("Banana");
        list.add("Mango");

        System.out.println("ArrayList: " + list);

        list.add(1, "Orange");
        System.out.println("After adding: " + list);

        list.remove("Banana");
        System.out.println("After removing: " + list);

        System.out.println("Element at index 0: " + list.get(0));

        System.out.println("Size: " + list.size());

        System.out.println("Contains Mango: " + list.contains("Mango"));

        list.set(0, "Grapes");
        System.out.println("After updating: " + list);

        list.clear();
        System.out.println("After clearing: " + list);
    }
}