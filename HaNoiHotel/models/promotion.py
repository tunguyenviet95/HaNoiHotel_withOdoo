from odoo import api, fields, models


class Promotion(models.Model):
    _name = 'promotion'

    name = fields.Char(string='Name')
    promotion = fields.Float(string='Promotion')
    description = fields.Char(string='Description')
    start_date = fields.Date(string='Start Date')
    expiration_date = fields.Date(string='Expiration Date')
    booking_ids = fields.One2many(comodel_name='booking', inverse_name='promotion', string='booking_ids')