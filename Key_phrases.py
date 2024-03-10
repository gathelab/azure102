from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    # Replace these with your Azure Text Analytics subscription key and endpoint
    subscription_key = "699d78bf82cb4546a1c11f13bac3952f"
    endpoint = "https://devailanguage8080.cognitiveservices.azure.com/"
    
    credential = AzureKeyCredential(subscription_key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    return text_analytics_client

def key_phrases():
    client = authenticate_client()

    try:
        documents = [
            {"id": "1", "language": "ja", "text": "猫は幸せ"},
            {"id": "2", "language": "de", "text": "Fahrt nach Stuttgart und dann zum Hotel zu Fu."},
            {"id": "3", "language": "en", "text": "My cat might need to see a veterinarian."},
            {"id": "4", "language": "es", "text": "A mi me encanta el fútbol!"},
            {"id": "5", "language": "ta", "text": "nallathey nadakum yendru nambungal!!!"}
        ]

        for document in documents:
            print("Asking key-phrases on '{}' (id: {})".format(document['text'], document['id']))

        response = client.extract_key_phrases(documents=documents)

        for document in response:
            print("Document Id: ", document.id)
            print("\tKey Phrases:")
            for phrase in document.key_phrases:
                print("\t\t", phrase)

    except Exception as err:
        print("Encountered exception. {}".format(err))

key_phrases()
