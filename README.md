# walktree
Usage: | walktree \<parent field\> \<child field\>

Outputs child mv field per parent.

Example:

[org_sample.csv](lookups/org_sample.csv)
- Adam
  - Matt
    - Bill
      - Geoff
      - Sidney
    - Ruben
  - Marwa
    - Ploy
- Roger
  - Joe
```
$ splunk search '| inputlookup org_sample.csv | walktree "Boss" "Employee" | eval children_count=mvcount(children) | table parent children children_count'

parent children children_count
------ -------- --------------
Bill   Geoff                 2
       Sidney




Matt   Bill                  4
       Ruben
       Geoff
       Sidney


Adam   Matt                  6
       Marwa
       Bill
       Ruben
       Geoff
       Sidney
Marwa  Ploy                  1





Roger  Joe                   1
```
```
$ splunk search '| inputlookup org_sample.csv | walktree "Boss" "Employee" | search parent="Matt" | mvexpand children | fields children'
children
--------
Bill
Ruben
Geoff
Sidney
```
