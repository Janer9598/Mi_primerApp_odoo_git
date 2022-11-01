# -*- coding: utf-8 -*-

from odoo import models, fields, api


class odoo_git_producto(models.Model):
    _name = 'odoo_git.producto'
    _description = 'odoo_git.producto'

    code = fields.Char(string='Código', required=True)
    description = fields.Char(string='Descripción', required=True)
    type_product = fields.Selection([('con', 'Consumible'),
                                     ('alm', 'Almacenable'),
                                     ('ser', 'Servicio')], string='Tipo de producto', default='con')
    unit_price = fields.Float(string='Precio unitario')
    unif_measure = fields.Selection([('lb', 'Libras'),
                                     ('kg', 'Kilos'),
                                     ('cm', 'Centimetros'),
                                     ('uni', 'Unidad')], string='Unidad de medida', default='uni')
    brand = fields.Char(string='Marca')
    country_id = fields.Many2one('res.country', string='País de procedencia')
    attributes_ids = fields.One2many('zue.curso.products.attributes', 'product_id', string='Atributos')
    observations = fields.Text(string='Observaciones')

    _sql_constraints =[
        ('odoo_git_producto_unique','UNIQUE(code)','Ya existe un producto con este codigo, por favor verique.')
    ]