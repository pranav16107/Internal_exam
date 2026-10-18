import java.io.File;

class Main {
    static void listFiles(File dir) {
        File[] files = dir.listFiles();

        if (files != null) {
            for (File f : files) {
                if (f.isFile())
                    System.out.println(f.getName());
                else
                    listFiles(f);
            }
        }
    }

    public static void main(String[] args) {
        File dir = new File("C:\\Users\\pranav\\OneDrive\\Desktop\\Internal_exam\\oops_internal\\src");
        listFiles(dir);
    }
}