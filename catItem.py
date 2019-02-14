import sqlalchemy
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Items, User

# opening connection with database

engine = sqlalchemy.create_engine('sqlite:///CatItems.db')
Base.metadata.bind = engine
# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create Fake user

user1 = User(name="Aya",
             picture='https://pbs.twimg.com/profile_images/2671170543/'
                     '18debd694829ed78203a5a36dd364160_400x400.png',
             email="aya.nasser.mohammed@gmail.com")
session.add(user1)
session.commit()

# adding Category
Category1 = Category(name="Mathematics", user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Mechanics", user_id=1)
session.add(Category2)
session.commit()

Category3 = Category(name="Biomedical Engineering", user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Programming", user_id=1)
session.add(Category4)
session.commit()

# adding items for each category

Math_1 = Items(name="Math 1", user_id=1,
               description="The SAT Subject Test in Mathematics Level 1 "
                           "(formerly known as Math I or MathIC"
                           "(the 'C' representing the use of a calculator)) "
                           " is the name of a one-hour"
                           " multiple choice test given on algebra, "
                           "geometry, basic trigonometry,"
                           " algebraic functions, elementary "
                           "statistics and basic foundations "
                           "of calculus by The College Board.",
               category=Category1)
session.add(Math_1)
session.commit()

Algorithms = Items(name="Algorithms and Data structures ", user_id=1,
                   description="Data Structures and Algorithms - Defined. "
                               "A data structure is an arrangement"
                               " of data in "
                               "a computer's memory or even disk "
                               "storage. An example of "
                               "several common data structures are"
                               " arrays, linked lists,"
                               " queues, stacks, binary trees, and "
                               "hash table.",
                   category=Category4)
session.add(Algorithms)
session.commit()

Math_2 = Items(name="Math 2 ", user_id=1,
               description="The SAT Subject Test in Mathematics Level 1 "
                           "(formerly known as Math I or "
                           "MathIC (the 'C' representing the use"
                           " of a calculator)) "
                           " is the name of a one-hour multiple "
                           "choice test given"
                           " on algebra, geometry, basic trigonometry,"
                           " algebraic functions, elementary statistics "
                           "and basic foundations of calculus "
                           "by The College Board.",
               category=Category1)
session.add(Math_2)
session.commit()

Languages = Items(name="Programming Languages", user_id=1,
                  description="A programming language is a formal"
                              " language, "
                              "which comprises a set of instructions "
                              "used to "
                              "produce various kinds of output."
                              " Programming languages are "
                              "used to create programs that "
                              "implement specific algorithms,",
                  category=Category4)
session.add(Languages)
session.commit()

Math_3 = Items(name="Math 3", user_id=1,
               description="repertoire of functions to include "
                           "polynomial, rational, and"
                           " radical functions."
                           " ... The standards in the integrated"
                           " Mathematics III course"
                           " come from the following"
                           " conceptual categories: "
                           "Modeling, Functions, Number and "
                           "Quantity, Algebra, Geometry, "
                           "and Statistics and "
                           "Probability.",
               category=Category1)
session.add(Math_3)
session.commit()

Biomedical_systems = Items(name="Biomedical systems", user_id=1,
                           description="Biomedical engineering,"
                                       " or bioengineering, "
                                       "is the application of"
                                       " engineering "
                                       "principles "
                                       "to the fields of biology "
                                       "and health care."
                                       " Bioengineers work with doctors, "
                                       "therapists and researchers"
                                       " to develop systems,"
                                       " equipment"
                                       " and devices in order to solve"
                                       " clinical problems,",
                           category=Category3)
session.add(Biomedical_systems)
session.commit()

Fluid = Items(name="Fluid", user_id=1,
              description=" Fluid mechanics is the branch "
                          "of physics concerned with "
                          "the mechanics of fluids and "
                          "the forces on them. "
                          " Fluid mechanics has a wide "
                          "range of applications, "
                          "including mechanical engineering,"
                          " civil engineering, "
                          " chemical engineering, biomedical"
                          " engineering, geophysics, "
                          "astrophysics, and biolog",
              category=Category2)
session.add(Fluid)
session.commit()

Thermo = Items(name="Thermodynamics", user_id=1,
               description="    the branch of physical"
                           " science that deals with the "
                           "relations between heat "
                           "and other forms of energy "
                           " (such as mechanical,"
                           " electrical, or chemical energy), and, "
                           "by extension, of the "
                           "relationships between all forms of energy.",
               category=Category2)
session.add(Thermo)
session.commit()

Anatomy = Items(name="Anatomy", user_id=1,
                description="the branch of science concerned"
                            " with the bodily structure"
                            " of humans, animals, and other"
                            " living organisms,"
                            " especially as revealed by dissection"
                            " and the separation of parts."
                            "he studied physiology and anatomy",
                category=Category3)
session.add(Anatomy)
session.commit()

# printing Category


items = session.query(Category).all()

for item in items:
    print(item.name)
# printing Items of Category
items = session.query(Items).all()

for item in items:
    print(item.name + " ( " + item.category.name + " ) ")
