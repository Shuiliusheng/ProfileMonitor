import crawlers

'''
type information:
    "IDS": find all html tags who's attribute id = ID, and save the areas, there can be more than 1 id. 
           such as "http://some.web.site.com IDS id1 id2 id3"
    "CLASSES": find all html tags who's attribute class = CLASS, and save the areas
           such as "http://some.web.site.com CLASSES class1 class2 class3"
    "KEYS": find the block that contain key word, then return 2 upper level contents
           such as "http://some.web.site.com KEYS key1 key2 key3"
     default:
'''

# 1. input: a file, which contain several lines config info
#           each line's format: url <type> <parameter1> <parameter2> ...
# 2. output: a list of dict, each dict contain "url", "type" and "parameters", 
#           "parameters" is a list.
# I didn't check the format, so if the format is wrong, there will be some error
def reader(file_name):
    result = []
    try:
        with open(file_name) as f:
            for line in f:
                web_item = {}
                line_content = line.split()
                if(len(line_content) >= 1):
                    web_item["url"] = line_content[0]
                if(len(line_content) >= 2):
                    web_item["type"] = line_content[1]
                parameters = []
                if(len(line_content) >= 3):
                    for i in line_content[2:]:
                        parameters.append(i)
                    web_item["parameters"] = parameters
                result.append(web_item)
    except:
        print("reader(): There is some error!")
    finally:
        f.close()
    return result


# 1. input: a dict, which must contain following keys: "url", "type" and "parameters"
# 2. process: according to the dict's "type" key to decide which crawler method to use
def judger(web_type_param):
    try:
        if web_type_param.get("type") == None :
            crawlers.crawler_all(web_type_param["url"])
        elif web_type_param.get("type") == "IDS" :
            crawlers.crawler_ids(web_type_param["url"],web_type_param["parameters"])
        elif web_type_param.get("type") == "CLASSES" :
            crawlers.crawler_classes(web_type_param["url"],web_type_param["parameters"])
        elif web_type_param.get("type") == "KEYS" :
            crawlers.crawler_keys(web_type_param["url"],web_type_param["parameters"])
        elif web_type_param.get("type") == "USELESS" :
            pass
    except:
        print(str(web_type_param.get("url")) + ":judger(): There is some error!")
        pass
        
def main():
    web_type_list = reader("/home/ztx/follower/MonitedSitesAndconfig.txt")
    for web_item in web_type_list:
       judger(web_item)

if __name__ == '__main__':
    main()
