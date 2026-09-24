"""
User model.
Owner: Member 1 (Auth)
"""


class User:
    def __init__(self, name, phone, email, gender, governorate,
                 password, age, national_id, role="user"):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.governorate = governorate
        self.password = password
        self.age = age
        self.national_id = national_id
        self.role = role  # "user" or "admin"

    def is_admin(self):
        return self.role == "admin"

    def to_dict(self):
        """Convert User object to a dict — used before saving to JSON."""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "governorate": self.governorate,
            "password": self.password,
            "age": self.age,
            "national_id": self.national_id,
            "role": self.role,
        }

    @staticmethod
    def from_dict(data):
        """Build a User object back from a dict loaded from JSON."""
        return User(
            name=data.get("name"),
            phone=data.get("phone"),
            email=data.get("email"),
            gender=data.get("gender"),
            governorate=data.get("governorate"),
            password=data.get("password"),
            age=data.get("age"),
            national_id=data.get("national_id"),
            role=data.get("role", "user"),
        )

    def __repr__(self):
        return f"User({self.name}, {self.email}, role={self.role})"
