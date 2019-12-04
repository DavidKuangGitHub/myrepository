/*leetcode_ReverseInteger.cpp
 *Description: Given a 32-bit signed integer, reverse digits of an integer
Example1: Input 123 	Output 321
Example2: Input -123	Output -321
Example3: Input 120	Output 21
 * */
#include <climits>
#include <iostream>
using namespace std;

class Solution {
public:
	int reverse(int x) {
		if (x == 0) return 0; 
		bool pos = x > 0;
		int res = 0;
		int dig = 0;
		while (x) {
			dig = x % 10;
			if (pos && (INT_MAX-dig)/10 < res    ) return 0;
			if (! pos && (INT_MAX-dig)/10 > res  ) return 0;
			res = res * 10 + dig;
			x = x /10;
		}
		return res; 
	}
};

int main() {
	Solution mySolutioncpp1;
	int inputValue= 120 /*-123*/;
	int result = mySolutioncpp1.reverse(inputValue); 
	cout << "In this iteration, Input is "<<  inputValue <<  " , After reverse, the Result is " << result << "  Done successfully!!!"<< endl; 
	return 0; 
}
