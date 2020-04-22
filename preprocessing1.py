import numpy as np
import pandas as pd
from pandas import ExcelWriter
xls_path ="discritize_033_TRAINING.xlsx"
# writer = pd.ExcelWriter('demo4.xlsx', engine='xlsxwriter')
x_line = np.linspace(0, 69, 208)
DF_list= list()

def read_sheet(num):
    path_ = 'C:/Users/sumed/Desktop/Spring20/data/ML_Data_Training.xlsx'
    df = pd.read_excel(path_ , sheet_name= num)
    return df
for sheet in range(512):
    df = read_sheet(sheet)
    new_df = pd.DataFrame(columns=['Voltage', 'Power'])

    for i in range(208):
        count = 0
        sum = 0
  
        # print("it is 0")
        range_before = float(x_line[i])
        range_after = float(x_line[i])+0.5
        for ind in df.index:
            val = df["Voltage"][ind]
            if( range_before<= val and val< range_after):
                if count == 0:
                    sum = df["Power"][ind]
                    count += 1
                else:
                    sum = sum + df["Power"][ind]
                    count += 1
        if sum!= 0:
            AvgP = sum/count
            # print(count)
        else:
            AvgP = 0
        new_df = new_df.append({'Voltage':x_line[i] , 'Power': AvgP},  ignore_index=True)

    # new_df.to_excel(writer, sheet_name=sheet, index=False)
    DF_list.append(new_df)
with ExcelWriter(xls_path) as writer:
    for n, df in enumerate(DF_list):
        df.to_excel(writer,'sheet%s' % n)
    writer.save()
