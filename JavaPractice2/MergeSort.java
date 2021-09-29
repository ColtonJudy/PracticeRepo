package JavaPractice2;

public class MergeSort {

    private static void divide(int[] arr, int[] firstHalf, int[] lastHalf) {
        for(int i = 0; i < firstHalf.length; i++) {
            firstHalf[i] = arr[i];
        }
        for(int i = 0; i < lastHalf.length; i++) {
            lastHalf[i] = arr[firstHalf.length + i];
        }
    }

    private static void merge(int[] arr, int[] firstHalf, int[] lastHalf) {
        int i = 0; int j = 0; int k = 0;

        while(j < firstHalf.length && k < lastHalf.length) {
            if(firstHalf[j] < lastHalf[k]) {
                arr[i++] = firstHalf[j++];
            }
            else {
                arr[i++] = lastHalf[k++];
            }
        }

        while(j < firstHalf.length) {
            arr[i++] = firstHalf[j++];
        }
        while(k < lastHalf.length) {
            arr[i++] = lastHalf[k++];
        }
    }

    public static void sort(int[] arr) {
        if(arr.length >= 2) {
            int halfLength = arr.length / 2;
            int[] firstHalf = new int[halfLength];
            int[] lastHalf = new int[arr.length - halfLength];

            divide(arr, firstHalf, lastHalf);
            sort(firstHalf);
            sort(lastHalf);
            merge(arr, firstHalf, lastHalf);
        }
    }
}
