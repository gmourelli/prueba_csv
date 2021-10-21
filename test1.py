import pandas as pd 
import os



file_name = 'df.csv'
path_export = os.path.join(file_name) 
path_export = os.path.abspath(path_export)


df_csv = pd.read_csv(path_export)
df_csv = df_csv.set_index('Nombre')


df_csv['Edad'] = df_csv['Edad'] / 2


if os.path.exists(path_export):
    os.remove(path_export)
    df_csv.to_csv(path_export)
else:
    df_csv.to_csv(path_export)