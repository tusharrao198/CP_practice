t = int ( input ())
n = int ( input ())
lst = list ( map ( int , input (). split ()))
if len ( lst )> 1 :
    for i in lst :
        for j in lst :
            if i!=j :
                diff = abs ( i - j )
                if diff <= 1 and i < j and i in lst : 
                    lst . remove ( i )
                
                elif diff <= 1 and i > j and j in lst : 
                    lst . remove ( j )
            else : 
                lst . remove ( j )
            
    if len ( lst ) == 1 :
        print ( "YES" )
    else :
        print ( "NO" )
else :
    if len ( lst ) == 1 :
        print ( "YES" )
    else :
        print ( "NO" )       