import pandas as pd
from .views import *

def dynamicrule(f,s,r):
    try:
        df = pd.read_excel('media2/' + f, sheet_name=s, header=r)
        # columnHead = list(df.columns)
        return df

    except Exception as e:
        df = "message "+str(e)
        return df


# import pandas as pd
#
# def dynamicrule(f,s,r):
#     try:
#         df = pd.read_excel('fileupload/media/' + f, sheet_name=s, header=r)
#         print(df)
#         print(f)
#         print(r)
#         print(s)
#         return df
#     except Exception as e:
#         s="messege"+e
#         return e

# try:
#     def dynamicrule(f,s,r):
#         df=pd.read_excel('fileupload/media/' + f , sheet_name=s,header=r)
#         print(df)
#         return df
#
# except Exception as e:
#     status_code= 403
#     message = "Your account doesn't have permissions to go so far!"


# #from ipynb.fs.full.DynamicRule_Module import *
# import pandas as pd
# import numpy as np
# from .views import *
# from pyxlsb import open_workbook
# # d2=pd.DataFrame()
# # df_og = []
# # wb = open_workbook("C:/Users/Admin/Desktop/ABHIL_p_ sagar.xlsb")
# # with wb.get_sheet(1) as sheet:
# #     for row in sheet.rows():
# #         df_og.append([item.v for item in row])
# # df_og = pd.DataFrame(df_og[1:], columns=df_og[0])
# # df=df_og
# # df=pd.read_excel(my_button.files[0],sheet_name=0,header=0)
# sheetName = Detail.objects.values('SHEET_NAME').last()
# rowno = Detail.objects.values('ROW_NO').last()
# fileData = File.objects.values('file').last()
# f = fileData['file']
# print(f)
# r = int(rowno['ROW_NO']) - 1
# s = sheetName['SHEET_NAME']
#
#
# df=pd.read_excel('fileupload/media/' + f , sheet_name=s,header=r)
#
# # from operator import *
# # ops = {'plus': add,
# #         'sub': sub,
# #        'concat':concat,
# #        'mul': mul,
# #        'equal':eq,
# #        'notequal':ne,
# #        'and':and_,
# #        'or':or_,
# #        'less':lt,
# #        'concat':add,
# #        'greater':gt
# #       }
# #
# #
# # def RuleDemo(size,Rule,d):
# #
# #     #...................... 1 Rule.................................................................................................
# #
# #     if(size==3):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         def Dym(col1,opr1,val1,d):
# #
# #                 data=In[d].loc[(ops[opr1](In[d][col1], val1))]
# #
# #                 return data
# #         data=Dym(col1,opr1,val1,d)
# #
# #
# #     #...................... 2 Rule.................................................................................................
# #     elif(size==7):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         if((log1=='and')or(log1=='or')):
# #
# #             #......................2 and  or.................................................................
# #
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1], val1)), (ops[opr2](In[d][col2], val2))))]
# #
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,d)
# #
# #     #...................... 3 Rule.................................................................................................
# #
# #     elif(size==11):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #
# #         if((log1=='and' and log2=='and')or(log1=='or' and log2=='or')):
# #
# #             #......................2 and / 2 or.................................................................
# #
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)), (ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3], val3))))]
# #
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d)
# #
# #
# #         elif((log1=='and') and (log2=='or')):
# #
# #             #......................1 and  1 or.................................................................
# #
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1],val1)),(ops[log2]((ops[opr2](In[d][col2],val2)),(ops[opr3](In[d][col3],val3))))))]
# #
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d)
# #
# #
# # #...................... 4 Rule.................................................................................................
# #
# #
# #     elif(size==15):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #
# #         if((log1=='and' and log2=='and' and log3=='and')or(log1=='or' and log2=='or' and log3=='or')):
# #
# #             #......................3 and / 3 or.................................................................
# #
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d):
# #
# #                 data=In[d].loc[(ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d)
# #
# #         elif((log1=='and' and log2=='and' and log3=='or')):
# #
# #             #......................2 and  1 or.................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1],val1)),(ops[opr2](In[d][col2],val2)))),(ops[log3]((ops[opr3](In[d][col3],val3)),(ops[opr4](In[d][col4],val4))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d)
# #
# #
# #         elif((log1=='and' and log2=='or' and log3=='or')):
# #
# #             #......................1 and  2 or.................................................................
# #
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1],val1)),(ops[log3]((ops[log2]((ops[opr2](In[d][col2],val2)),(ops[opr3] (In[d][col3],val3)))),(ops[opr4](In[d][col4],val4))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d)
# #
# #
# # #...................... 5 Rule.................................................................................................
# #
# #
# #     elif(size==19):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #         log4 =Rule[15]
# #         col5 =Rule[16]
# #         opr5 =Rule[17]
# #         val5 =int(Rule[18]) if Rule[18].isnumeric() else Rule[18]
# #         if((log1=='and' and log2=='and' and log3=='and' and log4=='and')or(log1=='or' and log2=='or' and log3=='or' and log4=='or')):
# #
# #             #......................4 and  or...................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d):
# #
# #                 data=In[d].loc[(ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d)
# #
# #         elif((log1=='and' and log2=='and' and log3=='and' and log4=='or')):
# #
# #             #......................3 and  1 or...................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d):
# #
# #                 data= In[d].loc[(ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[log4]((ops[opr4](In[d][col4],val4)),(ops[opr5](In[d][col5],val5))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d)
# #
# #         elif((log1=='and' and log2=='and' and log3=='or' and log4=='or')):
# #
# #             #......................2 and  2 or...................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)), (ops[opr2](In[d][col2], val2)))),(ops[log4]((ops[log3]((ops[opr3](In[d][col3],val3)),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5 ],val5))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d)
# #
# #         elif((log1=='and' and log2=='or' and log3=='or' and log4=='or')):
# #
# #             #......................1 and  3 or...................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1],val1)),(ops[log4]((ops[log3]((ops[log2]((ops[opr2](In[d][col2], val2)),(ops[opr3](In[d][col3], val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d)
# #
# #  #...................... 6 Rule....................................................................................
# #
# #
# #     elif(size==23):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #         log4 =Rule[15]
# #         col5 =Rule[16]
# #         opr5 =Rule[17]
# #         val5 =int(Rule[18]) if Rule[18].isnumeric() else Rule[18]
# #         log5 =Rule[19]
# #         col6 =Rule[20]
# #         opr6 =Rule[21]
# #         val6 =int(Rule[22]) if Rule[22].isnumeric() else Rule[22]
# #
# #
# #         if((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='and')or(log1=='or' and log2=='or' and log3=='or' and log4=='or' and log5=='or')):
# #
# #             #......................5 and / 5 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d):
# #
# #                 data=In[d].loc[(ops[log5]((ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6))))]
# #
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d)
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='or')):
# #
# #             #......................4 and  1 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d):
# #
# #                 data=In[d].loc[(ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1],val1)),(ops[opr2](In[d][col2],val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[log5]((ops[opr5](In[d][col5],val5)),(ops[opr6](In[d][col6],val6))))))]
# #
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d)
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='and' and log4=='or' and log5=='or')):
# #
# #             #......................3 and  2 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d):
# #
# #                 data= In[d].loc[(ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[log5]((ops[log4]((ops[opr4](In[d][col4],val4)),(ops[opr5](In[d][col5 ],val5)))),(ops[opr6](In[d][col6],val6))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d)
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='or' and log4=='or' and log5=='or')):
# #
# #             #......................2 and  3 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1],val1)),(ops[opr2](In[d][col2],val2)))),(ops[log5]((ops[log4]((ops[log3]((ops[opr3](In[d][col3],val3)),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d)
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='or' and log4=='or' and log5=='or')):
# #
# #             #......................1 and  4 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1],val1)),(ops[log5]((ops[log4]((ops[log3]((ops[log2]((ops[opr2](In[d][col2],val2)),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d)
# #
# #
# #     #......................................... 7 Rule.............................................................................
# #
# #
# #     elif(size==27):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #         log4 =Rule[15]
# #         col5 =Rule[16]
# #         opr5 =Rule[17]
# #         val5 =int(Rule[18]) if Rule[18].isnumeric() else Rule[18]
# #         log5 =Rule[19]
# #         col6 =Rule[20]
# #         opr6 =Rule[21]
# #         val6 =int(Rule[22]) if Rule[22].isnumeric() else Rule[22]
# #         log6 =Rule[23]
# #         col7 =Rule[24]
# #         opr7 =Rule[25]
# #         val7 =int(Rule[26]) if Rule[26].isnumeric() else Rule[26]
# #
# #
# #         if((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='and' and log6=='or' )):
# #
# #             #......................5 and  1 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data= In[d].loc[(ops[log5]((ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[log6]((ops[opr6](In[d][col6], val6)),(ops[opr7](In[d][col7],val7))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='or' and log6=='or' )):
# #
# #             #......................4 and  2 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data=In[d].loc[(ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2],val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[log6]((ops[log5]((ops[opr5](df[col5], val5)), (ops[opr6](In[d][col6], val6)))),(ops[opr7](In[d][col7], val7))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='and' and log4=='or' and log5=='or' and log6=='or' )):
# #
# #             #......................3 and  3 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data=In[d].loc[(ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[log6]((ops[log5]((ops[log4]((ops[opr4](In[d][col4], val4)),(ops[opr5](In[d][col5], val5)))),(ops[opr6](In[d][col6],val6)))),(ops[opr7](In[d][col7],val7))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='or' and log4=='or' and log5=='or' and log6=='or' )):
# #
# #             #......................2 and  4 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)), (ops[opr2](In[d][col2], val2)))),(ops[log6]((ops[log5]((ops[log4]((ops[log3]((ops[opr3](In[d][col3], val3)),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6)))),(ops[opr7](In[d][col7],val7))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #
# #
# #         elif((log1=='and' and log2=='or' and log3=='or' and log4=='or' and log5=='or' and log6=='or' )):
# #
# #             #......................1 and  5 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1], val1)), (ops[log6]((ops[log5]((ops[log4]((ops[log3]((ops[log2]((ops[opr2](In[d][col2], val2)),(ops[opr3](In[d][col3], val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6)))),(ops[opr7](In[d][col7],val7))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #
# #         elif((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='and' and log6=='and' )|(log1=='or' and log2=='or' and log3=='or' and log4=='or' and log5=='or' and log6=='or' )):
# #
# #             #.....................6 and / 6 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data=In[d].loc[(ops[log6]((ops[log5]((ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6)))),(ops[opr7](In[d][col7],val7))))]
# #                 return data
# #
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #
# #     return data
# #
# # def DemoB2CS(size,Rule,d):
# #
# #     if(size==11):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #
# #         if((log1=='and') and (log2=='or')):
# #
# #     #......................1 and  1 or.................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1],val1)),(ops[opr2](In[d][col2],val2)))),(ops[opr3](In[d][col3],val3))))]
# #                 return data
# #
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d)
# #
# #     elif(size==15):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #
# #
# #         if((log1=='and' and log2=='and' and log3=='or')):
# #
# #             #......................2 and  1 or.................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1], val1)),(ops[log3]((ops[log2]((ops[opr2](In[d][col2], val2)),(ops[opr3](In[d][col3],val3)))),(ops[opr4](In[d][col4],val4))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,d)
# #
# #     elif(size==19):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #         log4 =Rule[15]
# #         col5 =Rule[16]
# #         opr5 =Rule[17]
# #         val5 =int(Rule[18]) if Rule[18].isnumeric() else Rule[18]
# #
# #         if((log1=='and' and log2=='and' and log3=='and' and log4=='or')):
# #
# #             #......................3 and  1 or...................................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1],val1)),(ops[opr2](In[d][col2],val2)))),(ops[log4]((ops[log3]((ops[opr3](In[d][col3], val3)),(ops[opr4](In[d][col4],val4)))),(ops[opr5](In[d][col5],val5))))))]
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,d)
# #
# #
# #     elif(size==23):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #         log4 =Rule[15]
# #         col5 =Rule[16]
# #         opr5 =Rule[17]
# #         val5 =int(Rule[18]) if Rule[18].isnumeric() else Rule[18]
# #         log5 =Rule[19]
# #         col6 =Rule[20]
# #         opr6 =Rule[21]
# #         val6 =int(Rule[22]) if Rule[22].isnumeric() else Rule[22]
# #
# #         if((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='or')):
# #
# #             #......................4 and  1 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d):
# #
# #                 data=In[d].loc[(ops[log3]((ops[log2]((ops[log1]((ops[opr1](In[d][col1], val1)),(ops[opr2](In[d][col2], val2)))),(ops[opr3](In[d][col3],val3)))),(ops[log5]((ops[log4]((ops[opr4](In[d][col4], val4)),(ops[opr5](In[d][col5],val5)))),(ops[opr6](In[d][col6],val6))))))]
# #
# #                 return data
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,d)
# #
# #
# #     elif(size==27):
# #
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =int(Rule[2]) if Rule[2].isnumeric() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =int(Rule[6]) if Rule[6].isnumeric() else Rule[6]
# #         log2 = Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =int(Rule[10]) if Rule[10].isnumeric() else Rule[10]
# #         log3 =Rule[11]
# #         col4 =Rule[12]
# #         opr4 =Rule[13]
# #         val4 =int(Rule[14]) if Rule[14].isnumeric() else Rule[14]
# #         log4 =Rule[15]
# #         col5 =Rule[16]
# #         opr5 =Rule[17]
# #         val5 =int(Rule[18]) if Rule[18].isnumeric() else Rule[18]
# #         log5 =Rule[19]
# #         col6 =Rule[20]
# #         opr6 =Rule[21]
# #         val6 =int(Rule[22]) if Rule[22].isnumeric() else Rule[22]
# #         log6 =Rule[23]
# #         col7 =Rule[24]
# #         opr7 =Rule[25]
# #         val7 =int(Rule[26]) if Rule[26].isnumeric() else Rule[26]
# #         if((log1=='and' and log2=='and' and log3=='and' and log4=='and' and log5=='and' and log6=='or' )):
# #
# #             #......................5 and  1 or ....................................................
# #
# #             def Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d):
# #
# #                 data=df.loc[(ops[log4]((ops[log3]((ops[log2]((ops[log1]((ops[opr1](df[col1],val1)),(ops[opr2](df[col2],val2)))),(ops[opr3](df[col3],val3)))),(ops[opr4](df[col4],val4)))),(ops[log6]((ops[log5]((ops[opr5](df[col5], val5)),(ops[opr6](df[col6],val6)))),(ops[opr7](df[col7],val7))))))]
# #
# #                 return data
# #
# #             data=Dym(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,log3,col4,opr4,val4,log4,col5,opr5,val5,log5,col6,opr6,val6,log6,col7,opr7,val7,d)
# #
# #     return data
# #
# #
# #
# #
# #
# # def ConcatD(size,Rule,d,New_column):
# #
# #     if(size==1):
# #         col1=Rule[0]
# #
# #         def ConD(d,col1,New_column):
# #             In[d][New_column]=In[d][col1].map(str)
# #             return In[d]
# #         data=ConD(d,col1,New_column)
# #
# #
# #
# #     elif(size==2):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #
# #         a =In[d][col1].dtype.name
# #         if a=='object':
# #             In[d][col1]= In[d][col1].replace('^\s*$', np.nan, regex=True).fillna("NaN")
# #         else:
# #             In[d][col1]= In[d][col1].replace('^\s*$', regex=True).fillna(0)
# #
# #
# #         def ConD(d,col1,col2,New_column):
# #             In[d][New_column]=In[d][col1].map(str)+In[d][col2].map(str)
# #             return In[d]
# #         data=ConD(d,col1,col2,New_column)
# #
# #
# #     elif(size==3):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #
# #         a =In[d][col1].dtype.name
# #         if a=='object':
# #             In[d][col1]= In[d][col1].replace('^\s*$', np.nan, regex=True).fillna("NaN")
# #         else:
# #             In[d][col1]= In[d][col1].replace('^\s*$', regex=True).fillna(0)
# #
# #
# #         def ConD(d,col1,col2,col3,New_column):
# #             In[d][New_column]=In[d][col1].map(str)+In[d][col2].map(str)+In[d][col3].map(str)
# #             return In[d]
# #         data=ConD(d,col1,col2,col3,New_column)
# #
# #
# #
# #
# #     elif(size==4):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #         col4=Rule[3]
# #
# #         def ConD(d,col1,col2,col3,col4,New_column):
# #             In[d][New_column]=In[d][col1].map(str)+In[d][col2].map(str)+In[d][col3].map(str)+In[d][col4].map(str)
# #             return In[d]
# #         data=ConD(d,col1,col2,col3,col4,New_column)
# #
# #
# #     elif(size==5):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #         col4=Rule[3]
# #         col5=Rule[4]
# #
# #         def ConD(d,col1,col2,col3,col4,col5,New_column):
# #             In[d][New_column]=In[d][col1].map(str)+In[d][col2].map(str)+In[d][col3].map(str)+In[d][col4].map(str)+In[d][col5].map(str)
# #             return In[d]
# #         data=ConD(d,col1,col2,col3,col4,col5,New_column)
# #
# #
# #     return data
# # def Sum(size,Rule,d,New_column):
# #     if(size==2):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         In[d]=In[d][col1].astype(float)
# #         In[d]=In[d][col2].astype(float)
# #
# #
# #         def Sumval(d,col1,col2,New_column):
# #
# #             In[d][New_column]=In[d][[col1,col2]].sum(axis=1)
# #
# #             #In[d][New_column]=In[d][col1].astype(float)+In[d][col2].astype(float)
# #
# #             return In[d]
# #         data=Sumval(d,col1,col2,New_column)
# #
# #
# #     elif(size==3):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #         In[d][col1]=In[d][col1].astype(float)
# #         In[d][col2]=In[d][col2].astype(float)
# #         In[d][col3]=In[d][col3].astype(float)
# #
# #
# #
# #         def Sumval(d,col1,col2,New_column):
# #             In[d][New_column]=In[d][[col1,col2,col3]].sum(axis=1)
# #             return In[d]
# #         data=Sumval(d,col1,col2,New_column)
# #
# #
# #     elif(size==4):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #         col4=Rule[3]
# #         In[d][col1]=In[d][col1].astype(float)
# #         In[d][col2]=In[d][col2].astype(float)
# #         In[d][col3]=In[d][col3].astype(float)
# #         In[d][col4]=In[d][col4].astype(float)
# #
# #
# #
# #         def Sumval(d,col1,col2,col3,col4,New_column):
# #             In[d][New_column]=In[d][[col1,col2,col3,col4]].sum(axis=1)
# #             return In[d]
# #         data=Sumval(d,col1,col2,col3,col4,New_column)
# #
# #
# #     elif(size==5):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #         col4=Rule[3]
# #         col5=Rule[4]
# #
# #         In[d][col1]=In[d][col1].astype(float)
# #         In[d][col2]=In[d][col2].astype(float)
# #         In[d][col3]=In[d][col3].astype(float)
# #         In[d][col4]=In[d][col4].astype(float)
# #         In[d][col5]=In[d][col5].astype(float)
# #
# #
# #
# #         def Sumval(d,col1,col2,col3,col4,col5,New_column):
# #             In[d][New_column]=In[d][[col1,col2,col3,col4,col5]].sum(axis=1)
# #             return In[d]
# #         data=Sumval(d,col1,col2,col3,col4,col5,New_column)
# #
# #
# #     elif(size==6):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         col3=Rule[2]
# #         col4=Rule[3]
# #         col5=Rule[4]
# #         col6=Rule[5]
# #
# #         In[d][col1]=In[d][col1].astype(float)
# #         In[d][col2]=In[d][col2].astype(float)
# #         In[d][col3]=In[d][col3].astype(float)
# #         In[d][col4]=In[d][col4].astype(float)
# #         In[d][col5]=In[d][col5].astype(float)
# #         In[d][col6]=In[d][col6].astype(float)
# #
# #
# #         def Sumval(d,col1,col2,col3,col4,col5,col6,New_column):
# #             In[d][New_column]=In[d][[col1,col2,col3,col4,col5,col6]].sum(axis=1)
# #             return In[d]
# #         data=Sumval(d,col1,col2,col3,col4,col5,col6,New_column)
# #
# #
# #     return data
# #
# #
# # def GroupBy(size,Rule,d,New_column):
# #     if(size==2):
# #         col1=Rule[0]
# #         col2=Rule[1]
# #         In[d][col1]=In[d][col1].astype(float)
# #         In[d][col2]=In[d][col2].map(str)
# #
# #         def Transform(d,col1,col2,New_column):
# #
# #             In[d][New_column]=In[d][[col1]].sum(axis=1).groupby(In[d][col2]).transform('sum')
# #
# #             return In[d]
# #         data=Transform(d,col1,col2,New_column)
# #
# #     return data
# # def SetVal(d,Set_value,New_column):
# #        #print(Set_value)
# #         def Set_Val(d,Set_value,New_column):
# #             #print(Set_value)
# #             print(New_column)
# #             In[d][New_column]=Set_value
# #
# #             return In[d]
# #
# #         data=Set_Val(d,Set_value,New_column)
# #
# #         return data
# # #...................... 1 Rule.................................................................................................
# # def NewVal(d,Rule,size):
# #
# #     if(size==3):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =float(Rule[2]) if Rule[2].lstrip('-').replace('.','',1).isdigit() else Rule[2]
# #         def New_Val(col1,opr1,val1,d):
# #
# #                 data=In[d].loc[(ops[opr1](In[d][col1], val1))]
# #
# #                 return data
# #         data=New_Val(col1,opr1,val1,d)
# #
# #
# # #...................... 2 Rule.................................................................................................
# #
# #     elif(size==7):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =float(Rule[2]) if Rule[2].lstrip('-').replace('.','',1).isdigit() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =float(Rule[6]) if Rule[6].lstrip('-').replace('.','',1).isdigit() else Rule[6]
# #
# #         if((log1=='and')or(log1=='or')):
# #
# #             #......................2 and  or.................................................................
# #
# #
# #             def New_Val(col1,opr1,val1,log1,col2,opr2,val2,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1],val1)),(ops[opr2](In[d][col2],val2))))]
# #
# #                 return data
# #             data=New_Val(col1,opr1,val1,log1,col2,opr2,val2,d)
# #
# # #...................... 3 Rule.................................................................................................
# #
# #     elif(size==11):
# #         col1 =Rule[0]
# #         opr1 =Rule[1]
# #         val1 =float(Rule[2]) if Rule[2].lstrip('-').replace('.','',1).isdigit() else Rule[2]
# #         log1 =Rule[3]
# #         col2 =Rule[4]
# #         opr2 =Rule[5]
# #         val2 =float(Rule[6]) if Rule[6].lstrip('-').replace('.','',1).isdigit() else Rule[6]
# #         log2 =Rule[7]
# #         col3 =Rule[8]
# #         opr3 =Rule[9]
# #         val3 =float(Rule[10]) if Rule[10].lstrip('-').replace('.','',1).isdigit() else Rule[10]
# #
# #         if((log1=='and' and log2=='and')or(log1=='or' and log2=='or')):
# #
# #             #......................2 and / 2 or.................................................................
# #
# #
# #             def New_Val(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d):
# #
# #                 data=In[d].loc[(ops[log2]((ops[log1]((ops[opr1](In[d][col1],val1)), (ops[opr2](In[d][col2],val2)))),(ops[opr3](In[d][col3],val3))))]
# #
# #                 return data
# #             data=New_Val(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d)
# #
# #
# #         elif((log1=='and') and (log2=='or')):
# #
# #             #......................1 and  1 or.................................................................
# #
# #
# #             def New_Val(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d):
# #
# #                 data=In[d].loc[(ops[log1]((ops[opr1](In[d][col1],val1)),(ops[log2]((ops[opr2](In[d][col2],val2)),(ops[opr3](In[d][col3],val3))))))]
# #
# #                 return data
# #             data=New_Val(col1,opr1,val1,log1,col2,opr2,val2,log2,col3,opr3,val3,d)
# #
# #
# #
# #     return data
#
#
#
# import json
# import pymysql
# import pandas as pd
#
# stat = Detail.objects.values('STATUS').last()
# company = Detail.objects.values('COMPANY_NAME').last()
# Company_name = company['COMPANY_NAME']
# Status = stat['STATUS']
# conn = pymysql.connect(
#     host="localhost",user="root",password="root",db='mapper',port=3306)
# cursor = conn.cursor()
# # Company_name = input(str("Enter Company Name : "))
# # Status = input(str("Enter Status : "))
#
# data=cursor.execute("""SELECT * from new_company_rules WHERE Company_name = %s and Status = %s""", (Company_name,Status))
# result_set= cursor.fetchall()
#
# # item=[dict(zip([key[0] for key in cursor.description], row)) for row in result_set]
# # conn.close()
# # rule=pd.DataFrame(item).dropna(how='all')
# #
# #
# # # rule=pd.read_excel("C:/Users/Admin/Desktop/PR Oct 18.xlsx",sheet_name=3)
# # # print(rule)
# # last_row=len(rule)
# # print(last_row)
# # for i in range(last_row):
# #
# #     Rule=rule.iloc[i]['Rule']
# #     #print(type(Rule))
# #     print(Rule)
# #     d=rule.iloc[i]['Data_in']
# #     print(d)
# #     Column_value=rule.iloc[i]['Column_value']
# #     print(Column_value)
# #     Rule=str(Rule)
# #     Rule=Rule.split(',')
# #     size=len(Rule)
# #     print(size)
# #     New_column=rule.iloc[i]['New_column']
# #     print(New_column)
# #     Set_value=rule.iloc[i]['Set_value']
# #     print(Set_value)
# #
# #     if((Column_value=='Invoice_type')and(Set_value!='B2CS')):
# #         In={'df':df,}
# #         Invoice_type=RuleDemo(size,Rule,d)
# #
# #
# #         if(rule.iloc[i]['New_column'] in df.columns):
# #             df.loc[df.index.intersection(Invoice_type.index),rule.iloc[i]['New_column']]=Set_value
# #
# #
# #         else:
# #             print(rule.iloc[i]['New_column'])
# #             df[rule.iloc[i]['New_column']]='Error'
# #             df.loc[df.index.intersection(Invoice_type.index),rule.iloc[i]['New_column']]=Set_value
# #
# #     elif((Column_value=='Invoice_type')and(Set_value=='B2CS')):
# #         In={'df':df,}
# #         Invoice_type=DemoB2CS(size,Rule,d)
# #
# #
# #         if(rule.iloc[i]['New_column'] in df.columns):
# #             df.loc[df.index.intersection(Invoice_type.index),rule.iloc[i]['New_column']]=Set_value
# #
# #
# #         else:
# #             print(rule.iloc[i]['New_column'])
# #             df[rule.iloc[i]['New_column']]='Error'
# #             df.loc[df.index.intersection(Invoice_type.index),rule.iloc[i]['New_column']]=Set_value
# #
# #     elif(Column_value=='Invoice_subtype'):
# #         In={'df':df,}
# #         Invoice_subtype=RuleDemo(size,Rule,d)
# #         #df.loc[df.index.intersection(B2CL.index), 'Column_value'] = 'B2CL'
# #         if(rule.iloc[i]['New_column'] in df.columns):
# #
# #             df.loc[df.index.intersection(Invoice_subtype.index),rule.iloc[i]['New_column']] =Set_value
# #
# #         else:
# #             df[rule.iloc[i]['New_column']]=''
# #             df.loc[df.index.intersection(Invoice_subtype.index),rule.iloc[i]['New_column']] =Set_value
# #
# #     elif(Column_value=='CONCAT'):
# #         In={'df':df,}
# #         con=ConcatD(size,Rule,d,New_column)
# #         #print(d1)
# #         df=con
# #
# #     elif(Column_value=='SUM'):
# #         In={'df':df,}
# #         Sum_col=Sum(size,Rule,d,New_column)
# #         df=Sum_col
# #
# #     elif(Column_value=='GROUPBY'):
# #         In={'df':df,}
# #         Group_by=GroupBy(size,Rule,d,New_column)
# #         df=Group_by
# #
# #
# #     elif(Column_value=='SET'):
# #         In={'df':df,}
# #         SET=SetVal(d,Set_value,New_column)
# #         df=SET
# #
# #
# #     elif(Column_value=='NEW'):
# #         In={'df':df,}
# #         New_val1=NewVal(d,Rule,size)
# #         #print(New_val1)
# #         #df=SET
# #
# #         if(rule.iloc[i]['New_column'] in df.columns):
# #
# #             df.loc[df.index.intersection(New_val1.index),rule.iloc[i]['New_column']] =Set_value
# #
# #         else:
# #             df[rule.iloc[i]['New_column']]=''
# #             df.loc[df.index.intersection(New_val1.index),rule.iloc[i]['New_column']] =Set_value
# # print(df)
# # # writer = pd.ExcelWriter("e:/final2.xlsx")
# # # df.to_excel(writer, startrow=0, startcol=0, index=False)
# # # worksheet = writer.sheets['Sheet1']
# # # writer.save()
