from odoo import models, fields

class PayrollCompliance(models.Model):
    _name = 'payroll.compliance'
    _description = 'Payroll Compliance'

    name = fields.Char(string='Compliance Name')
    country_id = fields.Many2one('res.country', string='Country')
    tax_rate = fields.Float(string='Tax Rate (%)')
    currency_id = fields.Many2one('res.currency', string='Currency')
