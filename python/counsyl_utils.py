from counsyl.product.my.models import CustomerProfile


def show_profile(cp=None):
    """Dumps a human readable version of the CustomerProfile object.

       No params: Dump first 10 CustomerProfiles. Returns CustomerProfile.objects.all()  # nopep8
       First Param is integer: Dump the 'x'th CustomerProfile.
       First Param is a Customer Profile Object: Dump it.
    """

    if cp is None:
        max_idx = 10
        all_cps = CustomerProfile.objects.all()
        for i in range(min(max_idx, len(all_cps))):
            print ("----CustomerProfile[%d]----" % i)
            show_profile(all_cps[i])
            print ("")
        return CustomerProfile.objects.all()

    if isinstance(cp, int):
        return show_profile(CustomerProfile.objects.all()[cp])

    print ("Primary Key: \t" + str(cp.pk))

    name = "[No Name]"
    gender = "[No Gender]"
    if cp.person:
        if cp.person.fullname:
            name = cp.person.fullname
        if cp.person.gender:
            gender = "Female" if str(cp.person.gender) == "F" else "Male"

    email = "[No Email]"
    if cp.account and cp.account.email:
        email = cp.account.email

    barcode = "[No Barcode]"
    product = "[No Product]"
    disease_panel = "[No Disease Panel]"
    price = "[No Price]"
    state = "[No State]"
    if cp.order:
        if cp.order.barcode:
            barcode = cp.order.barcode
        if cp.order.product:
            product = cp.order.product
        if cp.order.disease_panel:
            disease_panel = cp.order.disease_panel
        if cp.order.total:
            price = cp.order.total
        if cp.order.state:
            state = cp.order.state

    print ("Name:\t\t" + name)
    print ("Email:\t\t" + email)
    print ("Gender:\t\t" + gender)
    print ("External Id:\t" + cp.external_id)
    print ("Barcode:\t" + str(barcode))
    print ("Product:\t" + str(product))
    print ("Disease Panel:\t" + str(disease_panel))
    print ("Price:\t\t" + str(price))
    print ("State:\t\t" + str(state))
    return cp
