import os
import random
import re
import sys
import numpy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    print(corpus)
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print("PageRank Results from Sampling (n = {})".format(SAMPLES))
    for page in sorted(ranks):
        print("  {}: {}".format(page,ranks[page]))
    ranks = iterate_pagerank(corpus, DAMPING)
    print("PageRank Results from Iteration")
    for page in sorted(ranks):
        print("  {}: {}".format(page,ranks[page]))


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    #print("DF: ", damping_factor)
    probs=dict()
    #print('APGE=',page)
    ln=len(corpus[page])
    
    ln2=len(corpus.keys())
    
    revDamp=(1-damping_factor)/ln2
    dampZero=damping_factor/ln2
    if ln>0:
        for p in corpus[page]:
            probs[p]=damping_factor/ln
    
    for k in corpus.keys():
        if k in corpus[page]:
            probs[k]+=revDamp
        else:
            probs[k]=revDamp
#    if ln==0:
#        for k in corpus.keys():
#            probs[k]+=dampZero
        
    #print("probs: ", probs)
    return probs
    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #print('page= ',list(corpus.keys())[1])
    #transition_model(corpus, list(corpus.keys())[1], damping_factor)
    

    page = random.sample(corpus.keys(), 1)[0]

    for k in corpus.keys():    
        if len(corpus[k])==0:
            corpus[k]=set(corpus.keys())  
        
    pagelist=[]
    rankdict=dict()
    for i in range(n):
        #print("***********",    page)
        pagelist.append(page)
        probs=transition_model(corpus, page, damping_factor)
        #print("########****",    probs)
        
        page=list(numpy.random.choice(list(probs.keys()),1, p=list(probs.values())))[0]
        
        
    #print(pagelist)
    list_set_pagelist=list(set(pagelist))
    print("list_set_pagelist= ",list_set_pagelist)
    freq=[pagelist.count(x)/len(pagelist) for x in list_set_pagelist]
    #list_pagelist=list(set_pagelist)
    for i in range(len(freq)):
        rankdict[list_set_pagelist[i]]=freq[i]
        
#
#    print('freq=',freq)
#    print('sum=',sum(freq))
#    print('rankdict= ',rankdict)
#    print(n)
#        
    
    
    return rankdict# NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    
    df, rdf=damping_factor, (1-damping_factor)
    iterdic=dict()
    n=len(corpus.keys())
    for k in corpus.keys():
        iterdic[k]=1/n
    
    # create a dict of pages -> pages that link to it
    linkedic=dict()
    for k in corpus.keys():
        linkedic[k]=set()
        if len(corpus[k])==0:
            corpus[k]=set(corpus.keys())    
        
        for k2, v in corpus.items():
            #print(k,"\t",k2,"\t",v)
            if k in v:
                #print("IN")
                linkedic[k].add(k2)
    
    PAGE=list(iterdic.keys())[3]
    prev0=sum(list(iterdic.values()))
    diff=1
    while diff>0.0001:
        for page in corpus.keys():
            iterdic[page]=round(rdf/n+df*sum([iterdic[p]/len(corpus[p]) for p in linkedic[page]]),4)
            diff=abs(prev0-sum(list(iterdic.values())))
            #print(diff)
            prev0=sum(list(iterdic.values()))
                 
  
      
    
    
    
    return iterdic


if __name__ == "__main__":
    main()
