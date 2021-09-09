*** Settings ***
Library    toolsqa
Library    toolsqa.TextBoxPage

Test Setup    toolsqa.TextBoxPage.Initiate Browser Instance
Test Teardown    toolsqa.TextBoxPage.Close Browser Instance

*** Test Cases ***
Test Ads Functionalities
    Close Bottom Ad
    Check Link Is Reachable For Right Side Ad
    
Test Textbox And Submit Updates
    Write In All 4 Textboxes    Adrian 23 !.    a3fm3@yahoo.com    ceva    Str Medg, Bl h2, ap 26 :)
    Click Submit Button
    ${answer}=    Check If Answer Is Shown    
    LOG    ${answer}
    Write In Textbox    userName    1111111    continue
    Write In Textbox    permanentAddress    Buc Nr 22    
    Click Submit Button
    ${answer1}=    Check If Answer Is Shown    
    LOG    ${answer1}
    
*** Keywords ***
Write In All 4 Textboxes
    [Arguments]    ${name}    ${email}    ${cur_adr}    ${perma_adr}
    Write In Textbox    userName    ${name}
    Write In Textbox    userEmail    ${email}
    Write In Textbox    currentAddress    ${cur_adr}
    Write In Textbox    permanentAddress    ${perma_adr}
    