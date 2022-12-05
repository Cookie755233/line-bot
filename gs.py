import pygsheets
import pandas as pd

auth_file = "gs-key.json"
url = "https://docs.google.com/spreadsheets/d/13UuliTofuUDBReMdL3-RTC03GY7m0so_rGadeWZRyKk/"
scope = ['https://www.googleapis.com/auth/spreadsheets']


gc = pygsheets.authorize(service_account_file=auth_file)
global_sheet = gc.open_by_url(url=url)

class GoogleSheets:
    def __init__(self, sheet_name = "ls"):
        # setting sheet        
        self.working_sheet = global_sheet.worksheet_by_title(sheet_name)
        self.df = self.working_sheet.get_as_df(numerize=False)
        
        
    @property
    def columns(self):
        return self.df.columns
    
    
    # def read(self, position):
    #     content = self.working_sheet.cell(position)
    #     print(content)
    #     print(content.value)

    # def write(self, position = "A1", content = "test"):    
    #     self.working_sheet.update_value(position, content)

    # def append(self, values = []):
    #     self.working_sheet.append_table(values=values) 

    # def insert(self, insert_rows = 1, values = []): # insert_rows = 1, start from 2
    #     self.working_sheet.insert_rows(insert_rows, number=1, values=values) 
