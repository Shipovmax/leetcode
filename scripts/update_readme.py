"""Auto-update README.md with current solution counts."""

import os
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent

# Topic keywords mapped from folder slug
TOPIC_KEYWORDS = {
    "Arrays & Hashing": ["two_sum", "contains_duplicate", "anagram", "group_anagrams",
                         "top_k", "encode", "product_except", "longest_consecutive"],
    "Two Pointers": ["two_pointers", "valid_palindrome", "three_sum", "container_water",
                     "trapping_rain"],
    "Sliding Window": ["sliding_window", "best_time", "longest_substring",
                       "longest_repeating", "permutation_in_string", "minimum_window"],
    "Stack": ["valid_parentheses", "min_stack", "reverse_polish", "generate_parentheses",
              "daily_temperatures", "car_fleet", "largest_rectangle"],
    "Binary Search": ["binary_search", "search_matrix", "koko", "rotated_sorted",
                      "minimum_rotated", "median_sorted"],
    "Linked List": ["linked_list", "reverse_linked", "merge_two", "reorder_list",
                    "remove_nth", "copy_list", "lru_cache", "merge_k"],
    "Trees": ["invert_binary", "max_depth", "diameter", "balanced", "same_tree",
              "subtree", "lowest_common", "level_order", "right_side", "count_nodes",
              "kth_smallest", "validate_bst", "construct_binary", "serialize"],
    "Graphs": ["number_of_islands", "clone_graph", "max_area", "pacific_atlantic",
               "surrounded_regions", "rotting_oranges", "walls_gates", "course_schedule",
               "redundant_connection", "word_ladder"],
    "Dynamic Programming": ["climbing_stairs", "min_cost", "house_robber", "longest_palindrome",
                            "decode_ways", "coin_change", "maximum_product", "word_break",
                            "partition_equal", "unique_paths", "jump_game", "edit_distance",
                            "distinct_subsequences", "interleaving", "longest_increasing"],
    "Backtracking": ["subsets", "combination_sum", "permutations", "word_search",
                     "palindrome_partitioning", "letter_combinations", "n_queens"],
}


def count_solutions() -> tuple[int, int]:
    """Count Python and Go solution files across all problem folders."""
    py_count = 0
    go_count = 0

    for folder in ROOT.iterdir():
        if not folder.is_dir():
            continue
        # Problem folders match pattern: NNNN_slug
        if not re.match(r"^\d{4}_", folder.name):
            continue
        if (folder / "solution.py").exists():
            py_count += 1
        if (folder / "solution.go").exists():
            go_count += 1

    return py_count, go_count


def count_topics() -> dict[str, int]:
    """Count solutions per topic based on folder name keywords."""
    topic_counts: dict[str, int] = defaultdict(int)

    for folder in ROOT.iterdir():
        if not folder.is_dir():
            continue
        if not re.match(r"^\d{4}_", folder.name):
            continue

        slug = folder.name.lower()
        has_solution = (
                (folder / "solution.py").exists()
                or (folder / "solution.go").exists()
        )
        if not has_solution:
            continue

        for topic, keywords in TOPIC_KEYWORDS.items():
            if any(kw in slug for kw in keywords):
                topic_counts[topic] += 1
                break

    return topic_counts


def build_stats_table(py_count: int, go_count: int) -> str:
    total = max(py_count, go_count)
    return (
        "| Language | Solved |\n"
        "|----------|--------|\n"
        f"| Python   | {py_count} |\n"
        f"| Go       | {go_count} |\n"
        f"| **Total**| **{total}** |"
    )


def build_topics_table(topic_counts: dict[str, int]) -> str:
    rows = []
    for topic in TOPIC_KEYWORDS:
        count = topic_counts.get(topic, 0)
        rows.append(f"| {topic} | {count} |")
    return "| Topic | Count |\n|-------|-------|\n" + "\n".join(rows)


def update_readme(py_count: int, go_count: int, topic_counts: dict[str, int]) -> None:
    readme_path = ROOT / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    stats_table = build_stats_table(py_count, go_count)
    topics_table = build_topics_table(topic_counts)

    # Replace Stats section
    content = re.sub(
        r"(## Stats\n\n)[\s\S]+?(\n\n## Topics)",
        rf"\g<1>{stats_table}\g<2>",
        content,
    )

    # Replace Topics section
    content = re.sub(
        r"(## Topics\n\n)[\s\S]+?(\n\n## Author)",
        rf"\g<1>{topics_table}\g<2>",
        content,
    )

    readme_path.write_text(content, encoding="utf-8")
    print(f"README updated — Python: {py_count}, Go: {go_count}")


if __name__ == "__main__":
    py_count, go_count = count_solutions()
    topic_counts = count_topics()
    update_readme(py_count, go_count, topic_counts)