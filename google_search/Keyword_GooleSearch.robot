*** Settings ***
Library    Custom_GoogleSearch1.py
Library    SeleniumLibrary


*** Keywords ***
My Search
    [Arguments]   ${site}  ${search_title}    ${search_target}
    Go Start   ${site}
    Search Target    ${search_title}
    Find Site     ${search_target}
    Driver Scroll To Bottom
    Driver Close   

