# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# counties = ["Arapahoe","Denver","Jefferson"]
# for i in range(len(counties)):
#     print(counties[i])

# counties_tuple = ("Arapahoe","Denver","Jefferson")
# for county in counties_tuple:
#       print(county)
#
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county)
#
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for voters in counties_dict.values():
#     print(voters)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(counties_dict[county])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(counties_dict.get(county))

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for key, value in counties_dict.items():
#     print(key, value)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(county, voters)
#
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
#
# for county_dict in voting_data:
#     print(county_dict)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county in range(len(voting_data)):
#       print(voting_data[county]['county'])

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#      print(county_dict['county'])
#

# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

