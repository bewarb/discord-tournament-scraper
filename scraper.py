from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://yankee.org/tournaments'

# Scraper function
def scrape_tournaments():
    response = requests.get(BASE_URL)
    response.raise_for_status()  # Raise an error if the request fails
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the tournament table
    table = soup.find("table", class_="tournamentList")

    # Initialize a list to store tournament data
    tournaments = []

    # Iterate through each row in the table body
    for row in table.find("tbody").find_all("tr"):
        try:
            # Extract data from each cell
            cells = row.find_all("td")  # Get all cells in the row

            date = cells[0].text.strip()  # Date column
            name = cells[1].text.strip()  # Tournament name
            link = cells[1].find("a")["href"] if cells[1].find("a") else None  # Tournament detail link
            location = cells[2].text.strip()  # Location column
            type_ = cells[3].text.strip()  # Type column
            level = cells[4].text.strip()  # Level column
            cost = cells[7].text.strip()  # Cost column
            max_teams = cells[9].text.strip()  # Max Teams column
            confirmed = cells[10].text.strip()  # Confirmed Teams column
            status = cells[11].text.strip()  # Status column

            # Append the extracted data as a dictionary
            tournaments.append({
                "date": date,
                "name": name,
                "link": link,
                "location": location,
                "type": type_,
                "level": level,
                "cost": cost,
                "max_teams": max_teams,
                "confirmed": confirmed,
                "status": status
            })
        except (AttributeError, IndexError):
            # Skip rows with missing or malformed data
            continue

    return tournaments

# Test the scraper
if __name__ == "__main__":
    data = scrape_tournaments()
    for tournament in data:
        print(tournament)