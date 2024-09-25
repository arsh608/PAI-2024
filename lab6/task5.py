import pandas as pd

data = {
    'Year': [1988, 1986, 1985, 1990, 1992, 1987, 1989, 1991, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004],
    'WHO Region': ['Western Pacific', 'Americas', 'Africa', 'Europe', 'Southeast Asia', 'Western Pacific', 'Americas', 'Africa', 'Europe', 'Southeast Asia',
                   'Western Pacific', 'Americas', 'Africa', 'Europe', 'Southeast Asia', 'Western Pacific', 'Americas', 'Africa', 'Europe', 'Southeast Asia'],
    'Country': ['Viet Nam', 'Uruguay', "Côte d'Ivoire", 'France', 'India', 'Japan', 'Brazil', 'Nigeria', 'Germany', 'Thailand',
                'China', 'Argentina', 'Kenya', 'United Kingdom', 'Sri Lanka', 'Philippines', 'Canada', 'Ghana', 'Spain', 'Indonesia'],
    'Beverage Types': ['Wine', 'Other', 'Wine', 'Spirits', 'Beer', 'Wine', 'Beer', 'Spirits', 'Wine', 'Other',
                       'Beer', 'Spirits', 'Wine', 'Beer', 'Spirits', 'Wine', 'Other', 'Wine', 'Beer', 'Spirits'],
    'Display Value': [0, 0.5, 1.62, 3.2, 2.1, 0.6, 1.8, 2.7, 2.3, 1.9, 1.5, 3.0, 2.2, 4.0, 1.3, 0.9, 2.4, 1.7, 2.8, 3.1]
}

df = pd.DataFrame(data)

df.to_csv(r'C:\Users\k236090\Desktop\world_alcohol_consumption.csv', index=False)
print(df)
print("Shape of the dataset:", df.shape)
print("Column names:", df.columns)
