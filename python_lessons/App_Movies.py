import numpy as n
import pandas as p
read_data = p.read_csv("AutoSurvey.csv")

def question1():    
    group = read_data.groupby(['Type','Purchased']).Mileage.mean()
    print(group)
    max_value= read_data.groupby(["Type"])["Vehicle_Age"].max() 
    min_value= read_data.groupby(["Type"])["Vehicle_Age"].min()
    calculate= max_value-min_value  
    print(calculate)

question1()