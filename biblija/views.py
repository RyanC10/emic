from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from biblija.forms import FormaTEXT, FormaMAJA
import pandas as pd
import json
from pandas import ExcelWriter

def hep(request):   
    return render(request, 'hep.html')

class majaforma(TemplateView):
    
    
    template_name='maja.html'

    def get(self,request):
        form = FormaMAJA()         
        
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        tekstjson = request.POST.get('tekst')
        potpis = request.POST.get('potpis')
        print(potpis)


        print(tekstjson)
        print(type(tekstjson))
        # Converting string to list
        res = json.loads(tekstjson)
        print(res)
        df = pd.DataFrame(res)
        print(df)
        df['pregledao']=potpis
        df_za_download = df.to_json()
        request.session['za_download'] = df_za_download

        df=df.to_html

        args= {'tekstjson':tekstjson,
               'df':df}
       
    
        return render(request, "rezultatmaja.html",args)
    

def ispismaja(request):
    izvor = request.session.get('za_download')
   
    #print(type(izvor))
    df_1=json.loads(izvor)
    #print(type(df_1))
    #print(df_1)
    df_1=pd.DataFrame.from_dict(df_1)
    doktor=df_1.iloc[0][10]
        
    from django.http import HttpResponse    
    from io import BytesIO as IO 
    excel_file = IO()
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    df_1.to_excel(writer, sheet_name='anketa', index=False)
    workbook  = writer.book
    worksheet = writer.sheets['anketa']

  
    formatB = workbook.add_format({'align': 'center'})
    worksheet.set_column('A:K', 20, formatB)


        
    worksheet.add_table('A1:K60', {'header_row': 0})
 

    
    writer.save()
    writer.close()
    excel_file.seek(0)
    response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename='+str(doktor)+'_ispis.xlsx'
    
    return response  


def maja(request):
    
                
 
       
    args = {}      
   
    return render(request, 'maja.html',args)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def netocno(request):
    return HttpResponse("Sorry prika, knjigu u ruke")



class pocetna(TemplateView):
    
    
    template_name='pocetna.html'

    def get(self,request):
        form = FormaTEXT()
        #print(dp)
    
        
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        print("pokrenuta aplikacija")
        mjerenje_1 = request.POST.get('mjerenje_1')
        mjerenje_2 = request.POST.get('mjerenje_2')
        mjerenje_3 = request.POST.get('mjerenje_3')
        mjerenje_4 = request.POST.get('mjerenje_4')
        mjerenje_5 = request.POST.get('mjerenje_5')
        mjerenje_6 = request.POST.get('mjerenje_6')
        mjerenje_7 = request.POST.get('mjerenje_7')
        mjerenje_8 = request.POST.get('mjerenje_8')
        mjerenje_9 = request.POST.get('mjerenje_9')
        mjerenje_11 = request.POST.get('mjerenje_11')
        mjerenje_12 = request.POST.get('mjerenje_12')
        mjerenje_13 = request.POST.get('mjerenje_13')
        mjerenje_14 = request.POST.get('mjerenje_14')
        mjerenje_15 = request.POST.get('mjerenje_15')
        mjerenje_16 = request.POST.get('mjerenje_16')
        mjerenje_17 = request.POST.get('mjerenje_17')
        mjerenje_18 = request.POST.get('mjerenje_18')
        mjerenje_19 = request.POST.get('mjerenje_19')
        mjerenje_20 = request.POST.get('mjerenje_20')
        mjerenje_21 = request.POST.get('mjerenje_21')
        mjerenje_22 = request.POST.get('mjerenje_22')
        mjerenje_23 = request.POST.get('mjerenje_23')
        mjerenje_24 = request.POST.get('mjerenje_24')
        mjerenje_25 = request.POST.get('mjerenje_25')
        mjerenje_26 = request.POST.get('mjerenje_26')
        mjerenje_27 = request.POST.get('mjerenje_27')
        mjerenje_28 = request.POST.get('mjerenje_28')
        mjerenje_29 = request.POST.get('mjerenje_29')
 
        odgovori=[mjerenje_1,mjerenje_2,mjerenje_3,mjerenje_4,mjerenje_5,
                  mjerenje_6,mjerenje_7,mjerenje_8,mjerenje_9,mjerenje_11,
                  mjerenje_12,mjerenje_13,mjerenje_14,mjerenje_15,mjerenje_16,
                  mjerenje_17,mjerenje_18,mjerenje_19,mjerenje_20,mjerenje_21,
                  mjerenje_22,mjerenje_23,mjerenje_24,mjerenje_25,mjerenje_26,
                  mjerenje_27,mjerenje_28,mjerenje_29]
        odgovori = [x.replace(' ', '') for x in odgovori]
        odgovori = [x.lower() for x in odgovori]
        #print(odgovori)
        tocni_odgovori=['set','metuzalem','henok','40','duga','noa','ur','melkisedek','175','ezav','13','benjamin','josip',
                        'job','mojsije','horeb','leviti','aron','40','jošua','jerihon','dalila','david','batšeba','salomon','ilija','jeremija','izajia']
        
        s = set(tocni_odgovori)
        krivi_odgovori = [x for x in odgovori if x not in s]
        #print(krivi_odgovori)

        form = FormaTEXT()
      
        if len(krivi_odgovori)>0 :
            tocno="netocno"
        else:
            tocno="tocno_1"

        #print(tocno)
        args= {'krivi_odgovori':krivi_odgovori,}
       
    
        return render(request, str(tocno)+".html",args)



def e02(request):
    
                
 
       
    args = {}      
   
    return render(request, 'e02.html',args)


def kraj(request,radnom):
    print(radnom)
                    

    return render(request, 'kraj.html',)

def ispis(request):
    data = {
      "calories": [420, 380, 390],
      "duration": [50, 40, 45]
    }

    
    df = pd.DataFrame(data)

        
    from django.http import HttpResponse    
    from io import BytesIO as IO 
    excel_file = IO()
    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='izracun', index=False)


    
    writer.save()
    writer.close()
    excel_file.seek(0)
    response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=AAnfo_A.xlsx'
    
    return response  

