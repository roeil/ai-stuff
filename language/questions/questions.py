import nltk
import sys
import os
import numpy as np

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """


    d=dict()
	    
    for f in os.listdir(directory):
        with open(os.path.join(directory,f),encoding='iso-8859-1') as doc: d[f] = doc.read()

    return d



def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """


    tokenizer = nltk.RegexpTokenizer(r"\w+")
    new_words = tokenizer.tokenize(document)
    
    stopwords=nltk.corpus.stopwords.words("english")
    return [w.lower() for w in new_words if not w in stopwords]
    



def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    
    words=set()
    for k in documents.keys():
        words=words.union(documents[k])
    
    idf=dict()
    for word in words:
        n=0
        for k in documents.keys():
    
            if word in documents[k]:
                n+=1
                
        idf[word.lower()]=np.log(len(documents.keys())/n)

    return idf
    


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """

    topdict=dict()
    for f in files.keys():
        topdict[f]=0
        for word in query:
            word=word.lower()
                    
            if word in files[f] and word in idfs.keys() :
                

                topdict[f]+=files[f].count(word)*idfs[word]
        
    
    topdict=sorted(topdict.items(), key=lambda x: x[1], reverse=True)
    topdict=[e[0] for e in topdict]
    
    return topdict[:n]
    


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    import copy
    topdict=dict()
    query_term_density=dict()
    for s in sentences.keys():
        topdict[s]=0
        query_term_density[s]=0
        for word in query:

            if word in sentences[s]:
                topdict[s]+=idfs[word]
                query_term_density[s]+=1/len(sentences[s])
    
    

    topdictOrig=copy.deepcopy(topdict)
    topdict=sorted(topdict.items(), key=lambda x: x[1], reverse=True)
    topdict_k=[e[0] for e in topdict]
    

    
    
    
    topdictOrigRev={}
    for i, v in topdictOrig.items():
            
        topdictOrigRev[v] = [i] if v not in topdictOrigRev.keys() else topdictOrigRev[v] + [i]
    
    
    
    
    
    topdict_final=[]
    i=0
    '''
    Implementation of the req.:
    "If two sentences have the same 
    value according to the matching word measure, 
    then sentences with a higher “query term density” should be preferred. 
    Query term density is defined as the proportion of words in the sentence that are also words in the query.
    For example, if a sentence has 10 words, 3 of which are in the query, 
    then the sentence’s query term density is 0.3."
    '''
    
    while len(topdict_final)<len(topdict_k):
        
        if len(topdictOrigRev[topdictOrig[topdict_k[i]]]) <=1:
            topdict_final.append(topdict_k[i])
            i+=1
        else:
            qtd_sub={}
            for e in topdictOrigRev[topdictOrig[topdict_k[i]]]:
                qtd_sub[e]=query_term_density[e]
            qtd_subS=sorted(qtd_sub.items(), key=lambda x: x[1], reverse=True)
            qtd_subS_k=[e[0] for e in qtd_subS]
            topdict_final[i:(i+len(qtd_subS_k))]=qtd_subS_k
            i+=len(qtd_subS_k)
            
    return topdict_final[:n]      
                
            
            

    
    
    

if __name__ == "__main__":
    main()
