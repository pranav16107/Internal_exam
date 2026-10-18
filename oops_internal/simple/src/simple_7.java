class Animal {
    Animal(String name) {
        System.out.println("Animal constructor called for: " + name);
    }

    void sound() {
        System.out.println("This is animal class");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name); 
        System.out.println("Dog constructor called");
    }

    @Override
    void sound() {
        super.sound(); // Calls the superclass method
        System.out.println("This is dog class");
    }
}

public class simple_7 {
    public static void main(String[] args) {
        Dog obj = new Dog("Buddy");
        obj.sound();
    }
}
