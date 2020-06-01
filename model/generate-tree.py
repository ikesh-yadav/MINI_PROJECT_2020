
import pandas as pd
import numpy as np

#data file is stored in the same folder as the this file
fh=open("../data/SampleData.csv","r")


df=pd.read_csv(fh,sep=",")
fh.close()
df.drop(["group_name"], axis = 1, inplace = True) #droppin column
df.drop(["semester"], axis = 1, inplace = True) #droppin column
#df.drop(["How often do you go out with your friends"], axis = 1, inplace = True) #droppin column #removed directly in the data
df.dropna()  #dropping rows which contain missing values
df.columns=[ 'gender', 'friends_time', 'faculty_time', 'attendance', 'attentiveness', 'co_extra_curricular', 'study_time', 'social_time', 'previous_score', 'extra_courses', 'health', 'sleep_time','library_time', 'Decision'] #renaming the column values
#gender={'Male':1,'Female':2,'Other':3}
#df.Gender=[gender[item] for item in df.Gender]  #changing gender values to numerical form
#fr={'High':1,'Moderate':2,'Low':3}
#df.Friend_time=[fr[item] for item in df.Friend_time] #time with friend
#fv={'High':1,'Moderate':2,'Low':3}
#df.Faculty_visit=[fv[item] for item in df.Faculty_visit]  #faculty visit
#atte={'85 to 75':2,'<75':3,'>85':1}
#df.avg_attendance=[atte[item] for item in df.avg_attendance]  #average attendence
#pc={'High':1,'Moderate':2,'Low':3}
#df.participation_corricular=[pc[item] for item in df.participation_corricular]  #participation in co-curricular activities
#att={'Very attentive':1,'Average':2,'Less attentive':3}
#df.attentive_class=[att[item] for item in df.attentive_class]  #attention in class
#st={'>4 hours':1,'1 to 4 hours':2,'<1 hour':3}
#df.study_time=[st[item] for item in df.study_time]   #study time
#smt={'>4 hours':1,'1 to 4 hours':2,'<1 hour':3}
#df.social_time=[smt[item] for item in df.social_time]   #social media time
#pm={'>9 GPA':1,'>7 but <9 GPA':2,'>5 but <7 GPA':3,'<5 GPA':4}
#df.cgpa=[pm[item] for item in df.cgpa]    #cgpa
#ex={'Often':1,'Sometimes':2,'Never':3}
#df.extra_crse=[ex[item] for item in df.extra_crse]  #extra courses
#sp={'>8':1,'6 to 8':2,'<6':3}
#df.sleep=[sp[item] for item in df.sleep]  #sleep 
#lt={'>4 hours':1,'1 to 4 hours':2,'<1 hour':3}  
#df.lib_time=[lt[item] for item in df.lib_time]  #time in library



print(df.head(6))
print(df.shape)

from chefboost import Chefboost as chef

config = {'algorithm': 'C4.5'}
model = chef.fit(df, config)
