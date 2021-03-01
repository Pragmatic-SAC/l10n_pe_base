# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PragmaticSunatResource(models.Model):
    _name = "pragmatic.catalog.tmpl"
    _description = "Khatu Sunat Resources."

    name = fields.Char(string="Name", index=True, required=True)
    code = fields.Char(string="Code", index=True, required=True)
    active = fields.Boolean(string="Active", default=True)

    def name_get(self):
        result = []
        for table in self:
            l_name = "%s - %s" % (table.code, table.name)
            result.append((table.id, l_name))
        return result
