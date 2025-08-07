#testing dummy models
#candidat comes first at load
from . import test_candidat
#
#here odoo will load departement first then contrat then employee
from . import departement,contrat
from . import employee
#if the models are not in the order you need to see the csv file in/security and put the rules in the order
