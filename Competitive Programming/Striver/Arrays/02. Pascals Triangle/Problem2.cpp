#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) 
    {
        vector<vector<int>> matrix;
        matrix.push_back({});
        matrix[0].push_back(1);
        for(int i = 1; i < numRows; i++)
        {
            matrix.push_back({});
            for(int j = 0; j < matrix.size(); j++)
            {
                if(j == 0 || j == matrix.size() - 1)
                {
                    matrix[i].push_back(1);
                }
                else
                {
                    int number = matrix[i-1][j-1] + matrix[i-1][j];
                    matrix[i].push_back(number);
                }

            }
        }

        return matrix;
    }
};

int main(int argc, char const *argv[])
{
    Solution test;
    vector<vector<int>> matrix;

    matrix = test.generate(5);
    for(int i = 0; i < matrix.size(); i++)
    {
        for(int j = 0; j < matrix[i].size(); j++)
        {
            cout << matrix[i][j];
        }
        cout << endl;
    }
    return 0;
}