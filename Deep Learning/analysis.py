import matplotlib.pyplot as plt

def analysis_each_genres_based_on_rating(df):

    avg_genre_ratings = df.groupby(['genres'], as_index=False)['vote_average'].mean()
    avg_genre_ratings = avg_genre_ratings.sort_values(by=['vote_average'], ascending=False)
    print("\nRatinglere gore tür siralamasi\n",avg_genre_ratings,"\n")

    avg_genre_ratings.plot.barh(x = 'genres', y='vote_average')
    plt.xlabel('Average Rating')
    plt.ylabel('Genres')

    plt.show()

# Kullanıcıların film tercihleriyle ilgili bir analiz yapan fonksiyon
def analyze_user_preferences(data):
  # Tüm kullanıcıların ortalama puanlarını saklayacağımız liste
  average_ratings = []

  # Tüm kullanıcıları döngüye alalım
  for userId in data['userId'].unique():
    # Kullanıcının puanladığı filmleri seçelim
    user_movies = data[data['userId'] == userId]

    # Kullanıcının ortalama puanını bulalım
    average_rating = user_movies['rating'].mean()
    average_ratings.append(average_rating)

  # Histogram ile tüm kullanıcıların ortalama puanlarını görselleştirin
  plt.hist(average_ratings)
  plt.title("Average Ratings of All Users")
  plt.xlabel("Rating")
  plt.ylabel("Number of Users")
  plt.show()

  # Tüm kullanıcıların en çok puanladıkları film türlerini sayalım
  genre_counts = data['genres'].value_counts()

  # Pie chart ile tüm kullanıcıların en çok puanladıkları film türlerini görselleştirin
  plt.pie(genre_counts, labels=genre_counts.index)
  plt.title("Favorite Genres of All Users")
  plt.show()
