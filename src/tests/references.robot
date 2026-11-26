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

Edit Reference Saves Changes To The Selected Book
    Create Reference    Dune    Frank Herbert    1965
    Create Reference    The Hobit    J. Tolkien    1936
    Go To    ${HOME_URL}
    Click    text=The Hobit
    ${book_url}=    Get Url
    Click    text=Edit reference
    Get Property    id=title    value    ==    The Hobit
    Get Property    id=author    value    ==    J. Tolkien
    Get Property    id=year    value    ==    1936

    Set Reference Title    The Hobbit
    Set Reference Author    J. R. R. Tolkien
    Set Reference Year    1937
    Click    input[value="Update reference"]
    Home Page Should Be Open
    Get Element Count    css=li a[href^="/reference/"]    ==    2

    Click    text=The Hobbit
    Get Url    ==    ${book_url}
    Reload
    Reference Should Be Visible    The Hobbit    J. R. R. Tolkien    1937
    Go To    ${HOME_URL}
    Click    text=Dune
    Reference Should Be Visible    Dune    Frank Herbert    1965

Edit Reference Rejects Blank Author
    Create Reference    Dune    Frank Herbert    1965
    Go To    ${HOME_URL}
    Click    text=Dune
    ${book_url}=    Get Url
    Click    text=Edit reference
    Set Reference Title    Changed title
    Set Reference Author    ${SPACE}
    Click    input[value="Update reference"]
    Get Text    css=.info    ==    author must be at least 1 letter

    Go To    ${book_url}
    Reference Should Be Visible    Dune    Frank Herbert    1965

Remove Reference
    Create Reference    Dune    Frank Herbert    1965
    Go To    ${HOME_URL}
    Click    text=Dune
    Click    text=Delete
    Get Title    ==    Delete Reference
    Get Text    body    *=    Are you sure you want to delete this reference?
    Click    input[name="delete"]
    Home Page Should Be Open
    Get Element Count    css=li a[href^="/reference/"]    ==    0
    Get Text    body    *=    No references found. 

View BibTeX Entry
    Create Reference    The Hobbit    J. R. R. Tolkien    1937
    Go To    ${HOME_URL}
    Click    text=The Hobbit
    Click    text=View BibTeX
    Get Text    pre    *=    @book{tolkien1937
    Get Text    pre    *=    title = {The Hobbit}
    Get Text    pre    *=    author = {J. R. R. Tolkien}
    Get Text    pre    *=    year = {1937}

BibTeX Page For Missing Reference Shows Not Found
    Go To    ${HOME_URL}/bibtex/999999
    Get Text    body    *=    Reference not found
