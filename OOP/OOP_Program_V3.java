import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        ArrayList<Integer> ages = new ArrayList<>();

        int totalPeople = 0;
        int totalAge = 0;
        int lowestAge = Integer.MAX_VALUE;
        String lowestName = "";
        int highestAge = Integer.MIN_VALUE;
        String highestName = "";

        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Read name variable
            System.out.print("Enter a name (or 'exit' to exit): ");
            System.out.print("\nWhat's your name?: ");
            String name = scanner.nextLine();
            if (name.equalsIgnoreCase("exit")) {
                break; // Exit loop if "exit" is entered
            }
            names.add(name);

            // Read age
            System.out.print("How old are you?: ");
            int age = Integer.parseInt(scanner.nextLine());
            ages.add(age);

            // Update total count and total age
            totalPeople++;
            totalAge += age;

            // Update lowest and highest age
            if (age < lowestAge) {
                lowestAge = age;
                lowestName = name;
            }
            if (age > highestAge) {
                highestAge = age;
                highestName = name;
            }
        }

        // Print total count
        System.out.println("Total people: " + totalPeople);

        // Print average age
        double averageAge = totalPeople > 0 ? (double) totalAge / totalPeople : 0;
        System.out.println("Average age: " + averageAge);

        // Print lowest age and corresponding name
        System.out.println("Lowest age: " + lowestAge + ", Name: " + lowestName);

        // Print highest age and corresponding name
        System.out.println("Highest age: " + highestAge + ", Name: " + highestName);
    }
}
