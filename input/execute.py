#!/usr/bin/env python
import sys
import time
import os
#sys.path.append(os.path.abspath("../clustering"))
import processData as clustering
# Execution of the project happens from this function.
# All the classes or methods will be invoked from here.
def main():    
    #i=1     
    #for i in range(4,31):
    #    if i<10:
    #        file_name = 'flows-2017-01-0'+str(i)+'.csv'
    #    else:
    #        file_name = 'flows-2017-01-'+str(i)+'.csv'
        dirs = os.listdir("../output")
        for file_name in dirs:
            if file_name == 'aggregated-features-flows-2017-01-01.csv':
                continue            
            start_time = time.time()
            #clustering.flows_to_features(file_name)
            #clustering.csv_to_database('features-'+file_name)
            #clustering.features_to_aggregated_features('features-'+file_name)
            clustering.cluster(file_name)
            #print("--- %s execution time for all methods on a single days data in seconds ---" % (time.time() - start_time))
         
if __name__ == "__main__":
    main()