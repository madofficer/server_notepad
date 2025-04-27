from datetime import datetime
from time import perf_counter

import requests
from fastapi import status


class NoteClient:
    def __init__(self, url):
        self.url = url
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        print("==== text processor ====")

    def create_note(self):
        try:
            start_time = perf_counter()
            title = input("title: ")
            text = input("text: ")
            end_time = perf_counter()
            api_url = f"http://{self.url}/note/"

            response = requests.post(
                api_url,
                json={
                    "title": title,
                    "text": text,
                    "metrics": {
                        "creation_time": end_time - start_time,
                        "created_at": self.created_at,
                        "char_count": len(text.replace(" ", ""))
                    }
                }
            )
            if response.status_code == status.HTTP_200_OK:
                print("Text saved")
        except KeyboardInterrupt:
            print("\n")
            print("Text canceled")


if __name__ == "__main__":
    client = NoteClient("localhost:8000")
    client.create_note()
