from src.extract.adzuna import fetch_jobs
from src.extract.save_raw import save_raw

data = fetch_jobs()

path = save_raw(data)

print(f"Saved to {path}")
print(data["count"])
print(data["results"][0].keys())

print(data["results"][0]["company"])
print(data["results"][0]["location"])