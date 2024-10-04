### Water Jug Problem

The Water Jug Problem is a classic problem in artificial intelligence and computer science that involves determining the steps to measure a specific amount of water using two jugs with different capacities. This project implements a solution to the problem using Python.

## Problem Statement

Given two jugs of different capacities, the objective is to measure a specific amount of water using the jugs, filling them, and pouring water between them as needed. The jugs can hold a maximum amount of water, and the goal is to find a sequence of steps to reach the desired measurement.

## Features

- Implements the Water Jug Problem using a breadth-first search algorithm.
- Displays the sequence of steps taken to reach the target amount of water.
- User-friendly interface for inputting jug capacities and the target amount.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rohancanish/PYTHON-PROJECTS.git
   ```

2. Navigate to the project directory:
   ```bash
   cd WATER_JUG_PROBLEM
   ```

3. Run the Python script:
   ```bash
   python water_jug_problem.py
   ```

## Usage

- Input the capacities of the two jugs and the desired amount of water.
- The program will output the sequence of steps to measure the target amount.

## Example

```
Enter the capacity of Jug 1: 4
Enter the capacity of Jug 2: 3
Enter the target amount: 2
```

Output:
```
Steps to reach the target amount:
1. Fill Jug 1
2. Pour water from Jug 1 to Jug 2
3. Empty Jug 2
4. Pour water from Jug 1 to Jug 2
5. Empty Jug 1
6. Pour water from Jug 2 to Jug 1
7. Fill Jug 2
8. Pour water from Jug 1 to Jug 2
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

Feel free to modify any sections to better fit your project's specifics!
