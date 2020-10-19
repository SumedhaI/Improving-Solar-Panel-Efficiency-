# Preprocessing
#
#
import pandas as pd
from preprocessing import read_sheet
from preprocessing import preprocess
from preprocessing import organize
from preprocessing import transpose
from preprocessing import ground_truth_gen
from preprocessing import data_with_gt
input_ = 'C:/Users/sumed/Desktop/Spring20/data/ML_Data_Training.xlsx'  # EXCEL INPUT FILE PATH

######  ML_Data_Training or ML_Data_Test
xl = pd.ExcelFile(input_)
total_sheet = len(xl.sheet_names)
discritize_path = preprocess(total_sheet, input_)

## ORGANIZE
#
organize_path = organize(total_sheet, discritize_path)

## TRANSPOSE
#
transpose_path = transpose(organize_path)

## Ground Truth
#
gt_path = ground_truth_gen(total_sheet, input_)

## Adding GT to the transpose data
#
final_ = data_with_gt(gt_path, transpose_path)
