import csv
import itertools
import sys
import numpy
import copy 

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])
    #print(people)
    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):


        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print("{}:".format(person))
        for field in probabilities[person]:
            print("  {}:".format(field.capitalize()))
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                #print("    {}: {p:.4f}".format(value,p))
                print("    {}: {}".format(value,p))


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    
    children=dict()
    jointprob=1
    for p1 in one_gene:#,two_genes):
        #print(p1,"\t",p2)
        if (people[p1]['father'] == None) and (people[p1]['mother'] == None):
            
            
            jointprob*=PROBS['gene'][1]*PROBS['trait'][1][p1 in have_trait]
    for p2 in two_genes:#,two_genes):
            
        if (people[p2]['father'] == None) and (people[p2]['mother'] == None):
            
                
            
            jointprob*=PROBS['gene'][2]*PROBS['trait'][2][p2 in have_trait]
            
            
    for person in people.keys():
        if (person not in one_gene) and (person not in two_genes) and (people[person]['father'] == None):
           jointprob*= PROBS['gene'][0]*PROBS['trait'][0][person in have_trait]  
    
    
    
    
    #generate child probabilities for 0, 1, and 2 genes
    #m is mother genes (as array of max length = 2), and f is father genes; mx is the mutation probability (0.01)
    def probs(m,f,d={0: 0.0, 1: 0.0, 2: 0.0},mx=0.01):
        #print("m: ",m," f: ",f)
        dic=copy.deepcopy(d)
        pf=1/len(f); pm=1/len(m)
        for i in f:
        
            for p1 in [0,1]:
                if p1 == i:
                    mf=1-mx
                else:
                    mf=mx
                for j in m:
                    
                    for p2 in [0,1]:
                        if p2 == j:
                            mm=1-mx
                        else:
                            mm=mx
                        res=p1+p2
                        dic[res]+=pf*pm*mf*mm
        return dic
    
    lst=[]
   
    #st=set((list(one_gene)[0],list(two_genes)[0]))
    for person in people.keys():
        if people[person]['father'] != None:
            if people[person]['father']  in one_gene:
                f=[0,1]
            elif people[person]['father'] in two_genes:
                f=[1]
            else:
                f=[0]
            if people[person]['mother']  in one_gene:
                m=[0,1]
            elif people[person]['mother']  in two_genes:
                m=[1]
            else:
                m=[0]
#            if person in have_trait:
#                trait=True
#            else:
#                trait=False
            probs_list=probs(m,f)
            if person in one_gene:
                children[person]=PROBS['trait'][1][person in have_trait]
                lst.append(probs_list[1])
            elif person in two_genes:
                children[person]=PROBS['trait'][2][person in have_trait]
                lst.append(probs_list[2])
            elif (person not in one_gene) and (person not in two_genes): #set((list(one_gene)[0],list(two_genes)[0])):
                children[person]=PROBS['trait'][0][person in have_trait]
                lst.append(probs_list[0])
                
            #probs(m,f)

    #final product
    #print("CHILDREN: ",children,"   LIST: ",lst, "JOINTPROB: ",jointprob)
    res=numpy.prod(lst)*numpy.prod(list(children.values()))*jointprob
    
    return res


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    #print("ONE GENE: {}, TWO GENES: {}, HAVE TRAIT: {}, P: {}".format(one_gene,two_genes,have_trait,p))
    for person in probabilities.keys():
        if person in one_gene:
            probabilities[person]['gene'][1]+=p
        elif person in two_genes:
            probabilities[person]['gene'][2]+=p
        elif person not in two_genes and person not in one_gene:
            probabilities[person]['gene'][0]+=p
        #if person in have_trait:
        probabilities[person]['trait'][person in have_trait]+=p
        #else:
         #   probabilities[person]['trait'][False]+=p
    
    
    


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    
    for person in probabilities.keys():
        genesum=sum(probabilities[person]['gene'].values())

        traitsum=sum(probabilities[person]['trait'].values())
        for i in range(2):
            if traitsum>0:
                probabilities[person]['trait'][i]=probabilities[person]['trait'][i]/traitsum

        for i in range(3):    
            if genesum>0:
                    
                probabilities[person]['gene'][i]=probabilities[person]['gene'][i]/genesum
        
    
    


if __name__ == "__main__":
    main()


