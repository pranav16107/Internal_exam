class Buffer {
    int data;
    boolean available = false;

    synchronized void produce(int n) {
        try {
            while (available)
                wait();

            data = n;
            System.out.println("Produced: " + data);
            available = true;
            notify();

        } catch (Exception e) {
            System.out.println(e);
        }
    }

    synchronized void consume() {
        try {
            while (!available)
                wait();

            System.out.println("Consumed: " + data);
            available = false;
            notify();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}

class Producer extends Thread {
    Buffer b;

    Producer(Buffer b) {
        this.b = b;
    }

    public void run() {
        for (int i = 1; i <= 5; i++)
            b.produce(i);
    }
}

class Consumer extends Thread {
    Buffer b;

    Consumer(Buffer b) {
        this.b = b;
    }

    public void run() {
        for (int i = 1; i <= 5; i++)
            b.consume();
    }
}

public class Main {
    public static void main(String[] args) {
        Buffer b = new Buffer();

        new Producer(b).start();
        new Consumer(b).start();
    }
}