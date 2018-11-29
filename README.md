# walktree
Usage: | walktree \<parent field\> \<child field\>

Outputs child mv field per parent.

Example:
```
$ cat org_sample.csv
Employee,Boss
Geoff,Bill
Sidney,Bill
Bill,Matt
Matt,Adam
Ruben,Matt
Ploy,Marwa
Marwa,Adam
Joe,Roger
 
$ splunk search '| inputlookup org_sample.csv | walktree "Boss" "Employee"'
children parent
-------- ------
Geoff    Bill
Sidney
 
Bill     Matt
Ruben
Geoff
Sidney
 
Matt     Adam
Marwa
Bill
Ruben
Geoff
Sidney
 
Ploy     Marwa
 
Joe      Roger
 
$ splunk search '| inputlookup org_sample.csv.csv | walktree "Boss" "Employee" | search parent="Matt" | mvexpand children | fields children'
children
--------
Bill
Ruben
Geoff
Sidney
```
