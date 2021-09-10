*** Settings ***
Library    toolsqa
Library    toolsqa.TextBoxPage

Test Setup    toolsqa.TextBoxPage.Initiate Browser Instance
Test Teardown    toolsqa.TextBoxPage.Close Browser Instance


*** Variables ***
${bad_email}    ??????????@yahoo.com


*** Test Cases ***
Test Textbox And Submit Updates
    
    Write In All 4 Textboxes    Adrian 23 !.    a3fm3@yahoo.com    ceva    Str Medg, Bl h2, ap 26 :)
    ${bool_button_worked0}    Click Submit Button
    RUN KEYWORD IF    ${bool_button_worked0}    Check And Log If Answer Is Shown Correct Or Not 
    ...    ELSE    LOG    Submit button didnt show anything.
 
    Write In Textbox    userName    111111
    Write In Textbox    permanentAddress    Buc Nr 22    
    Write In Textbox    userEmail    dasdas@adssad.com
    ${bool_button_worked1}    Click Submit Button
    RUN KEYWORD IF    ${bool_button_worked1}    Check And Log If Answer Is Shown Correct Or Not 
    ...    ELSE    LOG    Submit button didnt show anything.


Test Submit Not Work For Wrong Email Format
    
    Write In Textbox    userEmail    ${bad_email}
    ${bool_button_worked}    Click Submit Button
    RUN KEYWORD IF    ${bool_button_worked}    FAIL    Submit worked for wrong email example.
    ...    ELSE    LOG    Submit is behaving good for wrong email example.   


*** Keywords ***
Write In All 4 Textboxes
    
    [Arguments]    ${name}    ${email}    ${cur_adr}    ${perma_adr}
    Write In Textbox    userName    ${name}
    Write In Textbox    userEmail    ${email}
    Write In Textbox    currentAddress    ${cur_adr}
    Write In Textbox    permanentAddress    ${perma_adr}


Check And Log If Answer Is Shown Correct Or Not    
    
    ${answer}=    Check If Answer Is Shown    
    RUN KEYWORD IF    ${answer}    LOG    Ok! The answer is shown correct.
    ...    ELSE    FAIL    Shown answer not the same!