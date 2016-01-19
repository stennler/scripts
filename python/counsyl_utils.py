

def import_counsyl_utils():
    global fake_profile
    import counsyl.product.my.utils.fake as fake
    fake_profile = fake.fake_profile
