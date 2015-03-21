#
#    Copyright (C) 2015  Jonathan Finlay <jfinlay@riseup.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openerp.osv import osv, fields

_campaign_states = [
    ('draft', 'Draft'),
    ('progress', 'In progress'),
    ('done', 'Done'),
    ('cancel', 'Cancel')
]

class Campaign(osv.osv):
    """
    Class to configure data extraction campaigns
    """
    _name = 'swarm.campaign'
    _description = __doc__

    _columns = {
        'name': fields.char('Name'),
        'init_date': fields.datetime('Start date'),
        'end_date': fields.datetime('End date'),
        'tags_ids': fields.many2many('swarm_campaign_tag', 'swarm_campaign_tag_rel',
                                     'campaign_id', 'tag_id', 'Tags'),
        'max_items': fields.integer('Max items'),
        'state': fields.selection(_campaign_states, 'State'),
    }

class CampaignTag(osv.osv):
    """
    Campaign tags
    """
    _name = 'swarm.campaign.tag'
    _description = __doc__

    _columns = {
        'name', fields.char('Name')
    }