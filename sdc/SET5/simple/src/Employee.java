
import java.sql.*;

public class Employee {
    public static void main(String[] args) throws Exception {

        Connection con = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/college",
            "root",
            "Pranav@2007"
        );

        String sql = "INSERT INTO employee VALUES (?, ?, ?)";
        PreparedStatement ps = con.prepareStatement(sql);

        ps.setInt(1, 1);
        ps.setString(2, "Rahul");
        ps.setDouble(3, 25000);

        ps.executeUpdate();
        System.out.println("Record inserted successfully!");

        Statement st = con.createStatement();
        ResultSet rs = st.executeQuery("SELECT * FROM employee");

        while (rs.next()) {
            System.out.println(
                rs.getInt("id") + " " +
                rs.getString("name") + " " +
                rs.getDouble("salary")
            );
        }

        con.close();
    }
}
