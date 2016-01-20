from counsyl.product.my.models import CustomerProfile
from prettytable import PrettyTable


def get_profiles():
    """Returns a QuerySet of all the CustomerProfiles sorted by create_date"""
    return CustomerProfile.objects.all().order_by('create_date')


def get_cp_attributes(cp):
    """Returns a dictionary of string representations of CustomerProfile attributes"""   # nopep8

    if not isinstance(cp, CustomerProfile):
        raise TypeError("Not a Customer Profile: %s" % str(cp))

    # Set Defaults
    atts = {
        'pk': '[No PK]',
        'name': '[No Name]',
        'gender': '[No Gender]',
        'email': '[No Email]',
        'account': '[No Account]',
        'external_id': '[No External ID]',
        'barcode': '[No Barcode]',
        'product': '[No Product]',
        'disease_panel': '[No Disease Panel]',
        'price': '[No Price]',
        'state': '[No State]',
        }

    atts['pk'] = cp.pk
    atts['external_id'] = cp.external_id
    if cp.person:
        if cp.person.fullname:
            atts['name'] = cp.person.fullname
        if cp.person.gender:
            atts['gender'] = "Female" if str(cp.person.gender) == "F" else "Male"  # nopep8
    if cp.account:
        atts['account'] = repr(cp.account)
        if cp.account.email:
            atts['email'] = cp.account.email
    if cp.order:
        if cp.order.barcode:
            atts['barcode'] = cp.order.barcode
        if cp.order.product:
            atts['product'] = cp.order.product
        if cp.order.disease_panel:
            atts['disease_panel'] = cp.order.disease_panel
        if cp.order.total:
            atts['price'] = cp.order.total
        if cp.order.state:
            atts['state'] = cp.order.state.desc
    return atts


def show_profiles(short=False):
    """Dumps and returns all CustomerProfiles - short option dumps on one line"""  # nopep8
    all_cps = get_profiles()
    if short:

        labels = ['pk', 'Name', 'Email', 'Account']  # Label
        attrib = ['pk', 'name', 'email', 'account']  # Key

        t = PrettyTable(labels)
        t.align = 'l'
        for cp in all_cps:
            atts = get_cp_attributes(cp)
            row_atts = [atts[att_name] for att_name in attrib]
            t.add_row(row_atts)
        print (t)
    else:
        for cp in all_cps:
            show_profile(cp)
    return all_cps


def show_profile(cp=None, short=False):
    """Dumps and returns a human readable version of the CustomerProfile object

       No params: Dumps and returns all CustomerProfiles as a QuerySet.
       First Param is integer: Dump and return the 'x'th CustomerProfile.
       First Param is a Customer Profile Object: Dump and return it.
       short kwarg dumps all profiles on one line.
    """

    if cp is None:
        return show_profiles(short)
    if isinstance(cp, int):
        return show_profile(CustomerProfile.objects.get(pk=cp))

    labels = ['Name',
              'Email',
              'Gender',
              'Account',
              'External ID',
              'Barcode',
              'Product',
              'Disease Panel',
              'Price',
              'State']
    atts = get_cp_attributes(cp)
    atts_column = [atts['name'],
                   atts['email'],
                   atts['gender'],
                   atts['account'],
                   atts['external_id'],
                   atts['barcode'],
                   atts['product'],
                   atts['disease_panel'],
                   atts['price'],
                   atts['state']]

    t = PrettyTable()
    t.add_column("#%s" % atts['pk'], labels)
    t.add_column("Customer Profile Data", atts_column)
    t.align = 'l'
    print(t)
    print("")
    return cp
