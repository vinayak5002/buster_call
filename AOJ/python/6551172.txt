import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while(true) {
			String s = scan.next();
			if(s.equals("-")) {
				break;
			}
			int m = scan.nextInt();
			for(int i = 0; i < m; i++) {
				int t = scan.nextInt();
				s = s.substring(t, s.length()) + s.substring(0, t);
			}
			System.out.println(s);
		}
		scan.close();
	}
}
