*** Settings ***
Library    Custom_NASInfo.py

*** Keywords ***
Myfile
    Set Path   
Open
    [Arguments]    ${file_name}
    Create Myfile    ${file_name}
Write
    [Arguments]    ${LIST}
    Write Msg    ${LIST}
