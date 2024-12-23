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
            date = row.find("td").text.strip()
            name = row.find("td").find_next("td").text.strip()
            link = row.find("td").find_next("td").find("a")["href"]
            location = row.find("td").find_next("td").find_next("td").text.strip()
            type_ = row.find("td").find_next("td").find_next("td").find_next("td").text.strip()
            level = row.find("td").find_next("td").find_next("td").find_next("td").find_next("td").text.strip()
            cost = row.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").text.strip()
            max_teams = row.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").text.strip()
            confirmed = row.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").text.strip()
            status = row.find("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").text.strip()

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
        except AttributeError:
            # Skip rows with missing data
            continue

    return tournaments

# Test the scraper
if __name__ == "__main__":
    data = scrape_tournaments()
    for tournament in data:
        print(tournament)
