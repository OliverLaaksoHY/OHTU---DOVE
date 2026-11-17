*** Settings ***
Library  Browser
Library  ../AppLibrary.py

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         500ms
${HOME_URL}      http://${SERVER}
${ADD_URL}       http://${SERVER}/add_reference
${BROWSER}       chromium
${HEADLESS}      true

*** Keywords ***
Open And Configure Browser
    IF  $HEADLESS == 'true'
        New Browser  browser=${BROWSER}  headless=True
    ELSE
        New Browser  browser=${BROWSER}  headless=False  slowMo=${DELAY}
    END
    New Context
    New Page  about:blank

Reset Application And Go To Starting Page
    Reset Application
    Go To  ${HOME_URL}

Home Page Should Be Open
    Get Title  ==  DOVE --- Lähdeviitteiden hallintajärjestelmä

Add Reference Page Should Be Open
    Get Title  ==  Add Reference

Go To Add Reference Page
    Go To  ${ADD_URL}

Set Reference Title
    [Arguments]  ${title}
    Fill Text  id=title  ${title}

Set Reference Author
    [Arguments]  ${author}
    Fill Text  id=author  ${author}

Set Reference Year
    [Arguments]  ${year}
    Fill Text  id=year  ${year}

Click Create Reference
    Click  input[type="submit"]

Reference Should Be Visible
    [Arguments]  ${title}  ${author}  ${year}
    Get Text  body  *=  ${title}
    Get Text  body  *=  ${author}
    Get Text  body  *=  ${year}
