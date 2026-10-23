
package com.test;

import java.io.*;
import java.util.Date;
import javax.servlet.http.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/SessionTrack")
public class SessionTrack extends HttpServlet {

    public void doGet(HttpServletRequest request,
                      HttpServletResponse response)
                      throws IOException {

        HttpSession session = request.getSession();

        Integer count = (Integer) session.getAttribute("count");

        if (count == null)
            count = 0;
        else
            count++;

        session.setAttribute("count", count);

        String user = "ABCD";

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        out.println("<h1>Welcome to my website</h1>");
        out.println("<h2>Session Information</h2>");
        out.println("Session ID: " + session.getId() + "<br><br>");
        out.println("Creation Time: " + new Date(session.getCreationTime()) + "<br><br>");
        out.println("Last Access Time: " + new Date(session.getLastAccessedTime()) + "<br><br>");
        out.println("User ID: " + user + "<br><br>");
        out.println("Number of Visits: " + count);
        out.println("</body></html>");
    }
}
