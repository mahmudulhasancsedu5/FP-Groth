patterns=[]

def find_all_frequent_patterns(paths_arr):#path arr = [[(2,2)(1,2)(4,2)],[(2,3),(4,3)],[(1,1),(3,1),(4,1)]]
    print ''
    num_paths=len(paths_arr)
    if num_paths==0:
        return

    cleaned_path_arr=[]
    if num_paths>1:
        first_path_item=paths_arr[0][0][0]
        flag=0
        path_first_item_list=[]
        i=0
        for path in paths_arr:
            if path[0][0]!=first_path_item :
                flag=1
            path_first_item_list.append(path[0][0])
            i+=1
        print 'first item list = ',path_first_item_list
        if flag==1:
            print 'Diffrent starting item.Need to seperate them.'
            path_first_unique_item_list=list(set(path_first_item_list))
            for item in path_first_unique_item_list:
                #get those path whose first items are same
                paths_with_same_first_item=[ paths_arr[x] for x in range(len(path_first_item_list)) if path_first_item_list[x]==item ]
                
                find_all_frequent_patterns(paths_with_same_first_item)

            return
            
            
        
    print 'All path start with sem item. ',paths_arr
            
    #-----------------do main mining------------
    
    
    #-------------------------------------------------------------------
'''
2
before rev =  [[(2, 7)]]
after rev =  [[(2, 7)]]
1
before rev =  [[(1, 4), (2, 7)], [(1, 2)]]
after rev =  [[(2, 4), (1, 4)], [(1, 2)]]
3
before rev =  [[(3, 2), (2, 7)], [(3, 2), (1, 2)], [(3, 2), (1, 4), (2, 7)]]
after rev =  [[(2, 2), (3, 2)], [(1, 2), (3, 2)], [(2, 2), (1, 2), (3, 2)]]
4
before rev =  [[(4, 1), (2, 7)], [(4, 1), (1, 4), (2, 7)]]
after rev =  [[(2, 1), (4, 1)], [(2, 1), (1, 1), (4, 1)]]
5
before rev =  [[(5, 1), (1, 4), (2, 7)], [(5, 1), (3, 2), (1, 4), (2, 7)]]
after rev =  [[(2, 1), (1, 1), (5, 1)], [(2, 1), (1, 1), (3, 1), (5, 1)]]

'''
            
        
paths= [[(2, 1), (1, 1), (5, 1)], [(6, 1), (1, 1), (3, 1), (5, 1)],[(2, 1), (1, 1), (3, 1), (5, 1)]]
find_all_frequent_patterns(paths)
