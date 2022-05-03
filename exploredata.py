import pandas as pd

pd.set_option('display.max_columns', None)

tree_census = pd.read_csv('/mnt/d/project-chau/dataset/street_tree_census/2015-street-tree-census-tree-data.csv/2015-street-tree-census-tree-data.csv')
print(tree_census)

tree_census.columns