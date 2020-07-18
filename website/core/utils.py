import csv


STATE_COL = 'State'
EXCLUDED_CODES = ['yes', 'no','n/a' ,'']

# https://gist.github.com/rogerallen/1583593
STATE_TO_ABBREV = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

ABBREV_TO_STATE = dict(map(reversed, STATE_TO_ABBREV.items()))


def is_url(url):
    return urlparse.urlparse(url).scheme != ""


def load_data(path):
    # TODO replace with call to google sheets api directly
    # COLS: ['Type', 'Name', 'Contact', 'Url', 'Description', 'national', 'state']
    with open(path) as f:
        reader = csv.DictReader(f, dialect='excel')
        rows = list(reader)
        cols = reader.fieldnames
        assert STATE_COL in cols
    state_codes = set()
    states_a = {}
    for row in rows:
        state_codes.add(row[STATE_COL])
    for code in sorted(state_codes):
        if code not in EXCLUDED_CODES:
            states_a[code] = ABBREV_TO_STATE[code.upper()]
    data = {}
    for row in rows:
        entry_type = row['Type']
        state = row['State']
        if entry_type not in data:
            data[entry_type] = {}
        if state not in data[entry_type]:
            data[entry_type][state] = []
        # name, contact, url, desc
        data[entry_type][state].append((row['Name'], row['Contact'], row['Url'], row['Description']))
    return states_a, data
