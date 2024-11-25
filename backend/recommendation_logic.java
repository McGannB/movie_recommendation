import java.util.*;

public class RecommendationLogic {
    public static void main(String[] args) {
        int userId = Integer.parseInt(args[0]);

        // Example: Mock recommendation logic
        List<String> recommendations = new ArrayList<>();
        if (userId == 1) {
            recommendations = Arrays.asList("Inception", "The Matrix");
        } else if (userId == 2) {
            recommendations = Arrays.asList("The Matrix", "Inception");
        }

        // Output recommendations
        System.out.println(String.join(", ", recommendations));
    }
}