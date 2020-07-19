from flask import render_template, Blueprint, url_for
from .utils import load_data


DATA_FILE = 'website/static/csv_data.csv'
states_dict, state_to_category = load_data(DATA_FILE)
states_array = list(states_dict.items())
core = Blueprint('core', __name__)
Other_Resources = [("pbresources.com", "http://www.pb-resources.com"), ("HungryHungryHooker.com",
                                                                        "https://hungryhungryhooker.squarespace.com/blackownedbiz"), ("Adhesive Unity.com", "https://adhesiveunity.com/")]



@core.route('/')
def index():
    return render_template("index.html", states=states_array, other=Other_Resources)


@core.route('/NationalDonate')
def donate():
    return render_template('donate.html', title="Donate Nationwide", states=states_array, other=Other_Resources)


@core.route('/NationalOrganizations')
def organize():
    return render_template('organize.html', title="National Organizations", states=states_array, other=Other_Resources)


@core.route('/NationalPetitions')
def petitions():
    return render_template('petitions.html', title="National Petitions", states=states_array, other=Other_Resources)


@core.route('/state/<state_code>')
def state(state_code=None):
    if state is None:
        raise ValueError('No state given')
    title = states_dict[state_code]
    return render_template('state_home_page.html', title=title, states=states_array, code=state_code, other=Other_Resources)


@core.route('/state/<state_code>/donate')
def state_donate(state_code=None):
    title = states_dict[state_code]
    try:
        data = state_to_category['Donate'][state_code]
    except KeyError:
        data = []
    return render_template('state_donate.html', title=title, states=states_array, data=data, code=state_code, other=Other_Resources)

@core.route('/state/<state_code>/organizations')
def state_org(state_code=None):
    title = states_dict[state_code]
    try:
        data = state_to_category['Organization'][state_code]
    except KeyError:
        data = []
    return render_template('state_org.html', title=title, states=states_array, data=data, code=state_code, other=Other_Resources)

@core.route('/state/<state_code>/blackbusiness')
def state_biz(state_code=None):
    title = states_dict[state_code]
    try:
        data = state_to_category['Business'][state_code]
    except KeyError:
        data = []
    return render_template('state_biz.html', title=title, states=states_array, data=data, code=state_code, other=Other_Resources)
@core.route('/State_list')
def State_list():
    return render_template("States_list.html", states=states_array, other=Other_Resources)
