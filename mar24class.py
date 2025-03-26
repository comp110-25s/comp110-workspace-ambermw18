pids: set[int] = {710000000, 712345678}
pids.add(730120710)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No other orders of mint")

ice_cream.pop("strawberry")
