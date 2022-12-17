@ECHO OFF
%CD%\trollbot_env\Scripts\activate.bat
py %CD%\trollbot.py bypass_startup_protection
deactivate
