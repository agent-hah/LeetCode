package problems.bitmanipulation;

import java.util.*;

public class BinaryWatch {
    public static List<String> readBinaryWatch(int turnedOn) {
        List<String> res = new LinkedList<>();
            int[] hours = {8, 4, 2, 1};
            int[] minutes = {32, 16, 8, 4, 2, 1};


            for (int n = 0; n <= turnedOn; n++) {
                for (int grp = 0; grp + n - 1 < hours.length; grp ++) {
                    int[] hourTimes = Arrays.copyOfRange(hours, grp, grp + n);
                    int hour = 0;
                    for (int i : hourTimes) {
                        hour ^= i;
                    }
                    if (hour < 0 | hour > 11) {
                        continue;
                    }
                    int j = turnedOn - n;
                    for (int brp = 0; brp + j - 1 < minutes.length; brp ++) {
                        int[] minuteTimes = Arrays.copyOfRange(minutes, brp, brp + j);
                        if (hourTimes.length + minuteTimes.length != turnedOn) {
                        continue;
                        }
                        int minute = 0;
                        for (int k : minuteTimes) {
                            minute ^= k;
                        }
                        if (minute < 0 | hour > 59) {
                            continue;
                        }
                        if (minute < 10) {
                            String toAdd = hour + ":" + 0 + minute;
                            if (!res.contains(toAdd)) {
                                res.add(toAdd);
                            }
                        } else {
                            String toAdd = hour + ":" + minute;
                            if (!res.contains(toAdd)) {
                                res.add(toAdd);
                            }
                        }
                    }
                }
            }
            return res;
        }

        public static List<String> readBinaryWatch(int turnedOn, int helpMe) {
            List<String> res = new LinkedList<>();
            for (int h = 0; h < 12; h ++) {
                for (int m = 0; m < 60; m++) {

                    if (Integer.bitCount(h) + Integer.bitCount(m) == turnedOn) {
                        if (m < 10) {
                            res.add(h + ":0" + m);
                        } else {
                            res.add(h + ":" + m);
                        }
                    }
                }
            }
            return res;
        }

        public static void main(String[] args) {
            System.out.println(readBinaryWatch(2, 20).toString());
        }
}