{
    "name":"rif_odoo_2025_employee_part_2025",
    "sumarry":"building and testing rif_odoo_employee_part_2025 to be added in the official project",
    "version":"1.0",
    "license":":LGPL-3",
    "depends":[],
    "data":[
        #security
                #contrat
                "security/contrat_access.xml",
                #departement
                "security/departement_access.xml",
                #employee
                "security/employee_access.xml",
                #test_candidat
                "security/test_candidat_access.xml",
            "security/ir.model.access.csv",
        #views
            #contrat
                "views/contrat_views.xml",
                "views/contrat_menus.xml",
            #departement
                "views/departement_views.xml",
                "views/departement_menus.xml",
            #employee
                "views/employee_views.xml",
                "views/employee_menus.xml",
            #test_candidat
                "views/test_candidat_views.xml",
                "views/test_candidat_menus.xml",
            

    ],
    "demo":[],
    "assets":{}
}