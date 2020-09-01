def weekly(days, response) -> list:
    weeks = [response[i : i + days] for i in range(0, len(response), days)]

    res = [
        {"date": week[-1]["date"], "value": sum([val["value"] for val in week])}
        for week in weeks
    ]
    return res


def monthly(response) -> list:
    d = {}

    for date in response:
        year, month, _ = date["date"].split("-")

        if year in d:
            if month in d[year]:
                d[year][month].append(date)
            else:
                d[year][month] = [date]
        else:
            d[year] = {month: [date]}

    dates = []
    values = []
    for year in d.values():
        for month in year.values():
            dates.append(month[0]["date"])
            values.append(sum([val["value"] for val in month]))
    res = list(zip(dates, values))
    return [{"date": date, "value": value} for date, value in res]
