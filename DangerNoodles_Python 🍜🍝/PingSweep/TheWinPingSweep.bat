@REM @echo off
setlocal enabledelayedexpansion

if "%1"=="" (
    echo Type the IP address to scan.
    echo Example: pingsweep.bat 192.168.2
) else (
    echo Scanning IP addresses in the range %1.1 to %1.254...
    for /L %%i in (1,1,254) do (
        set "ip=!%1!.%%i"
        ping -n 1 !ip! | find "Reply from" >> results.txt
    )
    echo Ping sweep completed. Results are saved in results.txt.
)

endlocal