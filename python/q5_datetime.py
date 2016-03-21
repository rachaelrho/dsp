# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015' 
```
from datetime import datetime

date_format =  "%m-%d-%Y"
d1 = datetime.strptime(date_start, date_format)
d2= datetime.strptime(date_stop, date_format)
delta = d2-d1
print delta.days
```


####b)  
date_start = '12312013'  
date_stop = '05282015'  
```
from datetime import datetime

date_format =  "%m%d%Y"
d1 = datetime.strptime(date_start, date_format)
d2= datetime.strptime(date_stop, date_format)
delta = d2-d1
print delta.days
```

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 
```
from datetime import datetime

date_format =  "%d-%b-%Y"
d1 = datetime.strptime(date_start, date_format)
d2= datetime.strptime(date_stop, date_format)
delta = d2-d1
print delta.days
```
