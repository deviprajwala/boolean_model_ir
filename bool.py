#implementation of boolean model for document retrival

import pandas
terms = []
keys = []
vec_dic = {}
dicti = {}
dummy_list = []
    
def filter(documents,rows,cols):
    for i in range(rows):
        for j in range(cols):
            if(j == 0):
                keys.append(documents.loc[i].iat[j])
            else:
                dummy_list.append(documents.loc[i].iat[j])
                if documents.loc[i].iat[j] not in terms:
                    terms.append(documents.loc[i].iat[j])
                
        copy = dummy_list.copy()
        dicti.update({documents.loc[i].iat[0]:copy})
        dummy_list.clear()

def bool_representation(dicti,rows,cols):
    terms.sort()
    for i in (dicti):
        for j in terms:
            if j in dicti[i]:
                dummy_list.append(1)
            else:
                dummy_list.append(0)
        copy = dummy_list.copy()
        vec_dic.update({i:copy})
        dummy_list.clear()

def query_vector(query):
    qvect = []
    for i in terms:
        if i in query:
            qvect.append(1)
        else:
            qvect.append(0)
    return qvect        

def prediction(q_vect):
    dictionary = {}
    listi = []
    count = 0
    for i in vec_dic:
        #print(vec_dic[i]+q_vect)
        term_len = len(terms)

        for t in range(term_len):
            if(q_vect[t] == vec_dic[i][t]):
                count+=1
        dictionary.update({i:count})
        count = 0
    print(dictionary)
    for i in dictionary:
        listi.append(dictionary[i])
    listi = sorted(listi,reverse = True)
    ans = ' '

    print("ranking of the documents")
    for count,i in enumerate(listi):
        key = check(dictionary,i)
        if count == 0:
            ans = key
        print(key ,"rank is ",count+1)
        dictionary.pop(key)

    print(ans, "is the most relevant document for the given query")

def check(dictionary, val):
    for key, value in dictionary.items():
        if(val == value):
            return key

def main():
    documents = pandas.read_csv(r'documents.csv')
    rows = len(documents)
    cols = len(documents.columns) 
    filter(documents,rows,cols)
    #print(dicti)        
    bool_representation(dicti,rows,cols)
    print("Enter query")
    query = input()
    #hockey is a national sport
    query=query.split(' ')
    q_vect=query_vector(query)
    prediction(q_vect)

main()