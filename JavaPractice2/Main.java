package JavaPractice2;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        System.out.println("\nThis program will implement a binary search algorithm\n");

        int[] arr = createRandomArray(50, 100);
        displayArrayContents(arr);

        System.out.println("Running quickSort on array\n");
        QuickSort.sort(arr);

        displayArrayContents(arr);

        System.out.println("Running Binary Search for 21");
        System.out.println(BinarySearch.search(arr, 21, 0, arr.length));
    };

    static void displayArrayContents(int[] arr) {
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + ", ");
        }
        System.out.print("\n\n");
    }

    static int[] createRandomArray(int length, int maxSize) {
        Random rand = new Random();
        int[] arr = new int[length];
        for(int i = 0; i < arr.length; i++) {
            arr[i] = rand.nextInt(maxSize);
        }

        return arr;
    }
}
