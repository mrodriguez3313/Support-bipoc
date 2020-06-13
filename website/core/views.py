from flask import render_template, Blueprint
core = Blueprint('core', __name__)
states_a = ["California", "Texas", "Minnesota"]
states_array = sorted(states_a)


National_orgs_array = [
    ("American Civil Liberties Union",
     "https://www.aclu.org/issues/racial-justice", "ACLU today is the nation's largest non-profit and non-partisan law firm who select lawsuits that will have the greatest impact for breaking new ground and establishing new precedents that will strengthen American freedoms."),
    ("Black Lives Matter",
     "https://blacklivesmatter.com/", "Founded in response to the aquittal of Trayvon Martin's murderer. BLM's mission is to eradicate white supremacy and build local power to intervene in violence inflicted Black communities by the state and vigilantes."),
    ("Reclaim The Block", "https://www.reclaimtheblock.org/home", ""),
    ("Color of Change", "https://colorofchange.org/", ""),
    ("Advancement Project", "https://advancementproject.org/", ""),
    ("Moms Demand Action", "https://momsdemandaction.org/", ""),
    ("Black Visions Collective", "https://www.blackvisionsmn.org/", ""),
    ("Faith in Texas", "https://faithintx.org/", ""),
    ("Take Action Chapel Hill", "https://www.takeactionch.com/", ""),
    ("Austin Justice Coalition", "https://austinjustice.org/", ""),
    ("Dallas Alliance Against Racial and Political Repression",
     "https://dfwalliance.org/", "")
]


@core.route('/')
def index():
    return render_template("index.html", states=states_array)


@core.route('/NationalDonate')
def donate():
    return render_template('donate.html', title="Donate Nationwide", states=states_array)


@core.route('/NationalOrganizations')
def organize():
    return render_template('organize.html', title="National Organizations", states=states_array, orgs=National_orgs_array)


@core.route('/NationalPetitions')
def petitions():
    return render_template('petitions.html', title="National Petitions", states=states_array)


@core.route('/CampaignZero')
def zero():
    return render_template('campaign.html')


@core.route('/Texas')
def Texas():
    return render_template('Texas.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Businesses TX", "core.Tex_biz"))


@core.route('/Texas/donate')
def Texas_donate():
    return render_template('Texas_donate.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"))


@core.route('/Texas/organizations')
def Texas_org():
    return render_template('Texas_org.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"))


@core.route('/Texas/BlackBusiness')
def Tex_biz():
    return render_template('Texbiz.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"))


@core.route('/California')
def Cali():
    return render_template('Cali.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"))


@core.route('/California/donate')
def Cali_donate():
    return render_template('Cali_donate.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"))


@core.route('/California/organizations')
def Cali_org():
    return render_template('Cali_org.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"))


@core.route('/California/BlackBusiness')
def Cali_biz():
    return render_template('Calibiz.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"))


@core.route('/Minnesota')
def MN():
    return render_template('Minnesota.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"))


@core.route('/Minnesota/donate')
def MN_donate():
    return render_template('MN_donate.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"))


@core.route('/Minnesota/organizations')
def MN_org():
    return render_template('MN_org.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"))


@core.route('/Minnesota/BlackBusiness')
def MN_biz():
    return render_template('MNbiz.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"))
