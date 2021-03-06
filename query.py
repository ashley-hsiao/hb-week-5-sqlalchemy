"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

# db.session.query(Brand).get(8)
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

# db.session.query(Model).filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.

# db.session.query(Model).filter(Model.year < 1960).all()
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

# db.session.query(Brand).filter(Brand.founded > 1920).all()
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

# db.session.query(Model).filter(Model.name.like('Cor%')).all()
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

# db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()
# db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()
# Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()


# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

# Brand.query.filter( db.or_(Brand.discontinued != None, Brand.founded < 1950) ).all()
# Brand.query.filter( db.or_(Brand.discontinued.is_(None), Brand.founded < 1950) ).all()
# Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950) ).all()
Brand.query.filter( (Brand.discontinued.is_(None)) | (Brand.founded < 1950) ).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    '''
    Fill in get_model_info so that it takes a year as input, and prints each 
    model’s name, brand_name and brand headquarters for each car model from that year.
    '''

    db.session.query(Model.name, Model.brand_name, Brand.headquarters).join

    models = db.session.query(Model).filter(Model.year == year).all()

    for model in models:
        print model.name, model.brand_name, brand.headquarters

    # Need to figure out how to get the brand's headquarters
    # join tables???


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The returned value is <flask_sqlalchemy.BaseQuery object at 0x10257df90>, an object.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is a table whose main purpose is to link two tables together,
# helping to manage the Many to Many relationship between these two tables. It serves
# as the connection between the two tables, so that the relationships can be One to
# Many, and the two tables can access each other's information through the association
# table.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
