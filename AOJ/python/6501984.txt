import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int cnt = 0;
        String w, t;
        w = scanner.next();

        while (true) {
            t = scanner.next();
            if (t.equals("END_OF_TEXT")) break;

            if (t.toLowerCase().equals(w)) ++cnt;
        }
        System.out.println(cnt);
    }
}
