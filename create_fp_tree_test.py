
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
create_fp_tree(book_db)
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(root)
#print str(root)
