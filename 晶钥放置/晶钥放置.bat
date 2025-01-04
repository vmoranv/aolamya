@echo off
setlocal enabledelayedexpansion

set "output_file_path=replaced_strings.txt"
if exist "%output_file_path%" del "%output_file_path%"

for /L %%i in (2160,1,2200) do (
    set "template1=|#send={"param":{"pms":"%%i"},"id":13,"cmd":"1222"}|"
    set "template2=|#send={"param":{"petId":%%i},"id":42,"cmd":"ACK241227_4"}|"
    
    echo !template1!>>"%output_file_path%"
    echo !template2!>>"%output_file_path%"
)
endlocal
