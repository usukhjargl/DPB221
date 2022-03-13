#!/usr/bin/env python
# coding: utf-8

# In[19]:


np.arange(50,100)


# In[8]:


np.zeros(10)


# In[9]:


np.ones(10)


# In[24]:


np.ones(10)*6


# In[15]:


arr= np.array([[20.,21.,22.,23.],[24.,25.,26.,27.],[28.,29.,30.,31.]])
arr


# In[18]:


import numpy as np
m=np.arange(20,32).reshape((3,4))
print(m)


# In[36]:


import numpy as np
m=np.zeros(9).reshape((3,3))
np.fill_diagonal(m,(1))
print(m)


# In[25]:


import numpy as np
m=np.zeros(25).reshape((5,5))
np.fill_diagonal(m,(1,2,3,4,5))
print(m)


# In[50]:


import numpy as np
num=np.arange(4)
arr1=np.reshape(num,(2,2))
print('Original array:')
print(arr1)
result=arr1.sum(axis=0)
print("\nSum of all columns:")
print(result)


# In[1]:


import numpy as np
num=np.arange(100)
arr1=np.reshape(num,(10,10))
print('Original array:')
print(arr1)
result=arr1.sum(axis=0)
print("\nSum of all columns:")
print(result)


# In[2]:


import numpy as np
#Seasons
Seasons = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
Sdict = {'2012':0,"2013":1,'2014':2,"2015":3,"2016":4,"2017":5,"2018":6,"2019":7,"2020":8,'2021':9}
#Players
Players = ['LebronJames','JamesHarden','JohnWall','StephenCurry','GiannisAntetokounmpo','KevinDurant','PaulGeorge','ChrisPaul','LaMarcusAldridge','DeMarcusCousins']
Pdict = {"LebronJames":0,"JamesHarden":1,"JohnWall":2,"StephenCurry":3,"GiannisAntetokounmpo":4,"KevinDurant":5,'PaulGeorge':6,'ChrisPaul':7,'LaMarcusAldridge':8,'DeMarcusCousins':9}
#Salaries
LebronJames_salaries=[17545000,19067500,20644400,22970500,30963450,33285709,35654150,37436858,39219566,41180544]
JamesHarden_salaries=[5820416,13668750,14693906,15719062,26540100,28299399,30570000,38199000,41254920,44310840]
JohnWall_salaries=[5915880,7459924,13701250,14728844,15756438,18063850,19169800,38199000,41254920,44310840]
StephenCurry_salaries=[3958742,9887642,10629213,11370786,12112359,34682550,37457154,40231758,43006362,45780966]
GiannisAntetokounmpo_salaries=[0,1792560,1873200,1953960,2995420,22471911,24157304,25842697,27528088,39344900]
KevinDurant_salaries=[17548838,18773176,19997513,21971850,26540100,25000000,30000000,37199000,40108950,42018900]
PaulGeorge_salaries=[2574120,3282003,15800000,16900000,18100000,19300000,30560700,33005556,35450412,39344970]
ChrisPaul_salaries=[17779457,18668431,20068563,21468695,22868827,24268959,35654150,38506482,41358814,30800000]
LaMarcusAldridge_salaries=[13000000,14100000,15200000,19689000,20575005,21461010,22347015,26000000,17628340,2641619]
DeMarcusCousins_salaries=[3880800,4916973,13701250,14728844,15756438,18063850,5337000,3500000,3051832,683196]
Salaries=np.array([LebronJames_salaries,JamesHarden_salaries,JohnWall_salaries,StephenCurry_salaries,GiannisAntetokounmpo_salaries,KevinDurant_salaries,PaulGeorge_salaries,ChrisPaul_salaries,LaMarcusAldridge_salaries,DeMarcusCousins_salaries])
#Points
LebronJames_points=[2036,2089,1743,1920,1954,2251,1505,1698,1126,1376]
JamesHarden_points=[2023,1851,2217,2376,2356,2191,2818,2335,1083,1113]
JohnWall_points=[906,1583,1387,1531,1805,797,663,0,823,0]
StephenCurry_points=[1786,1873,1900,2375,1999,1346,1881,104,2015,1538]
GiannisAntetokounmpo_points=[0,525,1030,1350,1832,2014,1994,1857,1717,1661]
KevinDurant_points=[2280,2593,686,2029,1555,1792,2027,0,943,1135]
PaulGeorge_points=[1377,1737,53,1874,1775,1734,2159,1033,1259,641]
ChrisPaul_points=[1186,1185,1564,1446,1104,1081,906,1232,1149,866]
LaMarcusAldridge_points=[1560,1603,1661,1331,1243,1735,1727,1001,352,607]
DeMarcusCousins_points=[1280,1614,1421,1748,1942,1210,488,366,287,289]
Points=np.array([LebronJames_points, JamesHarden_points, JohnWall_points, StephenCurry_points, GiannisAntetokounmpo_points, KevinDurant_points, PaulGeorge_points, ChrisPaul_points, LaMarcusAldridge_points, DeMarcusCousins_points])
#Games_played
LebronJames_games=[76,77,69,76,74,82,55,67,45,47]
JamesHarden_games=[78,73,81,82,81,72,78,68,44,49]
JohnWall_games=[ 49,82,79,77,78,41,32,0,40,0]
StephenCurry_games=[78,78,80,79,79,51,69,5,63,60]
GiannisAntetokounmpo_games=[0,77,81,80,80,75,72,63,61,56]
KevinDurant_games=[ 81,81,27,72,62,68,78,0,35,39]
PaulGeorge_games=[79,80,6,81,75,79,77,48,54,26]
ChrisPaul_games=[ 70,62,82,74,61,58,58,70,70,58]
LaMarcusAldridge_games=[74,69,71,74,72,75,81,53,26,45]
DeMarcusCousins_games=[75,71,59,65,72,48,30,0,41,32]
games_played=np.array([LebronJames_games,JamesHarden_games,JohnWall_games,StephenCurry_games,GiannisAntetokounmpo_games,KevinDurant_games,PaulGeorge_games,ChrisPaul_games,LaMarcusAldridge_games,DeMarcusCousins_games])
# In[11]:
# Мөрөөр нэмсэн нь
print('10 тоглогчдийн 2012-2013 оноос 2021-2022 хүртэл улирлын нийт авсан цалин', Salaries.sum(axis=1))
print('10 тоглогчдийн 2012-2013 оноос 2021-2022 хүртэл улирлын нийт авсан оноо',Points.sum(axis=1))
print('10 тоглогчдийн 2012-2013 оноос 2021-2022 хүртэл улирлын нийт тоглосон тоо. Жич: Зөвхөн улирлын тоглолтуудад',games_played.sum(axis=1))
# In[12]:
# Баганаар нэмсэн нь
print('10 тоглогчдийн бүгдээрээ 2012-2013 оноос 2021-2022 хүртэл улирал тус бүр авсан цалин', Salaries.sum(axis=0))
print('10 тоглогчдийн бүгдээрээ 2012-2013 оноос 2021-2022 хүртэл улирал тус бүр авсан оноо',Points.sum(axis=0))
print('10 тоглогчдийн бүгдээрээ 2012-2013 оноос 2021-2022 хүртэл улирал тус бүр тоглосон тоо. Жич: Зөвхөн улирлын тоглолтуудад',games_played.sum(axis=0))
# In[16]:
# 10 тоглогч тус бүрийн хамгийн бага үзүүлэлтүүд
print(Points.min(axis=1))
print(Salaries.min(axis=1))
print(games_played.min(axis=1))
# In[18]:
print('DONE')


# In[ ]:




