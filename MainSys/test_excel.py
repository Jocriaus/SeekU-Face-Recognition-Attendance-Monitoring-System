import pandas as pd


# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('.\MainSys\pandas.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Insert an image.
worksheet.insert_image('A1', '.\SeekU\STI College Balagtas Logo medium.png')
worksheet.insert_image('F1', '.\SeekU\SeekU Logotype micro.png')
worksheet.insert_image('L1', '.\SeekU\SeekU small.png')
# Close the Pandas Excel writer and output the Excel file.
writer.close()