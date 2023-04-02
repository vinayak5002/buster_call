import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = 0;
        while (true) {
            String s1, s2;
            s1 = sc.next();
            if (s1.equals(".")) break;
            else s2 = sc.next();
            judge(s1, s2);
        }
    }
    static void judge(String s1, String s2) {
        if (s1.equals(s2)) {
            System.out.println("IDENTICAL");
            return;
        }
        String[] a1 = s1.split("\"", -1);
        String[] a2 = s2.split("\"", -1);
        int k = 0;
        if (a1.length == a2.length) {
            int n = a1.length;
            for (int i = 0; i < n; i++) {
                if (!a1[i].equals(a2[i])) {
                    if (i%2 == 0) k += 2;
                    else k += 1;
                }
            }
            if (k == 1) {
                System.out.println("CLOSE");
                return;
            }
        }
        System.out.println("DIFFERENT");
    }
}
