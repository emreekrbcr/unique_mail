# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:51:38 2021

@author: Emre
"""

def find_line_counts(line_list):
    line_counts=dict()
    
    for line in line_list:
        if line != '': #boş satır varsa atlasın diye
            if line not in line_counts.keys():
                line_counts[line]=0
    
            line_counts[line]+=1
            
    return line_counts

def show_repetitive_lines(line_counts):
    all_unique=True
    
    for key in line_counts:
        if line_counts[key]>1:
            all_unique=False
            print(key, line_counts[key])
        
    if all_unique==True:
        print("There are no repetitive lines")

def read_txt_to_list(filename):
    f=open(filename,"r")
    
    lst=f.read().splitlines()
    f.close()
    
    return lst

def write_list_to_txt(lst,filename):
    f=open(filename,"w")
    
    for item in lst:
        f.write(item+'\n')
    
    f.close()

mails=read_txt_to_list("liste.txt")
mail_counts=find_line_counts(mails)
#show_repetitive_lines(mail_counts)

#find_line_counts() metodu zaten unique olarak her bir satırı bulur ve key olarak atar.
#birden çok tekrar eden key'lerin, value'sunu artırır
#dolayısıyla key'ler unique old. için listeye çevirmek yeterlidir

unique_mail_list=list(mail_counts.keys())
write_list_to_txt(unique_mail_list, "yeni_liste.txt")

#%% test
yeni_liste=read_txt_to_list("yeni_liste.txt")
counts=find_line_counts(yeni_liste)
show_repetitive_lines(counts)