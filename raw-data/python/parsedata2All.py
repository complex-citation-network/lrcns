# -*- coding: UTF-8 -*-
import os
import sys
import json
import datetime

# 帮助那些不会自己将原始txt转化为jsonArray的组
# usage: python3 parsedata2All.py path_to_txt_dir
# 0   author
# 1   title
# 2   journal
# 3   year
# 4   DOI
# 5   month
# 6   citations(google scholar)
# 7   abstract
# 8   keywords
# 9   reference_count
# 10  references

def main():

    # PATH = sys.argv[1]
    PATH = "/Users/Halloween/Desktop/Study/复杂网络/data/InformationDiffusionDetection"
    
    addr_list = []
    for addr in os.walk(PATH):
        for fname in addr[2]:
            if(fname[0]!='.' and fname.split('.')[-1]=="txt"):
                addr_list.append(str(addr[0]+"/"+fname))

    paper_list = []
    for addr in addr_list:
        paper = {}
        author = []
        keywords = []
        references = []
        with open(addr, encoding='utf-8') as f:
            strs = f.readlines()
        print(addr)
        strs = [line.strip() for line in strs]

        for name in strs[0].split(','):
            author.append(name.strip(' '))
        paper["author"] = author
        paper["title"] = strs[1]
        paper["journal"] = strs[2]
        paper["year"] = int(strs[3])
        paper["DOI"] = strs[4].replace("https://doi.org/", "")
        paper["month"] = int(strs[5])
        paper["citations(google scholar)"] = int(strs[6])
        paper["abstract"] = strs[7]
        for keyword in strs[8].split(','):
            keywords.append(keyword.strip(' '))
        paper["keywords"] = keywords
        paper["reference_count"] = int(strs[9])
        references_strs = strs[10:]
        for ref in references_strs:
            if len(ref) < 10:
                continue
            reference = {}
            reference["ref"] = ref.strip(' ').replace(
                '“', '"').replace('”', '"')
            references.append(reference)
        paper["references"] = references
        paper_list.append(paper)

    with open("../raw/parsed_paper_list_" + last_dir +"_"+ datetime.datetime.now().strftime("%m-%d-%M-%S") + ".txt", "w", encoding='utf-8') as o:
        o.write(json.dumps(paper_list))


if __name__ == '__main__':
    main()
