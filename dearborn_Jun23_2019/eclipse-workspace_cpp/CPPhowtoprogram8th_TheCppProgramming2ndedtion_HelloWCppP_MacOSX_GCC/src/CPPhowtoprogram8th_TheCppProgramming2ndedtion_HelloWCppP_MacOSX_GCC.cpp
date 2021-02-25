//copied from fig04_10.cpp
#include <iostream>

#include "Leetcode_num75.cpp"
//#include "GradeBook.h"

using namespace std;

void printVector_int (vector<int>& nums_in_print)
{
	for(int i=0; i<nums_in_print.size(); ++i)
	  std::cout << nums_in_print[i] << ' ';
}

int main/*_changedonMay1_2019*/() {

	vector<int> g1;

	g1.push_back(2);
	g1.push_back(0);
	g1.push_back(2);
	g1.push_back(1);
	g1.push_back(1);
	g1.push_back(0);
	printVector_int(g1);

	Solution_leetcode_num75 myS_leetcode_num75;
	//vector<int> MyResult;
	//MyResult=myS_leetcode_num75.sortColors(g1));
	myS_leetcode_num75.sortColors(g1);
	cout<<"\nAfter being sorted, it becomes \n"<< endl;
	printVector_int(g1);
	//cout<<"\nDone"<< endl;
	return 0;
}
