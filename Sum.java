package unit09.lambdas;

import java.util.stream.IntStream;

public class Sum {
    public static int sum(int num) {
        //not inclusive
        // IntStream stream = IntStream.range(1, num);
        //exclusive
        IntStream stream = IntStream.rangeClosed(1, num);

        // stream.forEach(System.out::println);

        return stream.sum();
    }

    private static int shiftedSum(int num, int shift) {
        IntStream stream = IntStream.rangeClosed(1, num);
        return stream.map(
            value -> value + shift
        ).sum();
    }
    public static void main(String[] args) {
        System.out.println(sum(20));
        System.out.println(shiftedSum(20, 10));
    }
    
}
