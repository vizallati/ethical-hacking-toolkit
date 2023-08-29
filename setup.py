from faker import Faker

fake = Faker()


def generate_fake_user():
    return {
        'username': fake.user_name(),
        'email': fake.email(),
        'full_name': fake.name(),
        'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d'),
        'password': fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
        'address': fake.address(),
        'phone_number': fake.phone_number()
    }


def generate_fake_users(count):
    return [generate_fake_user() for _ in range(count)]


def save_fake_user_data_to_file(fake_user_list, file_path):
    with open(file_path, 'w') as file:
        for idx, fake_user in enumerate(fake_user_list, start=1):
            file.write(f"Fake User {idx}:\n")
            for key, value in fake_user.items():
                file.write(f"{key}: {value}\n")
            file.write("=" * 30 + "\n")

    print(f"Fake user data written to {file_path}")


num_fake_users = 10

# Generate fake user data three times
fake_user_list_1 = generate_fake_users(num_fake_users)
fake_user_list_2 = generate_fake_users(num_fake_users)
fake_user_list_3 = generate_fake_users(num_fake_users)

# Specify the file paths for the three files
file_path_1 = "fake_user_data_1.txt"
file_path_2 = "fake_user_data_2.txt"
file_path_3 = "fake_user_data_3.txt"

# Save fake user data to each file
save_fake_user_data_to_file(fake_user_list_1, file_path_1)
save_fake_user_data_to_file(fake_user_list_2, file_path_2)
save_fake_user_data_to_file(fake_user_list_3, file_path_3)
