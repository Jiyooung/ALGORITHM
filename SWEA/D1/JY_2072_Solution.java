/*
SWEA 2072 : 홀수만 더하기
solved by JY
DATE : 2020.01.20
*/
import java.util.Scanner;

public class JY_2072_Solution {
    public static void main(String args[]) throws Exception{
        // System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
         
        int T = sc.nextInt();
         
        for (int i=0; i<T; i++) {
            int answer = 0;
            for (int j=0; j<10; j++) {
                int num = sc.nextInt();
                if (num % 2 == 1) {
                    answer += num;
                }
            }
            System.out.printf("#%d %d\n", i+1, answer);         
        }
        sc.close();
    }
}