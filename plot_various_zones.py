import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



path_ = 'C:/Users/sumed/Desktop/Spring20/Feb27/March22/output/6/15.xlsx'
df = pd.read_excel(path_ , sheet_name= 0)
# index_list = df.index.values
index_list = np.array(df['index'])


path_2 = 'C:/Users/sumed/Desktop/Spring20/Feb27/March22/output/6/11.xlsx'
df2 = pd.read_excel(path_2 , sheet_name= 0)
# index_list = df.index.values
index_list2 = np.array(df2['index'])

path_3 = 'C:/Users/sumed/Desktop/Spring20/Feb27/March22/output/6/10.xlsx'
df3 = pd.read_excel(path_3 , sheet_name= 0)
# index_list = df.index.values
index_list3 = np.array(df3['index'])

path_4 = 'C:/Users/sumed/Desktop/Spring20/Feb27/March22/output/6/7.xlsx'
df4 = pd.read_excel(path_4 , sheet_name= 0)
# index_list = df.index.values
index_list4 = np.array(df4['index'])

path_5 = 'C:/Users/sumed/Desktop/Spring20/Feb27/March22/output/6/6.xlsx'
df5 = pd.read_excel(path_5 , sheet_name= 0)
# index_list = df.index.values
index_list5 = np.array(df5['index'])

def read_sheet(num):
    path_ = 'C:/Users/sumed/Desktop/Spring20/data/ML_Data_Training.xlsx'
    df = pd.read_excel(path_ , sheet_name= num)
    return df

print(index_list)
print(" ")
print(index_list2)
for i in index_list:
    print(i)
    df = read_sheet(i)
    df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
    df = df.drop_duplicates('Voltage')
    a_ = df.Voltage.values
    b_ = df.Power.values
    plt.scatter(a_, b_, c = "green")
    # plt.plot(concatinated_x, concatinated_y, 'tab:green')
for i in index_list2:
    print(i)
    df = read_sheet(i)
    df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
    df = df.drop_duplicates('Voltage')
    a_ = df.Voltage.values
    b_ = df.Power.values
    plt.scatter(a_, b_, c= "blue")

for i in index_list3:
    print(i)
    df = read_sheet(i)
    df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
    df = df.drop_duplicates('Voltage')
    a_ = df.Voltage.values
    b_ = df.Power.values
    plt.scatter(a_, b_, c= "red")

for i in index_list4:
    print(i)
    df = read_sheet(i)
    df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
    df = df.drop_duplicates('Voltage')
    a_ = df.Voltage.values
    b_ = df.Power.values
    plt.scatter(a_, b_, c= "orange")

for i in index_list5:
    print(i)
    df = read_sheet(i)
    df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
    df = df.drop_duplicates('Voltage')
    a_ = df.Voltage.values
    b_ = df.Power.values
    plt.scatter(a_, b_, c= "pink")

# test_path = 'C:/Users/sumed/Desktop/Spring20/data/ML_Data_Test.xlsx'
# test_df = pd.read_excel(test_path , sheet_name= 0)
# test_df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
# test_df = test_df.drop_duplicates('Voltage')
# a_ = test_df.Voltage.values
# b_ = test_df.Power.values
# plt.scatter(a_, b_ , c = "black" )


# test_path = 'C:/Users/sumed/Desktop/Spring20/data/ML_Data_Test.xlsx'
# test_df = pd.read_excel(test_path , sheet_name= 4)
# test_df.sort_values("Voltage", axis=0, ascending=True, inplace=True)
# test_df = test_df.drop_duplicates('Voltage')
# a_ = test_df.Voltage.values
# b_ = test_df.Power.values
# plt.scatter(a_, b_ , c = "red" )


import matplotlib.patches as mpatches
g_patch = mpatches.Patch(color='green', label='Zone 15')
b_patch = mpatches.Patch(color='blue', label='Zone 11')
r_patch = mpatches.Patch(color='red', label='Zone 10')
o_patch = mpatches.Patch(color='orange', label='Zone 7')
p_patch = mpatches.Patch(color='pink', label='Zone 6')

plt.legend(handles=[g_patch, b_patch,r_patch, o_patch,p_patch ])

plt.show()