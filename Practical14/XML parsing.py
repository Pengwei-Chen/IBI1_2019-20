print('Processing...(it takes about 1 minute)')
import xml.dom.minidom as xdm
import pandas as pd

#define a function to find the number of childnotes
def numberofchildnodes(no):
    global terms
    count=0
    
    #get is_a
    for term in terms:
        is_a=term.getElementsByTagName('is_a')
        
        for parent in is_a:
            
            #if is_a parent
            if parent.childNodes[0].data==no:
                count+=1
                
                #count children of the child
                nextno=term.getElementsByTagName('id')[0].childNodes[0].data
                count+=numberofchildnodes(nextno)

    return count

#create lists
ID=[]
name=[]
defination=[]
childnodes=[]

#open xml file with minidom parser
domtree=xdm.parse('go_obo.xml')
ontology=domtree.documentElement

#get all terms
terms=ontology.getElementsByTagName('term')

#get all content in <defstr>
for term in terms:
    define=term.getElementsByTagName('def')[0]
    defstr=define.getElementsByTagName('defstr')[0].childNodes[0].data
    
    #if 'autophagosome' found
    if defstr.find('autophagosome')>-1 or defstr.find('Autophagosome')>-1:
        
        #get id, name and add them to lists with defstr
        no=term.getElementsByTagName('id')[0].childNodes[0].data
        ID.append(no)
        name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        defination.append(defstr)
        
        #get the number of childnotes
        childnodes.append(numberofchildnodes(no))

#output into an excel file
data={
      'id':ID,
      'name':name,
      'defination':defination,
      'childnodes':childnodes
}
dataframe=pd.DataFrame(data)
dataframe.to_excel(r'D:\autophagosome.xlsx')

print('Done!')















