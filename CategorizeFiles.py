#!/usr/bin/env python
# coding: utf-8



import os
import shutil



#list of common file extensions
image_ext=["jpeg","jpg","png","gif","tiff","bmp"]
mov_ext=["mp4","avi","flv","wmv","mov","avi","ts"]
doc_ext=["docx","pdf","txt","pptx","pub"]
data_ext=["xlsx","csv"]
python_program=["py"]


def get_files_list():
    """
    This function get list of all the files in the current directory
    """
    file_list=[]
    contents=os.listdir()
    for content in contents:
        if os.path.isfile(content):
            file_list.append(content)
        else:
            continue
    return file_list



def create_folder():
    """
    This function creates directories if they doe not exist
    """
    folder_names=["Movies","Images","Uncategorized","Documents","Raw Data","Python Program"]
    for folder in folder_names:
        if not os.path.exists(folder.casefold()):
            os.mkdir(folder)
        else:
            continue
    
def check_and_move(file_list):
    """
    This function checks the extension of the file and move it to 
    appropriate directory
    """ 
    for file in file_list:
        if file.split(".")[-1].casefold() in image_ext:
            shutil.move(file,"Images".casefold())

        elif file.split(".")[-1].casefold() in mov_ext:
            shutil.move(file,"Movies")

        elif file.split(".")[-1].casefold() in doc_ext:
            shutil.move(file,"Documents")
        
        elif file.split(".")[-1].casefold() in data_ext:
            shutil.move(file,"Raw Data")
        
        elif file.split(".")[-1].casefold() in python_program:
            shutil.move(file,"Python Program")
            
        else:
            shutil.move(file,"Uncategorized")


def FileManagement():
    file_list=get_files_list()
    create_folder()
    check_and_move(file_list)
    print("Task complete")
    



FileManagement()




input("Press any button to exit")






