/*
 * Leetcode_num79wordsearch.cpp, then change 78, then change to 76,then 75
 *
 *  Created on: Apr. 13, 2019
 *      Author: family
 *//*Given a 2D board and a word */

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution_leetcode_num75 {
public:
	    void sortColors(vector<int>& nums) {
	        int numZeroes = 0;
	        int numOnes = 0;
	        int numTwos = 0;
	        for (auto it = nums.begin(); it != nums.end(); ++it) {
	            if (*it == 0) {
	                ++numZeroes;
	            } else {
	                if (*it == 1) ++numOnes;
	                else ++numTwos;
	                *it = 0;
	            }
	        }
	        nums.resize(numZeroes);
	        nums.insert(nums.end(), numOnes, 1);
	        nums.insert(nums.end(), numTwos, 2);
	    }
};
