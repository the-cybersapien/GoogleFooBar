/**
 * Solution to try
 Given n bricks for example, m is the first staircase,
 if we want to get the most staircases, it must follow this arrangement:
 m + (m-1)+ (m-2)...+1 = (m+1)*m/2 = n;
 (m+1)*m/2 >= m*m/2 
 So we got m<=sqrt(2*n); 
 Conclusion : The height of the first staircase must be smaller than sqrt(2*n);
 */
 package xyz.cybersapien;

import java.util.Arrays;

public class Solution {

    public static void main(String[] args) {
        System.out.println(answer(200));
    }

    public static int answer(int n) {
        int s = 0;
        int mem[][] = new int[n][n];
        for (int[] row : mem) {
            Arrays.fill(row, -1);
        }
        for (int i = (int) Math.floor(Math.sqrt(n * 2)); i < n; i++) {
            s += help(n - i, i, mem);
        }
        return s;
    }

    private static int help(int left, int prev, int[][] mem) {

        if (left == 0 || prev == 1)
            return 0;

        if (mem[left][prev] != -1)
            return mem[left][prev];

        int sum = 0;

        if (prev > left)
            sum++;

        for (int i = (int) Math.floor(Math.sqrt(left * 2)); i < left; i++) {

            if (i >= prev)
                break;

            sum += help(left - i, i, mem);
        }

        mem[left][prev] = sum;
        return sum;
    }

}