# YankeeScraper or discord tournament scraper

## Project Overview
The Discord Tournament Scraper is a bot designed to manage and retrieve tournament information from an external website and display it dynamically in a Discord server. The bot integrates a web scraper to fetch tournament data and uses Discord's API to communicate with users in real time.

### Current Features
`Basic Discord Bot`: A functional Discord bot that responds to the !test command to confirm it is online.
Bot Token Handling: The bot token is securely managed using a .env file, ensuring sensitive data is not exposed.
`Basic Framework`: The bot is set up to allow for future expansion, such as fetching and displaying tournament information.

Setup Instructions
1. Clone the Repository
Clone the project from the GitHub repository:
```
git clone https://github.com/<your-username>/discord-tournament-scraper.git
cd discord-tournament-scraper
```

2. Set Up the Virtual Environment
Create a virtual environment:
```
python3 -m venv venv
```
Activate the virtual environment:

On Mac/Linux:
```
source venv/bin/activate
```

On Windows:
```
venv\Scripts\activate
```
Install the required dependencies:
```
pip install -r requirements.txt
```

3. Add Your Discord Bot Token
Create a .env file in the project directory:

touch .env
Add your bot token to the .env file:

makefile
DISCORD_TOKEN=your_discord_bot_token

4. Invite the Bot to Your Discord Server
Go to the Discord Developer Portal.
Select your bot application and navigate to OAuth2 > URL Generator.
Under Scopes, check bot.
Under Bot Permissions, select the permissions your bot needs:
Send Messages
Read Message History
Copy the generated invite URL and open it in your browser.
Select the server to add the bot and click Authorize.

5. Run the Bot
Ensure the virtual environment is activated:

source venv/bin/activate
Start the bot:

python main.py
Go to your Discord server and type:

!test

The bot should respond:
Bot is running!

Next Steps

The next phase of development will focus on:

- Building the Web Scraper:
Scraping tournament information such as names, dates, and links.
- Integrating the Scraper with the Bot:
Adding commands like !tournaments to fetch and display scraped data.
- Caching Data:
Storing tournament data locally to avoid repeated scraping.

