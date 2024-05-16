import os,json
from re import findall as reg

def sct(so):
  acc_sid = so.replace("/.env","").replace("www.","").replace("mail.","").replace("webmail.","").replace("ns.","").replace("http://", "").replace("https://", "")
  files = open('coi.txt', 'a')
  files.write(str(acc_sid)+'\n')
  files.close()
def scg(so):
  keyid = so[1]
  secret = so[2]
  buid = str(keyid)+'|'+str(secret)
  remoer = str(buid).replace('\n', '')
  files = open('ws.txt', 'a')
  files.write(remoer+'\n')
  files.close()
  
def scgt(so):
  keyid = so[1]
  secret = so[2]
  keyid2 = so[3]
  secret2 = so[4]
  buid = str(keyid2)+'|'+str(secret2)
  remoer = str(buid).replace('\n', '')
  files = open('ws.txt', 'a')
  files.write(remoer+'\n')
  files.close()

nam = raw_input('List Ips: ')
with open(nam) as f:
    for site in f:
     #try:
        if 'AKIA' in site:
         so = site.split("|")
         scg(so)
        elif 'smtp' in site:
         so = site.split("|")
         scgt(so)
        else:
         sct(site)
         #sct(site)
     #except:
            #pass