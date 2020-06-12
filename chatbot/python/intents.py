import dialogflow_v2 as dialogflow
import guide
import os


def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)
    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])
    response = intents_client.create_intent(parent, intent)


def delete_intent(project_id, intent_id):
    intents_client = dialogflow.IntentsClient()
    intent_path = intents_client.intent_path(project_id, intent_id)
    intents_client.delete_intent(intent_path)

    
def upload_intents(f, project_id):
    intent_questions = guide.questions_reader(f)
    intent_answers = guide.answers_reader(f) 
    count = 0
    for k in range(len(intent_questions)):
        parts = intent_questions[k].split(" ")
        answer = ['%.300s' % intent_answers[k]]
        try:
            intents.create_intent(project_id, intent_questions[k], parts, answer)
            count += 1
        except:
            continue
    return counts