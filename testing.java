import java.util.ArrayList;

public class testing {

    private int error;
    private ArrayList<Integer> something;
    public String hehe;

    

    public testing(int error, ArrayList<Integer> something) {
        this.error = error;
        this.something = something;
    }


    public static void main(String[] args) {
        
    }



    public int getError() {
        return error;
    }



    public void setError(int error) {
        this.error = error;
    }



    private ArrayList<Integer> getSomething() {
        return something;
    }



    public void setSomething(ArrayList<Integer> something) {
        this.something = something;
    }

}