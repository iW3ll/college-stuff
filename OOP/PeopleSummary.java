import java.util.ArrayList;

public class PeopleSummary {
    private ArrayList<People> peopleList;

    public PeopleSummary(ArrayList<People> peopleList) {
        this.peopleList = peopleList;
    }

    public void printSummary() {
        // Starting accounting variables
      int totalPeople = peopleList.size();
      int totalAge = 0;
      int totalPeopleAbove18 = 0;
      int totalAgeAbove18 = 0;
      int totalPeopleUnder18 = 0;
      int totalAgeUnder18 = 0;

      int lowestAge = Integer.MAX_VALUE;
      String lowestName = "";
      int highestAge = Integer.MIN_VALUE;
      String highestName = "";

        // Calculate people age
      for (People person : peopleList) {
          int age = person.getAge();
          totalAge += age;

          if (age > 18) {
              totalPeopleAbove18++;
              totalAgeAbove18 += age;
          } else {
              totalPeopleUnder18++;
              totalAgeUnder18 += age;
          }

            // Get lowest age with name
          if (age < lowestAge) {
              lowestAge = age;
              lowestName = person.getName();
          }
            // Get highest age with name
          if (age > highestAge) {
              highestAge = age;
              highestName = person.getName();
          }
      }

      // Print total count
      System.out.println("Total people: " + totalPeople);

      // Print average age
      double averageAge = totalPeople > 0 ? (double) totalAge / totalPeople : 0;
      System.out.println("Average age: " + averageAge);

      // Print percentage of people above 18
      double percentageAbove18 = totalPeople > 0 ? ((double) totalPeopleAbove18 / totalPeople) * 100 : 0;
      System.out.println("Percentage of people above 18: " + percentageAbove18 + "%");

      // Print percentage of people under 18
      double percentageUnder18 = totalPeople > 0 ? ((double) totalPeopleUnder18 / totalPeople) * 100 : 0;
      System.out.println("Percentage of people under 18: " + percentageUnder18 + "%");

      // Print lowest age and corresponding name
      System.out.println("Lowest age: " + lowestAge + ", Name: " + lowestName);

      // Print highest age and corresponding name
      System.out.println("Highest age: " + highestAge + ", Name: " + highestName);
  }
}