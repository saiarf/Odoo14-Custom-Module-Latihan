from odoo import api, fields, models


class Partner(models.Model):
    _name = 'wedding.partner'
    _description = 'Standar class partners'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='Telepon/HP')
    
