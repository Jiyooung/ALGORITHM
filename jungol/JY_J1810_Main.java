
/*
jungol 1810 : 백설공주(Snow White)
solved by JY
DATE : 2021.01.20
BruteForce 이용
*/
import java.io.BufferedReader;
// import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class JY_J1810_Main {
    static int pick[];
    public static void main(String[] args) throws NumberFormatException, IOException {
        // System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        print(arr, arr.length);
        
        for (int j = 0; j < 7; j++) {
            System.out.println(arr[pick[j]]);
        }
    }

    public static void print(int[] arr, int n) {
        pick = new int[7];
        for (int i = 0; i < (1 << n); i++) {
            if (count(i) == 7) { // 조합 중 요소가 7개인 것만 출력
                int sum = 0;
                int p = 0;
                for (int j = 0; j < n; j++) {
                    if ((i & (1 << j)) != 0) {  // 7개 요소 더하기
                        sum += arr[j];
                        pick[p++] = j;
                    }
                }
                if (sum == 100) {
                    return;
                }
            }
        }
    }

    // num을 2진수로 표현했을때 1의 갯수 리턴
    public static int count(int num) {
        int count = 0;

        while (num > 0) {
            if ((num & 1) == 1)
                count++;
            num >>= 1;
        }

        return count;
    }
}
