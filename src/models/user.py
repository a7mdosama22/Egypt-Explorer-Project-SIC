class User:
    def __init__(self, name, phone, email, gender, governorate, password, age, user_type="normal"):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.governorate = governorate
        self.password = password
        self.age = age
        self.user_type = user_type

    def is_admin(self):
        return self.user_type == "admin"

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender,
            "governorate": self.governorate,
            "password": self.password,
            "age": self.age,
            "type": self.user_type
        }

    @staticmethod
    def from_dict(data):
        user_type = data.get("type", "normal")

        if user_type == "admin":
            return Admin(
                name=data.get("name", ""),
                phone=data.get("phone", ""),
                email=data.get("email", ""),
                gender=data.get("gender", ""),
                governorate=data.get("governorate", ""),
                password=data.get("password", ""),
                age=data.get("age", 0),
            )

        return NormalUser(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", ""),
            gender=data.get("gender", ""),
            governorate=data.get("governorate", ""),
            password=data.get("password", ""),
            age=data.get("age", 0),
        )


class NormalUser(User):
    def __init__(self, name, phone, email, gender, governorate, password, age):
        super().__init__(name, phone, email, gender, governorate, password, age, "normal")


class Admin(User):
    def __init__(self, name, phone, email, gender, governorate, password, age):
        super().__init__(name, phone, email, gender, governorate, password, age, "admin")