package com.google.challenges; 

import java.math.BigInteger;
import java.util.*;

public class Answer {   
    public static String answer(int[] xs) {

        // Creating all the lists with the max possible size
        // Wastage of space, but time is saved B)
        List<Integer> allNums = new ArrayList<>(xs.length);
        List<Integer> negs = new ArrayList<>(xs.length);

        // Sort the original array
        Arrays.sort(xs);

        int numNegs = 0;

        // Assign to the specified lists
        for (int x : xs) {
            allNums.add(x);
            if (x < 0)
                negs.add(x);
        }

        // Sort the damn lists!
        Comparator<Integer> sortingComp = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return Integer.compare(Math.abs(o1), Math.abs(o2));
            }
        };

        Collections.sort(allNums, sortingComp);
        Collections.sort(negs, sortingComp);

        if (negs.size() % 2 != 0) {
            numNegs = negs.size() - 1;
        } else if (negs.size() != 0) {
            numNegs = negs.size();
            int min = allNums.get(allNums.size() - 1);
            if (min < 0) {
                min *= -1;
            }
            for (int x : allNums) {
                if (x >= 0 && x < min) {
                    min = x;
                }
            }
            allNums.remove(allNums.indexOf(min));
            allNums.add(0, 0);
        }

        BigInteger result = new BigInteger("1");

        if (allNums.size() == 1) {
            result = new BigInteger(allNums.get(0).toString());
        } else {
            for (int i = allNums.size() - 1; i > 0; i--) {
                if (allNums.get(i) < 0 && numNegs >= 1) {
                    numNegs--;
                    result = result.multiply(new BigInteger(allNums.get(i).toString()));
                }  else if (allNums.get(i) < 0 && numNegs <= 0) {
                    // Empty just so I don't have to put these conditions in reverse again and again!
                    // For some reason, if I just reverse this statment and put the next 2 here as a nested block,
                    // 2 test cases fail. I seriously don't get it!
                } else if (result.longValue() == 1 && i == 1 && allNums.get(i) == 0) {
                    result = new BigInteger(String.valueOf("0"));
                } else if (allNums.get(i) != 0){
                    result = result.multiply(new BigInteger(allNums.get(i).toString()));
                }
            }
        }
        return result.toString();
    }
}