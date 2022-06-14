# importing necessary libraries
import pandas as pd
import datetime

# read a csvfile into dataframe
df1 = pd.read_csv("Expiration Pull Out.csv")

# dropping unnecessary columns form the dataframe
df1.drop(columns=["Unnamed: 0", "Location ID", "Location Name", "Product ID", "Is Pull from Shelf Day? (Yes / No)"],
         axis=1, inplace=True)

# clean up position id column
df1["Position ID"] = df1["Position ID"].str.replace(r"\([^()]*\)", " ", regex=True)


# convert expiration date to datetime format
df1["Expiration Date"] = pd.to_datetime(df1["Expiration Date"]).dt.date


# # 30 days for baby products, 1 day for ready to eat, two days for baker, eggs, dairy , fruit and Veg
# # 7 days for rest of the category
#create a list of category to specify  number of days prior to expiry date to calculate pullout date
one_day_pull = pd.array(["Ready to Eat", "Fruit & Veg"])
month_pull = pd.array(["Baby"])
two_day_pull = pd.array(["Fruit & Veg", "Eggs & Dairy", "Bakery", "Meat & Fish"])

# you can get series with boolean values using comparision operator
# bakery_check = df1["Category"] == "Bakery"
# df1[bakery_check]

# grabbing category  snd  expiration date series
cats = df1["Category"]
exp_dates = df1["Expiration Date"]

# create a conditional statement to calculate expiry date based on product category
def pulldate(cats, exp_dates):
    pull_dates = []
    one_day = datetime.timedelta(1)
    two_day = datetime.timedelta(2)
    month_day = datetime.timedelta(30)
    seven_day = datetime.timedelta(7)
    for i in range(0, len(cats)):
        if cats[i] in one_day_pull:
            days = exp_dates[i] - one_day
            pull_dates.append(days)
        elif cats[i] in two_day_pull:
            days = exp_dates[i] - two_day
            pull_dates.append(days)
        elif cats[i] in month_pull:
            days = exp_dates[i] - month_day
            pull_dates.append(days)
        else:
            days = exp_dates[i] - seven_day
            pull_dates.append(days)

    return pull_dates


pullOut_dates = pd.Series(pulldate(cats, exp_dates))
pullOut_dates = pullOut_dates

df1["Pull Out Date"] = pullOut_dates

today_date = pd.to_datetime("today").date()

filt = df1["Pull Out Date"] <= today_date
# filt.value_counts()

df2 = df1[filt]

df2 = df2[~(df2["Category"] == "Fruit & Veg")]

df3=df1.drop("Pull Out Date",axis=1)
recom_dates=df1["Pull From Shelf Days"]
recom_pulldates=list()
for i in range(0,len(recom_dates)):
    recom_days=datetime.timedelta(int(recom_dates[i]))
    recom_pulldate=exp_dates[i]-recom_days
    recom_pulldates.append(recom_pulldate)

df3["Recommended Pull Out Date"]=recom_pulldates

df2.to_csv("Expiration_Pull_Out_clean2.csv",index=False)
df1.to_csv("Expiration_Pull_Out_clean1.csv",index=False)
df3.to_csv("Expiration_Pull_Out_clean3_recommendeddate.csv",index=False)
print("Three csv file has been created")
input("Press Enter to exit")
