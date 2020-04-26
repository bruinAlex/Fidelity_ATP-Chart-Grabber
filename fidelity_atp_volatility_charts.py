# fidelity_atp_volatility_charts.py
import pyautogui
from datetime import datetime
import os


TICKERS = ['SPY', 'QQQ', 'AAPL', 'TSLA', 'MSFT']
TITLE = "Fidelity Active Trader Pro"
SCREENSHOT_REGION = (0, 0, 2540, 985)
SAVE_DIR = "output/"


# Get the window with the `title` in the window title
# Returns as a list with (hopefully) only one element
atp_window = pyautogui.getWindowsWithTitle(TITLE)[0]

# Ensure window is maximized
atp_window.maximize()


# Create screenshot output dir if not exist
if os.path.exists(SAVE_DIR):
	print("Output directory found")
else:
	print("Output directory not found; creating directory!")
	os.mkdir(SAVE_DIR)


# Loop through all tickers
for ticker in TICKERS:
	# Click on the ticker search input box
	pyautogui.doubleClick(75, 57)

	# Delete in case there's already a string
	pyautogui.press('delete')

	# Type in ticker symbol
	# pyautogui.write([ticker, 'enter'])
	pyautogui.write(ticker)
	pyautogui.press('enter')
	print(f"{ticker} written!")

	# Wait n seconds to ensure some indicators load (HV & IV can be very slow)
	pyautogui.sleep(1.5)

	# Take a region screenshot
	im = pyautogui.screenshot(region=SCREENSHOT_REGION)

	# Clean up current datetime which has illegal characters for windows file names (colons)
	current_utc_datetime = datetime.utcnow().strftime('%Y-%m-%dT%H_%M_%S')

	# Create appropriate file name with ticker_datetime_period_window.png
	# TODO create another loop that does other time periods and windows
	file_name = "{}_{}_{}_{}.png".format(ticker, current_utc_datetime, "daily", "30")

	# Save image
	im.save(SAVE_DIR + file_name)

pyautogui.alert(text='Charts saved!', title='Autochart Complete', button='OK')
print("Done!")