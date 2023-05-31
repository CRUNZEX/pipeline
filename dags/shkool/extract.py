import pandas as pd
import glob

def run():
    try:
        folder_path = '/opt/airflow/data/source'
        dataFrame = []
        first_file = True
        for file_path in glob.glob(f'{folder_path}/raw*.csv'):
            if first_file is True:
                df = pd.read_csv(file_path,sep="|",header=0)
                first_file = False
            else:
                df = pd.read_csv(file_path,skiprows=0,sep="|",)
            dataFrame.append(df)

        merged_df = pd.concat(dataFrame)
        # print(merged_df)
        merged_df.to_csv("/opt/airflow/data/sourceFile.csv", index=False)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    run()