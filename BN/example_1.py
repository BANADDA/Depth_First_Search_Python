#import pyAgrum
import pyAgrum as gum

# create a BN
bn=gum.fastBN("A->B[3]<-C{yes|No}->D")
# specify some CPTs (randomly filled by fastBN)
bn.cpt("A").fillWith([0.3,0.7])

# and then generate a database
gum.generateCSV(bn,"sample.csv",1000,with_labels=True,random_order=False) 
# which returns the LL(database)