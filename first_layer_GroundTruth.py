import pandas as pd

new_df = pd.DataFrame(columns = ["sheet", "category"])

def read_sheet(num):
    path_ = 'C:/Users/sumed/Desktop/Spring20/data/ML_Data_Training.xlsx'
    df = pd.read_excel(path_ , sheet_name= num)
    return df
w, h = 4,4
p_div = 300/h
v_div = 67.5/w
Matrix = [[0 for x in range(w)] for y in range(h)] 
count = 0
for i in range(w):
    for j in range(h):
        Matrix[i][j] = count
        count+=1
        # print(Matrix[i][j])


for i in range(0,512):
    df = read_sheet(i)
    maxP = df.Power.max()
    print('maxP: ',maxP)
    valV = df.loc[df['Power'] == maxP, 'Voltage'].iloc[0]
    print('valV: ',valV)
   
    cat2 = int(maxP/p_div)
    cat1 = int(valV/v_div)
    print(cat1, cat2)
    if cat2 > h-1:
        cat2 = h-1
    if cat1>w-1:
        cat1 = w-1
    category = Matrix[cat2][cat1]
    print('category: ', category)
   
    new_df = new_df.append({'sheet': i, 'category': category },  ignore_index=True)

new_df.to_excel("C:/Users/sumed/Desktop/Spring20/Feb27/March22/data/GT_PV16_Train_____.xlsx")
