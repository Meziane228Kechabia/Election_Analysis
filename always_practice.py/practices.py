
counties = ["Arapahoe", "Denver", "Jefferson"]
counties_tuple = ("Arapahoe", "Denver", "Jefferosn")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county" : "Arapahoe", "registred_voters": 422829},{"county": "Denver", "registred_voters": 463353},{"county": "Jeferson", "registred_votrers": 432438}]

for i in range(len(counties)):
    print(counties[i])

voting_data = [{"county" : "Arapahoe", "registered_voters": 422829},{"county": "Denver", "registered_voters": 463353},{"county": "Jeferson", "registered_votrers": 432438}]

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the elction?")) 
print(f" I received {my_votes / total_votes * 100} % of the total votes.")

