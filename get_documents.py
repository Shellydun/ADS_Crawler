# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:06:38 2021

@author: Lenovo
"""
import pandas as pd 
import wget 
import itertools

#making the Url column from crawl dataframe string type
def str_conversion(url_column):    
  
    #convert urls to type string
    url_str = []
    for i in url_column:
        str(i)
        url_str.append(i)
    
    return url_str

# subsetting target urls 
def cleandb(url_str, target_substr):
       
    #we add every url that contains the target characters to a new list
    target_urls = []
    for url in url_str:
        if url.__contains__(target_substr):
            target_urls.append(url)   
    return target_urls

# downloading the documents using wget
def download_docs(target_urls, directory):
                
    #we download everything in the cleaned list 
    for url in itertools.islice(target_urls , 10, 20): 
        try:
            wget.download(url=url, out=directory)
        
        except: 
            print("Failed to download:", url)

# final function to download the target documents from crawldb 
def get_docs(crawldb_dir, target_substr, out_dir):
    crawldb = pd.read_csv(crawldb_dir)
    url_str = str_conversion(url_column = crawldb['Url'])
    target_urls = cleandb(url_str, target_substr)
    download_docs(target_urls, out_dir)
    
# example usage of get_docs  
# specify firstly the directory of the Nutch Crawldb, the unique url component & output directory 
# get_docs(
#     crawldb_dir = "C:/cygwin64/apache-nutch-1.18-bin/apache-nutch-1.18/Backup/crawl_excelfile/crawldb_csv/part-r-00000",
#     target_substr = "epar-public-assessment-report",
#     out_dir = "C:/Users/Lenovo/Documents/Applied Data Science/Thesis/EPAR_PDFS"
#     )

    