// Link: https://leetcode.com/problems/set-matrix-zeroes/

#include <iostream>
#include <vector>

using namespace std;

class Solution 
{
public:
    void setZeroes(vector<vector<int>>& matrix) 
    {
        int col0 = 1, rows = matrix.size(), cols = matrix[0].size();
        for(int i = 0; i < rows; i++)
        {
            if(matrix[i][0] == 0)
            {
                col0 = 0;
            }
            for(int j = 1; j < cols; j++)
            {
                if(matrix[i][j] == 0)
                {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for(int i = rows - 1; i >= 0; i--)
        {
            for(int j = cols - 1; j >= 1; j--)
            {
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                {
                    matrix[i][j] = 0;
                }
            }
            if(col0 == 0)
            {
                matrix[i][0] = 0;
            }
        }
    }
};


int main(int argc, char const *argv[])
{
    Solution test;
    vector<vector<int>> matrix;
    for(int i = 0; i < 3; i++)
    {
        matrix.push_back({});
        for(int j = 0; j < 3; j++)
        {
            matrix[i].push_back(i);
            cout << matrix[i][j];
        }
        cout << endl;
    }
    cout << " rows = " << matrix.size() << "Columns = " << matrix[0].size();
    test.setZeroes(matrix);

    
    
    return 0;
}
