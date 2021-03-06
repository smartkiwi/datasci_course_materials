register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by object column
objects = group ntriples by (object) PARALLEL 50;

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_object = foreach objects generate flatten($0), COUNT($1) as count PARALLEL 50;

--order the resulting tuples by their count in descending order
count_by_object_ordered = order count_by_object by (count)  PARALLEL 50;

-- store the results in the folder /user/hadoop/example-results
store count_by_object_ordered into '/user/hadoop/example-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';


getting results to master node:
hadoop fs -getmerge  /user/hadoop/example-results example-results
hadoop@ip-10-253-20-14:~$ tail example-results
"0528570000096"^^<http://www.w3.org/2001/XMLSchema#string>      1
"7376810000046"^^<http://www.w3.org/2001/XMLSchema#string>      1
"0492980000024"^^<http://www.w3.org/2001/XMLSchema#string>      1
"7809660000084"^^<http://www.w3.org/2001/XMLSchema#string>      1
"0708684351226"^^<http://www.w3.org/2001/XMLSchema#string>      1
"0120490000028"^^<http://www.w3.org/2001/XMLSchema#string>      1
"7863280000060"^^<http://www.w3.org/2001/XMLSchema#string>      1
"0752110000028"^^<http://www.w3.org/2001/XMLSchema#string>      1
<http://purl.org/goodrelations/v1#BusinessEntity>       333
<http://openean.kaufkauf.net/id/businessentities/>      334


Data types:
grunt> describe ntriples
ntriples: {subject: chararray,predicate: chararray,object: chararray}
grunt> describe objects
objects: {group: chararray,ntriples: {(subject: chararray,predicate: chararray,object: chararray)}}
grunt> describe count_by_object
count_by_object: {group: chararray,count: long}
grunt> describe count_by_object_ordered
count_by_object_ordered: {group: chararray,count: long}
