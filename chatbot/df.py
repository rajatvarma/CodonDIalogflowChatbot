import os
import dialogflow_v2 as dialogflow

def detect_intent_texts(project_id, session_id, text, language_code="en"):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    answer = response.query_result.fulfillment_text
    return answer
