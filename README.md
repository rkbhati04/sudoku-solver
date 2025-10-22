# Sudoku Solver (C++/Python)

A fast Sudoku solver using C++ for performance, callable from Python. Includes a simple GUI for interactive solving.

## Prerequisites

- Python 3.6 or newer
- pip (Python package manager)
- Microsoft Visual C++ Build Tools (Windows only, for compiling C++ extensions)

## Setup Steps

1. **Clone or download this repository.**
2. **Install required Python packages:**
   ```
   pip install setuptools pybind11
   ```
3. **Build the C++ extension:**
   ```
   python setup.py build_ext --inplace
   ```

## Usage

### Run the test script
   ```
   python test_sudoku.py
   ```
This will solve a sample puzzle and print the solution in the terminal.

### Run the GUI
   ```
   python sudoku_gui.py
   ```
Enter your puzzle in the grid and click "Solve" to see the solution interactively.

## Files

- `sudoku_solver.cpp`: C++ solver and pybind11 bindings
- `setup.py`: Build script for the extension
- `test_sudoku.py`: Example usage from Python
- `sudoku_gui.py`: Minimal Tkinter GUI for interactive solving
- `README.md`: Project instructions
- `.gitignore`: Recommended git ignore settings
