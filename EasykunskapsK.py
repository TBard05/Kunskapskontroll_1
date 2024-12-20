import pandas as pd
import sqlite3
import logging
import time
logger = logging.getLogger()

logging.basicConfig(
    filename=r'C:\Users\theod\OneDrive\Skrivbord\Tuc\VSCode\logfile.log',
    format='[%(asctime)s][%(levelname)s] %(message)s', 
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M')

con = sqlite3.connect('games.db')
df = pd.read_csv('games.csv', index_col=False)

new_df = df.convert_dtypes()

columns_to_remove = [
    'Peak CCU', 'Linux', 'Header image', 'Screenshots', 'Metacritic score',
    'Metacritic url', 'Mac', 'Notes', 'Average playtime two weeks',
    'Median playtime two weeks', 'Positive', 'Negative', 'Supported languages',
    'Support email', 'Movies', 'Support url', 'User score', 'Score rank',
    'Recommendations', 'Full audio languages', 'DiscountDLC count', 'About the game', 
    'Reviews', 'Website', 'Windows']
time.sleep(3)

columns_to_remove = [col for col in columns_to_remove if col in new_df.columns]
if columns_to_remove:
    logger.info(f"Följande kolumner tas bort: {columns_to_remove}")
    new_df = new_df.drop(columns=columns_to_remove)

logger.info('Kolumner har tagist bort')

# tycker att ett medelvärde är bätter en tex 0 - 200000.
new_df['Estimated owners'] = new_df['Estimated owners'].astype(str)
new_df['Estimated owners'] = new_df['Estimated owners'].apply(
    lambda x: sum(map(int, x.split('-'))) // 2 if '-' in x else int(x))
logging.debug('Beräknat medelvärdet av Estimated owners')  

new_df.to_csv('games.csv', index=False)
new_df.to_sql('game_stats', con, if_exists='replace')

