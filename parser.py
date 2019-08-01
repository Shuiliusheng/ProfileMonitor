import sys
import re


def delete_html_tag(data):
    result = ""
    reg = re.compile('<[^>]*>')
    for line in data.splitlines():
            line_p = reg.sub('',line).replace('\n','').replace(' ','')
            if(len(line_p) > 0):
                result += line_p
                result += "\n"
    return result



def main():
    data = ""
    if len(sys.argv) != 2:
        print("input error")
    try:
        f = open(sys.argv[1],"r")
        data = delete_html_tag(f.read())
    except:
        print("file process error!")
    finally:
        f.close()

    try:
        f = open(sys.argv[1],"w")
        f.write(data)
    except:
        print("file process error!")
    finally:
        f.close()

if __name__ == '__main__':
    main()
