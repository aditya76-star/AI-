import spacy


nlp = spacy.load("en_core_web_sm")


health_tips = {
    "fever": [
        "Stay hydrated and rest.", "Take over-the-counter fever reducers.", "Monitor your temperature.", "Wear light clothing.",
        "Take lukewarm baths.", "Avoid caffeine.", "Eat light meals.", "Use a wet cloth on your forehead."
    ],
    "cough": [
        "Drink warm fluids.", "Use a humidifier.", "Avoid smoking.", "Try honey and ginger tea.",
        "Gargle with warm salt water.", "Use throat lozenges.", "Take steam inhalation.", "Avoid cold foods."
    ],
    "headache": [
        "Drink plenty of water.", "Rest in a dark room.", "Use a cold or warm compress.", "Limit caffeine.",
        "Practice deep breathing.", "Take breaks from screens.", "Massage your temples.", "Ensure proper posture."
    ],
    "fatigue": [
        "Ensure enough sleep.", "Eat a balanced diet.", "Exercise regularly.", "Avoid excessive caffeine.",
        "Take short breaks.", "Practice mindfulness.", "Get sunlight exposure.", "Stay hydrated."
    ],
    "stomach pain": [
        "Avoid heavy foods.", "Drink chamomile tea.", "Consult a doctor if pain persists.", "Use a hot compress.",
        "Avoid spicy foods.", "Chew food slowly.", "Try peppermint tea.", "Avoid carbonated drinks."
    ],
    "cold": [
        "Drink plenty of fluids.", "Use saline nasal spray.", "Gargle with salt water.", "Consume vitamin C.",
        "Inhale steam.", "Keep warm.", "Take honey and lemon.", "Wash hands frequently."
    ],
    "sore throat": [
        "Drink warm tea.", "Use lozenges.", "Rest your voice.", "Drink warm broths.",
        "Stay hydrated.", "Avoid dairy.", "Gargle with turmeric water.", "Breathe through your nose."
    ],
    "nausea": [
        "Drink ginger tea.", "Eat small, bland meals.", "Avoid strong odors.", "Stay hydrated.",
        "Rest upright after eating.", "Chew food properly.", "Try acupressure.", "Avoid lying down."
    ],
    "insomnia": [
        "Maintain a sleep schedule.", "Avoid screens before bed.", "Try meditation.", "Limit evening caffeine.",
        "Keep your bedroom dark.", "Follow a bedtime routine.", "Exercise but not before bed.", "Avoid heavy meals before sleep."
    ],
    "anxiety": [
        "Practice deep breathing.", "Engage in physical activity.", "Avoid caffeine.", "Try journaling.",
        "Listen to calming music.", "Spend time in nature.", "Stay connected with friends.", "Practice gratitude."
    ],
    "allergy": [
        "Avoid known allergens.", "Take antihistamines.", "Use an air purifier.", "Wash bedding frequently.",
        "Wear a mask outdoors.", "Keep windows closed during pollen season.", "Rinse nasal passages with saline.", "Consult an allergist if severe."
    ],
    "high blood pressure": [
        "Reduce salt intake.", "Exercise regularly.", "Manage stress levels.", "Maintain a healthy weight.",
        "Avoid excessive alcohol.", "Eat potassium-rich foods.", "Monitor blood pressure regularly.", "Limit caffeine consumption."
    ],
    "low blood pressure": [
        "Stay hydrated.", "Eat small frequent meals.", "Avoid standing up too quickly.", "Increase salt intake moderately.",
        "Wear compression stockings.", "Consume more fluids.", "Avoid alcohol.", "Consult a doctor if persistent."
    ],
    "diarrhea": [
        "Drink oral rehydration solutions.", "Eat bland foods like rice and bananas.", "Avoid dairy and spicy foods.", "Rest adequately.",
        "Wash hands frequently.", "Stay hydrated.", "Avoid caffeine and alcohol.", "Monitor for dehydration symptoms."
    ],
    "constipation": [
        "Increase fiber intake.", "Drink plenty of water.", "Exercise regularly.", "Avoid processed foods.",
        "Try probiotics.", "Use natural laxatives like prunes.", "Don't ignore the urge to go.", "Maintain a consistent bathroom routine."
    ],
    "dehydration": [
        "Drink water frequently.", "Consume electrolyte-rich fluids.", "Avoid excessive caffeine.", "Eat water-rich foods like cucumbers.",
        "Monitor urine color for hydration levels.", "Rest in a cool place.", "Wear loose clothing.", "Limit alcohol intake."
    ],
    "joint pain": [
        "Exercise gently.", "Use hot or cold compresses.", "Maintain a healthy weight.", "Take omega-3 supplements.",
        "Try turmeric for inflammation.", "Stay active but avoid overexertion.", "Stretch regularly.", "Wear comfortable shoes."
    ],
    "back pain": [
        "Maintain good posture.", "Stretch regularly.", "Use proper lifting techniques.", "Apply heat or cold packs.",
        "Sleep on a firm mattress.", "Avoid sitting for long periods.", "Strengthen core muscles.", "Consult a doctor if pain persists."
    ]
}

def get_health_tips(symptoms):
    """Suggests health tips based on input symptoms."""
    doc = nlp(symptoms.lower())
    tips = []
    for token in doc:
        if token.text in health_tips:
            tips.extend(health_tips[token.text])
    
    return tips if tips else ["No specific tips found. Stay healthy!"]

def main():
    print("AI Health Tip Generator. Type 'exit' to quit.")
    while True:
        symptoms = input("Enter your symptoms: ")
        if symptoms.lower() == "exit":
            break
        
        tips = get_health_tips(symptoms)
        print("\nHealth Tips:")
        for tip in set(tips):  
            print(f"- {tip}")
        print("\n")

if __name__ == "__main__":
    main()
