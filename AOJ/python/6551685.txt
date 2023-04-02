import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        HashSet<String> set = new HashSet<>();

        for (int i = 0; i < n; ++i) {
            String command = scanner.next(), str = scanner.next();

            if (command.equals("insert")) set.add(str);
            else System.out.println((set.contains(str) ? "yes" : "no"));
        }
    }
}
