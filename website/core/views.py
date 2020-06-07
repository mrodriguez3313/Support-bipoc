from flask import render_template, Blueprint
core = Blueprint('core', __name__)
states_array=["California", "Texas", "Minnesota"]

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
    return render_template('donate.html')

@core.route('/NationalOrganizations')
def organize():
    return render_template('organize.html')

@core.route('/CampaignZero')
def zero():
    return render_template('campaign.html')

# probably do a for loop here to fill in for all states if needed.

@core.route('/Texas')
def Texas():
    return render_template('Texas.html', title="Texas", Content=dict["texas_Content"])

@core.route('/Texas/donate')
def Texas_donate():
    return render_template('Texas_donate.html')

@core.route('/Texas/organizations/')
def Texas_org():
    return render_template('Texas_org.html')

@core.route('/Texas/BlackBusiness')
def Tex_biz():
    return render_template('Texbiz.html')

@core.route('/California')
def Cali():
    return render_template('Cali.html', title="California", Content=dict["cali_Content"])

@core.route('/California/donate')
def Cali_donate():
    return render_template('Cali_donate.html')

@core.route('/California/organizations/')
def Cali_org():
    return render_template('Cali_org.html')

@core.route('/California/BlackBusiness')
def Cali_biz():
    return render_template('Calibiz.html')

@core.route('/Minnesota')
def MN():
    return render_template('Minnesota.html', title="Minnesota", Content=dict["minn_Content"])

@core.route('/Minnesota/donate')
def MN_donate():
    return render_template('MN_donate.html')

@core.route('/Minnesota/organizations/')
def MN_org():
    return render_template('MN_org.html')

@core.route('/Minnesota/BlackBusiness')
def MN_biz():
    return render_template('MNbiz.html')
