from wiki_counter import Cities, CityIterator

if __name__ == '__main__':
    city_iterator = CityIterator("countries.json")
    print(next(city_iterator))
    print(next(city_iterator))
    print(next(city_iterator))
    print(next(city_iterator))
    print(next(city_iterator))
