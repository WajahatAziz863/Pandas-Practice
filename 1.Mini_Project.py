import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'John', 'Ahmed', 'Zara', 'Usman', 'Hina'],
    'City': ['Lahore', 'Karachi', 'Lahore', 'Multan', 'Karachi', 'Lahore', 'Multan'],
    'Subject': ['Math', 'Math', 'English', 'Math', 'English', 'English', 'Math'],
    'Marks': [80, 90, None, 70, 95, None, 60]
}

df = pd.DataFrame(data)
#Step1 Data Cleaning
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df)
#Step2 Basic Analysis
marks_analysis=(df['Marks'].agg(['mean','max','min']))
print(marks_analysis)
#Step3 City Analysis
Avg_Marks=(df.groupby('City')['Marks'].mean().sort_values(ascending=False))
print(Avg_Marks)
#Step4 Subject Analysis
subject_stats=(df.groupby('Subject')['Marks'].agg(['mean','max']))
print(subject_stats)
#Step5 Smart Filtering
print(df[(df['Marks']>75)&(df['City'].isin(['Lahore','Karachi']))])