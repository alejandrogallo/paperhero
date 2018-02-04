import datetime


def create(data):
    allowed_keys = ['title', 'year', 'comments', 'journal', 'keyword', 'month', 'pages', 'volume']
    cleaned_data = {k: data[k] for k in allowed_keys if k in list(data.keys())}
    cleaned_data['author'] = data['authors'].replace(";", " and ")
    if not isinstance(cleaned_data['year'], int):
        if len(cleaned_data['year']) < 10:
            del cleaned_data['year']
        else:
            cleaned_data['year'] = cleaned_data['year'][:10]
            cleaned_data['month'] = datetime.date(1900, int(cleaned_data['year'][5:7]), 1).strftime('%b')
    bib_data = ",\n".join(["  %s={%s}" % (k, v) for k, v in list(cleaned_data.items())])
    return "@article{%s,\n%s\n}" % (data['id'], bib_data)
