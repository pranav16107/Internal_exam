// single inheritance
class animal{
    void sound(){
        System.out.println("This is is a animal class.");
    }
}
class dog extends animal{ 
    void bark(){
        System.out.println("Dog barks");
    }
}

public class simple_5_1 {
    public static void main(String []args){
        dog obj=new dog();
        obj.sound();
        obj.bark();
    }
}
