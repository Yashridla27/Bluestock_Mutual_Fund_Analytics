import requests
import pandas as pd

scheme_codes = [119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(f"Data/Raw/nav_{code}.csv", index=False)

    print(f"Saved NAV for {code}")