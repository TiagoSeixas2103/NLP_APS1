import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

df = pd.read_csv('Data.csv')

#vectorizer = TfidfVectorizer() 
#X = vectorizer.fit_transform(df['Servant Name'])
#Q = vectorizer.transform(['Artoria'])
#R = X @ Q.T
#top_ten = np.argsort(-R.data)[:10]
#rows, cols = R.nonzero()
#top_ten_rows = rows[top_ten]
#top_ten_cols = cols[top_ten]
#results = []
#if len(rows) > 0:
#    for i in range(len(top_ten)):
#        output = {'title':df.iloc[top_ten_rows[i]]["Servant Name"],
#            'content':"Teste",
#            'relevance': R[top_ten_rows[i], top_ten_cols[i]].item()
#            }
#        results.append(output)
#print(results)

def get_name(query):
    results = {"results": [], "message": "OK"}

    vectorizer = TfidfVectorizer() 
    X = vectorizer.fit_transform(df['Servant Name'])
    Q = vectorizer.transform([query])
    R = X @ Q.T
    top_ten = np.argsort(-R.data)[:10]
    rows, cols = R.nonzero()
    top_ten_rows = rows[top_ten]
    top_ten_cols = cols[top_ten]
    if len(rows) > 0:
        for i in range(len(top_ten)):
            output = {'title':df.iloc[top_ten_rows[i]]['Servant Name'],
                'content':'Teste',
                'relevance': R[top_ten_rows[i], top_ten_cols[i]].item()
                }
            results['results'].append(output)
    return results
        