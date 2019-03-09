def tc(a):
    i=0
    o=""

    if a[-2:] == "am":
        
        if a[:2] == "12":
            o="00" + a[2:5]
        
        if a[1] == ":":
            o=a[0:4]
        
        if a[2] == ":" and a[:2] != "12":
            o=a[0:5]
            
    if a[-2:] == "pm":
      
      if a[1] == ":":
          i=int(a[0]) + 12
          o=str(i)+a[1:4]
      
      if a[2] == ":" and a[:2] != "12":
        i=int(a[0:2]) + 12
        o=str(i) + a[2:5]   
    
      if a[:2] == "12":
          o=a[:5]
          
    return o

#insert your list here

l =["12:00am","12:01am","1:00am","11:00am","11:59am","12:00pm","12:01pm","1:00pm","5:01pm","11:00pm","11:59pm"]
for c in (l):
    print(tc(c),"   ",c)