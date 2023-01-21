
from ast import literal_eval

def get_text(text, obj='name'):
    text = literal_eval(text)
    
    if len(text) == 1:
        for i in text:
            return i[obj]
    else:
        s = []
        for i in text:
            s.append(i[obj])
        return ', '.join(s)


def text_columns(df):
    df['genres'] = df['genres'].apply(get_text)
    df['production_companies'] = df['production_companies'].apply(get_text)
    df['production_countries'] = df['production_countries'].apply(get_text)
    df['crew'] = df['crew'].apply(get_text)
    df['keywords'] = df['keywords'].apply(get_text)

    return df


def new_columns(df):
    df['characters'] = df['cast'].apply(get_text, obj='character')
    df['actors'] = df['cast'].apply(get_text)
    
    df.drop('cast', axis=1, inplace=True)
    df = df[~df['original_title'].duplicated()]
    df = df.reset_index(drop=True)

    return df