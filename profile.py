from pandas_profiling import ProfileReport
import pandas as pd

df = pd.read_excel('project.xlsx')



# prof = ProfileReport(df, title = 'Delivery Report ',minimal = True, explorative=True)
prof = ProfileReport(df, title = 'Delivery Report ', minimal = True)
prof.to_file(output_file='output.html')
