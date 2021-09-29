package JavaPractice2;

public class BinarySearch {
    public static int search(int[] arr, int target, int first, int last) {
        int result = -1;

         //the range is not empty
        if(first <= last){
            int mid = (first + last)/2;

            //the target is found 
            if(target == arr[mid]) {
                result = mid;
            }

            //the target must come before mid
            else if(target < arr[mid]) {
                result = search(arr, target, first, mid-1);
            }
            else {
                result = search(arr, target, mid + 1, last);
            }
        }
        return result;
    }
}
