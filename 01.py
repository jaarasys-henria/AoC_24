# https://adventofcode.com/2024/day/1


# Part 1 - Distance Calculation
INPUT_FILENAME = "inputs.txt"


def read_input_values():
    ids_left = []
    ids_right = []
    with open(INPUT_FILENAME, "r") as f:
        while line := f.readline():
            left, right = line.split()
            ids_left.append(int(left))
            ids_right.append(int(right))

    return ids_left, ids_right


def distance(left, right):
    return max(left, right) - min(left, right)


ids_left, ids_right = read_input_values()
paired_ids = zip(sorted(ids_left), sorted(ids_right))
pairwise_distances = [distance(left, right) for left, right in paired_ids]
total_distance = sum(pairwise_distances)

print(total_distance)  # 2344935


# Part 2 - Similarity Score
similarity_score_summands = [id * ids_right.count(id) for id in ids_left]
similarity_score = sum(similarity_score_summands)

print(similarity_score)  # 27647262
