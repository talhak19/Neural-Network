import NN_for_classification
import NN_for_rating
import csv_class
import data_staff
import text_transformation
import analysis
import determine_user_type
import warnings
warnings.filterwarnings('ignore')


credits = csv_class.CSV('./data/credits.csv')
keywords = csv_class.CSV('./data/keywords.csv')
ratings = csv_class.CSV('./data/ratings_small.csv')
movies =csv_class.CSV('./data/movies_metadata.csv')


#Bazı sütunları drop edip, tip dönüşümü uyguluyoruz.
movies = data_staff.data_cleaning(movies.df)
#Dataları merge ediyoruz
df = data_staff.data_merge(movies,keywords.df,credits.df)
#Boş satırlara işlemler uyguluyoruz.
df = data_staff.process_about_nan_rows(df)


# Yeni sütunlar üretmek ve seçilmiş sütunların içeriğini text yapmak için
df = text_transformation.text_columns(df)
df = text_transformation.new_columns(df)

df = df.merge(ratings.df, left_on='id', right_on='movieId')

#Analiz yapabilmek için film türlerini , ile ayırma işlemi
df["genres"]= df['genres'].apply(lambda x: x.strip().split(',')[0])


#Analiz yaptığımız işlemler için
print("\nAnalyze each genres based on ratings \n")
analysis.analysis_each_genres_based_on_rating(df)
print("\nAnalyze user preferences\n")
analysis.analyze_user_preferences(df)


#User type belirleme ve user type'a dair islemler
df["user_types"]=determine_user_type.determine_user_types(df)
print(df['user_types'].value_counts())
df["user_types"] = [0 if x=="Kotumser" else 1 for x in df["user_types"]]


#User type classification'u icin işlemlerimiz
NN_for_classification.create_nn_model_and_fit(df)


#Rating predictionu için işlemlerimiz
NN_for_rating.create_nn_model_and_fit(df)
