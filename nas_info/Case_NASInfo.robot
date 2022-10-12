*** Settings ***

#Library    Selenium2Library
Resource    Keyword_NASInfo.robot
Library     Selenium2Library
Library    Collections
*** Variables ***
${USER_NAME}    admin1
${USER_PW}      Dqv@61650
${INF_FILE}       NAS_inf
&{INF_LIST}
*** Test Cases ***  
Open My NAS
    Open Browser    http://10.4.148.44:8080/cgi-bin/    chrome
    Input Text    id:username    ${USER_NAME}
    Input Text    id:pwd         ${USER_PW}
    Click Button    id:submit
    Wait Until Element Is Visible    id:ext-gen175
    Click Button    id:ext-gen153
    ${SEVER_NAME} =     Get Text    class:hostname.fb
    ${DEVICE} =         Get Text    class:model-name
    Set To Dictionary    ${INF_LIST}    User_Name    ${USER_NAME}
    Set To Dictionary    ${INF_LIST}    User_Passwrod     ${USER_PW}
    Set To Dictionary    ${INF_LIST}    Sever_Name     ${SEVER_NAME}
    Set To Dictionary    ${INF_LIST}    Model_name     ${DEVICE}
    Click Button    id:ext-gen153
    Click Button    id:ext-gen175
    Click Element    id:ext-comp-1046
    Close Browser

    
    
Store Inf in File
    Myfile  
    Open    ${INF_FILE}
    Write   ${INF_LIST}