
from multiprocessing import Pool
import sys
import time
from collections import defaultdict
import re

word_pattern = '[a-z]+'


def count_words(words):
    words_dict = defaultdict(int)
    for word in words:
        words_dict[word.lower()] += 1
    
    print(len(words_dict))
    return words_dict

def combine_text(word_lists):
    for word_list in word_lists:
        for word in word_list:
            yield word

def proccess_files(*args):
    pool=Pool()
    return pool.imap_unordered(process_file, args)
   
def process_file(name):
    #words = []
    with open(name, 'r' ,encoding="utf8") as f:
        words = re.findall(word_pattern,f.read(), flags=re.IGNORECASE)
            
    return words

def write_file(words_dict):
    
    with open('result.txt','w') as f:
        for k, v in sorted(words_dict.items()):
            for i in range(v):
                f.write(k+', ')
            
    
    

if __name__ == '__main__':
    #start=time.time()
    
    word_lists = proccess_files('file1.txt','file2.txt','file3.txt')
    
    words = combine_text(word_lists)
    words_dict = count_words(words)
    write_file(words_dict)
    maximum  = max(words_dict, key=words_dict.get)
    print(maximum, words_dict[maximum])
   
  
    #os.path.walk('input/', process_files, None)
    #print ("process_files_parallel()", time.time()-start)


 