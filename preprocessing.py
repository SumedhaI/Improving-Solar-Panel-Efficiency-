import numpy as np
import pandas as pd
from pandas import ExcelWriter
xls_path ="discritize_033_TEST.xlsx"
# writer = pd.ExcelWriter('demo4.xlsx', engine='xlsxwriter')
x_line = np.linspace(0, 69, 208)
DF_list= list()



def read_sheet(num, input_):
    path_ = input_
    df = pd.read_excel(path_ , sheet_name= num)
    return df

def preprocess(total_sheet, input_):    
    for sheet in range(total_sheet):
        df = read_sheet(sheet, input_)
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
    xls_path ="discritize_033_.xlsx"  # NAME OF THE DISCRITIZED FILE
    with ExcelWriter(xls_path) as writer:
        for n, df in enumerate(DF_list):
            df.to_excel(writer,'sheet%s' % n)
        writer.save()
    return xls_path


def organize(total_sheet, discritize_path):
    new_df = pd.DataFrame()
    xls_path = "organize_.xlsx" # ORGANIZE OUTPUT FILE NAME
    for sheet in range(total_sheet):
        df = read_sheet(sheet, discritize_path)
        new_df[sheet] = df.Power

    # print(new_df)
    new_df.to_excel(xls_path, header=False, index=False)
    return xls_path

def transpose(organize_path):
    xls_path = "Transpose_.xlsx"
    df = pd.read_excel(organize_path, header=None)
    # print(df.shape)
    df1_transpose = df.T   
    df1_transpose.to_excel(xls_path, header=False, index=False)
    return xls_path

def ground_truth_gen(total_sheet, input_):
    new_df = pd.DataFrame(columns = ["category"])
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


    for i in range(total_sheet):
        df = read_sheet(i, input_)
        maxP = df.Power.max()
        # print('maxP: ',maxP)
        valV = df.loc[df['Power'] == maxP, 'Voltage'].iloc[0]
        # print('valV: ',valV)
    
        cat2 = int(maxP/p_div)
        cat1 = int(valV/v_div)
        # print(cat1, cat2)
        if cat2 > h-1:
            cat2 = h-1
        if cat1>w-1:
            cat1 = w-1
        category = Matrix[cat2][cat1]
        # print('category: ', category)
    
        new_df = new_df.append({'category': category },  ignore_index=True)
    xls_path = "GT_16_.xlsx"
    new_df.to_excel(xls_path, header=False, index=False)
    return xls_path

def data_with_gt(gt_path, transpose_path):
    df_gt = pd.read_excel(gt_path, header=None)
    df = pd.read_excel(transpose_path, header=None)
    df.insert(df.shape[1], "GT", df_gt)
    # print(df.head(5))
    #####################################################
    #####################################################
    ##### Change the file name TEST or TRAIN ############
    xls_path = "final_TRAIN.xlsx" 
    df.to_excel(xls_path, header=False, index=False)
    return xls_path