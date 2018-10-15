# testGoogleWebPage
Test suite for automated testing of Google home page (www.google.com)
This testsuite tests the following scenarios
1. The Google logo image is present.
2. The Search text field is present.
3. The Google Search button is present. 
4. Search text may be entered into the Search text field (e.g. ‘True Fit’)
5. Clicking the ‘Google Search’ button with search text yields search results. 
6. Clicking the ‘Google Search’ button with no search text will not perform a search.

# Installation Instructions
* Clone the repo locally 
* pip install -r requirements.txt (This installs behave, selenium and other requirements)
* Update the path to the chromedriver in the file features/environment.py
[Download here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* Run the test suite by executing 'behave' at the command line
