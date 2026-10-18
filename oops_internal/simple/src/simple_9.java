public class simple_9 {
    public static void main(String[] args) {
        int n = 10; // Upper limit

        // Odd Thread
        Thread odd = new Thread(() -> {
            for (int i = 1; i <= n; i += 2) {
                System.out.println("Odd: " + i);
                try { Thread.sleep(1000); } catch (Exception e) {}
            }
        });

        // Even Thread
        Thread even = new Thread(() -> {
            try { Thread.sleep(500); } catch (Exception e) {} // Slight headstart for Odd
            for (int i = 2; i <= n; i += 2) {
                System.out.println("Even: " + i);
                try { Thread.sleep(1000); } catch (Exception e) {}
            }
        });

        // Start both threads
        odd.start();
        even.start();
    }
}
