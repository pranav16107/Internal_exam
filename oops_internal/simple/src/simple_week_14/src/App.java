import javax.swing.*;

class Main {
    public static void main(String[] args) {
        JFrame f = new JFrame("JTree Example");

        String[] data = {"CSE", "ECE", "EEE"};

        JTree tree = new JTree(data);

        f.add(new JScrollPane(tree));
        f.setSize(300, 300);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}