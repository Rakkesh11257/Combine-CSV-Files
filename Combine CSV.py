import os
import pandas as pd

def combine_csv_files(folder_path, output_file):
    # Initialize an empty list to store data from each file
    all_data = []
    
    # Recursively traverse through all directories and subdirectories
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.csv'):
                file_path = os.path.join(root, filename)
                # Read each CSV file and append its contents to the list
                df = pd.read_csv(file_path)
                all_data.append(df)
    
    if all_data:
        # Concatenate all data frames in the list
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # Write the combined data frame to a new CSV file
        combined_df.to_csv(output_file, index=False)
        print(f"Combined data written to {output_file}")
    else:
        print("No CSV files found in the specified folder and its subfolders.")

def main():
    folder_path = r"C:\Users\rakkesh_r\Downloads\CARSX-AMA"  # Change this to the folder containing your CSV files
    output_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'Combined.csv')

    combine_csv_files(folder_path, output_file)

if __name__ == "__main__":
    main()