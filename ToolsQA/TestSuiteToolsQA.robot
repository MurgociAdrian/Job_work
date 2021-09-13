*** Settings ***
Library    toolsqa
Library    toolsqa.TextBoxPage
Library    toolsqa.CheckBoxPage
Library    toolsqa.RadioButtonPage
Library    toolsqa.ButtonsPage

Test Setup    toolsqa.TextBoxPage.Initiate Browser Instance
Test Teardown    toolsqa.TextBoxPage.Close Browser Instance


*** Variables ***
${bad_email}    ??????????@yahoo.com
${radio_button_name}    yes


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
    RUN KEYWORD IF    ${bool_expanded}    LOG    Plus button is working.
    ...    ELSE    FAIL    Plus button not working.
    
    Click Expand Or Collapse All Button    Collapse all
    ${bool_expanded}=    Check If There Is Something Expanded
    RUN KEYWORD IF    ${bool_expanded}    FAIL    Minus button not working.
    ...    ELSE    LOG    Minus button is working.


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
    ${bool_displayed}=    Check If All Selected Are Displayed    ${list_displayed_res}
    RUN KEYWORD IF    ${bool_displayed}    LOG    All selected are displayed.
    ...    ELSE    FAIL    Not all selected items are displayed.


Test Radio Buttons
    
    toolsqa.RadioButtonPage.Click Element From Left Pannel Menu    Radio Button
    ${bool_displayed}=    Click Radio Button And Check Displayed    ${radio_button_name}
    RUN KEYWORD IF    ${bool_displayed}    LOG    Radio button is working and displayed text matches pressed button.
    ...    ELSE IF    ${bool_displayed} == False    FAIL    Radio button is working but displayed failed.
    ...    ELSE    FAIL    Radio button is not working. 


Test Buttons
    
    toolsqa.ButtonsPage.Click Element From Left Pannel Menu    Buttons
    ${bool_working_button}=    Check Double Click Me Button
    RUN KEYWORD IF    ${bool_working_button}    LOG    Double Click Button is working.
    ...    ELSE    FAIL    Functionality of the button is bad.    

    ${bool_working_button}=    Check Right Click Me Button
    RUN KEYWORD IF    ${bool_working_button}    LOG    Right Click Button is working.
    ...    ELSE    FAIL    Functionality of the button is bad.

    ${bool_working_button}=     Check Click Me Button
    RUN KEYWORD IF    ${bool_working_button}    LOG    Click Button is working.
    ...    ELSE    FAIL    Functionality of the button is bad.
    

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