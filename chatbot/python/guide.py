import csv

def get_guides(path):
    filenames = []
    for file in path:
    if file.endswith(".csv"):
        filenames.append(file)
    return filenames

def questions_reader(f):
    with open(f, newline='') as csvfile:
        reader = csv.reader(csvfile)
        questions = []
        for row in reader:
            try:
                int(row[0])
                questions.append(row[1])
            except:
                continue
    return questions


def answers_reader(f):
    with open(f, newline='') as csvfile:
        reader = csv.reader(csvfile)
        answers = []
        for row in reader:
            if row[0] == "Ans." or row[0] == "Ans":
                answers.append(row[1])
    return answers
