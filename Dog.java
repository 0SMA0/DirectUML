import java.util.ArrayList;

public class Dog {   
    public String body;
    private String sound;
    private String sound2;
    private ArrayList<String> lst = new ArrayList<>();
    String thing;

    public Dog(String sound) {
        this.sound = sound;
    }

    public String getSound() {
        return this.sound;
    }

}