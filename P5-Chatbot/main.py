"""
This code implements an elementary chatbot for Volkswagen car inquiries,
including variants, engine options, and transmission options.
"""

from nltk.chat.util import Chat, reflections

# Define variants, engines, and transmissions for each car model
car_variants = {
    'Polo': ['Trendline', 'Comfortline', 'Highline', 'GT Line'],
    'Golf': ['Life', 'Style', 'R-Line', 'GTI', 'R'],
    'Tiguan': ['Trendline', 'Comfortline', 'Highline', 'R-Line', 'Allspace']
}

car_engines = {
    'Polo': ['1.0L MPI (75 HP)', '1.0L TSI (95 HP)', '1.0L TSI (110 HP)', '1.5L TSI (150 HP)'],
    'Golf': ['1.5L TSI (130 HP)', '1.5L eTSI Mild Hybrid (150 HP)', '2.0L TSI (245 HP)', '2.0L TSI (320 HP)'],
    'Tiguan': ['1.5L TSI (150 HP)', '2.0L TSI (190 HP)', '2.0L TSI (245 HP)', '2.0L TDI (150 HP)', '2.0L TDI (200 HP)']
}

car_transmissions = {
    'Polo': ['5-Speed Manual', '6-Speed Manual', '7-Speed DSG Automatic'],
    'Golf': ['6-Speed Manual', '7-Speed DSG Automatic'],
    'Tiguan': ['6-Speed Manual', '7-Speed DSG Automatic', '8-Speed Automatic']
}

# Main car information
cars = {
    'Polo': ['Compact hatchback', 'Starting from INR 9,00,000', 'Features: Touchscreen infotainment, LED headlights'],
    'Golf': ['Versatile hatchback', 'Starting from INR 25,00,000', 'Features: Digital cockpit, adaptive cruise control'],
    'Tiguan': ['Compact SUV', 'Starting from INR 42,00,000', 'Features: Panoramic sunroof, 4MOTION all-wheel drive']
}

