# Standard Imports
import os
import time
import argparse

# Extra Imports
import dotenv

# Project Imports
from TinderSession import TinderSession

def main():
    """
    Run the Tinderbot to automatically swipe profiles and collect data
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("number", type=int, 
                        help="the number of swipes to perform in a day")
    parser.add_argument("ratio", type=float, 
                        help="the fraction swipes that will be likes")
    parser.add_argument("--debug", action="store_true",
                        help="Run in a more manually-controlled way to check "
                             "application state")
    args = parser.parse_args()
       
    dotenv.load_dotenv()
    
    username    = os.getenv("FACEBOOK_USERNAME")
    password    = os.getenv("FACEBOOK_PASSWORD")
    driver_path = os.getenv("CHROME_DRIVE_LOCATION")
    
    session = TinderSession(username, password, driver_path, args.debug)
    session.login_facebook()
    # Add code to use a TinderSession method for processing permissions
    session.auto_swipe(args.number, args.ratio)
    session.close()

if __name__ == '__main__':
    main()
