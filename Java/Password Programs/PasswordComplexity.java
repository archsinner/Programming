// Create a program that creates username and password  and checks the password complexity.
// Password should be at least 8 characters long and should contain at least one number, one uppercase letter and one lowercase letter.
// If the password is not complex enough, the program should print "Password is not complex enough" and ask the user to enter a new password.
// If the password is complex enough, the program should print "Password is complex enough" and ask the user to enter a new password.

import java.util.Scanner;
// import standard input
import java.util.regex.Pattern;

// Create a class named JavaProject that contains a main method.
public class PasswordComplexity {
    // Create a main method that creates a Scanner object and asks the user to enter
    // a username and password.
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your username: ");
        String username = input.nextLine();
        System.out.println("Enter your password: ");
        String password = input.nextLine();
        // Create a while loop that checks the password complexity.
        while (!password.matches("(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}")) {
            System.out.println("Password is not complex enough");
            System.out.println("Enter your password: ");
            password = input.nextLine();
        }
        System.out.println("Password is complex enough");
    }
}