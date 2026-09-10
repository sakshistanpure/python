print("------------ Price Engine -----------")

asset_cost = []

n = int(input("Enter Number Of Assets : "))

for i in range(n):
    cost = float(input("Enter Asset Cost : "))
    asset_cost.append(cost)

for i in range(len(asset_cost)):
    for j in range(i+1, len(asset_cost)):

        if asset_cost[i] < asset_cost[j]:
            asset_cost[i], asset_cost[j] = asset_cost[j], asset_cost[i]

print("Top 3 Priciest Assets :")

for i in range(3):
    print(asset_cost[i])

    