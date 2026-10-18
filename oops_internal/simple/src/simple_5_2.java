class ani8mal{
    void sound(){
        System.out.println("this is animal class.");
    }
}
class dog extends ani8mal{
    void bark(){
        System.out.println("Dog is barking");
    }
}
class puppy extends dog{
    void play(){
        System.out.println("Puppy is playing");
    }
}

public class simple_5_2 {
    public static void main(String []args){
        System.out.println("This is code is about multi-inheritance.");
        puppy obj=new puppy();
        obj.sound();
        obj.bark();
        obj.play();
    }
}
