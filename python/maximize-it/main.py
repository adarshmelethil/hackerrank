#!/usr/bin/env python3

from itertools import product


K, M = map(int, input().split())

print(max(map(lambda x: sum(x) % M,
              product(
                  *[[int(x)**2
                     for i, x in enumerate(input().split()) if i > 0]
                    for _ in range(K)]))))
