*** Settings ***
Library    ex_selenium_modif_pt_robot.MainPage
Library    ex_selenium_modif_pt_robot.ReleasePage
Library    ex_selenium_modif_pt_robot.ResultPage
Library    ex_selenium_modif_pt_robot.SearchResultPage
Library    ex_selenium_modif_pt_robot

Test Setup    ex_selenium_modif_pt_robot.MainPage.Initiate Browser Instance
Test Teardown    ex_selenium_modif_pt_robot.MainPage.Close Browser Instance


*** Test Cases ***
Check For 5 Ex
    Search In Box    decorator
    Click First Search Result
    Click Hyperlink From Content    Examples
    ${nr_ex}=    Return Count Of Paragraphs    examples
    Should Be Equal    ${nr_ex}    ${5}
    
Get Last Py Release
    Go to All Releases Page
    ${last_rel_version}=    Return Last Release Version
    LOG    ${last_rel_version}

Check Coresp Rel For Latest Py Version 
    Go to All Releases Page
    ${last_py_version}=    Return Specific First Row From Py Table    release-version    text
    ${bool_coresp}=    Search String In Specific Release Table    release-number    ${last_py_version}
    Fail If Value Not True    ${bool_coresp}    There is a corresponding    No corresponding

Check Rel Date After Py Rel
    Go to All Releases Page
    ${date_last_py_vers}=    Return Specific First Row From Py Table    release-start    date
    ${last_py_version}=    Return Specific First Row From Py Table    release-version    text
    ${date_last_rel}=    Return Date For Specific Version    ${last_py_version}
    ${bool_first_date_greater}=    Compare Dates    ${date_last_rel}    ${date_last_py_vers}
    RUN KEYWORD IF    ${bool_first_date_greater}    LOG    OK! -> The date for latest release version (coresp to latest py vers) is more recently.
    ...    ELSE    FAIL    Error!  


*** Keywords ***
Go to All Releases Page
    Open Dropdown Submenu    downloads
    Click Element From Dropdown Submenu    All releases
    
Fail If Value Not True
    [Arguments]    ${bool_value}    ${text_if_true}    ${text_if_false}
    RUN KEYWORD IF    ${bool_value}    LOG    ${text_if_true}        
    ...    ELSE    FAIL    ${text_if_false}
           