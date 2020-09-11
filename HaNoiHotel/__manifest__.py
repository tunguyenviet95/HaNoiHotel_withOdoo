{
    'name': 'Ha Noi Hotel',
    'version': '1.0',
    'category': 'Manager',
    'sequence': 1,
    'summary': '',
    'description': "This module provides tasks related to hotel management",
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'views/promotion.xml',
        'views/booking.xml',
        'views/service.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
