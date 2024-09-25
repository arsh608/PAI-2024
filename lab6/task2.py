import pandas as pd
df=pd.read_csv(r'C:/Users/k236090/Desktop/TMDB_movie_dataset_v11.csv')
#reference: Full TMDB Movies Dataset 2024 (1M Movies) from kaggle.com

sorted_movies = df.sort_values(by='runtime', ascending=False)
print(sorted_movies)
