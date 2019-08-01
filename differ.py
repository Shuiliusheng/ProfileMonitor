import os
from bs4 import BeautifulSoup
import difflib
#from lxml.html.diff import htmldiff, html_annotate
import parser

def find_file_pairs():
    file_pairs = []
    for root, dirs, files in os.walk("./"):
        old_files = []
        for f in files:
            if f.endswith(".old"):
                old_files.append(f)
        for old_file in old_files:
            file_pair = {}
            for f in files:
                if old_file[0:-4] == f:
                    file_pair["old_version"] = old_file
                    file_pair["new_version"] = f
                    file_pairs.append(file_pair)
    return file_pairs



def state_update(file_pairs):
    for file_pair in file_pairs:
        os.remove(file_pair["old_version"])
    for files in os.listdir("./"):
        if files.endswith(".html"):
            os.rename(files,files + ".old")



def diff_html(data1 ,data2, url):
    data1_lines = data1.splitlines()
    data2_lines = data2.splitlines()
    d = difflib.HtmlDiff()
    q = d.make_file(data1_lines,data2_lines,url + "' old version data","new version data",True)
    return q



def main():
    os.chdir("/home/ztx/follower/TargetArearHtml")

    total_diff = ""

    file_pairs = find_file_pairs()
    for file_pair in file_pairs:
        try:
            old_f = open(file_pair["old_version"])
            new_f = open(str(file_pair["new_version"]))
            url = old_f.readline()
            url = new_f.readline()
            data1 = old_f.read()
            data2 = new_f.read()
        except:
            print("read file process error!")
        finally:
            old_f.close()
            new_f.close()
        data1 = parser.delete_html_tag(data1)
        data2 = parser.delete_html_tag(data2)
        diff_html_data = diff_html(data1,data2,url)
        if "No Differences Found" not in diff_html_data:
            total_diff += diff_html_data

        #try:
            #diff_f = open(file_pair["new_version"][0:-4] + "diff.html",'w')
            #diff_f.write(diff_html_data)
        #except:
            #print("write file error!")
        #finally:
            #diff_f.close()

    if(total_diff):
        soup = BeautifulSoup(total_diff,"html.parser")
        tags = soup.find_all('table',class_="diff")
        for tag in tags:
            if not tag.has_attr("summary"):
                tag["width"] = '100%'
        total_diff = str(soup)
    else:
        total_diff = "<h1>No changes</h1>"
    try:
        total_diff_f = open("/home/ztx/follower/TargetArearHtml/.diff/TotalDiff.html",'w')
        total_diff_f.write(total_diff)
    except:
        print("write file error!")
    finally:
        total_diff_f.close()
 
    state_update(file_pairs)
    os.chdir("../")


if __name__ == '__main__':
    main()
