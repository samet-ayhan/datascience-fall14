import csv
import collections
import itertools
from collections import defaultdict

def preProcess(filename1, filename2):
    f = open(filename2,"w")
    fw = csv.writer(f)
    fw.writerow(("True ID","id"))

    rfilename = filename1
    counter = 0

    with open(rfilename, 'r') as handle:
        reader = csv.DictReader(handle, ['idAmazon', 'idGoogleBase'])
        data = defaultdict(list)
        key = ''
        firstline = True
        for line in reader:
     	    if firstline:
	        firstline = False
	        continue
	    if (key != line['idAmazon']):
	        counter += 1
	        key = line['idAmazon']
	        data[counter].append(line['idAmazon'])
	    data[counter].append(line['idGoogleBase'])
	    
    for k,v in data.iteritems():    
        for m in v:
	    fw.writerow((k, m))      
   
    f.close()

def evaluateDuplicates(found_dupes, true_dupes):
    true_positives = found_dupes.intersection(true_dupes)
    false_positives = found_dupes.difference(true_dupes)
    uncovered_dupes = true_dupes.difference(found_dupes)

    print 'found duplicate'
    print len(found_dupes)

    print 'precision'
    print 1 - len(false_positives) / float(len(found_dupes))

    print 'recall'
    print len(true_positives) / float(len(true_dupes))


def dupePairs(filename, rowname) :
    dupe_d = collections.defaultdict(list)

    with open(filename) as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"')
        for row in reader:
            dupe_d[row[rowname]].append(row['id'])

    if 'x' in dupe_d :
        del dupe_d['x']

    dupe_s = set([])
    for (unique_id, cluster) in dupe_d.iteritems():
        if len(cluster) > 1:
            for pair in itertools.combinations(cluster, 2):
                dupe_s.add(frozenset(pair))

    return dupe_s

pre_manual_clusters = 'product_mapping.csv'
manual_clusters = 'post_product_mapping.csv'
dedupe_clusters = 'products_out.csv'

preProcess(pre_manual_clusters, manual_clusters)

true_dupes = dupePairs(manual_clusters, 'True ID')
test_dupes = dupePairs(dedupe_clusters, 'Cluster ID')

evaluateDuplicates(test_dupes, true_dupes)
