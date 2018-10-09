import os
 
import shutil
file_path= os.path.expanduser('~')
 
 
file_name = file_path+'\\' +'rules.txt'

file_t = open(file_name,"r")
 
path=file_t.readline()
print (path)
mode = file_t.readline()
print (mode)
 
mode = mode.strip('\n')

print (mode)
 
path1 = path.strip('\n')

print (path)

dict1 = {}



def rules():
 
    
 
    for each in file_t:
 
        each = each.strip("\n")
 
    if each.split(":",1)[0] :
 
        file_ext,dest_path = each.split(":",1)
     
        file_ext = file_ext.strip()

            
        dest_path = dest_path.strip()
     
        dict1[file_ext]=dest_path
     
    return dict1

    print (dict1)

def file_move(files_list):

    for files in files_list :
     
        if "." in files:
         
            ext = files.rsplit(".",1)[1]
         
            ext= ext.strip()
     
            if ext in dict1:
     
                dst = dict1[ext]
 
try:
 
    print (files)
    print (dst)
 
    shutil.move(files, dst)
 
except Exception as e :
 
    print (e)

def single_dir(path1):
     
    os.chdir(path1)
     
    files = os.listdir(".")

    print (files)
    
    file_move(files)

def rec_dirs(path1):
 
    for root, dirs, files in os.walk(path1, topdown=True, onerror=None, followlinks=False):
 
#print files
 
        os.chdir(root)
     
        file_move(files)
     
        print ("files are moved")
     
        dict1 = rules()
 
if mode =="r":
 
    rec_dirs(path1)
 
else:
 
    single_dir(path1)
