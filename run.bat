@echo off
:while
cls
set option=0
echo .: OS UTN TOOLS :.
echo.
echo [1] Processes
echo [2] Memory
echo [3] Input/Output
echo.
set /p option="Enter option: "
if %option%==1 (python -m os_utn.processes)
if %option%==2 (python -m os_utn.memory)
if %option%==3 (python -m os_utn.input_output)
goto :while