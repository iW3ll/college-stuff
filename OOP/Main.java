import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        ArrayList<People> peopleList = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Read name variable
            System.out.print("Type 9 to exit\n");
            System.out.print("What's your name?: ");
            String name = scanner.nextLine();
            if (name.equalsIgnoreCase("9")) {
                break; // Exit loop if "9" is typed
            }

            // Read age
            System.out.print("How old are you?: ");
            int age = Integer.parseInt(scanner.nextLine());

            People person = new People(name, age);
            peopleList.add(person);
        }

        PeopleSummary summary = new PeopleSummary(peopleList);
        summary.printSummary();
    }
}
