from bs4 import BeautifulSoup
import urllib.request

header = {'User-Agent' : 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
def crawler_all(url):
    req = urllib.request.Request(url,headers = header)
    page = urllib.request.urlopen(req)
    data = page.read()
    soup = BeautifulSoup(data,"html.parser")

    title = ''.join(list(filter(str.isalnum,soup.title.string)))
    try:
        f = open("/home/ztx/follower/TargetArearHtml/"+ title + "TargetArea.html","w")
        f.write(url + "\n" + str(soup.body))
    except:
        print("process " + title + "TargetArea.html error!")
    finally:
        f.close()



# not strong, simply find *2 upper level* block that contain the key
def crawler_keys(url,keys):
    req = urllib.request.Request(url,headers = header)
    page = urllib.request.urlopen(req)
    data = page.read()
    soup = BeautifulSoup(data,"html.parser")

    title = ''.join(list(filter(str.isalnum,soup.title.string)))
    target = ""
    for key in keys:
        for aa in soup.find_all(text = key):
            for sibling in aa.parent.parent.next_siblings:
                target += str(sibling)
    try:
        f = open("/home/ztx/follower/TargetArearHtml/"+ title + "TargetArea.html","w")
        f.write(url + "\n" + target)
    except:
        print("process " + title + "TargetArea.html error!")
    finally:
        f.close()


def crawler_ids(url,ids):
    req = urllib.request.Request(url,headers = header)
    page = urllib.request.urlopen(req)
    data = page.read()
    soup = BeautifulSoup(data,"html.parser")

    title = ''.join(list(filter(str.isalnum,soup.title.string)))
    target = ""
    for my_id in ids:
        #target += str(soup.find_all(id = my_id))
        target += str(soup.select("#" + my_id))
    try:
        f = open("/home/ztx/follower/TargetArearHtml/"+ title + "TargetArea.html","w")
        f.write(url + "\n" + target)
    except:
        print("process " + title + "TargetArea.html error!")
    finally:
        f.close()
    

def crawler_classes(url,classes):
    req = urllib.request.Request(url,headers = header)
    page = urllib.request.urlopen(req)
    data = page.read()
    soup = BeautifulSoup(data,"html.parser")

    title = ''.join(list(filter(str.isalnum,soup.title.string)))
    target = ""
    for my_class in classes:
        target += str(soup.find_all(class_ = my_class))
    try:
        f = open("/home/ztx/follower/TargetArearHtml/"+ title + "TargetArea.html","w")
        f.write(url + "\n" + target)
    except:
        print("process " + title + "TargetArea.html error!")
    finally:
        f.close()
    
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("crawler_id: usage error!")
