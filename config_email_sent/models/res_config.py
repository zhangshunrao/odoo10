# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BaseConfigSettings(models.TransientModel):

    _inherit = "base.config.settings"

    can_sent_email = fields.Boolean(string=u'允许发送邮件',
                                    default=False,
                                    help=u'勾选允许发送邮件，否则不允许发送邮件')

    @api.model
    def get_default_can_sent_email(self, fields):
        return {
            'can_sent_email': True if self.env['ir.config_parameter'].get_param('can_sent_email', False) == 'true' else False
        }

    @api.multi
    def set_default_can_sent_email(self):
        ir_config = self.env['ir.config_parameter']
        for wizard in self:
            if wizard.can_sent_email:
                ir_config.set_param('can_sent_email', 'true')
            else:
                ir_config.set_param('can_sent_email', 'false')