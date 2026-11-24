_conspects = []
def save(filename: str, summary_data: dict) -> dict:
    summary_data["id"] = len(_conspects) + 1
    summary_data["filename"] = filename
    _conspects.append(summary_data)
    return summary_data
