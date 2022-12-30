from taskmanager import db


# We are creating 2 seperate tables - represented by class-based models
# using SQLAlchemy's ORM - each class uses the declarative base from the
# SQLAlchemy model

# Each table will have a unique ID used for the primary key (Integers that
# will auto increment)

# As we are using Flask-SQLAlchemy we don't need to import each column type at
# the top of the file - The db variable contains each of these already - so
# allows us to use dot notation to specify column data types

# Each model also needs a function __repr__ that takes itself as the argument
# (like this in JS). It is a standard Python function which stands for
# represent - it means to represent the class objects as a string

# unique=True - makes sure each new category added to the database is unique
# nullable=False - this makes sure that field isn't empty or blank,
# makes it a required field


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self


# CATEGORY TABLE NOTES
# db.relationship - not a visible column on the table - it references a one to
# many relationship (category < tasks)

# To link we need to specify which table is being targeted ("Tasks")
# & use a backref - this establishes the bidirectional relationship

# Cascade - will find all the related tasks and delete them

# Lazy=True - means that when we query the database for categories, it can
# simutaneously identify any task linked to the categories


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id",
                            ondelete="CASCADE"), nullable=False
                            )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )


# TASKS TABLE NOTES
# category_id - this uses the Category table as a foreign key
# ondelete="CASCADE" - this is added to the foreign key - so that if the
# foreign key entry is deleted it will cascade and delete any tasks that are
# linked to it - preventing errors

# If using a foreign key a relationship needs to be set up in the table that
# it is being pulled from

# when returning a string from the task class we could have just returned
# the task name like the category table
# the above uses some python formatting to include different columns
# the {0}, {1}, {2} are placeholders - the .format() specifies what these are

# we could have alternatively used f"{strings}" -
# return f"#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"
