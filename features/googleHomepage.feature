Feature: Google Homepage Automation

  Scenario: Google logo is present
      When we search for the logo
      Then logo is present!

  Scenario: Google Search Text field is present
  	  When we search for the search text field
      Then search text field is present!


  Scenario: Google Search Button field is present
  	  When we search for the Search Button
      Then Search Button field is present!


  Scenario: "True Fit" is entered in the search text field and clicking the search button yields some results 
  	Given Search Text Field is present
  	  When we enter "True Fit" in the Search Text Field and click on Search Button
      Then the title is updated to "True Fit" and yields some results


  Scenario: Cannot perform search when Search Text Field is empty 
  	Given Search Text Field is there
  	  When there is no text in the Search Text Field and Search Button is clicked
      Then no results are displayed
