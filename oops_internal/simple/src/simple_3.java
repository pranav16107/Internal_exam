
public class simple_3 {

    void add(int a) {
        System.out.println("This is a method with one variable that is :" + a);
    }

    void add(int a, int b) {
        System.out.printf("This is a method with two variables a:%d and b:%d", a, b);
    }

    public static void main(String[] args) {
        System.out.println("This is method overloading");
        simple_3 obj = new simple_3();
        obj.add(5);
        obj.add(5, 6);

    }
}
