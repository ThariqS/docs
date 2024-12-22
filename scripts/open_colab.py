import base64
import webbrowser

import requests


def open_notebook_in_colab(url):
    # Download the notebook content
    response = requests.get(url)
    notebook_content = response.text

    # Encode the notebook content
    encoded_content = base64.b64encode(notebook_content.encode()).decode()

    # Create a data URL
    colab_url = (
        f"https://colab.research.google.com/notebook#create=true&data={encoded_content}"
    )
    webbrowser.open(colab_url)


if __name__ == "__main__":
    open_notebook_in_colab("https://www.goodfire.ai/notebooks/jailbreak.ipynb")
