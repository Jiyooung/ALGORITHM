/*
jungol 1810 : 백설공주(Snow White)
solved by JY
DATE : 2020.01.21
재귀 사용
*/
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

// 재귀 사용
public class JY_J1810_2_Main {
    static int N = 9;
	static int[] arr = new int[N];
	static boolean[] b = new boolean[N];

	public static void main(String[] args) throws NumberFormatException, IOException {
		System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 9; i++) {
			arr[i] = Integer.parseInt(br.readLine().trim());
		}

		check(0, 0, 0);
	}

	public static void check(int idx, int cnt, int sum) {
		if (sum > 100) return ;
		if (cnt == 7 && sum == 100) {
			for (int i = 0; i < N; i++) {
				if (b[i]) System.out.println(arr[i]);
			}
			return ;
		}
		if (cnt >= 7 || idx == 9) return ;

		b[idx] = true;
		check(idx + 1, cnt + 1, sum + arr[idx]);

		b[idx] = false;
		check(idx + 1, cnt, sum);
	}
}