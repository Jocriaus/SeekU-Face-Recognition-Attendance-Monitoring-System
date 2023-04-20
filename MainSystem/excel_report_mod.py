import pandas as pd
import query_mod as qry
import os

class excelClass:

    def __init__(self, master=None):
        self.sql_query = qry.dbQueries()
        

    def save_student(self,filename,filepath, date1, date2):
        data, columns = self.sql_query.sort_student_report_bydate_excel(date1, date2)
        df = pd.DataFrame(list(data), columns=columns)
        writer = pd.ExcelWriter(filepath+'/'+filename+'.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1',startrow=12,startcol=4, header = True, index = False)
        worksheet = writer.sheets['Sheet1']
        worksheet.insert_image('A1', '.\SeekU\STI College Balagtas Logo medium.png')
        worksheet.insert_image('F1', '.\SeekU\SeekU Logotype micro.png')
        worksheet.insert_image('L1', '.\SeekU\SeekU small.png')
        writer.save()

    def save_personnel(self,filename,filepath, date1, date2):
        data, columns = self.sql_query.sort_personnel_report_bydate_excel(date1, date2)
        df = pd.DataFrame(list(data), columns=columns)
        writer = pd.ExcelWriter(filepath+'/'+filename+'.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1',startrow=12,startcol=4, header = True, index = False)
        worksheet = writer.sheets['Sheet1']
        worksheet.insert_image('A1', '.\SeekU\STI College Balagtas Logo medium.png')
        worksheet.insert_image('F1', '.\SeekU\SeekU Logotype micro.png')
        worksheet.insert_image('L1', '.\SeekU\SeekU small.png')
        writer.save()

    def save_visitor(self,filename,filepath, date1, date2):
        data, columns = self.sql_query.sort_visitor_report_bydate_excel(date1, date2)
        df = pd.DataFrame(list(data), columns=columns)
        writer = pd.ExcelWriter(filepath+'/'+filename+'.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1',startrow=12,startcol=4, header = True, index = False)
        worksheet = writer.sheets['Sheet1']
        worksheet.insert_image('A1', '.\SeekU\STI College Balagtas Logo medium.png')
        worksheet.insert_image('F1', '.\SeekU\SeekU Logotype micro.png')
        worksheet.insert_image('L1', '.\SeekU\SeekU small.png')
        writer.save()

    def print_student(self,filename,filepath, date1, date2):
        pass

    def print_personnel(self,filename,filepath, date1, date2):
        pass

    def print_visitor(self,filename,filepath, date1, date2):
        pass
