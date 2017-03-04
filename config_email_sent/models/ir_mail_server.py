# -*- coding: utf-8 -*-
from odoo import api, models


class IrMailServer(models.Model):

    _inherit = "ir.mail_server"

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False):
        if self.env['ir.config_parameter'].get_param('can_sent_email', 'false') == 'false':
            return False
        res = super(IrMailServer, self).send_email(self, message, mail_server_id=mail_server_id,
                                                   smtp_server=smtp_server, smtp_port=smtp_port,
                                                   smtp_user=smtp_user, smtp_password=smtp_password,
                                                   smtp_encryption=smtp_encryption,
                                                   smtp_debug=smtp_debug)

        return res
