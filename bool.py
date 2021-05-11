#implementation of boolean model for document retrival

import pandas

documents = pandas.read_csv(r'documents.csv')

terms = []
keys = []
vecs = []
dicti = {}
dummy_list = []
rows = len(documents)
cols = len(documents.columns) -1

#print(documents.loc[0].iat[0])

for i in range(rows):
    for j in range(cols):
        if(j == 0):
            keys.append(documents.loc[i].iat[j])
        else:
            terms.append(documents.loc[i].iat[j])
            dummy_list.append(documents.loc[i].iat[j])
    copy = dummy_list.copy()
    dicti.update({documents.loc[i].iat[0]:copy})
    dummy_list.clear()
print(dicti)
            
