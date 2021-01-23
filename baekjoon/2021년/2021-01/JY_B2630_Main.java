import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

// 색종이 만들기
public class JY_B2630_Main {
	static int[] answer = {0, 0};
	static int [][] paper;
	public static void main(String[] args) throws NumberFormatException, IOException {
//		System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        paper = new int[N][N];
        
		for (int i=0; i<N; i++) {
            String[] tmp = br.readLine().split(" ");
			for (int j=0; j<N; j++) {
				paper[i][j] = tmp[j].charAt(0) - '0';
			}
		}
        
		int y = 0, x = 0;
		divide(y, x, N);
		System.out.printf("%d\n%d", answer[0], answer[1]);
	}
	
	public static void divide(int y, int x, int N) {
		int ret = check(y, x, N);
		if (ret != -1) {
			answer[ret]++;
			return ;
		}
		
		divide(y	 	, x			, N/2);
		divide(y	 	, x + N/2	, N/2);
		divide(y + N/2	, x			, N/2);
		divide(y + N/2 	, x + N/2	, N/2);
	}

	public static int check(int y, int x, int N) {
		int color = paper[y][x];
		for(int i=y; i< y + N; i++) {
			for (int j=x; j< x + N; j++) {
				if (paper[i][j] != color) return -1;
			}
		}
		return color;
	}
}

