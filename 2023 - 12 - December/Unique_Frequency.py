# Value of frequency of each element of array is unique or not 

def  is_frequency_unique(arr):
    frequency_dict = {}
    unique_frequencies = set()
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    for element, frequency in frequency_dict.items():
        #print(f"{element}: {frequency} times")
        if frequency in unique_frequencies:
            return False
        unique_frequencies.add(frequency)

    return True

my_array = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2]
result = is_frequency_unique(my_array)

if result:
    print("All frequencies are unique.")
else:
    print("Frequencies are not unique.")