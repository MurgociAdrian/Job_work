*** Settings ***
Library    toolsqa
Library    toolsqa.TextBoxPage

Test Setup    toolsqa.TextBoxPage.Initiate Browser Instance
Test Teardown    toolsqa.TextBoxPage.Close Browser Instance

*** Variables ***
${bad_email}    ???????@yahoo.com

*** Test Cases ***
Test Textbox And Submit Updates
    Write In All 4 Textboxes    Adrian 23 !.    a3fm3@yahoo.com    ceva    Str Medg, Bl h2, ap 26 :)
    Click Submit Button
    ${answer}=    Check If Answer Is Shown    
    RUN KEYWORD IF    ${answer}    LOG    Ok! The answer is shown correct.
    ...    ELSE    FAIL    Shown answer not the same!
    Write In Textbox    userName    111111
    Write In Textbox    permanentAddress    Buc Nr 22    
    Click Submit Button
    ${answer1}=    Check If Answer Is Shown    
    RUN KEYWORD IF    ${answer1}    LOG    Ok! The answer is shown correct.
    ...    ELSE    FAIL    Shown answer not the same!

Test Submit Not Work For Wrong Email Format
    Write In Textbox    userEmail    ${bad_email}
    Click Submit Button
    # ....    

*** Keywords ***
Write In All 4 Textboxes
    [Arguments]    ${name}    ${email}    ${cur_adr}    ${perma_adr}
    Write In Textbox    userName    ${name}
    Write In Textbox    userEmail    ${email}
    Write In Textbox    currentAddress    ${cur_adr}
    Write In Textbox    permanentAddress    ${perma_adr}
    