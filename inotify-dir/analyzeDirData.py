import json
import matplotlib.pyplot as plt

def classify_directory_stats(file_path, threshold=1.0):
    with open(file_path, 'r') as json_file:
        directory_stats = json.load(json_file)

    classifications = []

    for directory, stats in directory_stats.items():
        create_count = stats.get("CREATE_FILE", 0)
        modify_count = stats.get("MODIFY_FILE", 0)

        if modify_count == 0:
            # Avoid division by zero, classify as False
            classifications.append((directory, False))
        else:
            ratio = create_count / modify_count
            classifications.append((directory, ratio > threshold))

    return classifications

def flag(classifications):
    for (name, isCovert) in classifications:
        if (isCovert):
            print("POSSIBLE COVERT CHANNEL FOUND: " + name)

def visualize_directory_stats(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    directories = list(data.keys())
    create_file_values = [stats["CREATE_FILE"] for stats in data.values()]
    del_file_values = [stats["DEL_FILE"] for stats in data.values()]
    modify_file_values = [stats["MODIFY_FILE"] for stats in data.values()]

    bar_width = 0.25
    index = range(len(directories))

    plt.bar(index, create_file_values, bar_width, label='CREATE_FILE')
    plt.bar([i + bar_width for i in index], del_file_values, bar_width, label='DEL_FILE')
    plt.bar([i + 2 * bar_width for i in index], modify_file_values, bar_width, label='MODIFY_FILE')

    plt.xlabel('Directories')
    plt.ylabel('Count')
    plt.title('File Access Statistics by Directory')
    plt.xticks([i + bar_width for i in index], directories, rotation=45, ha="right")
    plt.legend()

    plt.tight_layout()
    plt.savefig("./")


    

if __name__ == "__main__":
    # file_path = "./directory_stats_random.json"  
    file_path = "./directory_stats_normal.json"
    print("Analyzing " + file_path)
    # visualize_directory_stats(file_path)
    c = classify_directory_stats(file_path)
    flag(c)