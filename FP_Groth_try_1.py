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

sorted_item_list=[ind for (fre,ind) in sorted_fre_ind_list]

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

#----------------------------sort itemset accroding to support frequency--------
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
#----------------------------printed sorted db of itemset-----------------
print 'len accepted itemset = ',len(sorted_database_list)
print 'ok end'
str1='\n'
str1+=str(sorted_database_list)
str1+='\n'
outputFile.write(str1)           

#--------------------create FP_tree---------------------

header_table=[[] for i in range(max_item+1)]
root=[-1,0,[],-1]
def insert(itemset,node):
    print '1 insert call --------',itemset
    if len(itemset)==0:
        print 'Itemset is empty----->'
        return
    print len(itemset)
    first_item=itemset.pop(0)
    print '2 first_item = ',first_item
    print '3 itemset after pop = ',itemset
    print '4 node 0 = ',node[0]
    
    if node[0]==first_item:
        print '5 Match so go to child'
        node[1]+=1
        if len(itemset)!=0:
            node_childs_len=len(node[2])
            if node_childs_len==0:
                print '6 Current node has no child .Create and Insert as child'
                i=[itemset[0],0,[],node]
                print '7 Child created =  ',i,' and inserted in node with val =',node[0]
                
                #-------------maintain header table----------------
                header_table[itemset[0]].append(i)
                #--------------------------------------------------
                    
                node[2].append(i)
                insert(itemset,i)
                
            
            else:
                print '8 Current Node has child.Check child for match'
                flag=0
                child_list=node[2]
                for child in child_list:
                    print '9 Check if any child value match'
                    if itemset[0]==child[0]:
                        print '10 In child match found with = ',child[0],' go to that child .'
                        insert(itemset,child)
                        flag=1
                        break
                    
                if flag==0:
                    print '11 No match found in child so create a new node and insert it as child.'
                    i=[itemset[0],0,[],node]
                    print '12 child created = ',i
                #-------------maintain header table----------------
                    
                    header_table[itemset[0]].append(i)
                #--------------------------------------------------
                    node[2].append(i)
                    insert(itemset,i)
                    
                    
                        
        else:
            print '13 Itemset has no item to go deep.'
            #header_table[first_item].append()
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
#---------------- create fp tree---------------------------------
create_fp_tree(sorted_database_list)
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(root)
#print str(root)

h_t=[(i,len(header_table[i])) for i in range(len(header_table))]
print 'header_table = ',h_t

#------------------sort item in small to large frequency-----------
print sorted_item_list
sorted_item_rev=[x for x in sorted_item_list]
sorted_item_rev.reverse()
print sorted_item_rev
#--------------------------------------------------------------------

#---------------separate each item path from FP_TRee------------------

item_paths=[[] for i in range(max_item+1)]#--------------will contain all the items path-------------
for item in sorted_item_rev:
    pointer_item_arr=header_table[item]
    for p_item in pointer_item_arr:
        #p_item=[val,fre,[],parent]
            
        arr=[]
        pp=p_item
        while pp[0]!=-1:
            arr.append((pp[0],pp[1]))#(item,fre)
            pp=pp[3]
        item_paths[item].append(arr)#[(item4,fre4),(item3,fre3),(item2,fre2),(item1,fre1)] path = item4 <-- item3 <-- item2 <-- item1
        
print item_paths[5]

#----------------print all paths-------------------------------------

print '----------all parh-----------'
i=0
for path_arr in item_paths:
    print 'item = ',i
    
    j=0
    for path in path_arr:
        
        j+=1
        if len(path):
            pp=[x for (x,y) in path]
            pp.reverse()
            print pp
    i+=1

#--------------------------------------------------------------------



    
    


for item in sorted_item_list:

    print item
    print 'before rev = ',item_paths[item]
    paths=item_paths[item]
    for path in paths:
        for i in range(len(path)):
            path[i]=(path[i][0],path[0][1])
        path.reverse()
        path.pop()#---------------------removing the last item from item path-----------

    
    #find_all_frequent_patterns(paths[i])
    print 'after rev = ',paths
    

    
        
    




        
#---------------------------------------------------
inputFile.close()
outputFile.close()




