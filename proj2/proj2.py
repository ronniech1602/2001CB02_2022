import pandas as pd
import os
from openpyxl import load_workbook
import streamlit as st
from openpyxl.styles import Border,Side,PatternFill
from datetime import datetime
start_time = datetime.now()


#Page Configuration
st.set_page_config(page_title='Octant Analysis',page_icon=':cyclone:',layout='wide')

with st.container():
    st.header('Welcome To Our CS384 Project :cyclone:')
    st.write('##')
    



    
def output_compute(file_in):
    
    cd=os.chdir(file_in)
    for file in file_in:
        #border function
        def border(rs,re,cs,ce):
            top=Side(border_style='medium',color='000000')
            bottom=Side(border_style='medium',color='000000')
            left=Side(border_style='medium',color='000000')
            right=Side(border_style='medium',color='000000')
            border=Border(top=top,bottom=bottom,left=left,right=right)
            for r in range(rs,re+1):
                for co in range(cs,ce+1):
                    ws.cell(row=r,column=co).border=border
         
        #cell coloring function
        def cell_color(cell_row,cell_column):
            fill=PatternFill(patternType='solid',fgColor='FFFF00')
            ws.cell(row=cell_row,column=cell_column).fill=fill
        
        wb=load_workbook(file)
        df=pd.read_excel(file)
        ws=wb.worksheets[0]
        
    

        
        
    
with st.container():
    File_input=st.text_input('Provide The File Directory :',key='fd')
    Mod_input=st.text_input('Provide The Mod Value :',key='mi')        
    st.button('Compute',key='bt',onclick='')







#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))

