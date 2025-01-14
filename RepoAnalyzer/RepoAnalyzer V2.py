import http.client
import json

def გადამოწმება_ცარიელი_ფაილები_რეპოში(owner, repo, ფილიალი="main", token=None):
    """
    გადაამოწმებს, შეიცავს თუ არა GitHub რეპოზიტარი ცარიელ ფაილებს.

    :param owner: რეპოზიტარის მფლობელი (username ან ორგანიზაცია).
    :param repo: რეპოზიტარის სახელი.
    :param ფილიალი: ფილიალი, რომელსაც გადაამოწმებს (default: 'main').
    :param token: გOptional GitHub personal access token for authentication.
    :return: ცარიელი ფაილების გზების სია.
    """
    # API endpoint-ის განსაზღვრა
    #                  gitname, gitrepo               gitmain
    api_url = f"/repos/{owner}/{repo}/git/trees/{ფილიალი}?recursive=1"

    # კონექციის აწყობა
    connection = http.client.HTTPSConnection("api.github.com")
    
    # 헤დერების დაყენება, საჭირო Token-ით ან თუნდაც გარეშე ავტორიზაციისთვის
    headers = {
        "User-Agent": "Python ცარიელი ფაილების შემოწმება"
    }
    if token:
        headers["Authorization"] = f"token {token}"
    
    # მოთხოვნის განხორციელება
    connection.request("GET", api_url, headers=headers)
    response = connection.getresponse()
    
    if response.status != 200:
        raise Exception(f"Failed to fetch repository data: {response.status} - {response.reason}")
    
    # JSON-ის პარსინგი
    data = json.loads(response.read())
    
    # ცარიელი ფაილების შემოწმება
    ცარიელი_ფაილები = []
    if "tree" in data:
        for item in data["tree"]:
            if item["type"] == "blob" and item.get("size", 0) == 0:  # ცარიელი ფაილების შემოწმება
                ცარიელი_ფაილები.append(item["path"])
    
    return ცარიელი_ფაილები

# გამოყენების მაგალითი:
if __name__ == "__main__":
    owner = "Gochagoa1771"  # შეცვალეთ რეპოზიტარის მფლობელი
    repo = "GOA---homework"   # შეცვალეთ რეპოზიტარის სახელი
    token = ""  # შეცვალეთ თქვენი GitHub token ან None საჯარო რეპოზიტარებისთვის

    try:
        ცარიელი_ფაილები = გადამოწმება_ცარიელი_ფაილები_რეპოში(owner, repo, token=token)
        if ცარიელი_ფაილები:
            print("ცარიელი ფაილები მოიძებნა:")
            for file_path in ცარიელი_ფაილები:
                print(f"- {file_path}")
        else:
            print("ცარიელი ფაილები არ მოიძებნა.")
    except Exception as e:
        print(f"შეცდომა: {e}")
