def get_value_from_dict(d, key):
    try:
        return d[key]
    except KeyError as e:
        print(f"Xato: {e}. Kalit topilmadi!")
        return None


# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(get_value_from_dict(my_dict, 'b'))  # 2
print(get_value_from_dict(my_dict, 'd'))  # Xato: 'd'. Kalit topilmadi! None