patterns = [
    (r'hi|hello|hey',
     ['Hello! How can I assist you with Volkswagen cars today?', 'Hey there! Looking for information on VW cars?',
      'Hi! Ready to learn about our Volkswagen models?']),
    (r'how are you',
     ['I am just a bot, but I am always ready to help you with VW car information!',
      'I am doing well, thanks for asking. How can I assist you with Volkswagen cars today?']),
    (r'(.*) car(.*)',
     ['Here is the list of Volkswagen cars: ' + ', '.join(cars.keys()) + '. Which model interests you?',
      'Sure! Here are the VW models we have information on: ' + ', '.join(cars.keys()) + '.']),
    (r'(.*) (model|models)',
     ['We have information on these Volkswagen models: ' + ', '.join(cars.keys()) + '. Which one would you like to know about?',
      'The VW models I can tell you about are: ' + ', '.join(cars.keys()) + '.']),
    (r'(.*) (specification|specifications|specs)',
     ['Here are the specifications for each Volkswagen model:' + ''.join([f"\n{car}: {', '.join(specs)}" for car, specs in cars.items()])]),
    (r'(.*) (feature|features)',
     ['Here are the features for each Volkswagen model:' + ''.join([f"\n{car}: {specs[2]}" for car, specs in cars.items()])]),
    (r'(.*) (variant|variants)',
     ['Here are the variants for each Volkswagen model:' + ''.join([f"\n{car}: {', '.join(variants)}" for car, variants in car_variants.items()])]),
    (r'(.*) (engine|engines)',
     ['Here are the engine options for each Volkswagen model:' + ''.join([f"\n{car}: {', '.join(engines)}" for car, engines in car_engines.items()])]),
    (r'(.*) (transmission|transmissions)',
     ['Here are the transmission options for each Volkswagen model:' + ''.join([f"\n{car}: {', '.join(transmissions)}" for car, transmissions in car_transmissions.items()])]),
    (r'(.*) polo variant(.*)',
     [f"The Volkswagen Polo is available in these variants: {', '.join(car_variants['Polo'])}."]),
    (r'(.*) golf variant(.*)',
     [f"The Volkswagen Golf is available in these variants: {', '.join(car_variants['Golf'])}."]),
    (r'(.*) tiguan variant(.*)',
     [f"The Volkswagen Tiguan is available in these variants: {', '.join(car_variants['Tiguan'])}."]),
    (r'(.*) polo engine(.*)',
     [f"The Volkswagen Polo offers these engine options: {', '.join(car_engines['Polo'])}."]),
    (r'(.*) golf engine(.*)',
     [f"The Volkswagen Golf offers these engine options: {', '.join(car_engines['Golf'])}."]),
    (r'(.*) tiguan engine(.*)',
     [f"The Volkswagen Tiguan offers these engine options: {', '.join(car_engines['Tiguan'])}."]),
    (r'(.*) polo transmission(.*)',
     [f"The Volkswagen Polo offers these transmission options: {', '.join(car_transmissions['Polo'])}."]),
    (r'(.*) golf transmission(.*)',
     [f"The Volkswagen Golf offers these transmission options: {', '.join(car_transmissions['Golf'])}."]),
    (r'(.*) tiguan transmission(.*)',
     [f"The Volkswagen Tiguan offers these transmission options: {', '.join(car_transmissions['Tiguan'])}."]),
    (r'(.*) (polo|Polo)',
     [f"The Volkswagen Polo: {', '.join(cars['Polo'])}. Would you like to know more about this model's variants, engines, or transmissions?"]),
    (r'(.*) (golf|Golf)',
     [f"The Volkswagen Golf: {', '.join(cars['Golf'])}. Would you like to know more about this model's variants, engines, or transmissions?"]),
    (r'(.*) (tiguan|Tiguan)',
     [f"The Volkswagen Tiguan: {', '.join(cars['Tiguan'])}. Would you like to know more about this model's variants, engines, or transmissions?"]),
    (r'(.*) (price|cost)',
     [f"Prices vary by region, variant, and specific configuration. Would you like to schedule a visit to a dealership for detailed pricing?"]),
    (r'(.*) (test drive|testdrive)',
     ['We can arrange a test drive at your nearest Volkswagen dealership. Would you like me to help you schedule one?']),
    (r'(.*) (book|schedule|appointment)',
     ['I can help you connect with a Volkswagen sales representative. Please provide your contact information.']),
    (r'(.*) (bye|goodbye)',
     ['Thank you for your interest in Volkswagen. Have a great day!', 'Goodbye! We hope to see you at a VW dealership soon!', 'Bye! Drive safely!']),
]

# create a chatbot
vw_bot = Chat(patterns, reflections)


def schedule_appointment(car_model, variant, name, contact):
    return f"Appointment confirmed! A Volkswagen representative will contact you about the {car_model} {variant} soon.\nWe have your details as: {name}, {contact}."


def main():
    import tkinter as tk
    from tkinter import scrolledtext

    root = tk.Tk()
    root.title("VW ChatBot")

    chat_log = scrolledtext.ScrolledText(root, state='disabled', width=60, height=20, wrap='word')
    chat_log.pack(padx=10, pady=10)

    entry_frame = tk.Frame(root)
    entry_frame.pack(fill='x', padx=10, pady=(0,10))
    user_input = tk.Entry(entry_frame, width=50)
    user_input.pack(side='left', fill='x', expand=True)
    send_button = tk.Button(entry_frame, text="Send", width=10, command=lambda: send_message())
    send_button.pack(side='left', padx=(5,0))

    def send_message():
        msg = user_input.get()
        if not msg.strip():
            return
        chat_log.config(state='normal')
        chat_log.insert('end', "You: " + msg + "\n")
        response = vw_bot.respond(msg)
        if response:
            chat_log.insert('end', "VW Bot: " + response + "\n")
        else:
            chat_log.insert('end', "VW Bot: Could not understand context.\n")
        chat_log.see('end')
        chat_log.config(state='disabled')
        user_input.delete(0, 'end')

    chat_log.config(state='normal')
    chat_log.insert('end', "VW Bot: Hello! Welcome to the Volkswagen ChatBot. How can I assist you today?\n")
    chat_log.config(state='disabled')

    root.bind('<Return>', lambda event: send_message())
    root.mainloop()


main()
