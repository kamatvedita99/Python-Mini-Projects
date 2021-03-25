import sys
import subprocess
import requests
import webbrowser
import os 
cwd = os.getcwd()
def extracterror(cmd):
    
    # args = cmd.split(' ')
    for name in os.listdir(cwd):
        print(name)
        if name =='hello.c':
            print("found!")

    # print(cmd)
    # s = subprocess.run("gcc hello.c -o out1;./out1") 
    # print(", return code", s) 
    subprocess.call(["gcc", "hello.c"]) # OR gcc for c program
    subprocess.call("./a.exe")
    # print("printing result")
    # print(tmp)
    # theproc = subprocess.Popen(["gcc", cmd],stdout=subprocess.PIPE,stderr = subprocess.PIPE)
    # out = theproc.stderr.read().decode("utf-8") 
    # out.rstrip('\n')
    # print(type(out))
    # if(out ==""):
    #     print("No errors found!")
    # else:
    #     stroutput = (out.splitlines()[-1])
    #     print(stroutput)
        # sendreq(stroutput)
        
        
def getlinks(rjson):     
    url_list = []
    countlinks=0
        
    for i in rjson["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
        countlinks+=1
        if(countlinks==5 or countlinks==len(rjson["items"])):
            break
        
    for i in url_list:
        webbrowser.open(i)

def sendreq(stroutput):
    errortype,errormsg = stroutput.split('Error:')
    respoutput = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(stroutput))
    restype = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errortype))
    respmsg = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errormsg))
    getlinks(respoutput.json())
    getlinks(restype.json())
    getlinks(respmsg.json())

if __name__ == "__main__":
    extracterror("error.cpp")



