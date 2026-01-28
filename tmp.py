import pingouin as pg

from analyzer.data import DataContainer
from analyzer.plotting import GraphicalAnalyzer
from analyzer.stats import StatisticalAnalyzer

# Given
# method = 'pearson'
method = 'spearman'
col1 = "x"
col2 = "y"
col_covars = ["cv1"]

# Read sample dataset and create DataContainer
df = pg.read_dataset("partial_corr")
data = DataContainer.from_dataframe(df)
# print(data.df)

# Create statistical analyzer object
cols_of_interest = [col1, col2] + col_covars
anal = StatisticalAnalyzer(data_dir="~/data/", results_dir="~/research/results/",
                           data_container=data, cols_of_interest=cols_of_interest)

# Perform partial correlation analysis
corr, pval = anal.calculate_partial_corr(col1, col2, col_covars, method=method)
print(f"The partial correlation ({method}) between {col1} and {col2}, controlling for {col_covars}: {corr:0.3f} ({pval:0.2E})")

# Draw scatter plot
anal = GraphicalAnalyzer(data_dir="~/data/", results_dir="~/research/results/", data_container=data)
anal.scatter_plot_covariates(col1, col2, col_covars)
