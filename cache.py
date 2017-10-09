cacheSize = int(input())
cities = list(map(str, input().lower().replace('[', '').replace(']', '').replace(' ', '').split(',')))

LRU_cache = list()
runtime = 0

for city in cities:
    if city in LRU_cache:
        runtime += 1
    else:
        runtime += 5
        if cacheSize is not 0:
            if len(LRU_cache) >= cacheSize:
                LRU_cache.pop(0)
            LRU_cache.append(city)

print(runtime)
