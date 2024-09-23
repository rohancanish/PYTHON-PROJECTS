
## Naive Bayesian Classifier

This repository contains a Jupyter Notebook implementation of a Naive Bayesian Classifier using the Iris dataset. The classifier leverages the Gaussian Naive Bayes algorithm to classify iris flower species based on their features.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Overview

The Naive Bayesian Classifier is a simple yet powerful classification algorithm based on Bayes' theorem. This project demonstrates its application on the well-known Iris dataset, which includes three species of iris flowers and four features: sepal length, sepal width, petal length, and petal width.

## Features

- Loads and preprocesses the Iris dataset.
- Splits the data into training and testing sets.
- Scales features for better performance.
- Implements a Gaussian Naive Bayes classifier.
- Evaluates the model using accuracy, confusion matrix, precision, and recall.
- Predicts the species of an unknown iris flower.

## Installation

To run this project, you need to have Python and the required libraries installed. You can install the necessary libraries using pip:

```bash
pip install numpy pandas scikit-learn
```

If you're using Jupyter Notebook, make sure to have it installed as well:

```bash
pip install jupyter
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/rohancanish/PYTHON-PROJECTS.git
   cd PYTHON-PROJECTS/NAIVE_BAYESIAN_CLASSIFIER
   ```

2. Open the Jupyter Notebook:

   ```bash
   jupyter notebook Naive_Bayesian_Classifier.ipynb
   ```

3. Run the notebook cells to execute the code and see the results.

## Results

The classifier achieved an accuracy of **1.0** on the test set, indicating perfect classification. The results include:

- **Confusion Matrix**: Displays the true positive and false positive predictions.
- **Classification Report**: Provides detailed metrics including precision, recall, and F1-score for each class.
- **Predicted class for an unknown flower**: Demonstrates the classifier's ability to predict unseen data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

### Notes:
- Make sure the links and commands match your actual project structure and setup.
- You can further customize the content based on any specific details you want to highlight.
