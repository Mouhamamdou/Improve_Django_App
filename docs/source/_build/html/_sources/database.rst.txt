Database Structure and Data Models
==================================

The database is structured as follows:

- **User:** Standard Django user model.
- **Profile:** Extends the user model with additional information.
  - Fields: user, favorite_city
- **Letting:** Represents a property letting.
  - Fields: title, address

The models are defined in the `models.py` file of each app.

