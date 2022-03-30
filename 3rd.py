import pandas as pd
import statistics as st
df=pd.read_csv('height-weight.csv')
height=df['Height(Inches)'].tolist()
std=st.stdev(height)
mean=st.mean(height)
fsstd=mean-3*std
festd=mean+3*std
fstd=[]
for data in height:
    if(data>fsstd and data<festd):
        fstd.append(data)
fp=(len(fstd)/len(height))*100
print(fp)