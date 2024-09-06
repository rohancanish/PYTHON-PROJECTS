# Iris Dataset PCA Analysis

## Project Description

This project performs Principal Component Analysis (PCA) on the Iris dataset to reduce its dimensionality and visualize the results. PCA is used to transform the features into a new coordinate system where the greatest variances by any projection of the data come to lie on the first coordinates (principal components).

## Files

- `IRIS_DATASET.csv`: The dataset containing Iris flower data with features and target labels.
- `pca_analysis.py`: The Python script performing PCA and visualizing the results.

## Requirements

This project requires Python with the following packages:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

You can install the required packages using `pip`:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Usage

1. **Prepare the Dataset:**
   Ensure that the Iris dataset CSV file (`IRIS_DATASET.csv`) is in the same directory as the script or provide the correct path to the file.

2. **Run the Script:**
   Execute the Python script to perform PCA and visualize the results.

   ```bash
   python pca_analysis.py
   ```

3. **View the Results:**
   The script will produce a scatter plot of the first two principal components, showing the distribution of different Iris species in the reduced-dimensional space.

## Code Explanation

- **Data Loading:**
  The script reads the Iris dataset from a CSV file using `pandas`.

- **Feature and Target Extraction:**
  Features and target variables are separated for further processing.

- **Standardization:**
  Features are standardized to have a mean of 0 and a standard deviation of 1, which is essential for PCA.

- **PCA Execution:**
  PCA is performed to reduce the dimensionality of the dataset to 2 components.

- **Visualization:**
  The results of PCA are plotted using `matplotlib`, with different colors representing different Iris species.

## Example Output

The script generates a scatter plot where:
- The x-axis represents Principal Component 1.
- The y-axis represents Principal Component 2.
- Each point is colored according to its Iris species.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

