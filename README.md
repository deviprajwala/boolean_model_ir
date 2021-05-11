# boolean_model_ir
Information retrieval (IR) is finding material (usually documents) of an unstructured nature, that satisfies an information need from within large collections.Boolean model is a simple 
retrieval model based on set theory and boolean algebra. Queries are designed as boolean expressions which have precise semantics. Retrieval strategy is based on binary decision 
criterion. Boolean model considers that index terms are present or absent in a document.

This repositary consists of a program which is the implementation of the boolean model, a document file which the names of the documents and the terms present in them, a text file which 
the output obtained when the particular query is given as input.

In the program, initially we read the data from the csv file as a dataframe,and separate the name of the documents and the terms present in it to a separate list  from the data frame 
and also create a dictionary which has the name of the document as key and the terms present in it as the list of strings  which is the value of the key. Then we get a boolean 
representation of the terms present in the documents in the form of lists, later we create a dictionary which contains the the name of the documents as key and value as the list of 
boolean values representing the terms present in the document
    
Later we get the query as the input from the user and then represent the query in the form of boolean vector.Prediction is made regarding which document is related to the given query by 
performing the boolean operations. We also generate the rankings for the documents based on the relevance
           
