class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies


def vanity_sort(influencers):
    return sorted(influencers, key=vanity)

'''
Almost every action you take in a web app relies on sorted data. Just looking up a user's profile in a database likely relies on a sorted index (which we'll talk about in another course).

Fortunately, most programming languages provide their own standard sorting implementation. In Python, for example, we can use the sorted function:

items = [1, 5, 3]
print(sorted(items)) # [1, 3, 5]

Assignment
We need to sort influencers by vanity. Complete the vanity and vanity_sort functions.

The vanity function accepts an instance of an Influencer and returns their vanity score. The vanity score should be the number of links in their bio multiplied by 5, plus their number of selfies. (Links in bio are weighted more heavily)

The vanity_sort function should return a list of influencers, ordered by their vanity from least to greatest. You can pass a function as a named parameter called key to sorted to control the metric the sorting algorithm will use for comparisons.
'''