class Solution {
    int ROWS;
    int COLS;
    vector<vector<char>>* nickBoard;
private:
    void dfs(int r, int c) {
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || (*nickBoard)[r][c] != 'O') {
            return;
        }
        (*nickBoard)[r][c] = 'T';
        dfs(r + 1, c);
        dfs(r, c + 1);
        dfs(r - 1, c);
        dfs(r, c - 1);
    }
public:
    void solve(vector<vector<char>>& board) {
        ROWS = board.size();
        COLS = board[0].size();
        nickBoard = &board;

        for (int r = 0; r < ROWS; r++) {
            dfs(r, 0);
            dfs(r, COLS - 1);
        }
        for (int c = 0; c < COLS; c++) {
            dfs(0, c);
            dfs(ROWS - 1, c);
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                } else if (board[r][c] == 'T') {
                    board[r][c] = 'O';
                }
            }
        }
    }
};
