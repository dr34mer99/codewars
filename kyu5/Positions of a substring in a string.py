'''
Let us go through an example.

You have a string (here a short one):

s = "GCAGCaGCTGCgatggcggcgctgaggggtcttgggggctctaggccggccacctactgg",
with only upper or lower cases letters A, C, G, T.

You want to find substrings in this string. Each substring to find has a label.
The different substrings to find are given in a string of the following form:

Base = "Version xxxx

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Partial Database
http://...
Copyright (c) All rights reserved.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

<>

AaaI (XmaIII)                     CGGCCG
AacI (BamHI)                      GGATCC
AaeI                              GGATCC
AagI (ClaI)                       ATCGAT
AarI                              CACCTGCNNNN
Acc38I (EcoRII)                   CCWGG
AceI (TseI)                       GCWGC"
Only the first lines of a Base are given here.

In first place you get a few lines of comments. Then in three columns:
the labels of the substrings, in the second one -
that can be empty - kind of comments, in the 3rd one
the substring corresponding to the label.

Notice that other letters than A, C, G, T appear.

The conventions for these other letters follow:

R stands for G or A
Y stands for C or T
M stands for A or C
K stands for G or T
S stands for G or C
W stands for A or T
B stands for not A ie (C or G or T)
D stands for not C ie (A or G or T)
H stands for not G ie (A or C or T)
V stands for not T ie (A or C or G)
N stands for A or C or G or T
In the tests there are two different Bases called Base
and Base1 and two long strings: data and data1.

Given a base base (Base or Base1), a string strng
(which will be data or data1) and a query name query -
e.g label "AceI" - the function get_pos will return:

the non-overlapping positions in strng
where the query substring has been found.
In the previous example we will return "1 7"
since the positions are numbered from 1 and not from 0.

Explanation:
label "AceI" is the name of the substring "GCWGC"
that can be written (see conventions above) "GCAGC"
found at position 1 in s or "GCTGC" found at position 7.

Particular cases
If query name doesn't exist in Base return:

"This query name does not exist in given Base".

If query name exists but query is not found in strng return:

"... is not in given string" (... being the query argument).

Examples:
get_pos(Base, str, "AceI") => "1 7"
get_pos(Base, str, "AaeI") => "AaeI is not in given string"
get_pos(str, "XaeI") => "This query name does not exist in given Base"
Notes
You can see another examples in the "Sample tests".
Translators are welcome for all languages, except for
Ruby since the Bash random tests needing Ruby a Ruby
reference solution is already there though not yet published.
'''
#unfinished
def get_pos(base, strng, query):
    no_header = base.split('<>')[1][2:]
    base1 = [i for i in no_header.split('\n')]
    b = {}
    for i in base1:
        if len(i.split()) > 2:
            b[i.split()[0]] = i.split()[2]
            b[i.split()[1][1:-1]] = i.split()[2]
        elif len(i.split()) <= 2:
            b[i.split()[0]] = i.split()[1]
    if query not in b:
        return "This query name does not exist in given Base"
    try:
        return strng.index(b[query])
    except:
        return f'{query} is not in given string'


Base = """Version xxxx                                             

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
Partial Database   
http://... 
Copyright (c) All rights reserved. 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 

<>

AaaI (XmaIII)                     CGGCCG 
AacI (BamHI)                      GGATCC 
AaeI (BamHI)                      GGATCC 
AagI (ClaI)                       ATCGAT 
AaqI (ApaLI)                      GTGCAC 
AarI                              NNNNNNNNGCAGGTG 
AatI (StuI)                       AGGCCT 
AatII                             GACGTC 
AauI (Bsp1407I)                   TGTACA 
AbaI (BclI)                       TGATCA 
AbeI (BbvCI)                      CCTCAGC 
AbrI (XhoI)                       CTCGAG 
AcaI (AsuII)                      TTCGAA 
AcaII (BamHI)                     GGATCC 
AcaIII (MstI)                     TGCGCA 
AcaIV (HaeIII)                    GGCC 
AccI                              GTMKAC 
AccII (FnuDII)                    CGCG 
AccIII (BspMII)                   TCCGGA 
Acc16I (MstI)                     TGCGCA 
Acc36I (BspMI)                    ACCTGCNNNN 
Acc38I (EcoRII)                   CCWGG 
Acc65I (KpnI)                     GGTACC 
Acc113I (ScaI)                    AGTACT 
AccB1I (HgiCI)                    GGYRCC 
AccB2I (HaeII)                    RGCGCY 
AccB7I (PflMI)                    CCANNNNNTGG 
AccBSI (BsrBI)                    CCGCTC 
AccEBI (BamHI)                    GGATCC 
AceI (TseI)                       GCWGC 
AceII (NheI)                      GCTAGC 
AceIII                            CAGCTCNNNNNNN 
AciI                              CCGC 
AclI                              AACGTT 
AclNI (SpeI)                      ACTAGT 
AclWI (BinI)                      GGATCNNNN"""

data= "GCAGCaGCAGCgatggcggcgctgaggggtcttgggggctctaggccggccacctactgg"

print(get_pos(Base, data, 'AceI'))