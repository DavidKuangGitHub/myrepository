/*Acodingq14_FindLowandHighIndex.java
Given a sorted array of integers, return the low and high index of the given value/key. You must return -1 if the indexes are not found. The array array length can be in the millions with many duplicates.
Example: 1 2 5 5 5 5 5 5 5 5 20
its index0 1 2 3 4 5 6 7 8 9 10
Value1, low=0 high=0
Value2, low=0 high=1
Value5, low=2 high=9
Value20 low=10high=10
Value21 -1
*/
class Acodingq14_FindLowandHighIndex { 
	public static void findFirstAndLast(int arr[], int x) 
	{ 
		int n = arr.length; 
		int first = -1, last = -1; 
		for (int i = 0; i < n; i++) { 
			if (x != arr[i]) 
				continue; 
			if (first == -1) 
				first = i; 
			last = i; 
		} 
		if (first != -1) { 
			System.out.println("For Element Value of "+ x + " that you have choose, Its "+"Low = " + first + "	High = " + last); 
			//System.out.println(" = " + last); 
		} 
		else
			System.out.println("Not Found"); 
	} 

	public static void main(String[] args) 
	{ 
		int arr[] = { 1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20 }; 
		int x = 5 /*10 20*/;
		/*int arr[] = { 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 }; 
		int x = 8;*/ 
		findFirstAndLast(arr, x); 
	} 
} 
