*** Settings ***
Library    toolsqa
Library    toolsqa.TextBoxPage
Library    toolsqa.CheckBoxPage

Test Setup    toolsqa.TextBoxPage.Initiate Browser Instance
Test Teardown    toolsqa.TextBoxPage.Close Browser Instance


*** Variables ***
${bad_email}    ??????????@yahoo.com


*** Test Cases ***
Test Textbox And Submit Updates
    
    Write In All 4 Textboxes    name=Adrian 23 !.    email=a3fm3@yahoo.com    cur_adr=ceva    perma_adr=Str Medg, Bl h2, ap 26 :)
    ${bool_button_worked}    Click Submit Button
    RUN KEYWORD IF    ${bool_button_worked}    Check And Log If Answer Is Shown Correct Or Not 
    ...    ELSE    LOG    Submit button didnt show anything.
 
    Write In Textbox    userName    111111
    Write In Textbox    permanentAddress    Buc Nr 22    
    Write In Textbox    userEmail    dasdas@adssad.com
    ${bool_button_worked}    Click Submit Button
    RUN KEYWORD IF    ${bool_button_worked}    Check And Log If Answer Is Shown Correct Or Not 
    ...    ELSE    LOG    Submit button didnt show anything.


Test Submit Not Work For Wrong Email Format
    
    Write In Textbox    userEmail    ${bad_email}
    ${bool_button_worked}    Click Submit Button
    RUN KEYWORD IF    ${bool_button_worked}    FAIL    Submit worked for wrong email example.
    ...    ELSE    LOG    Submit is behaving good for wrong email example.   


Test If Plus And Minus Buttons Are Working
    
    toolsqa.CheckBoxPage.Click Element From Left Pannel Menu    Check Box
    Click Expand Or Collapse All Button    Expand all
    ${bool_expanded}=    Check If There Is Something Expanded
    RUN KEYWORD IF    ${bool_expanded}    LOG    Plus button working.
    ...    ELSE    FAIL    Plus button not working.
    Click Expand Or Collapse All Button    Collapse all
    ${bool_expanded}=    Check If There Is Something Expanded
    RUN KEYWORD IF    ${bool_expanded}    FAIL    Minus button not working.
    ...    ELSE    LOG    Minus button working.


Test Check Box Menu And Displayed Results
    
    toolsqa.CheckBoxPage.Click Element From Left Pannel Menu    Check Box
    Click Expand Or Collapse All Button    Expand all   
    Make Action On Box Item    veu    Click
    Make Action On Box Item    desktop    Click
    Make Action On Box Item    office    Click
    Make Action On Box Item    office    Toggle
    Make Action On Box Item    office    Click
    Make Action On Box Item    excelFile    Click 
    Make Action On Box Item    office    Click
    @{list_displayed_res}=    Return Displayed Results
    ${bool_displayed}=    Check If All Selected Are Displayed    @{list_displayed_res}
     RUN KEYWORD IF    ${bool_displayed}    LOG    All selected are displayed.
    ...    ELSE    FAIL    Fail.


*** Keywords ***
Write In All 4 Textboxes
    
    [Arguments]    &{dict_info}
    Write In Textbox    userName    ${dict_info}[name]
    Write In Textbox    userEmail    ${dict_info}[email]
    Write In Textbox    currentAddress    ${dict_info}[cur_adr]
    Write In Textbox    permanentAddress    ${dict_info}[perma_adr]


Check And Log If Answer Is Shown Correct Or Not    
    
    ${answer}=    Check If Answer Is Shown    
    RUN KEYWORD IF    ${answer}    LOG    Ok! The answer is shown correct.
    ...    ELSE    FAIL    Shown answer not the same!