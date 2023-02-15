def determine_user_types(data):
  # Kullanıcıların puanlarının ortalamasını hesaplayalım
  mean_rating = data['rating'].mean()

  # Kullanıcıları sınıflandıracağımız sözlük
  user_types = {}

  # Tüm kullanıcıları döngüye alalım
  for userId in data['userId'].unique():
    # Kullanıcının verdiği puanları seçelim
    user_ratings = data[data['userId'] == userId]['rating']

    # Kullanıcının puanlarının ortalamasını hesaplayalım
    user_mean_rating = user_ratings.mean()

    # Kullanıcının puan ortalaması ortalama puanın altında ise Kotumser Kullanıcı, üstündeyse İyimser Kullanıcı olarak sınıflandıralım
    if user_mean_rating < mean_rating:
      user_types[userId] = "Kotumser"
    else:
      user_types[userId] = "İyimser"

  # Sözlük verisini sütun haline getirin
  user_types_column = []
  for index, row in data.iterrows():
    if row['userId'] in user_types:
      user_types_column.append(user_types[row['userId']])
    else:
      user_types_column.append(None)

  
  return user_types_column
