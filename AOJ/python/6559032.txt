import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            char cc;
            boolean flg = Character.isLowerCase(c);
            if (flg == true) {
                cc = Character.toUpperCase(c);
            } else {
                cc = Character.toLowerCase(c);
            }
            System.out.print(cc);
        }
        System.out.println();
        sc.close();
    }
}
