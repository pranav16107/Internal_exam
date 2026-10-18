import javax.swing.*;

class Main {
    public static void main(String[] args) {
        JFrame f = new JFrame("JTable Example");

        String data[][] = {
            {"101", "Ravi", "CSE"},
            {"102", "Ram", "ECE"},
            {"103", "Raj", "EEE"}
        };

        String columns[] = {"ID", "Name", "Branch"};

        JTable t = new JTable(data, columns);

        f.add(new JScrollPane(t));
        f.setSize(300, 200);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}