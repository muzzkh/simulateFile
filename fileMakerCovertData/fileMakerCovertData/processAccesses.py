import os
import json

def process_file_accesses(file_accesses):
    directory_stats = {}

    for file_access in file_accesses:
        filepath = file_access["filepath"]
        access_data = file_access["access"]

        directory = os.path.dirname(filepath)

        if directory not in directory_stats:
            directory_stats[directory] = {"CREATE_FILE": 0, "DEL_FILE": 0, "MODIFY_FILE": 0}

        for access_type, count in access_data.items():
            if access_type == "CREATE":
                directory_stats[directory]["CREATE_FILE"] += count
            elif access_type == "DELETE":
                directory_stats[directory]["DEL_FILE"] += count
            elif access_type == "MODIFY":
                directory_stats[directory]["MODIFY_FILE"] += count

    return directory_stats

def main():
    input_file_path = "./watchLogs/output_random.json"  # Update this with the actual path to your JSON file
    with open(input_file_path, 'r') as input_file:
        json_objects = json.load(input_file)

    directory_stats = process_file_accesses(json_objects)

    # Print the resulting directory statistics
    for directory, stats in directory_stats.items():
        print(f'Directory: {directory}, Stats: {stats}')
    # Write directory statistics to a file
    output_file_path = "random_directory_stats.json"
    with open(output_file_path, 'w') as output_file:
        json.dump(directory_stats, output_file, indent=2)


if __name__ == "__main__":
    main()