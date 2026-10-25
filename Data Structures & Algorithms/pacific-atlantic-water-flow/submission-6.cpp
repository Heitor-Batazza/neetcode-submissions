class Solution {
public:
    int ROWS;
    int COLS;
    const vector<vector<int>>* heightsPtr;

    void dfs(int r, int c, set<vector<int>>& visit, int prevHeight) {
        if (visit.count({r, c}) || r < 0 || c < 0 || r == ROWS || c == COLS || prevHeight > (*heightsPtr)[r][c]) {
            return;
        }
        visit.insert({r, c});
        dfs(r, c + 1, visit, (*heightsPtr)[r][c]);
        dfs(r + 1, c, visit, (*heightsPtr)[r][c]);
        dfs(r, c - 1, visit, (*heightsPtr)[r][c]);
        dfs(r - 1, c, visit, (*heightsPtr)[r][c]);
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> res;
        ROWS = heights.size();
        COLS = heights[0].size();
        heightsPtr = &heights;

        set<vector<int>> pac;
        set<vector<int>> atl;

        for (int r = 0; r < ROWS; r++) {
            dfs(r, 0, pac, (*heightsPtr)[r][0]);
            dfs(r, COLS - 1, atl, (*heightsPtr)[r][COLS - 1]);
        }

        for (int c = 0; c < COLS; c++) {
            dfs(0, c, pac, (*heightsPtr)[0][c]);
            dfs(ROWS - 1, c, atl, (*heightsPtr)[ROWS - 1][c]);
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (pac.count({r, c}) && atl.count({r, c})) {
                    res.push_back({r, c});
                }
            }
        }

        return res;
    }
};
