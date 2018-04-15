{
    'name': "Dietetic",
    'version': '10.0.0.1',
    'category': 'Test',
    'author': "Amebalibre",
    'website': "http://www.???.es",
    'depends': [
        'base',
    ],
    'data': [
        'data/eatable_demo.xml',
        'views/category_views.xml',
        'views/eatable_views.xml',
        'views/eatable_eatable_rel_views.xml',
        'views/measure_views.xml',
        'views/season_views.xml',
        # 'views/price_views.xml',
        'views/sidemenu_views.xml',
    ],
    'post_init_hook': 'populate_post_init_hook',
    'application': True,
}
