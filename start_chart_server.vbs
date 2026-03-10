Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd /d C:\Users\klein\financial-charts && python charting_app\app.py > chart_server.log 2>&1", 0, False
