Expensipy
==
A python interface to Expensify's API.

[Expensify's API is documented here](https://integrations.expensify.com/Integration-Server/doc/), but it's pretty horrifying to use so this project attempts to at least cover up some of the horror.

Example
--
```python
import expensipy

# These are not your normal Expensify login credentials. You can find your
# 'integration' credentials by visiting https://www.expensify.com/tools/integrations/
# while logged in.
userid = "integration_username"
secret = "integration_password"

ex = expensipy.Expensify(userid, secret)
reports = ex.reports("Personal")
for report_id, report in reports.iteritems():
    print "Report %s has %d transactions:" % (report['name'],
        len(report['transactions']))
    for transaction in report['transactions']:
        print " * %2.2f %s at merchant %s" % (transaction['amount'] / 100.0,
            transaction['currency'], transaction['merchant'])
```

```
Report Personal has 4 transactions:
 * 1.01 EUR at merchant Test
 * 1.04 USD at merchant Test Currency
 * 4.50 EUR at merchant Lemon
 * 18.00 EUR at merchant Fudge
```

Bugs
--
Probably plenty! Don't use this for anything important.

Contributing
--
Pull requests welcome!
