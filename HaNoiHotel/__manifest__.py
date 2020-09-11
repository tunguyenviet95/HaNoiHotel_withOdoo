{
    'name': 'Ha Noi Hotel',
    'version': '1.1',
    'category': 'Manager',
    'sequence': 1,
    'summary': "This module provides tasks related to hotel management",
    'description': "This module provides tasks related to hotel management",
    'author': "Nguyen Ngoc Hai, Nguyen Viet Tu, Duong Trung Hieu",
    'website': '',
    'depends': [
        'base',
    ],
    'data': [
        'views/promotion.xml',
        'views/booking.xml',
        'views/service.xml',
        'data/promotion_data_default.xml',
        'data/service_data_default.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
