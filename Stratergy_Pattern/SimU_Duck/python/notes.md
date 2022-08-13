The first version :

- One super class inherited by multiple subclasses

Issues:
- Allows access to unnecessary and incorrect behaviour to a few subclasses
- Subclasses need to override functions to define their functionality : leading to no code reuse in case of same behaviour for multiple Subclasses

Solution 1:

