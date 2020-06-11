from flask import render_template, Blueprint
core = Blueprint('core', __name__)
states_a = ["California", "Texas", "Minnesota"]
states_array = sorted(states_a)
dict = {
    "cali_Content" :  "This is where Cali links and content will go.",
    "texas_Content" : "This is where Texas links and content will go.",
    "minn_Content" : "This is where Minnesota links and content will go."
}

@core.route('/')
def index():
    return render_template("index.html", states=states_array)

@core.route('/NationalDonate')
def donate():
    return render_template('donate.html', title="Donate")

@core.route('/NationalOrganizations')
def organize():
    return render_template('organize.html')

@core.route('/NationalPetitions')
def petitions():
    return render_template('petitions.html', title="National Petitions")

@core.route('/CampaignZero')
def zero():
    return render_template('campaign.html')

@core.route('/Texas')
def Texas():
    return render_template('Texas.html', title="Texas", Content=dict["texas_Content"], states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Businesses TX", "core.Tex_biz"))

@core.route('/Texas/donate')
def Texas_donate():
    return render_template('Texas_donate.html', title="Texas", Content=dict["texas_Content"], states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"))

@core.route('/Texas/organizations')
def Texas_org():
    return render_template('Texas_org.html', title="Texas", Content=dict["texas_Content"], states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"))

@core.route('/Texas/BlackBusiness')
def Tex_biz():
    return render_template('Texbiz.html', title="Texas", Content=dict["texas_Content"], states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"))

@core.route('/California')
def Cali():
    return render_template('Cali.html', title="California", Content=dict["cali_Content"], states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA","core.Cali_biz") )

@core.route('/California/donate')
def Cali_donate():
    return render_template('Cali_donate.html', title="California", Content=dict["cali_Content"], states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA","core.Cali_biz") )

@core.route('/California/organizations')
def Cali_org():
    return render_template('Cali_org.html', title="California", Content=dict["cali_Content"], states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA","core.Cali_biz") )

@core.route('/California/BlackBusiness')
def Cali_biz():
    return render_template('Calibiz.html', title="California", Content=dict["cali_Content"], states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA","core.Cali_biz") )

@core.route('/Minnesota')
def MN():
    return render_template('Minnesota.html', title="Minnesota", Content=dict["minn_Content"], states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz") )

@core.route('/Minnesota/donate')
def MN_donate():
    return render_template('MN_donate.html', title="Minnesota", Content=dict["minn_Content"], states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz") )

@core.route('/Minnesota/organizations')
def MN_org():
    return render_template('MN_org.html', title="Minnesota", Content=dict["minn_Content"], states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz") )

@core.route('/Minnesota/BlackBusiness')
def MN_biz():
    return render_template('MNbiz.html', title="Minnesota", Content=dict["minn_Content"], states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz") )
