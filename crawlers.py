from bs4 import BeautifulSoup
import urllib.request

def crawler_all(url):
    req = urllib.request.Request(url)
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



def crawler_keys(url,keys):
    req = urllib.request.Request(url)
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
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    data = page.read()
    soup = BeautifulSoup(data,"html.parser")

    title = ''.join(list(filter(str.isalnum,soup.title.string)))
    target = ""
    for my_id in ids:
        target += str(soup.find_all(id = my_id))
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
