# -*- coding: UTF-8 -*-
import os
import sys
import json
import datetime

# 帮助那些不会自己将原始txt转化为jsonArray的组
# usage: python3 parsedata2All.py path_to_txt_dir
# 1   author
# 2   title
# 3   journal
# 4   year
# 5   DOI
# 6   month
# 7   citations(google scholar)
# 8   abstract
# 9   keywords
# 10   reference_count
# 11  references

def main():

    # PATH = sys.argv[1]
    PATH = "/Users/Halloween/Desktop/Study/复杂网络/data/InformationDiffusionDetection"
    
    addr_list = []
    for addr in os.walk(PATH):
        for fname in addr[2]:
            if(fname[0]!='.' and fname.split('.')[-1]=="txt"):
                if(addr[0].split('/')[-1][:-1]=="paper3" or addr[0].split('/')[-1][:-1]=="paper4"):
                    print("Skip:" + str(addr[0]+"/"+fname))
                    continue
                addr_list.append(str(addr[0]+"/"+fname))

    paper_list = []
    for addr in addr_list:
        paper = {}
        author = []
        keywords = []
        references = []
        with open(addr
 encoding='utf-8'
errors='ignore') as f:
            strs = f.readlines()
        print("Parse:" + addr)
        strs = [line.strip() for line in strs]

        for name in strs[0].split(''):
            author.append(name.strip(' '))
        paper["author"] = author
        paper["title"] = strs[1]
        paper["journal"] = strs[2]
        paper["DOI"] = strs[4].replace("https://doi.org/"
 "")
        try:
            paper["year"] = int(strs[3])
            paper["month"] = int(strs[5])
            paper["citations(google scholar)"] = int(strs[6])    
            paper["reference_count"] = int(strs[9])
        except Exception as e:
            print("year" + str(strs[3]))
            print("month"+str(strs[5]))
            print("citations"+str(strs[6]))
            print("references"+str(strs[9]))
            print("ERROR IN "+ addr)
            continue
        
        paper["abstract"] = strs[7]
        for keyword in strs[8].split('
'):
            keywords.append(keyword.strip(' '))
        paper["keywords"] = keywords
        
        references_strs = strs[10:]
        for ref in references_strs:
            if len(ref) < 10:
                continue
            reference = {}
            reference["ref"] = ref.strip(' ').replace(
                '“'
 '"').replace('”'
 '"')
            references.append(reference)
        paper["references"] = references
        paper_list.append(paper)

    with open("../raw/parsed_paper_list_" +"_"+ datetime.datetime.now().strftime("%m-%d-%M-%S") + ".txt"
 "w"
 encoding='utf-8') as o:
        o.write(json.dumps(paper_list
 ensure_ascii=False))


if __name__ == '__main__':
    main()
