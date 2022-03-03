#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


#get the file name
filename=input("Enter the name of the excel workbook: ")

#create dataframe object
wb_obj=pd.ExcelFile(filename)

#get list of sheet_names
sheetnames=wb_obj.sheet_names
    
#get the name of the column to be filtered by
column_name=input("Enter the column name to be filtered by:")


# In[3]:


#create an excel workbook and sheets with differnt name
def same_workbook():
    output_filename=column_name+".xlsx"
    writer=pd.ExcelWriter(output_filename)
    for sheetname in sheetnames:
        df=wb_obj.parse(sheetname)
        if column_name in df.columns:
            unique_names=df[column_name].unique()
            for unique_name in unique_names:
                df_new=df[df[column_name]==unique_name]
                newsheet_name=unique_name+"_"+str(sheetnames.index(sheetname))
                df_new.to_excel(writer,newsheet_name,index=False)
            print("Task complete")
        else:
            print("The column name does not exist.")
            break
    writer.save()


# In[4]:


#create an different workbooks 
def different_workbook():
    for sheetname in sheetnames:
        df=wb_obj.parse(sheetname)
        if column_name in df.columns:
            unique_names=df[column_name].unique()
            for unique_name in unique_names:
                output_filename=unique_name+".xlsx"
                writer=pd.ExcelWriter(output_filename)
                df_new=df[df[column_name]==unique_name]
                newsheet_name=unique_name+"_"+str(sheetnames.index(sheetname))
                df_new.to_excel(writer,newsheet_name,index=False)
                writer.save()
            print("Task complete")
        else:
            print("The column name does not exist.")
            break


# In[5]:


while True:
       print("""
       Please enter the number that corresponds with the task you want to perform.
       1. Create one workbook.
       2. Create multiple workbook
       """)
       choice=input("Please enter the number here: ")
       try:
           choice=int(choice)
           if choice==1:
               same_workbook()
               break
           elif choice==2:
               different_workbook()
               break
           else:
               print("The choice you entered is not valid or the column name does not exist")
               continue
       except:
           print("You have entered a character and not a number or the column name does not exist")


# In[6]:


input("Press any button to exit")


# In[ ]:




