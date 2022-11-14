import math
import datetime
import pandas as pd

for x in range(0, int(2 * math.pi)):
    print(f"Sin {x} = {math.sin(x)}")

print(datetime.datetime.now())

df = pd.DataFrame(
    {
        "Name": [
            "Yurchishin, Danilo",
            "Bakayev, Roman",
            "Egey, Olecsandr",
        ],
        "Age": [19, 18, 19],
        "Sex": ["male", "male", "male"],
    }
)

print(df)