from setuptools import setup, find_packages

setup(
    name='tw2.jqplugins.tagify',
    version='2.0b1',
    description='Tagify for ToscaWidgets2',
    author='Greg Jurman',
    author_email='gdj2214@rit.edu',
    url='https://github.com/gregjurman/tw2.jqplugins.tagify/',
    install_requires=[
        "tw2.core",
        'mako',
        'tw2.forms',
        'tw2.jqplugins.ui',
        ## Add other requirements here
        # "Genshi",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2', 'tw2.jqplugins'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jqplugins.tagify
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
