import pandas as pd
data = {
    'title': ['Movie A', 'Movie B', 'Movie C'],
    'revenue': [3000000, 2500000, 1500000],
    'budget': [500000, 700000, 300000]}

df = pd.DataFrame(data)
#index rather than 0
df.index = range(100, 100 + len(df))
print(df)
