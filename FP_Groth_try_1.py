"""
input

1sp2sp3spnl
34sp45sp1spnl

"""
#--------------------------------------------------------------------
import math
min_sup=0.2

#min_sup=0.04
min_conf=0.7
#---------------------------------input file processing------------
#inputFile=open('T10I4D100K.dat.txt','r')
inputFile=open('input.txt','r')
outputFile=open('output.txt','w')

data=inputFile.readlines()

print data[0]

sup_fre=int(math.ceil(len(data)*min_sup))


linear_list=data

L=[[] for i in range(1000)]
C=[[] for i in range(1000)]
data_fre=[]
data_pointer=[[] for i in range(1000)]
item_set=[]

data_array=[]
data_array_2=[]
max_item=-1
i=0

for line in data:
     
    data_array.append(line.replace('\n','-').split(' '))
    if '-' in data_array[i]:
        data_array[i].remove('-')
        flag=0
        arr=[]
    for val_str in data_array[i]:

        item=int(val_str)
        data_pointer[item].append(i)
        arr.append(item)
        if item>max_item:
            max_item=item
    data_array_2.append(arr)#content the data list
    i+=1

str1=str(data_array_2)
outputFile.write(str1)
print 'data_pointer = ',len(data_pointer)
print 'max_item = ',max_item

data_fre=[len(data_pointer[i]) for i in range(max_item+1)]

fre_ind_list=[(data_fre[i],i) for i in range(len(data_fre))]
#print fre_ind_list

sorted_fre_ind_list=[(f,i) for (f,i) in sorted(fre_ind_list)]# return the sorted index list according to frequency value(assending order)
#print 'sort =',sorted_fre_ind_list
sorted_fre_ind_list.reverse()#assending order----->decending order
#print 'rev =',sorted_fre_ind_list


print 'sup_fre = ',sup_fre
for i in range(len(sorted_fre_ind_list)):
    if sorted_fre_ind_list[i][0]<sup_fre:
        del sorted_fre_ind_list[i:]
        break

print 'after del =',sorted_fre_ind_list

sorted_item_list=[y for (x,y) in sorted_fre_ind_list]

#-----------change sequence of sorted item list-------------not necessary------------

ss_len=len(sorted_item_list)-1
j=0
while j<ss_len: 

    a=sorted_item_list[j]
    b=sorted_item_list[j+1]
    if data_fre[a]==data_fre[b] and a > b :
        sorted_item_list[j],sorted_item_list[j+1]=sorted_item_list[j+1],sorted_item_list[j]
    j+=1
#------------------------------------------------------------------------------------------      
    
    

#print 'item_list = ',sorted_item_list

#-------------
print 'ok 1'
sorted_database_list=[]
for line in data_array_2:
    sorted_array=[]
    for item in sorted_item_list:
        if item in line:
            sorted_array.append(item)
    if len(sorted_array):
        sorted_database_list.append(sorted_array)
#print sorted_database_list

print 'len accepted itemset = ',len(sorted_database_list)
print 'ok end'
str1='\n'
str1+=str(sorted_database_list)
str1+='\n'
outputFile.write(str1)           

#--------------------create FP_tree---------------------

root=[-1,0,[],-1]
def insert(itemset,node):
    print 'insert call --------',itemset
    if len(itemset)==0:
        return
    print len(itemset)
    first_item=itemset.pop(0)
    print 'first_item = ',first_item
    print 'itemset after pop = ',itemset
    print 'node 0 = ',node[0]
    
    if node[0]==first_item:
        print 'Match so go to child'
        node[1]+=1
        if len(itemset)!=0:
            node_childs_len=len(node[2])
            if node_childs_len==0:
                print 'No child .Create and Insert as child'
                i=[itemset[0],0,[],node]
                node[2].append(i)
                insert(itemset,i)
                print 'ok'
            
            else:
                print 'Had child.Check child'
                flag=0
                child_list=node[2]
                for child in child_list:
                    print 'Check if any child value match'
                    if itemset[0]==child[0]:
                        print 'In child match found'
                        insert(itemset,child)
                        flag=1
                        break
                    
                if flag==0:
                    print 'No match found in child'
                    i=[itemset[0],0,[],node]
                    node[2].append(i)
                    insert(itemset,i)
                    
                    
                        
        else:
            print 'Itemset has no item to go deep.'
        return
    
        
    
def create_fp_tree(sorted_database_list):
    for itemset in sorted_database_list:
        if len(itemset)!=0:
            itemset1=[-1]
            itemset1+=itemset
            insert(itemset1,root)

'''
b=[[1, 2, 5],[2, 4],[2, 3],[1, 2, 4],[1, 3],[2, 3],[1, 3],[1, 2, 3, 5],[1, 2, 3]] 
b=[[1, 2, 5],[2, 4],[2, 3],[1, 2, 4],[1, 3],[2, 3],[1, 3],[1, 2, 3, 5],[1, 2, 3]]
a=[[1,2,4,5],[1,2,3]]

book_db=[[2, 1, 5], [2, 4], [2, 3], [2, 1, 4], [1, 3], [2, 3], [1, 3], [2, 1, 3, 5], [2, 1, 3]]
'''
create_fp_tree(sorted_database_list)
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(root)
#print str(root)



        
#---------------------------------------------------
inputFile.close()
outputFile.close()




