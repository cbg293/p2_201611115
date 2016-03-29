
# coding: utf-8

# In[1]:

import os
mywd = get_ipython().magic(u'pwd')
myplantdir=os.path.join(mywd,'lib')
mydot="C:\\Program Files (x86)\\Graphviz 2.28\\bin\\dot.exe"


# In[2]:

import glob
get_ipython().magic(u'cd {myplantdir}')
glob.glob(r'./*.jar')


# In[3]:

import os
os.environ['GRAPHVIZ_DOT']=mydot
print os.environ['GRAPHVIZ_DOT']
get_ipython().system(u'java -jar {myplantdir}/plantuml.jar -testdot')


# In[6]:

get_ipython().magic(u'install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py')


# In[7]:

get_ipython().magic(u'load_ext plantuml_magics')


# In[8]:

get_ipython().run_cell_magic(u'plantuml', u'', u'@startuml\nstart\n:set how many turns;\n:set how much to grow bigger;\n:set angle;\n:set start size;\nrepeat\nif (i is divided by 2) then\n    :grow bigger;\nendif\n:draw;\nrepeat while(turns)\nstop\n@enduml')

