import nltk
import string
from text2digits import text2digits

d = {"dollars": "$", "dollar": "$"}

t = {"single": 1, "double": 2, "triple": 3}

def process(text):
    t = nltk.word_tokenize(text)
    t = text_to_digits(t)
    t = currency_signs(t)
    t = abbrevations(t)
    t = some_name(t)
    t = punct_inplace(t)
    return(t)

def text_to_digits(text_list):
    text = " ".join(text_list)
    t2d = text2digits.Text2Digits()
    text = t2d.convert(text)
        
    return(nltk.word_tokenize(text))

def rem_elems(text_list, r):
    for i in range(len(r)):
        text_list.pop(r[i] - i)

    return (text_list)
    

def abbrevations(text_list):
    l = len(text_list)
    i = 0
    r = []
    while i < l:
        p = text_list[i]
        k = i
        if len(p)==1 and p.isalpha():
            while i+1 < l and len(text_list[i+1]) == 1 and text_list[i+1].isalpha():
                i+=1
                text_list[k] += text_list[i]
                r.append(i)
            
            if text_list[k] != 'a':
                text_list[k] = text_list[k].upper()
                
        i+=1        

        
    text_list = rem_elems(text_list, r)

    return (text_list)
                
def some_name(text_list):
    r = []
    for i in range(len(text_list)-1):
        p = t.get(text_list[i], None)
        if p!= None and (text_list[i+1].isupper() or text_list[i+1] == 'a'):
            text_list[i] = (text_list[i+1].upper())*p
            r.append(i+1)
    
    text_list = rem_elems(text_list, r)

    return (text_list)
            


def punct_inplace(text_list):
    
    r = []
    for i in range(1, len(text_list)):
        p = text_list[i]
        if len(p) == 1:
            if p in string.punctuation:
                text_list[i-1] = text_list[i-1] + p
                r.append(i)
                
    text_list = rem_elems(text_list, r)

    return (text_list)
                

def currency_signs(text_list):
    r = []
    for i in range(len(text_list)-1):
        p = text_list[i]
        if is_int(p):
            k = d.get(text_list[i+1], None)
            if k != None:
                text_list[i] = k + p
                r.append(i+1)
                
    text_list = rem_elems(text_list, r)
        
    return(text_list) 

def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

    
    
