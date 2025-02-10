package unit09.lambdas;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * A class that represents a student with a first and last na
 */
public class Student implements Comparable<Student> { // remove Comparable
    /**
     * The student's first name.
     */
    private final String firstName;

    /**
     * The student's last name.
     */
    private final String lastName;

    /**
     * Creates a new student.
     * 
     * @param firstName The new student's first name.
     * @param lastName  The new student's last name.
     */
    public Student(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    @Override
    public int compareTo(Student other) {
        return this.firstName.compareTo(other.firstName);
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    @Override
    public String toString() {
        return "{" + this.lastName + ", " + this.firstName + "}";
    }

    public static void main(String[] args) {
        Student one = new Student("sam", "ruan");
        Student two = new Student("mikail", "alam");
        Student three = new Student("donald", "liang");
        Student four = new Student("stuff", "things");
        List<Student> list = new ArrayList<>();
        list.add(one);
        list.add(two);
        list.add(three);
        list.add(four);

        list.sort(new Comparator<Student>() {
            @Override
            public int compare(Student arg0, Student arg1) {
                return arg0.lastName.compareTo(arg1.lastName);
            };
        });
        System.out.println(list);

        list.sort(
                (Student arg0, Student arg1) -> {
                    return arg1.lastName.compareTo(arg0.lastName);
                });
        System.out.println(list);

        //don't have to inculde the curley braces after the arrow 
        list.sort((arg0, arg1) -> arg1.firstName.compareTo(arg0.firstName));
        System.out.println(list);

        //prints without the {}
        list.stream().forEach((student) -> System.out.println(student.firstName + " " + student.lastName));

        //prints with {}
        list.stream().forEach(System.out::println);


    }
}
