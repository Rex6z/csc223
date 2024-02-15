/*
Step 1:
IF START = NULL
    Write UNDERFLOW
    Go to Step 10
[END OF IF]

Step 2:
SET PTR = START

Step 3:
SET PREPTR = PTR

Step 4:
Repeat Steps 5 and 6 while PREPTR -> DATA != NUM

Step 5:
    SET PREPTR = PTR

Step 6:
    SET PTR = PTR -> NEXT

Step 7:
SET TEMP = PTR

Step 8:
SET PREPTR -> NEXT = PTR -> NEXT

Step 9:
FREE TEMP

Step 10:
EXIT
*/

