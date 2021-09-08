*** Settings ***
Library    ex_selenium_modif_pt_robot.MainPage
Library    ex_selenium_modif_pt_robot.ReleasePage
Library    ex_selenium_modif_pt_robot.ResultPage
Library    ex_selenium_modif_pt_robot.SearchResultPage

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
    Open Dropdown Submenu    downloads
    Click Element From Dropdown Submenu    All releases
    ${last_version}=    Return Last Release Version
    LOG    ${last_version}
        