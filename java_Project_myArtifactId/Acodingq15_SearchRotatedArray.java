/*Acodingq15_SearchRotatedArray.java
Search for a given number in a sorted array, with unique elements, that has been
 rotated by some arbitrary number. 
Return -1 if the number does not exist. Assume that the array does not contain duplicates
example:1 10 20 47 59 63 75 88 99 107 120 133 155 162 176 188 199 200 210 222
After performing rotation on this array 6 times: 
	   176 188 199 200 210 222 1 10 20 47 59 63 75 88 99 107 120 133 155 162 So, index=3, 200true, 201false. 
*/
class Acodingq15_SearchRotatedArray {
	public static int binarySearch(int[] arr, int start, int end, int key) {
		if (start > end) {
			return -1;
		}
		int mid = start + (end - start) / 2;
		if (arr[mid] == key) {
			return mid;
		}
		if (arr[start] <= arr[mid] && key <= arr[mid] && key >= arr[start]) {
			return binarySearch(arr, start, mid - 1, key);
		} else if (arr[mid] <= arr[end] && key >= arr[mid] && key <= arr[end]) {
			return binarySearch(arr, mid + 1, end, key);
		} else if (arr[end] <= arr[mid]) {
			return binarySearch(arr, mid + 1, end, key);
		} else if (arr[start] >= arr[mid]) {
			return binarySearch(arr, start, mid - 1, key);
		}
		return -1;
	}

	static int binarySearchRotated(int[] arr, int key) {
		return binarySearch(arr, 0, arr.length - 1, key);
	}

	public static void main(String[] args) {
		int[] v1 = { 176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162 };
		boolean compareresult = false;
		int sourcevalue = 200 /* 201 */;

		int compareint = 100;
		try {
			compareint = Integer.compare(sourcevalue, v1[binarySearchRotated(v1, sourcevalue)]);
		} catch (ArrayIndexOutOfBoundsException myAIOOBE) {
			// System.out.println("Exception caught is "+ myAIOOBE.toString());
		}

		if (!((compareint > 0) || (compareint < 0))) {
			compareresult = true;
		}
		System.out.println("Result of " + sourcevalue + " is " + compareresult);
	}
}
