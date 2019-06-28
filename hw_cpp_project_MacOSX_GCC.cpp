//============================================================================
// Name        : hw_cpp_project_MacOSX_GCC.cpp
// Author      : David Kuang
// Version     :
// Copyright   : Your copyright notice_YHK2
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

/*using namespace std;
int main()
{
	cout << "This is a c++ demo modified/updated from an existing working project by David Kuang in Michigan US on Jun 28th 2019.";
	return 0;
}*/


#include "Solution_cppSourcefile.cpp"
using namespace std;

void printVector_int (vector<int>& nums_in_print)
{
	for(int i=0; i<nums_in_print.size(); ++i)
	  std::cout << nums_in_print[i] << ' ';
}
int main() {
	vector<int> g1;
	g1.push_back(2);
	g1.push_back(7);
	g1.push_back(11);
	g1.push_back(15);
	printVector_int(g1);
	cout<<endl;
	int target=26;

	//cout << "Hello World_on Apr 13, 2019" << endl; // prints !!!Hello World!!!
	Solution mySolution;
	vector<int> theResult;
	theResult=mySolution.twoSum(g1,target);
	printVector_int(theResult);
	//cout<<"Done "<<endl;
	return 0;
}
