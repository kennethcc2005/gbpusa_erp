# -*- coding: utf-8 -*-
from openerp import models, fields
class ProductList(models.Model):
    # _name = 'gbpusa_product.list'
    _name = 'gbpusa_product.list'
    is_done = fields.Boolean('Done?')
    active = fields.Char('Active Status', required=True)
    product_type = fields.Char('Type', required=True)
    item = fields.Char('Item', required=True)
    description_product = fields.Char('Description')
    tax_code = fields.Char('Sales Tax Code', required=True)
    account = fields.Char('Account', required=True)
    account_cogs = fields.Char('COGS Account')
    account_asset = fields.Char('Asset Account')
    depreciation_accumulated = fields.Integer('Accumulated Depreciation', required=True)
    description_purchase = fields.Char('Purchase Description')
    quantity_on_hand = fields.Integer('Quantity On Hand')
    cost = fields.Float('Cost', required = True)
    vendor_preferred = fields.Char('Preferred Vendor')
    agency_tax = fields.Char('Tax Agency')
    price = fields.Char('Price', required = True)
    reorder = fields.Char('Reorder Pt (Min)')
    MPN = fields.Char('MPN')


