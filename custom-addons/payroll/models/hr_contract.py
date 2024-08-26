from odoo import models, fields

class HrContract(models.Model):
    _inherit = 'hr.contract'

    salary_structure_id = fields.Many2one('payroll.structure', string='Salary Structure')
    wage = fields.Float(string='Wage', related='salary_structure_id.line_ids.amount', readonly=True)
