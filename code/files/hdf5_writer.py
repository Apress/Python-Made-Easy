import h5py

with h5py.File('people.h5', 'w') as f:
    people = f.create_group('people')
    person1 = people.create_group('person1')
    person1.create_dataset('name', data='Donald Duck')
    person1.create_dataset('age', data=42)
    person1.create_dataset('city', data='Duckburg')
    person2 = people.create_group('person2')
    person2.create_dataset('name', data='Mickey Mouse')
    person2.create_dataset('age', data=40)
    person2.create_dataset('city', data='Disneyland')