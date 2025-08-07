from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
#logging for print data in server console
import logging
_logger = logging.getLogger(__name__)

class Employee(models.Model):
    _name="employee.rif.2025"
    _description="employee_rif_2025"

    #need to use session user to compare data from candidat
    session_user = fields.Many2one("res.users",string="Session User",readonly=True,
        compute="_compute_session",store=False)
    session_user_name=fields.Char(string=_("session user name:"),readonly=True,
        compute="_compute_session",store=False)
    session_user_email=fields.Char(string=_("session user email:"),readonly=True,
        compute="_compute_session",store=False)

    #force the context with the session data
    @api.depends_context('uid')
    def _compute_session(self):
        for rec in self:
            #fetch the user session
            user = self.env.user
            rec.session_user = user
            rec.session_user_name = user.name
            rec.session_user_email = user.email
    #        _logger.info(str({
    #    "session_user_name":rec.session_user_name,
    #    "session_user_email":rec.session_user_email,
    # }))
    
    
    # employee get all the data from candidat
    # that's why i need a relation if it dosent exist to get the data and filter it
    # filtrying will be in func
    #  replace with the real candidat.model
    _inherits={"test_candidat.rif.2025":"employee_data_candidat"}
    
   #employee_data_candidat=fields.Many2one("test_candidat.rif.2025",compute="_compute_data_of_employee_candidat")
    employee_data_candidat=fields.Many2one("test_candidat.rif.2025",ondelete="cascade",onupdate="cascade")
    #i cant override the default_get() twice here so i will get the session with the records
    @api.model
    def default_get(self,fields_list):
        defaults=super().default_get(fields_list)
        #fetch user session
        user=self.env.user
        defaults['session_user'] = user
        defaults['session_user_name']=user.name
        defaults['session_user_email']=user.email     
        return defaults
    #now i will create a rh field and set it to True
    #so i can controle it in view
    rh=fields.Boolean()
    #now i will try to reset the rh fields if modified
    @api.onchange("employee_data_candidat")
    def departement_rh(self):
        for i in self:
            #fetch user data from candidat
            #candidat=self.env["test_candidat.rif.2025"].search([('email','=',i.session_user_email)],limit=1)
            candidat=self.env["test_candidat.rif.2025"].search([('email','=','test@mail.com')],limit=1)
            if(candidat):
                if(candidat.is_accepted):    
                    if(candidat.departement=='rh'):
                        if(candidat.poste=='rh'):
                            i.rh=True
                        else:
                            i.rh=False
                    else:
                        i.rh=False
                if(i.rh==False):
                    raise ValidationError(_("you can't change those fields"))
                i.employee_data_candidat = candidat
            
            
    
    
    
