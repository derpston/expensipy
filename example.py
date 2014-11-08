import expensipy

# These are not your normal Expensify login credentials. You can find your
# 'integration' credentials by visiting https://www.expensify.com/tools/integrations/
# while logged in.
userid = "integration_username"
secret = "integration_password"

ex = expensipy.Expensify(userid, secret)
reports = ex.reports("Personal")
for report_id, report in reports.iteritems():
    print "Report %s has %s transactions:" % (report['name'], len(report['transactions']))
    for transaction in report['transactions']:
        print " * %2.2f %s at merchant %s" % (transaction['amount'] / 100.0,
            transaction['currency'], transaction['merchant'])

