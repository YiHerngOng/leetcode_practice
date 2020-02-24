class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indexes = {}; 
        for(int i = 0; i < nums.size(); i++){
            int first = nums[i];
            for(int j = 0; j < nums.size(); j++){
                int second = nums[j];
                if((j > i)&&(first + second == target)){
                    indexes = {i, j};
                }
            }
            
        }
    return indexes;       
    }
};