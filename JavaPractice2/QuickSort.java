package JavaPractice2;

public class QuickSort {

    private static void swap(int[] arr, int i1, int i2) {
        int temp = arr[i1];
        arr[i1] = arr[i2];
        arr[i2] = temp;
    }

    private static int partition(int[] arr, int pivot, int firstIndex, int lastIndex) {
        int i = firstIndex;
        int j = lastIndex;

        while(i < j) {
            while(arr[i] <= pivot && i < lastIndex) {
                i++;
            }
            while(arr[j] > pivot && j > firstIndex) {
                j--;
            }
            if(i < j) {
                swap(arr, i, j);
            }
        }
        return j;
    }

    public static void sort(int[] arr) {
        sort(arr, 0, arr.length - 1);
    }

    public static void sort(int[] arr, int firstIndex, int lastIndex) {
        if(firstIndex < lastIndex) {
            int pivotPoint = partition(arr, arr[firstIndex], firstIndex, lastIndex);
            swap(arr, firstIndex, pivotPoint);
            sort(arr, firstIndex, pivotPoint - 1);
            sort(arr, pivotPoint + 1, lastIndex);
        }
    }
}