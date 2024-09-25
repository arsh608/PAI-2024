import pandas as pd
df=pd.read_csv(r'C:/Users/k236090/Desktop/TMDB_movie_dataset_v11.csv')

#reference: Full TMDB Movies Dataset 2024 (1M Movies) from kaggle.com
#whose revenue is more than 2 million and spent less than 1 million.

filtered_movies = df[(df['revenue'] > 2000000) & (df['budget'] < 1000000)]
result = filtered_movies[['title', 'revenue', 'budget']]
print(result)
