cities = {
    'Chongqing': ['China', '32.05 million', "It is the largest city in the "
                  "world by population."],
    'Dhaka': ['Bangladesh', '21.28 million', "It’s at the center of national "
              "government, trade and culture."],
    'Kinshasa': ['Democratic Republic of the Congo', '17.07 million',
                 "It was formerly named Léopoldville."]
    }

for city, information in cities.items():
    print(f"\nThe city of {city} is located within {information[0]} "
          f"and has a population of approximately {information[1]}. "
          f"Fun fact: {information[2]}")