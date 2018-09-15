import webrequest
import treetaggerwrapper
from copy import deepcopy
import math
import sys

#tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
#tags = tagger.tag_text("Welches ist keine eiszeitliche geologische Periode?")
#tags2 = treetaggerwrapper.make_tags(tags)
#pprint.pprint(tags2)

TAG_WHITELIST = ['NN', 'NE', 'ADJA', 'CARD', 'VVFIN']
NEGOTIATIONS = ('NEIN', 'NICHT', 'KEIN')

def search_ranking(q_str, a1_str, a2_str, a3_str, nr_str):

    tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')

    tag_list = [] # 1: Frage; 2,3,4: Antworten
    #TreeTagger
    for i in (q_str, a1_str, a2_str, a3_str):
        i = i.replace('-', ' ')
        
        tags = tagger.tag_text(i)
        tag_line = []
        for j in tags:
            tag_line += [[x for x in j.split('\t')]]
        tag_list.append(tag_line)
    
    #Wörter die kleiner 3 Zeichen sind wegschmeißen
    tag_list = clear_mini_tags(tag_list)

    #Whitelist filter
    tag_list = whitlist_filter(tag_list)

    #Such String für Google + Suche
    query = ''
    for i in tag_list[0]:
        if i == tag_list[0][-1]:
            query += i[0] #letzter Eintrag ohne +
        else:
            query += i[0] + ' + '
    
    search_string = webrequest.google_search(q_str, nr_str).upper()
    #with open(r'C:\Users\Gottkönig\Desktop\cashshow\hist\300818_9\4.txt', 'r') as inputfile:
    #    search_string = inputfile.read().upper()

    #Antworten in Request suchen(Original String)
    tag_list = search_answer(tag_list, search_string, False)

    #Prüfen ob Suche erfolgreich, wenn nicht neu suchen mit halbierten Antwort String
    ant_cnt = 0
    for antwort in tag_list:
        if antwort == tag_list[0]: #ersten Eintrag überspringen(Frage)
            continue
        if antwort[-1] > 0:
            ant_cnt = antwort[-1]
    
    #oder wenn zwei antworten gleich sind 
    if ant_cnt == 0:
        tag_list = search_answer(tag_list, search_string, True)
    
    #Negierung beachten
    negotiate_flag = False
    for neg in NEGOTIATIONS:
        q_str_up = q_str.upper()
        if q_str_up.find(neg) >= 0:
            negotiate_flag = True
            break

    if negotiate_flag == False:
        if tag_list[1][-1] > tag_list[2][-1] and tag_list[1][-1] > tag_list[3][-1]:
            ans_a = 'A'
        elif tag_list[2][-1] > tag_list[1][-1] and tag_list[2][-1] > tag_list[3][-1]:
            ans_a = 'B'
        elif tag_list[3][-1] > tag_list[1][-1] and tag_list[3][-1] > tag_list[2][-1]:
            ans_a = 'C'
        else:
            ans_a = ''
    else:
        if tag_list[1][-1] < tag_list[2][-1] and tag_list[1][-1] < tag_list[3][-1]:
            ans_a = 'A'
        elif tag_list[2][-1] < tag_list[1][-1] and tag_list[2][-1] < tag_list[3][-1]:
            ans_a = 'B'
        elif tag_list[3][-1] < tag_list[1][-1] and tag_list[3][-1] < tag_list[2][-1]:
            ans_a = 'C'
        else:
            ans_a = ''

    answer_tuples = [('A', a1_str),
                     ('B', a2_str),
                     ('C', a3_str),]
    #print(tag_list)
    return answer_tuples, ans_a

def clear_mini_tags(liste):
    temp_liste = []
    for eintrag in liste:
        temp_liste += [[i for i in eintrag if len(i[0]) >= 3]]
    return temp_liste

def whitlist_filter(liste):
    '''Antworten bereinigen ... nur Wörter aus TAG_WHITELIST(NN, NE, ...)'''
    temp_liste = []
    for eintrag in liste:
        temp_liste += [[i for i in eintrag if i[1] in TAG_WHITELIST]]
    return temp_liste

def search_answer(liste, search_str, flag_short):
    temp_liste = deepcopy(liste)

    if flag_short == True: #bereits bestehende Zahlen löschen
        for antwort in temp_liste:
            if antwort == temp_liste[0]: 
                continue
            del antwort[-1]
        
        for antwort in temp_liste:
            if antwort == temp_liste[0]: 
                continue
            for wort in antwort:
                del wort[-1]

    for antwort in temp_liste:
        if antwort == temp_liste[0]: #ersten Eintrag überspringen(Frage)
            continue

        for wort in antwort:
            wort_str = wort[0].upper()
            if flag_short == True:
                laenge = math.floor(len(wort_str) / 2)
                if laenge > 5:
                    wort_str = wort_str[:-laenge] 
  
            cnt = search_str.count(wort_str)
            wort.append(cnt)

    for antwort in temp_liste:
        if antwort == temp_liste[0]: #ersten Eintrag überspringen(Frage)
            continue

        cnt = 0
        for wort in antwort:
            if type(wort[0]) == int:
                del wort
            cnt += wort[3]

        antwort.append(cnt)
    return temp_liste

def search_ranking_old(search_string, a1_str, a2_str, a3_str):

    search_string = search_string.upper()
    a1_str = a1_str.upper()
    a2_str = a2_str.upper()
    a3_str = a3_str.upper()

    cnt_a1 = search_string.count(a1_str)
    cnt_a2 = search_string.count(a2_str)
    cnt_a3 = search_string.count(a3_str)
    
    if cnt_a1 > cnt_a2 and cnt_a1 > cnt_a3:
        ans_a = 'A'
    elif cnt_a2 > cnt_a1 and cnt_a2 > cnt_a3:
        ans_a = 'B'
    elif cnt_a3 > cnt_a1 and cnt_a3 > cnt_a2:
        ans_a = 'C'
    else:
        ans_a = ''

    answer_tuples = [('A', a1_str, cnt_a1),
                     ('B', a2_str, cnt_a2),
                     ('C', a3_str, cnt_a3),]

    return cnt_a1, cnt_a2, cnt_a3, ans_a, answer_tuples


if __name__ == "__main__":
    pass