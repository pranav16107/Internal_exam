package week_7;

import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/ShoppingCartController")
public class ShoppingCartController extends HttpServlet {
	
	public void doGet(HttpServletRequest request,
            HttpServletResponse response)
            throws IOException {
response.sendRedirect("login.html");
}

    public void doPost(HttpServletRequest request,
                       HttpServletResponse response)
                       throws IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String userName = request.getParameter("userName");
        String password = request.getParameter("password");

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/week7", "root", "Pranav@2007");

            PreparedStatement ps = con.prepareStatement(
                "SELECT * FROM users WHERE username=? AND password=?");

            ps.setString(1, userName);
            ps.setString(2, password);

            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                out.println("<h1>" + userName + ": Welcome to Home Page</h1>");
                out.println("<h1>Login Successful</h1>");
            } else {
                out.println("<h1>" + userName +
                    ": please enter correct UserName and Password</h1>");
                out.println("<h1>login failed</h1>");
            }

            con.close();

        } catch (Exception e) {
            out.println(e);
        }
    }
}