from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = [
        ('email_unique',
         'unique(email)',
         'Email has to be unique!')
    ]
