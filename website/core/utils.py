import csv
import pprint


STATE_COL = 'State'
EXCLUDED_CODES = ['yes','n/a' , '']

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
    # COLS: ['Type', 'Name', 'Contact', 'Url', 'Description', 'National', 'State', 'City']
    # Opens file, reads it with csv package in csv format, extracts all data to variable 'rows',
    # extracts header to variable cols, check if 'State' col is in 'cols'
    # There are 4 different types: Business, Organization, Donate, Petition.
    with open(path) as f:
        reader = csv.DictReader(f, dialect='excel')
        rows = list(reader)
        cols = reader.fieldnames
        assert STATE_COL in cols
    # state_codes will hold disctint values.
    state_codes = set()
    states_a = {}
    # for every row in our csv file, add every distinct value into this set.
    for row in rows:
        state_codes.add(row[STATE_COL])
    # for every state in the states_code array, create an array of their codes, skip over excluded values that are in our file and might have been inserted for States column.
    for code in sorted(state_codes):
        if code not in EXCLUDED_CODES:
            states_a[code] = ABBREV_TO_STATE[code.upper()]
    data = {}
    national_data = {}
    # for every row in our data, grab the 'Type' value, 'State' value, and 'National' value. Use these to check if they exists yet, if not initialize it.
    # finally add data to that sub array in our data array.
    for row in rows:
        entry_type = row['Type']
        state = row['State']
        national = row['National']
        # print("National abbreviation ", national)
        # print("state abbreviation ", state)

        # initialize array
        if entry_type not in data:
            data[entry_type] = {}
        # initialize sub-array
        if state not in data[entry_type]:
            data[entry_type][state] = []
            # print("initializing state array", state)
        # initialize different subarray
        if national not in data[entry_type]:
            data[entry_type][national] = []
            # print("initialized nat array")
        if national == 'nat':
            data[entry_type][national].append((row['Name'], row['Contact'], row['Url'], row['Description'], row['City']))
            # print("printing national", data[entry_type][national])
        else:
            # entry_type = name, contact, url, desc, city; state = 'CA', 'MN','TX', etc.
            data[entry_type][state].append((row['Name'], row['Contact'], row['Url'], row['Description'], row['City']))
            # print("printing state", data[entry_type][state])

    # print(data[entry_type][national])
    return states_a, data
