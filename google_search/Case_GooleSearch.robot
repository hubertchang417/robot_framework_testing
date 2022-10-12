*** Settings ***
Resource    Keyword_GooleSearch.robot
*** Variables ***
${site}    http://www.google.com.tw
${target}  維基百科
*** Test Cases ***
Google search
    My Search    ${site}    nas    ${target}