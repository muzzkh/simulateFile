import json
import re
def parse_log_file(log_file_path):
    file_objects = {}

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            file_path, event = parse_log_line(line)
            if file_path not in file_objects:
                file_objects[file_path] = {'filepath': file_path, 'access': {}}
            
            if event in file_objects[file_path]['access']:
                file_objects[file_path]['access'][event] += 1
            else:
                file_objects[file_path]['access'][event] = 1

    return list(file_objects.values())

def parse_log_line(log_line):
    parts = log_line.strip().split(' -- ')
    
    event = parts[3].split(': ')

    if (len(event) == 1):
        event = parts[2]
        pattern = re.compile(r'^(?P<filepath>.*?/)(?P<event>[^/]+)$')
        match = pattern.match(parts[2])
        file_path = match.group('filepath')
        event = match.group('event')

    else:
        event = event[1]
        file_path = parts[2].split(':')[1]

    return file_path, event

def main():
    log_file_path = './watch.log'  # Update this with the actual path to your log file
    json_objects = parse_log_file(log_file_path)

    # Write the generated JSON objects to a JSON file
    output_file_path = './normal.json'  # Update this with the desired output file path
    with open(output_file_path, 'w') as output_file:
        json.dump(json_objects, output_file, indent=2)


if __name__ == "__main__":
    main()

