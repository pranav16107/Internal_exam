import java.util.Random;
class A extends Thread {
    public void run() {
        Random r = new Random();
        while (true) {
            int n = r.nextInt(10);
            System.out.println("Number: " + n);
            if (n % 2 == 0)
                new B(n).start();
            else
                new C(n).start();
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }
}
class B extends Thread {
    int n;
    B(int n) { this.n = n; }
    @Override
    public void run() {
        System.out.println("Square: " + (n * n));
    }
}
class C extends Thread {
    int n;
    C(int n) { this.n = n; }
    @Override
    public void run() {
        System.out.println("Cube: " + (n * n * n));
    }
}
public class Main {
    public static void main(String[] args) {
        new A().start();
    }
}