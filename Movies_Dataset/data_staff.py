
def data_cleaning(movies):

    movies = movies.drop(['belongs_to_collection', 'homepage',"spoken_languages",'imdb_id', 'poster_path', 'status', 'title', 'video'], axis=1).\
            drop([19730, 29503, 35587]) # Incorrect data type

    movies['id'] = movies['id'].astype('int64')

    return movies

def data_merge(movies,keywords,credits):
    
    df = movies.merge(keywords, on='id').\
        merge(credits, on='id')

    return df


def process_about_nan_rows(df):
    df['original_language'] = df['original_language'].fillna('')
    df['runtime'] = df['runtime'].fillna(0)
    df['tagline'] = df['tagline'].fillna('')

    df.dropna(inplace=True)

    return df