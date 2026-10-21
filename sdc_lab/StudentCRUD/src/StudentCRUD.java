
import java.sql.*;
import java.util.Scanner;

public class StudentCRUD {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root", "Pranav@2007"
        );

        while (true) {
            System.out.println("\n1.Insert  2.Display  3.Update  4.Delete  5.Exit");
            int ch = sc.nextInt();

            if (ch == 5) break;

            if (ch == 1) {
                System.out.print("ID, Name, Marks: ");
                int id = sc.nextInt();
                String name = sc.next();
                int marks = sc.nextInt();

                PreparedStatement ps = con.prepareStatement(
                    "INSERT INTO student VALUES(?,?,?)");
                ps.setInt(1, id);
                ps.setString(2, name);
                ps.setInt(3, marks);
                ps.executeUpdate();
                System.out.println("Inserted");
            }

            else if (ch == 2) {
                ResultSet rs = con.createStatement().executeQuery(
                    "SELECT * FROM student");
                while (rs.next())
                    System.out.println(rs.getInt(1) + " " +
                        rs.getString(2) + " " + rs.getInt(3));
            }

            else if (ch == 3) {
                System.out.print("Enter ID and new marks: ");
                int id = sc.nextInt();
                int marks = sc.nextInt();

                PreparedStatement ps = con.prepareStatement(
                    "UPDATE student SET marks=? WHERE id=?");
                ps.setInt(1, marks);
                ps.setInt(2, id);
                ps.executeUpdate();
                System.out.println("Updated");
            }

            else if (ch == 4) {
                System.out.print("Enter ID: ");
                int id = sc.nextInt();

                PreparedStatement ps = con.prepareStatement(
                    "DELETE FROM student WHERE id=?");
                ps.setInt(1, id);
                ps.executeUpdate();
                System.out.println("Deleted");
            }
        }

        con.close();
        sc.close();
    }
}
