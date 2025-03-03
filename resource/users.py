from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_number: str
    month: str
    year: str
    day:str
    gender: str
    subjects: str
    hobbies: str
    images: str
    current_address: str
    state: str
    city: str


new_user = User(
    first_name ='vlad',
    last_name = 'biryukov',
    user_email = '123@gmail.com',
    user_number = '1234567890',
    month = 'January',
    year = '2008',
    day = '27',
    gender =  'Male',
    hobbies='Sports',
    images = 'photo.png',
    current_address = 'pushkina 1',
    subjects='Maths',
    state = 'NCR',
    city = 'Delhi',
)