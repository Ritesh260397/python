from .Dynamic_rule import *
from rest_framework.views import APIView
from django_mysql.models import JSONField
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser,JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, DetailSerializer,TemplateSerializer
from rest_framework import viewsets
from .models import Detail, File,Template
from django.http import HttpResponse
import json,os
import pandas as pd
import sqlalchemy
import  numpy as np
import pymysql
from pathlib import Path
from time import strftime
from django.http import JsonResponse


# class DetailView(APIView):
#     def post(self, request):
#         detail = DetailSerializer(data=request.data)
#         if detail.is_valid():
#             detail.save()
#             ok={"swedfghok":"okasdf"}
#             return HttpResponse(ok,status=status.HTTP_201_CREATED)
class DetailView(APIView):
    def post(self, request):
        detail = DetailSerializer(data=request.data)
        if detail.is_valid():
            detail.save()
        # if (type(df) != str):
            a=[1,2,3,4,5,6,7,8,9]
            return HttpResponse(json.dumps({"status": "SUCCESS","columnHead": a}))
        # else:
        #     dict1 = {"exception": df, "status": "UNSUCCESS"}
        #     return HttpResponse(json.dumps(dict1))
        # sheetName = Detail.objects.values('SHEET_NAME').last()
        # rowno = Detail.objects.values('ROW_NO').last()
        # # print(rowno)
        # # print(type(rowno))
        # fileData = File.objects.values('file').last()
        # f = fileData['file']
        # r = int(rowno['ROW_NO'])-1
        # # print(r)
        # s = sheetName['SHEET_NAME']
        # df = dynamicrule(f, s, r)
        # if (type(df) != str):
        #     out = df.to_json(orient='records')
        #     dict1 = {"excelData": out, "sheetName": s, "filename": f, "status": "SUCCESS"}
        #     return HttpResponse(json.dumps(dict1), status=status.HTTP_201_CREATED)
        # else:
        #     dict1 = {"exception": df, "status": "UNSUCCESS"}
        #     return HttpResponse(json.dumps(dict1))

