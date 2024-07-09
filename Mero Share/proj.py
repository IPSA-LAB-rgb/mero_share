import requests as r
from bs4 import BeautifulSoup
import pendulum

def meroshare(company_name):
    url = "https://merolagani.com/LatestMarket.aspx"
    a = r.get(url)
    htmlcontent = a.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    table = soup.find('table', {'class': 'table table-hover live-trading sortable'})
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns:
            symbol = columns[0].text.strip()
            if symbol == company_name:
                ltp = columns[1].text.replace(',', '')
                return float(ltp)
				
    print("You've entered the wrong symbol or the company isn't enlisted.")
    return None

def company_shares():
    while True:
        company = input("Which company's current share value would you like to see (Express in symbol)? ")
        current_value = meroshare(company.upper())
        if current_value is None:
            print("Sorry, we've failed to retrieve the current share value.")
            continue
        print(current_value)
        No_of_kitta = int(input("What is the number of shares you bought? "))
        old_value = int(input("What was the price per share when you bought it? "))
        Total = No_of_kitta * current_value - No_of_kitta * old_value
        time = pendulum.now()
        
        if Total > 0:
            print(f"Congratulations!! As of {time} you've earned a total profit of {Total}. ")
        elif Total == 0:
            print(f"As of  {time}, you're neutral . ")
        else:
            print(f"Sorry, as of  {time} you're at a loss. ")
        
        w = input("Do you want to see the profit/loss that you've gained for other companies as well (Y/N)? ")
        
        if w.upper() != "Y":
            break

company_shares()
