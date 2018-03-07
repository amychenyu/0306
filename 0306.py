
# coding: utf-8

# In[6]:

x=1
y=3
a=5
t=x+y+a
t+=6
t


# In[85]:

poem='''\"abcdefg\",\"hijklmnopq\",\"rstuvwxyz\"'''
print(poem.replace('a','b'))
print(poem)
print(poem[0]+"b"+poem[2:])
print("b"+poem[2:])



# In[92]:

print(poem.split(','))


# In[97]:

poem1='''abcdefg\nhijklmnopq\nrstuvwxyz'''
print(poem1)
print(poem1.split('\n'))


# In[101]:

poem2 =['a b c d e f g', 'hijknopq', 'rstuvwxyz']
s='~'
s.join(poem2)


# In[102]:

s.join(poem2).replace('~','')


# In[103]:

s.join(poem2).replace('~','').replace(' ','')


# In[120]:

s1="GitHub通常用於軟體開發。GitHub還支援以下格式和功能文件：\n包括自動生成的、採用類Markdown語言的README檔案。\n問題追蹤系統（同時可用於功能需求GitHub Pages支援用戶透過軟體倉庫建立靜態網站或靜態部落格（透過一個名為Jekyll的軟體實現）。\n任務列表\n甘特圖\n視覺化的地理位置分析\n預覽3D彩現檔案。[9]預覽功能透過WebGL和Three.js實現。\n預覽Photoshop的PSD檔案，甚至可以比較同一檔案的不同版本。"
s1.startswith('您')
s1.startswith('G')
s1.endswith('_')
s1.find("Git")
s1.rfind("Git")
s1.count("Git")


# In[130]:

import requests
response = requests.get("http://khnovel.com/outlander/page-1-10006352.html")
response.encoding = "BIG5"
novel1 = response.text
novel1
#novel1.count("Jack")


# In[ ]:



