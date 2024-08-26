from odoo import models, fields, api

class SalaryComponent(models.Model):
    _name = 'salary.component'
    _description = 'Salary Component'

    name = fields.Char(string='Component Name', required=True)
    type = fields.Selection([('earnings', 'Earnings'), ('deductions', 'Deductions')], string='Type', required=True)
    calculation_method = fields.Selection([('fixed', 'Fixed'), ('percentage', 'Percentage')], string='Calculation Method', required=True)
    amount = fields.Float(string='Amount')
    percentage = fields.Float(string='Percentage')

class PayrollStructure(models.Model):
    _name = 'payroll.structure'
    _description = 'Payroll Structure'

    name = fields.Char(string='Name', required=True)
    component_ids = fields.Many2many('salary.component', string='Salary Components')

class Payslip(models.Model):
    _name = 'payroll.payslip'
    _description = 'Payslip'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date = fields.Date(string='Date', required=True)
    structure_id = fields.Many2one('payroll.structure', string='Payroll Structure', required=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount')

    @api.depends('structure_id.component_ids')
    def _compute_total_amount(self):
        for payslip in self:
            total = 0.0
            for component in payslip.structure_id.component_ids:
                if component.calculation_method == 'fixed':
                    total += component.amount
                elif component.calculation_method == 'percentage':
                    total += (component.percentage / 100) * payslip.employee_id.contract_id.wage
            payslip.total_amount = total
