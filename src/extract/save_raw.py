import json
from datetime import datetime
from pathlib import Path


def save_raw(data):
    Path("data/raw").mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"data/raw/jobs_{timestamp}.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2,
        )

    return filename