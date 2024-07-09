class Solution {

    public static int smallestSubWithSum(int x, int[] arr) {
        int n = arr.length;
        int minLength = Integer.MAX_VALUE;
        int start = 0, end = 0, currentSum = 0;

        while (end < n) {
            while (currentSum < x && end < n) {
                currentSum += arr[end++];
            }
            while (currentSum >= x && start < n) {
                minLength = Math.min(minLength, end - start);
                currentSum -= arr[start++];
            }
        }
        return (minLength == Integer.MAX_VALUE) ? 0 : minLength;
    }
}