class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    def post(self, request,*args, **kwargs):
        file_obj = File.objects.values()
        listFile=[]
        for f in file_obj:
            listFile.append(f['file'])
        key=str(request.data['file'])
        if key in listFile:
            return HttpResponse(json.dumps({"message": "File already exists"}))
        else:
            file_serializer = FileSerializer(data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                fileData = File.objects.values('file').last()
                f = fileData['file']
                filename_download = Path(f).stem
                print(filename_download)
                return HttpResponse(json.dumps({"message": "Successfully Saved","filename_download":filename_download+" "+strftime("%d-%m-%y %H:%M:%S")}), status=status.HTTP_201_CREATED)



class xyz(APIView):
    def post(self, request):
        base = request.data['Company_Name']
        print(base)
        type = request.data['Status']
        print(type)
        # if len(base) == 1:
        #     invoice_type = 'where invoiceType = "'+base[0]+'" and type = "'+type+'"'
        # else:
        #     invoice_type = 'where invoiceType in '+str(tuple(base))+' and type = "'+type+'"'
        # # print(type)
        connection = pymysql.connect(host="localhost", user="root", password="root", db='mapper6')
        sysCol = pd.read_sql(
            'SELECT * FROM `system col_new` where Company_name="'+base+'" and status="'+type+'"', connection)
        aaaa = sysCol.to_json(orient='records')
        print(aaaa)
        # ok={"ok":"ok"}
        # return Response(ok)
        return HttpResponse(json.dumps(aaaa), status=status.HTTP_201_CREATED)
# class abcView(viewsets.ModelViewSet):
#     queryset = Template.objects.all()
#     serializer_class = TemplateSerializer
#     def perform_create(self,serializer):
#         Template_Name = self.request.data['Template_Name']
#         print(Template_Name)
#         key = serializer.save(Template_Name=Template_Name)
#         print(key)
#     def perform(self,serializer):
#         column_header = self.request.data['column_header']
#         print(column_header)
#         Bey = serializer.save(column_header=column_header)
#         print(Bey)
#     def perform_create1(self,serializer):
#         Company_Name = self.request.data['Company_Name']
#         print(Company_Name)
#         test = serializer.save(Template_Name=Company_Name)
#         print(test)
#     def perform_create2(self,serializer):
#         Status = self.request.data['Status']
#         print(Company_Name)
#         test = serializer.save(Status=Status)
#         print(test)

class abcView(APIView):
    def post(self, request):
        file_obj2 = Template.objects.values()
        # print(file_obj2)
        listTemplate=[]
        for temp_name in file_obj2:
            listTemplate.append(temp_name['Template_Name'])
        key2=str(request.data['Template_Name'])
        if key2 in listTemplate:
            return HttpResponse(json.dumps({"message": "Template Name already exists"}))
        else:
            temp = TemplateSerializer(data=request.data)
            # print(temp)
            if temp.is_valid():
                temp.save()
            Company_name = Template.objects.values('Company_Name').last()
            p = Company_name['Company_Name']
            connection = pymysql.connect(host="localhost", user="root", password="root", db='mapper6')
            sysCol2 = pd.read_sql('SELECT * FROM `file_app_template` where COMPANY_NAME="'+p+'"',connection)
            test=sysCol2.to_json(orient='records')
            # print(type(test))
            d = json.loads(test)
            # print("d",d)
            # print(type(d))
            # print(d)
            # print(test)
            ohh = Template.objects.values('on_off').last()
            o= ohh['on_off']
            # print(o)
            ok={"xyz":d}
            # print(ok)
            return HttpResponse(json.dumps({"ok":ok,"message": "Successfully Saved"}))
        # return HttpResponse(temp.data)
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.on_off = request.data.get("on_off")
    #     instance.save()
    #
    #     temp = self.get_serializer(instance)
    #     temp.is_valid(raise_exception=True)
    #     self.perform_update(temp)
    #
    #     return Response(temp.data)


class TemplateView(APIView):
    def get(self,request):
        Company_name = Detail.objects.values('COMPANY_NAME').last()
        f = Company_name['COMPANY_NAME']
        status=Detail.objects.values('STATUS').last()
        r=status['STATUS']
        connection = pymysql.connect(host="localhost", user="root", password="root", db='mapper6')
        sysCol = pd.read_sql("SELECT * FROM `file_app_detail` where Company_name='"+f+"' and status='"+r+"'",connection)
        bb= sysCol.to_json(orient='records')
        # print("bb",bb)
        kk= bb.replace("\\", '')
        d1= json.loads(kk)
        # Company_name = Template.objects.values('Company_Name').last()
        # p = Company_name['Company_Name']
        sysCol2 = pd.read_sql("SELECT * FROM `file_app_template` where Company_name='"+f+"' and status='"+r+"'",connection)
        test=sysCol2.to_json(orient='records')
        d2 = json.loads(test)
        bye={"sq":d1,"xyz":d2}
        return HttpResponse(json.dumps(bye))
# class Active_Status(APIView):
#     def post(self, request):
#         check = On_OffSerializer(data=request.data)
#         print(check)
#         if check.is_valid():
#             check.save()
#             print(check.data)
#         Company_name = Template.objects.values('Company_Name').last()
#         p = Company_name['Company_Name']
#         ohh = active.objects.values('on_off').last()
#         o= ohh['on_off']
#         print(o)
#         connection = pymysql.connect(host="localhost", user="root", password="root", db='mapper6')
#         sysCol2 = pd.read_sql('SELECT * FROM `file_app_template` where COMPANY_NAME="'+p+'"',connection)
#         test=sysCol2.to_json(orient='records')
#         print(test)
#         ok={"xyz":test,"Active_Status":o}
#         return HttpResponse(json.dumps(ok))
class IdchangerView(APIView):
    def post(self, request):
        see=request.data
        print(see)
        a=see['on_off']
        print('on_off:',a)
        z=see['id']
        print('id:',z)
        see2=Template.objects.filter(id=z).update(on_off=a)
        return Response(see2)

class SubmitView(APIView):
    def post(self, request):
        temp_n=request.data
        print(temp_n)
        # see4=Template.objects.values_list().get(Template_Name=temp_n1)
        # print("temp_name:",temp_n)
        # connection = pymysql.connect(host="localhost", user="root", password="root", db='mapper6')
        # sysCol3 = pd.read_sql('SELECT * FROM `file_app_template` where Template_Name="'+temp_n+'"',connection)
        # print("sysCol3",sysCol3)
        # test2=sysCol3.to_json(orient='records')
        # print(test2)
        # sheetName = Detail.objects.values('SHEET_NAME').last()
        # rowno = Detail.objects.values('ROW_NO').last()
        # fileData = File.objects.values('file').last()
        # f = fileData['file']
        # r = int(rowno['ROW_NO'])-1
        # s = sheetName['SHEET_NAME']
        # df = dynamicrule(f, s, r)
        # out=df.to_json(orient='records')
        # print(out)
        #
        # ok={"ok":"ok"}
        sheetName = Detail.objects.values('SHEET_NAME').last()
        s = sheetName['SHEET_NAME']
        rowno = Detail.objects.values('ROW_NO').last()
        r = int(rowno['ROW_NO']) - 1
        fileData = File.objects.values('file').last()
        f = fileData['file']
        filename_download = Path(f).stem
        print(filename_download)
        df = dynamicrule(f, s, r)
        if(type(df)!=str):
            genCSVPath = 'C:/Users/Admin/Desktop/file_upload/fileupload/generatedCSV/'+filename_download+'.csv'
            df.to_csv(genCSVPath)
            FilePointer = open(genCSVPath, "r")
            response = HttpResponse(FilePointer, content_type="application/octet-stream")
            filen=filename_download+'.csv'
            response['Content-Disposition'] = b'attachment; filename=%s' % filen.encode(encoding='utf-8')
            response['Cache-Control'] = 'no-cache'
            print(response)
            print("hello")
            return response
        else:
            dict1 = {"exception": df, "status": "UNSUCCESS"}
            print(dict1)
            return JsonResponse(dict1)

        # return HttpResponse(ok,status=status.HTTP_201_CREATED)

# class mitView(APIView):
#     def post(self, request):
#         temp_n1=request.data['Template_Name']
#         print(temp_n1)
#         see4=str(Template.objects.filter(Template_Name=temp_n1).values())
#         print(type(see4))
#         print(see4)
#         # y = json.loads(see4)
#         # print(y)
#         # ok={"swedfghok":"okasdf"}
#         return HttpResponse(ok,status=status.HTTP_201_CREATED)
