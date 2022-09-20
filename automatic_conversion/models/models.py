# -*- coding: utf-8 -*-
import pdfkit
from odoo.tools.misc import find_in_path
import os
import base64
from odoo import models, fields, api
from odoo.modules import get_module_resource


class automatic_conversion(models.Model):
    _name = 'automatic_conversion.automatic_conversion'
    _description = 'automatic_conversion.automatic_conversion'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


    def test(self):
        print(find_in_path('wkhtmltopdf'))
        url_guia='http://www.sicm.gob.ve/g_4cguia.php?id_guia='
        inicializar_guia = 30583661
        
        img_path = get_module_resource(
                'guia_sicm', 'static', 'tmp')

        print(img_path,url_guia+str(inicializar_guia))
        pdf = pdfkit.from_url('https://www.google.com', img_path+ '/' +str(inicializar_guia)+'.pdf')
        print(img_path,pdf)