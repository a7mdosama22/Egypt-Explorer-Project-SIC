class User:
    """Represents one registered user (normal user or admin)."""

    def __init__(self, name, phone, email, gender, governorate,
                 password, age, national_id, is_admin=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.governorate = governorate
        self.password = password
        self.age = age
        self.national_id = national_id
        self.is_admin = is_admin

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "governorate": self.governorate,
            "password": self.password,
            "age": self.age,
            "national_id": self.national_id,
            "is_admin": self.is_admin,
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", ""),
            gender=data.get("gender", ""),
            governorate=data.get("governorate", ""),
            password=data.get("password", ""),
            age=data.get("age", 0),
            national_id=data.get("national_id", ""),
            is_admin=data.get("is_admin", False),
        )

    def __repr__(self):
        return f"User({self.name}, {self.email}, admin={self.is_admin})"