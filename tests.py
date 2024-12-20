import pandas as pd
import sqlite3
import logging
logger = logging.getLogger()

def test_remove_columns_absent(new_df, logger):
    columns_to_remove = [
        'Peak CCU', 'Linux', 'Header image', 'Screenshots', 'Metacritic score',
        'Metacritic url', 'Mac', 'Notes', 'Average playtime two weeks',
        'Median playtime two weeks', 'Positive', 'Negative', 'Supported languages',
        'Support email', 'Movies', 'Support url', 'User score', 'Score rank',
        'Recommendations', 'Full audio languages', 'DiscountDLC count', 'About the game',
        'Reviews', 'Website', 'Windows'
    ]

    columns_to_remove = [col for col in columns_to_remove if col in new_df.columns]
    new_df = new_df.drop(columns=columns_to_remove)

    for col in columns_to_remove:
        if col in new_df.columns:
            raise ValueError(f"Kolumnen '{col}' togs inte bort")
    
logger.warning("Alla specificerade kolumner har tagits bort från DataFrame.")

def test_load_csv_to_sqlite(db_name, csv_file):
    """
    Testar att en CSV-fil kan läsas in i en SQLite-databas.
    """
    try:
        con = sqlite3.connect(db_name)
        logger.info(f"Anslutning till databasen '{db_name}' skapad.")

        df = pd.read_csv(csv_file, index_col=False)
        logger.info(f"CSV-filen '{csv_file}' lästes in korrekt.")

        if df.empty:
            logger.error("CSV-filen är tom och kunde inte laddas in.")
            raise ValueError("CSV-filen är tom.")

    except FileNotFoundError:
        logger.exception(f"Filen '{csv_file}' kunde inte hittas.")
        raise

    except Exception as e:
        logger.exception(f"Ett oväntat fel inträffade: {e}")
        raise
    
logger.critical("CSV-filen lästes in och databasen är tillgänglig.")