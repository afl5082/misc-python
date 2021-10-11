import pandas as pd

test_df = {1928: [[1, 20], [3, 4]], 1929: [[1, 2], [3, 4]]}

df1 = pd.DataFrame.from_dict(test_df, orient='index').stack().reset_index()
df1[['column1', 'column2']] = pd.DataFrame(df1[0].tolist(), index=df1.index)
print(df1)
