

### Support Vector Machines

This repository contains Python implementations of Support Vector Machine (SVM) algorithms, focusing on classification tasks using various datasets, including the popular handwritten digits dataset.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Features

- Implementation of SVM with a linear kernel.
- Evaluation metrics including classification reports and confusion matrices.
- Visualization of support vectors.
- Easy-to-understand code structure with comments.

## Installation

To run the code in this repository, ensure you have Python installed along with the following libraries:

```bash
pip install numpy pandas scikit-learn matplotlib
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/rohancanish/PYTHON-PROJECTS.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PYTHON-PROJECTS/SUPPORT_VECTOR_MACHINES
   ```

3. Run the SVM implementation:

   ```bash
   python svm_digits.py  # Replace with the appropriate script name
   ```

## Results

The implementation provides classification reports and confusion matrices as output. Additionally, it visualizes support vectors used by the model.

### Example Output

```plaintext
Classification Report:
              precision    recall  f1-score   support

           0       0.97      0.97      0.97        55
           1       0.98      0.95      0.96        57
           2       0.93      0.98      0.95        50
...
Confusion Matrix:
[[53  1  0]
 [ 0 54  3]
 [ 0  0 49]]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
