' Hidden launcher for server_watchdog.ps1.
' wscript.exe is a Windows-subsystem binary, so no conhost window
' is ever attached when Task Scheduler invokes this — strictly silent.
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "powershell.exe -NoProfile -ExecutionPolicy Bypass -File ""C:\Users\klein\financial-charts\scripts\server_watchdog.ps1""", 0, True
Set WshShell = Nothing
