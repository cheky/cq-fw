import os,mimetypes,json

#init current dir
conf_path=os.getcwd()
# Opening JSON file
conf_json=open(conf_path+"\config.json")
#returns JSON object as a dictionary
conf=json.load(conf_json)
#init path
curr_path=conf["dir"]
all_files=[]
for root,dirs,files in os.walk(curr_path):
    if len(files)>0:
        for file in files:
            if root not in conf["disallow_dir_scan"]:
                fullpath=root+"\\"+file
                all_files.append({
                    "fullpath":fullpath,
                    "created":os.path.getctime(fullpath),
                    "modified":os.path.getmtime(fullpath),
                    "mime_type":mimetypes.guess_type(fullpath)[0],
                    "size":os.path.getsize(fullpath)
                })
with open("log/lock_files.json", "w") as outfile:
    json.dump(all_files, outfile)

conf_json.close()
#print all scanned
print("Total file terkunci : "+str(len(all_files)))
print("Lihat log pada folder log")