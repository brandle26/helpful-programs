import pygsheets
import pandas as pd
import datetime
from pathlib import Path


#=================================================
#This section will deal with cleaning the  data using pandas library#
df1=pd.read_csv("Expiration Pull Out.csv")

df1.drop(columns=["Unnamed: 0","Location ID","Location Name","Product ID","Is Pull from Shelf Day? (Yes / No)"],inplace=True,axis=1)

df1["Position ID"] = df1["Position ID"].str.replace(r"\([^()]*\)", " ", regex=True)

#create a datetime format on expiration date column
df1["Expiration Date"] =pd.to_datetime(df1["Expiration Date"]).dt.date

#getting a list of recommended pullout dates form the pull form shelf days column
recom_dates=df1["Pull From Shelf Days"]

#getting the Series  or list of expiry date
exp_dates = df1["Expiration Date"]

#create an empty list which will be populated by reommended pull out date calculateed
recom_pulldates=list()

#loop to update the list of recommened pull out dates
for i in range(0,len(recom_dates)):
    recom_days=datetime.timedelta(int(recom_dates[i]))
    recom_pulldate=exp_dates[i]-recom_days
    recom_pulldates.append(recom_pulldate)

df1["Recommended Pull Out Date"]=recom_pulldates

#sort data 
df1.sort_values(by="Position ID",inplace=True)

#=========================================================
#this section wioll get today's date
today=datetime.date.today()
today=today.strftime("%d/%m/%Y")

#=========================================================
#This section will update the google sheet 
gc=pygsheets.authorize(service_account_file="Secrets.json")
gsheet=gc.open("pull_out_report_slack")
gsheet.add_worksheet(today)  #create a new worksheet on the current worksheet
cws=gsheet.worksheet("title", today)
cws.clear()
cws.set_dataframe(df1,(1,1))

#==============================================================
#Code to remove the expiration pull csv file
path_to_file=Path("Expiration Pull Out.csv")
path_to_file.unlink()



















