"""Write a program to create the power set of a given set."""

# Q19. Create the power set of a given set
# The power set contains every possible subset, including the empty set.

elements = set(input("Enter distinct elements separated by spaces: ").split())
power_set = [set()]

for element in elements:
    new_subsets = []
    for subset in power_set:
        new_subsets.append(subset | {element})
    power_set.extend(new_subsets)

print("Power set:")
for subset in power_set:
    print(subset)
print("Total number of subsets:", len(power_set))
