from odoo import models, fields, api


class Booking(models.Model):
    _name = 'booking'
    _rec_name = 'id'

    check_in = fields.Date(string='Check-in')
    check_out = fields.Date(string='Check-out')
    amount_adult = fields.Integer(string='Adult')
    amount_child = fields.Integer(string='Child ')
    cost = fields.Float(string='Cost')
    service = fields.Many2many(comodel_name='service', string='Service')
    # room_ids = fields.One2many(comodel_name='room', inverse_name='booking_ids', string='Room')
    promotion = fields.Many2one(comodel_name='promotion', string='Promotion')

    # def _total_price(self):
    #     for booking in self:
    #         total_time = booking.check_out - booking.check_in
    #         total_time = total_time.total_seconds()
    #         price=0
    #         for c in booking.room_ids:
    #             print(c.price_room)
    #             price += c.price_room
    #         if total_time < 172800:
    #             sum_price = price + price * 0.7
    #         elif (total_time > 172800) and (total_time < 432000):
    #             sum_price = price + price * 0.5
    #         else:
    #             sum_price = price + price * 0.2
    #         print(sum_price)
    #         booking.cost = sum_price

