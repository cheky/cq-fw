import os,json,mimetypes
#init current dir
conf_path=os.getcwd()
# Opening JSON file
conf_json=open(conf_path+"/config.json")
#returns JSON object as a dictionary
conf=json.load(conf_json)
#init path
curr_path=conf["dir"]
# Opening JSON file
json_file=open("log/lock_files.json")
#returns JSON object as a dictionary
datas=json.load(json_file)
#init lose files
lose_files=""
count_lose_files=0
#init new files
new_files=""
count_new_files=0
#init modified files
modif_files=""
count_modif_files=0
#Iterating through the json list
for data in datas:
    #if file not exist
    if os.path.isfile(data["fullpath"])==False:
        lose_files+=data["fullpath"]+"\r"
        count_lose_files=count_lose_files+1
        print("("+str(count_lose_files)+" file hilang) : "+data['fullpath'])
# Closing file
json_file.close()
#create and write info lose files
write_lose = open("log/lose_files.log", "w")
write_lose.write(lose_files)
write_lose.close()
#rescan all files
for root,dirs,files in os.walk(curr_path):
    if len(files)>0:
        for file in files:
            disallow=False
            for not_allowed in conf["disallow_dir_scan"]:
                if not_allowed==root[0:len(not_allowed)]:
                    disallow=True
            if disallow==False:
                fullpath=root+"/"+file
                full_prop_new_file=str(os.path.getctime(fullpath))+str(os.path.getmtime(fullpath))+str(mimetypes.guess_type(fullpath)[0])
                file_exist=False
                file_not_modif=True
                #Iterating through the json list
                for data in datas:
                    if data["fullpath"]==fullpath:
                        file_exist=True
                        full_prop_lock_file=str(data["created"])+str(data["modified"])+str(data["mime_type"])
                        if full_prop_new_file==full_prop_lock_file:
                            file_not_modif=True
                        else:
                            file_not_modif=False
                #if new file not exist in lock files
                if file_exist==False:
                    new_files+=fullpath+"\r"
                    count_new_files=count_new_files+1
                    print("("+str(count_new_files)+" file baru) : "+fullpath)
                #if new file not modified in lock files
                if file_not_modif==False:
                    modif_files+=fullpath+"\r"
                    count_modif_files=count_modif_files+1
                    print("("+str(count_modif_files)+" file dimodifikasi) : "+fullpath)
#create and write info new files
write_new = open("log/new_files.log", "w")
write_new.write(new_files)
write_new.close()
#create and write info modified files
write_modif = open("log/modified_files.log", "w")
write_modif.write(modif_files)
write_modif.close()
#print all scanned
print("Total file hilang : "+str(count_lose_files)+", Total file baru : "+str(count_new_files)+", Total file dimodifikasi : "+str(count_modif_files))
print("Lihat log pada folder log")
