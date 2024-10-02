import pandas as pd
df=pd.read_csv(r'C:\Users\k236090\Desktop\heart.csv')

print(df['ca'].unique())
print(df[df['ca']== 2])
print(df[df['ca']== 1])
cagroup= df.groupby('ca')
#when we apply filter to groupby so selection is single group single column (male and their salary analysis)
print(cagroup['age'].mean())
#single group multiple column (male and their salary age etc analysis)
print(cagroup[['age','cp']].mean())
#multiple group single analysis (male female division and further filter to hijab and non hijab)
cpgroup= df.groupby(['ca','cp'])
print(cpgroup['age'].mean())
#multiple group multiple analysis
print(cpgroup[['age','chol']].mean())
