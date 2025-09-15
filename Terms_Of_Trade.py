def terms_of_trade(index_of_export_price, index_of_import_price):

    tot = (index_of_export_price / index_of_import_price) * 100

    return tot


index_of_export = 150
index_of_import = 50

print('Term of Trade is ', terms_of_trade(index_of_export, index_of_import))
