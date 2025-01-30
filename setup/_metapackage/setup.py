import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-akretion-odoo-mail",
    description="Meta package for akretion-odoo-mail Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-mail_filter',
        'odoo10-addon-mail_picking_available',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
