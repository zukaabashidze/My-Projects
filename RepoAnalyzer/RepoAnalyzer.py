import http.client
import json
from datetime import datetime

def შეამოწმე_ცარიელი_ფაილები(owner, repo, branch="main", token=None):
    """ამოწმებს რეპოზიტორიას ცარიელი ფაილებისთვის.

    :param owner: რეპოზიტორიის მფლობელი.
    :param repo: რეპოზიტორიის სახელი.
    :param branch: განშტოება (ნაგულისხმები: 'main').
    :param token: GitHub ტოკენი.
    :return: ცარიელი ფაილების სია.
    """
    api_url = f"/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    connection = http.client.HTTPSConnection("api.github.com")
    headers = {"User-Agent": "Python Empty File Checker"}
    if token:
        headers["Authorization"] = f"token {token}"
    connection.request("GET", api_url, headers=headers)
    response = connection.getresponse()
    if response.status != 200:
        raise Exception(f"მონაცემების მიღება ვერ მოხერხდა: {response.status} - {response.reason}")
    data = json.loads(response.read())

    folders = set()
    empty_files = []

    for item in data.get("tree", []):
        if item["type"] == "blob" and item.get("size", 0) == 0:
            empty_files.append(item["path"])
        elif item["type"] == "tree":
            folders.add(item["path"])

    total_folders_count = len(folders)
    numbered_folders = [folder for folder in folders if folder.split("/")[-1].isdigit()]

    return empty_files, len(numbered_folders), total_folders_count

def მიიღეს_ბოლო_ატვრის_დრო(owner, repo, token=None):
    """იღებს რეპოზიტორიაზე ბოლო ატვრის დროს.

    :param owner: რეპოზიტორიის მფლობელი.
    :param repo: რეპოზიტორიის სახელი.
    :param token: GitHub ტოკენი.
    :return: ბოლო ატვრის დრო სტრინგის სახით.
    """
    api_url = f"/repos/{owner}/{repo}"
    connection = http.client.HTTPSConnection("api.github.com")
    headers = {"User-Agent": "Python Repo Info Checker"}
    if token:
        headers["Authorization"] = f"token {token}"
    connection.request("GET", api_url, headers=headers)
    response = connection.getresponse()
    if response.status != 200:
        raise Exception(f"მონაცემების მიღება ვერ მოხერხდა: {response.status} - {response.reason}")
    data = json.loads(response.read())
    return datetime.fromisoformat(data["pushed_at"].replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M:%S")

def შეამოწმე_წყობა(file_paths):
    """ამოწმებს ფაილების წყობას და აბრუნებს არასტორი წყობის მხონე ფაილების სიას.

    :param file_paths: ფაილების გზების სია.
    :return: არასტორი წყობის ფაილების სია.
    """
    sorted_paths = sorted(file_paths)
    disordered_files = [file for file, sorted_file in zip(file_paths, sorted_paths) if file != sorted_file]
    return disordered_files

# გამოყენების მაგალითი
if __name__ == "__main__":
    owner = "zukaabashidze"
    repo = "GOA-Group-11"
    token = ""  # საუგიროების შემთხვევის შემთავალი GitHub ტოკენი.

    try:
        ცარიელი_ფაილები, დანომრილი_ფოლდერების_რაოდენობა, ჯამური_ფოლდერების_რაოდენობა = შეამოწმე_ცარიელი_ფაილები(owner, repo, token=token)
        ბოლო_ატვირთვის_დრო = მიიღეს_ბოლო_ატვრის_დრო(owner, repo, token=token)

        print(f"{repo} ({owner}) რეპოზიტორიის ინფორმაცია:")
        print(f"ბოლო ატვრის დრო: {ბოლო_ატვირთვის_დრო}")

        if ცარიელი_ფაილები:
            print("\u10eaარიელი \u10e4აილე\u10d1\u10d8:")
            for file in ცარიელი_ფაილები:
                print(f"- {file}")
        else:
            print("\u10ea\u10d0\u10e0\u10d8\u10d4\u10da\u10d8 \u10e4\u10d0\u10d8\u10da\u10d4\u10d1\u10d8 \u10d0\u10e0 \u10d0\u10e0\u10e1\u10d4\u10d1\u10dd\u10d1\u10e1.")

        print(f"\u10d3\u10d0\u10dc\u10dd\u10db\u10e0\u10d8\u10da\u10d8 \u10e4\u10dd\u10da\u10d3\u10d4\u10e0\u10d4\u10d1\u10d8\u10e1 \u10e0\u10d0\u10dd\u10d3\u10d4\u10dc\u10dd\u10d1\u10d0: {დანომრილი_ფოლდერების_რაოდენობა}")
        print(f"ჯამური ფოლდერების რაოდენობა: {ჯამური_ფოლდერების_რაოდენობა}")

    except Exception as e:
        print(f"შეცდომა: {e}")