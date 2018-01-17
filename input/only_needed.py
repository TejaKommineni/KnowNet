import csv

def only_needed():    
    out = csv.writer(open("essential-flows-2017-12-05.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow('source_ip,destination_ip,source_port,destination_port,protocol,tcp_flags,duration,packets,bytes'+"\n")
    i =0
    with open('features-flows-2017-12-05.csv', 'rU') as f:
        reader = csv.reader(f)
        for rec in csv.reader(f, delimiter=','):
            print(i)
            i = i +1
            with open('clustered-aggregated-features-flows-2017-12-05.csv', 'rU') as f1:
                reader1 = csv.reader(f1)
                for rec1 in csv.reader(f1, delimiter=','):
                    temp = rec1[0] 
                    temp = temp[1:]
                    temp = temp[:len(temp)-1]
                    if temp== rec[0]:
                        out.writerow(rec)
                        print(rec)
                       
            f1.close()            
    f.close()
    out.close()
                 
only_needed()    