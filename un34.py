import os

nam = input('List Ips  :')
with open(nam) as f:
    for site in f:
     #try:
         if "AC5d841e2f443021550afc983905762975" not in site:
          files = open('twclean.txt', 'a')
          files.write(site+'\n')
          files.close()
         else:
          files = open('bad.txt', 'a')
          files.write(site+'\n')
          files.close()
     #except:
            #pass
            
            
            
