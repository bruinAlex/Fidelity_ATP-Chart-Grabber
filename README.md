# Fidelity Active Trader Pro Chart Grabber

## Save screenshots of charts for a bunch of tickers
![Demo gif](https://github.com/bruinAlex/demo_gifs/blob/master/atp_pyautogui_demo.gif)

## Required packages
- Python 3.7
- PyAutoGUI 0.9.50

## Instructions
- Open script and update list of tickers in the `TICKERS` array to the desired tickers and save
- Open ATP and log in using username and password
- Open shell and ensure the shell window does not cover the ticker input box in the top left
- Run script from shell: `python fidelity_atp_volatility_charts.py`
- When script is finished, an alert box will pop up
- Look in the `output` directory for your screenshots

## TODO
- Add ability to choose other time periods for charting
- Detect and handle other open ATP windows
