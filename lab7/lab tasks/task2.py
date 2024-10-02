import pandas as pd
df=pd.read_csv(r'C:\Users\k236090\Desktop\heart.csv')
#heart.csv in lab 6 repository uploaded

df.rename(columns={'sex': 'gender'}, inplace=True)
df['gender'] = df['gender'].map({0: 'female', 1: 'male'})
print(df)

gengroup= df.groupby('gender')
print(gengroup['chol'].max())
mgengroup= df.groupby(['gender','restecg','oldpeak','chol'])
print(mgengroup.describe())
