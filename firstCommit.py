from bs4 import BeautifulSoup;
import requests;

page = requests.get("https://colleague-ss.uoguelph.ca/Student/Planning/DegreePlans/PrintSchedule?termId=F24&hideProxyDialog=false")
soup = BeautifulSoup(page.content, 'html.parser') # Parse the HTML content of the page

#courseName = soup.findAll('span', attrs={'databind': 'text: $data.FullTitleDisplay()', 'id': 'full-title-display-1'}) # Find all span tags with the attribute data-bind='text: courseNam