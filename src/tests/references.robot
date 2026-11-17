*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page

*** Test Cases ***
Open Add Reference Page
    Click  text=Add a book reference
    Add Reference Page Should Be Open

Create Reference
    Go To Add Reference Page
    Set Reference Title  The Hobbit
    Set Reference Author  J. R. R. Tolkien
    Set Reference Year  1937
    Click Create Reference
    Home Page Should Be Open
    Reference Should Be Visible  The Hobbit  J. R. R. Tolkien  1937

Open Reference Details
    Create Reference  The Hobbit  J. R. R. Tolkien  1937
    Go To  ${HOME_URL}
    Click  text=The Hobbit
    Get Text  body  *=  The Hobbit
    Get Text  body  *=  Author: J. R. R. Tolkien
    Get Text  body  *=  Year: 1937

Reject Invalid Year
    Go To Add Reference Page
    Set Reference Title  The Hobbit
    Set Reference Author  J. R. R. Tolkien
    Set Reference Year  937
    Click Create Reference
    Add Reference Page Should Be Open
    Get Text  body  *=  Year must be an integer between 1000 and 2999
