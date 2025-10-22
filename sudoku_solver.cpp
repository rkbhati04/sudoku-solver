#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
using namespace std;
namespace py = pybind11;

bool isvalid(vector<vector<int>>& a, int ch, int r, int c) {
    for(int i = 0; i < 9; i++){
        if(a[i][c] == ch || a[r][i] == ch){
            return false;
        }
        int cd = 3*(c /3) + i/3;
        int rd = 3*(r / 3) + i%3;
        if(a[rd][cd] == ch){
            return false;
        }
    }
    return true;
}

bool fn(vector<vector<int>>& a) {
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(a[i][j] == 0){
                for(int k = 1; k <= 9; k++){
                    if(isvalid(a, k, i, j)){
                        a[i][j] = k;
                        if (fn(a)) return true;
                        a[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}


// wrapper for python list
void solveSudoku(py::list py_board) {
    vector<vector<int>> board(9, vector<int>(9));
    // convert python list to C++ vector
    for(int i = 0; i < 9; ++i){
        for(int j = 0; j < 9; ++j){
            board[i][j] = py_board[i].cast<py::list>()[j].cast<int>();
        }
    }
    // solve
    fn(board);
    // copy back to python list
    for(int i = 0; i < 9; ++i){
        for(int j = 0; j < 9; ++j){
            py_board[i].cast<py::list>()[j] = board[i][j];
        }
    }
}
PYBIND11_MODULE(sudoku_solver, m) {
    m.def("solveSudoku", &solveSudoku, "Solve a 9x9 Sudoku puzzle in-place");
}
