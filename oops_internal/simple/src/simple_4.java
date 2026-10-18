public class simple_4 {
    simple_4(){
        System.out.println("This is the constructor with no parameter passed.");}
    simple_4(int a){
        System.out.println("This is a constructor with parameter a:"+a);
    }
    public static void main(String []args){
        simple_4 obj=new simple_4();
        simple_4 obj1=new simple_4(5);

    }
}
