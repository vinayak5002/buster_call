import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static final int BIG_NUM  = 2000000000;
	public static final int MOD  = 1000000007;

	public static void main(String[] args) {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		try {
			int N = Integer.parseInt(br.readLine());
			String input[] = new String[N];
			input = br.readLine().split("\\s+");

			int S[] = new int[N];
			for(int i = 0; i < input.length; i++){
				S[i] = Integer.parseInt(input[i]);
			}

			int Q = Integer.parseInt(br.readLine());
			String inputQ[] = new String[Q];
			inputQ = br.readLine().split("\\s+");

			int T[] = new int[Q];
			for(int i = 0; i < inputQ.length; i++){
				T[i] = Integer.parseInt(inputQ[i]);
			}

			Arrays.sort(T);

			int ans = 0;
			int left = 0,right,m;

			for(int i = 0; i < T.length; i++){
				right = S.length-1;
				m = (left+right)/2;

				while(left <= right){
					if(S[m] == T[i]){
						ans++;
						left = m;
						break;
					}else if(S[m] > T[i]){
						right = m-1;
					}else{
						left = m+1;
					}
					m = (left+right)/2;
				}
			}

			System.out.println(ans);

		} catch (NumberFormatException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}

