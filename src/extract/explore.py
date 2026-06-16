import json

with open(
    "data/raw/YOUR_FILE.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

job = data["results"][0]

for key, value in job.items():
    print(f"{key}: {type(value)}")