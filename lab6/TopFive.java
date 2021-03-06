package org.myorg;

import java.io.IOException;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;

import java.io.IOException;
import java.util.*;	
import java.util.Map;
import java.util.HashMap;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.apache.log4j.Logger;

	
	public class TopFive {
	private static final Logger LOG = Logger.getLogger(TopFive.class);

	public static class ValueComparator implements Comparator<String> {

	    java.util.Map<String, Integer> base;
	    public ValueComparator(java.util.Map<String, Integer> base) {
		this.base = base;
	    }

	    public int compare(String a, String b) {
		if (base.get(a) >= base.get(b)) {
		    return -1;
		} else {
		    return 1;
		} 
	    }
	}

        public static class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
            private Text newKey = new Text();
	    private Text val = new Text();

            public void map(LongWritable key, Text value, OutputCollector output, Reporter reporter) throws IOException {
                String line = value.toString();
		String[] parts = line.split(" ");
		String word1 = parts[0]; 
		String part2 = parts[1]; 
		String[] parties = part2.split("\t");
		String word2 = parties[0];
		String count = parties[1];
		newKey.set(word1);
	    	val.set(word2 + " " + count);
		output.collect(newKey, val);
            }
        }
	
	public static class Reduce extends MapReduceBase implements Reducer<Text, Text, Text, Text> {
	    private Text finalKey = new Text();
	    private Text sonuc = new Text();

	    public void reduce(Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {

		HashMap<String,Integer> map = new HashMap<String,Integer>();
        	ValueComparator bvc =  new ValueComparator(map);
        	TreeMap<String,Integer> sorted_map = new TreeMap<String,Integer>(bvc);

                while (values.hasNext()) {
		    String line = values.next().toString();
		    String[] parts = line.split(" ");
		    if (parts.length > 1)
		    {
			String word2 = parts[0];
		    	int count = Integer.parseInt(parts[1]);
		    	map.put(word2, count);
		    }
		}

		sorted_map.putAll(map);
	    	int i = 0;
		Iterator iter = sorted_map.entrySet().iterator(); 

    		while (iter.hasNext()) {
		    java.util.Map.Entry entry = (java.util.Map.Entry) iter.next();
		    if (i < 5)
		    {
		    	finalKey.set(key.toString() + " " + entry.getKey());
      		    	sonuc.set(entry.getValue().toString());
		    	output.collect(finalKey, sonuc);
			i++;
		    }
    		}
            }
        }


	   public static void main(String[] args) throws Exception {
	     JobConf conf = new JobConf(TopFive.class);
	     conf.setJobName("topfive");
	
	     conf.setMapOutputKeyClass(Text.class);
	     conf.setMapOutputValueClass(Text.class);
	     conf.setOutputKeyClass(Text.class);
	     conf.setOutputValueClass(Text.class);
	
	     conf.setMapperClass(Map.class);
	     //conf.setCombinerClass(Reduce.class);
	     conf.setReducerClass(Reduce.class);
	
	     conf.setInputFormat(TextInputFormat.class);
	     conf.setOutputFormat(TextOutputFormat.class);
	
	     FileInputFormat.setInputPaths(conf, new Path(args[0]));
	     FileOutputFormat.setOutputPath(conf, new Path(args[1]));
	
	     JobClient.runJob(conf);
	   }
    }
