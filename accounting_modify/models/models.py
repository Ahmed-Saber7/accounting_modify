# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'


