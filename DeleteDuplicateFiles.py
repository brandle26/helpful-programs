#!/usr/bin/env python
# coding: utf-8




import os



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
        
    


def main():
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
   





main()
input("Press any buttion to exit")







