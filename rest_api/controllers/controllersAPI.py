from operator import index

from odoo import http
from odoo.http import request


class helloapi(http.Controller):


    @http.route('/api', type='json', auth='public', website=False, methods=['GET', 'POST'], csrf=False)
    def hello(self, **kw):
        contact_user = http.request.env['res.partner'].sudo().search(
            [('id', '=', kw['id'])])
        contact_user.write({'name': kw['name'],
                            'phone': kw['phone'], })

       #http.request.env['res.partner'].sudo().create({'name':kw['name']})
       #to create a new contact
        return kw
        # postman{
        #     "params": {
        #                   "name": "odoo",
        #                   "id": 9,
        #                   "email": "benzina@gmail.com"
        #
        #               }
    @http.route('/api/delete', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_contact_field(self, **kw):
            # Get the contact record by ID
        contact_user = request.env['res.partner'].sudo().search([('id', '=', kw['id'])])
        if not contact_user:
             return {"error": "Contact not found"}

            # Update the contact by removing the specified field's value (e.g., name)
        #contact_user.write({'email': False})
        contact_user.unlink()
        return {"success": "Field 'name' deleted for contact with ID %s" % kw['id']}

        # contacts = http.request.env['res.partner'].sudo().search([])
        #
        # contact_list = [
        #
        # ]
        # for contact in contacts:
        #     contact_list.append(
        #         {
        #             'name': contact.name,
        #             'email': contact.email,
        #         }
        #     )
        # return contact_list

    @http.route('/api/update', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_contact(self, **kw):
        # Find the contact by ID
        contact_user = request.env['res.partner'].sudo().search([('id', '=', kw['id'])])
        if not contact_user:
            return {"error": "Contact not found"}

        # Update the contact with provided fields
        update_data = {}
        if 'name' in kw:
            update_data['name'] = kw['name']
        if 'email' in kw:
            update_data['email'] = kw['email']
        # Add other fields as needed
        contact_user.write(update_data)

        return {"success": "Contact updated successfully", "updated_fields": update_data}