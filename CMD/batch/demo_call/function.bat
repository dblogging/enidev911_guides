::---------start function.cmd--------
@echo off 
:: Add 25 to %1
SET /a _number=%1 + 25
:: Store %2
SET _description=[%2]
echo Press to continue
pause>nul
::----------end function.cmd--------
