def weekly(days, response) -> list:
    weeks = [response[i : i + days] for i in range(0, len(response), days)]
    res = [
        {"date": week[-1]["date"], "value": sum([val["value"] for val in week])}
        for week in weeks
    ]
    return res


def monthly(response):
    pass
