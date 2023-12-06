def range_overlap(range1, range2):
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 <= y2 and y1 <= x2

def test(seed, range_start, range_length, start_map):
    new_seeds = []
    if range_overlap(seed, range(range_start, range_start + range_length)):
        if (
            seed[0] >= range_start
            and seed[-1] <= range_start + range_length
        ):
            print("1")
            new_seeds.append(
                range(
                    seed[0] - (range_start - start_map),
                    seed[-1] - (range_start - start_map) + 1,
                )
            )
        elif (
            range_start > seed[0]
            and range_start + range_length >= seed[-1]
        ):
            print("2")
            new_seeds.append(range(seed[0], range_start))
            new_seeds.append(
                range(
                    range_start - (range_start - start_map),
                    seed[-1] - (range_start - start_map) + 1,
                )
            )
        elif (
            range_start > seed[0]
            and range_start + range_length < seed[-1]
        ):
            print("3")
            new_seeds.append(range(seed[0], range_start))
            new_seeds.append(
                range(
                    range_start - (range_start - start_map),
                    (range_start + range_length) - (range_start - start_map),
                )
            )
            new_seeds.append(
                range((range_start + range_length), seed[-1] + 1)
            )
        elif (
            range_start <= seed[0]
            and range_start + range_length >= seed[0]
            and range_start + range_length <= seed[-1]
        ):
            print("4")
            new_seeds.append(
                range(
                    seed[0] - (range_start - start_map),
                    range_start + range_length - (range_start - start_map),
                )
            )
            new_seeds.append(range(range_start + range_length, seed[-1] + 1))

    return new_seeds

assert test(range(80, 90), 85, 10, 1) == [range(80, 85), range(1, 6)]

assert test(range(80, 90), 70, 30, 10) == [range(20, 30)]

assert test(range(80, 90), 70, 15, 10) == [range(20, 25), range(85, 90)]

assert test(range(80, 90), 80, 10, 0) == [range(0, 10)]

assert test(range(80, 90), 81, 2, 0) == [range(80, 81), range(0, 2), range(83, 90)]

assert test(range(0, 10), 9, 10, 100) == [range(0, 9), range(100, 101)]