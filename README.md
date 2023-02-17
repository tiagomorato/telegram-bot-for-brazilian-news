# What is it?
The Telegram bot provides a quick and efficient way to retrieve news from the G1 website. It shows the title of the first news and an index number, which can be used to select a specific article. By typing the index number, the bot displays the corresponding link to the article, making the process of retrieving news much more straightforward.  

# Quick start
This bot uses the Beautiful Soup and pyTelegramBotAPI libraries. To install, run the following command:
``` pip install -r requirements.txt ```

After installation, set the API_KEY variable with your bot's API key. The bot is now ready to run. To access the latest news, simply send the /g1 command in the Telegram chat with your bot. You will then be prompted to select a specific news article by its number.

