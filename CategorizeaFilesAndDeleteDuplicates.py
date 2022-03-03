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
    This funciton gets the list of all the files in the current working directory
    """
    contents=list() #emtpy list to store the file names 
    for content in os.listdir():
        if os.path.isfile(content):
            contents.append(content)
        else:
            continue
    return contents
    




def get_duplicates(file_list):
    """
    This funciton goes though list of filesnames and check if it contains the string "copy" as it means the file has been copied
    """
    duplicate_names=[]
    for filename in file_list:
        if (filename[0:4].casefold() != "Copy".casefold()) and ("Copy".casefold() in filename.casefold())  :
            duplicate_names.append(filename)
        else:
            continue
    return duplicate_names




def remove_files(duplicate_list):
    """
    This function deletes all the files with filenames passed to it as a list
    """
    for file in duplicate_list:
        os.remove(file)
        
    


def delete_duplicates():
    print("The current working directory:")
    print(os.getcwd())
    print("=================================================================================================================")
    
    #get the list of all the files in the current working directory by calling the function i created
    contents=get_files_list()
    
    #get the list of all the filenames which has "Copy" on its string
    duplicates=get_duplicates(contents)
    
    #deleting allt he files passed as a string
    remove_files(duplicates)
    
    print("Task Completed")
   




#The section below creates function to move and sort files





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
    


delete_duplicates()

FileManagement()




input("Press any button to exit")






