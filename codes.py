import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("netflix_titles.csv")
print(df.shape)
print(df.head())
print(df.isnull().sum())
df.fillna({'country':"Unknown"},inplace=True)
df.fillna({'rating':"Unknown"},inplace=True)
df['date_added']=pd.to_datetime(df['date_added'],errors='coerce')
df['year_added']=df['date_added'].dt.year
#Movies vs TV shows count
sns.countplot(data=df, x='type',palette='pastel')
plt.title('Count of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()
#Content added per year
df['year_added'].value_counts().sort_index().plot(kind='bar',figsize=(10,5),color='lightgreen')
plt.title('Content Added to Netflix Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.grid(axis='y')
plt.show()
#Top 10 countries producing content
top_countries=df['country'].value_counts().head(10)
top_countries.plot(kind='barh',color='orange')
plt.title('Top 10 Countries Producing Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()
#Most common ratings
df['rating'].value_counts().head(10).plot(kind='bar',color='blue')
plt.title('Most Common Content Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()
#Top Genres
from collections import Counter
genre_list=[]
df['listed_in'].dropna().apply(lambda x:genre_list.extend(x.split(',')))
top_genres=pd.Series(Counter([genre.strip() for genre in genre_list])).sort_values(ascending=False).head(10)
top_genres.plot(kind='barh',color='purple')
plt.title("Top 10 Most Frequent Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()
#Top 10 directors
top_directors=df['director'].dropna().value_counts().head(10)
top_directors.plot(kind='bar',color='coral')
plt.title('Top 10 Most Featured Directors on Netflix')
plt.xlabel('Director')
plt.ylabel('Count')
plt.show()
