import java.awt.*;
import java.awt.event.*;
class Main extends Frame {
    String msg = "";
    Main() {
        setSize(400, 300);
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                msg = "Mouse Clicked";
                repaint();
            }
            @Override
            public void mousePressed(MouseEvent e) {
                msg = "Mouse Pressed";
                repaint();
            }
            @Override
            public void mouseReleased(MouseEvent e) {
                msg = "Mouse Released";
                repaint();
            }
            @Override
            public void mouseEntered(MouseEvent e) {
                msg = "Mouse Entered";
                repaint();
            }
            @Override
            public void mouseExited(MouseEvent e) {
                msg = "Mouse Exited";
                repaint();
            }
        });
        setVisible(true);
    }

    @Override
    public void paint(Graphics g) {
        g.drawString(msg, 150, 150);
    }

    public static void main(String[] args) {
        new Main();
    }
}
