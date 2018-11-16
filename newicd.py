# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:57:54 2018

@author: Parisa Sarikhani
"""

import pandas as pd
import sys

#file=pd.('2018_I9gem.txt',sep=' ')


def onthology2(path1,path2):
    # 1-many mappings from ICD10 to 9:
    #path1='./2018_I10gem.txt'
    df = pd.read_fwf(path1, sep=' ', header=None,names= ['icd10','icd9','flags'],converters= {0: str, 1:str, 2:str})
    icd10_df = pd.DataFrame(df) 
    #icd10_df=icd10_df.drop('flags',axis=1)
    #1-many mappings are those repeated more than once on the first column(icd)
    grouped=icd10_df.groupby('icd10')
    one_to_many=grouped.filter(lambda x: len(x) > 1)
    print('total number of 1-many mappings= '+str(len(one_to_many)))
    
    no_map_count=0
    for flag in icd10_df['flags']:
        # no mappings happen when we have second flag(no map)=1
        if int(flag[1])==1:
            no_map_count+=1
    print('total number of no mappings= '+str(no_map_count))
    
    one_to_one=grouped.filter(lambda x: len(x) == 1)
    print('total number of 1-1 mappings= ' + str(len(one_to_one)-no_map_count))
     
     
    #----------Read the California state ICD9 diagnosis files:
    # I have converted the original file into two plain text files:
    #path2='C:/Users/paris/Downloads/Q1-Q3-ICD-9-CM.txt'
    df2 = pd.read_csv(path2, sep='\t' , header=None, converters= {0: str, 1:str})
    cal_icd9 = pd.DataFrame(df2) 
    cal_icd9.drop(cal_icd9.columns[2:], axis=1,inplace=True)
    #df3 = pd.read_csv('C:/Users/paris/Downloads/Q4-ICD-10-CM.txt', sep='\t' , header=None, converters= {0: str, 1:str})
    #cal_icd10= pd.DataFrame(df3) 
    #ICD10CMCode=cal_icd10.iloc[1:-1][0]#ICD10CMCode
    #TotalDiag10=cal_icd10.iloc[1:-1][1]#TotalDiag of california icd10
    #-----number of each icd10 codes in '2018_I10gem.txt' file:
    counter_icd10codes=icd10_df.groupby('icd10').size().reset_index(name ='#')
    Counts=counter_icd10codes[counter_icd10codes['#']>1]
                                                 
    DFrame = pd.merge(icd10_df,Counts, on='icd10')
    
    
    
    cal_icd9_edited=[0]*len(cal_icd9)
    for j in range(len(cal_icd9)-2):
        
        cal_icd9_edited[j+1]=cal_icd9[1:-1][0][j+1]
        
     
        
    text_file = open("Output.txt", "w")
    maxfreq=0
    INDEX=0
    cc=0
    
    for index, row in DFrame.iterrows():
        
        current_counter=row['#']
        row['icd9']=row['icd9'][0:3]+'.'+row['icd9'][3:]
        #print(row['icd9'])
      
        if cc==0:
            cc+=1
            prev_code=DFrame['icd10'][cc-1]
            index=cal_icd9_edited.index(row['icd9'])
            coun=cal_icd9_edited.count(row['icd9'])
            for h in range(coun):
                if int(cal_icd9[1:-1][1][index+h])>maxfreq:
                    maxfreq=int(cal_icd9[1:-1][1][index+h])
                    INDEX=h+index
                    
        elif cc!=0 and row['icd10']== prev_code:
            prev_code=DFrame['icd10'][cc]
            cc+=1
        
            if row['icd9'][1:] in cal_icd9_edited[:-2]:
                index=cal_icd9_edited.index(row['icd9'])
                coun=cal_icd9_edited.count(row['icd9'])
                for h in range(coun):
                    if int(cal_icd9[1:-1][1][index+h])>maxfreq:
                        maxfreq=int(cal_icd9[1:-1][1][index+h])
                        INDEX=h+index
    
                      
        elif cc!=1 and row['icd10']!= prev_code:#+str(cal_icd9_edited[INDEX])
            prev_code=DFrame['icd10'][cc]
            if maxfreq!=0:
                text_file.write(DFrame['icd10'][cc-1]+'\t'+str(cal_icd9_edited[INDEX])+'\t'+str(maxfreq)+'\n')
            cc+=1
            maxfreq=0
            #INDEX=0  
            if row['icd9'] in cal_icd9_edited[:-2]:
                index=cal_icd9_edited.index(row['icd9'])
                coun=cal_icd9_edited.count(row['icd9'])
                for h in range(coun):
                    if int(cal_icd9[1:-1][1][index+h])>maxfreq:
                        maxfreq=int(cal_icd9[1:-1][1][index+h])
                        INDEX=h+index
                             #print(INDEX)
        
    
    
    text_file.close()
                                   
    
if __name__== "__main__":
    
    onthology2(sys.argv[1],sys.argv[2])                                   
