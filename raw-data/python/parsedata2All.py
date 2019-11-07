# -*- coding: UTF-8 -*-
import os
import sys
import json
import datetime

# 帮助那些不会自己将原始txt转化为jsonArray的组
# usage: python3 parsedata2All.py path_to_txt_dir

def main():
    PATH = sys.argv[1]
    addr_list = os.listdir(PATH)
    
    last_dir = PATH.split('/')[-1] 
    if last_dir == "":
        last_dir = PATH.split('/')[-2]

    paper_list = []
    for addr in addr_list:
        if(addr[0] == '.'):
            print("skip:" + PATH + addr)
            continue

        paper = {}
        author = []
        keywords = []
        references = []
        with open(PATH+addr, encoding='utf-8') as f:
            strs = f.readlines()

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
