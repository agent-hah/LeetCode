package problems.bitManipulation;

public class findTheDifference {
    public static char method(String s, String t) {
        int res = 0;

        for (char c : s.toCharArray()) {
            res ^= (int) c;
        }
        for (char c : t.toCharArray()) {
            res ^= (int) c;
        }
        return (char) res;
    }

    public static void main(String[] args) {
        char res = findTheDifference.method("ilovemen", "ilovemnes");
        System.out.print(res);
    }
}