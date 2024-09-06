from flask import Flask, request, jsonify
import os
from crewai import Agent, Task, Crew
from langchain.chat_models import ChatOpenAI
from flask_cors import CORS
from langchain_community.llms import Ollama
ollama_llm = Ollama(model="llama3")

def run_chatbot(prompt):
    os.environ["OPENAI_API_KEY"] = ""
    
     
     

    # gpt35 = ChatOpenAI(
    # temperature=0.7,
    # model_name="gpt-3.5-turbo",
    # )

    PROMPT = prompt

    researcher = Agent(
    role='FT sweets Research Analyst',
    goal='Research data on FT Sweets a sweet confectionist',
    backstory="""FT Description: Since 1920, FT Sweets has been a family-owned Sweets business dedicated to 
    preserving the rich traditions of Bombay Line Sweets called Mithai situated in Karachi, Pakistan. 
    Our Mithai (which are sweets) are made with love and using traditional recipes that have been passed down for generations.
    Brand Motive: At FT Mithai Mart, we take pride in delivering the finest and freshest mithai (sweets) to your doorstep.
    Make sure to remember the details below to answer user queries:
    Ft Sweets Shop timings: Monday to Saturday 9am - 9pm, Sunday: 9 am- 2 pm
    Ft Sweets provides Delivery: which is Only available on weekdays (Monday to Friday) 12pm - 6pm Only available in Defence, Clifton, Saddar and Nanakwara
    Address: Shop no.2, Hakimi Manzil, Wellington street, Surgical Market, Lucky Star, Saddar, Karachi, Pakistan
    If the user asks for a recommendation recommend a product from only these explicitly to the user with small and engaging description of the recommended product.
    Products:
    1 product name: Badam Pak Products desc: Experience the tradition of sweet craftsmanship with 'Badam Pak,' our one of the special halwas made from high-quality almonds, rich khoya (Which is made from milk), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and crunchy almonds mixed with khoya (made from milk) and sugar, this sweet is for you.
    2 product name: Pista Pak Products desc: Experience the tradition of sweet craftsmanship with 'Pista Pak,' our one of the special halwas made from high-quality Pistachios, rich khoya (Which is made from milk), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 2000 per kg taste: If you like rich and crunchy pistachios mixed with khoya (made from milk) and sugar, this sweet is for you.
    3 product name: Kaju Pak Products desc: Experience the tradition of sweet craftsmanship with 'Kaju Pak,' our one of the special halwas made from high-quality cashews, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and crunchy cashews mixed with khoya (made from milk) and sugar, this sweet is for you.
    4 product name: Akhrot Pak Products desc: Experience the tradition of sweet craftsmanship with 'Akhrot Pak,' our one of the special halwas made from high-quality Walnuts, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and crunchy walnut mixed with khoya (made from milk solid) and sugar, this sweet is for you.
    5 product name: Khopra Pak Products desc: Experience the tradition of sweet craftsmanship with 'Khopra Pak,' our one of the special halwas made from high-quality coconut, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of softness, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and soft coconut mixed with khoya (made from milk) and sugar, this sweet is for you. Tastes like bounty chocolate
    6 product name: Pineapple Pak Products desc: Experience the tradition of sweet craftsmanship with 'Pineapple Pak,' our one of the special halwas made from high-quality Pineapple and coconut, rich khoya (Which is made from milk solids), premium sugar, and expertise. This delightful treat offers a harmonious blend of nuttiness and creaminess, offering the same taste it had a 100 years back. category: Halwa (Halwa is a popular sweet dish originating from the Indian subcontinent and is widely enjoyed across various cultures and regions. It is a dense, sweet confectionery made from a variety of ingredients) price: 1600 per kg taste: If you like rich and soft pineapple and coconut mixed with khoya (made from milk) and sugar, this sweet is for you.
    7 product name: Zafrani Paira Products desc: Savor the royal flavors of our special Zafrani Paira, crafted with pure khoya and the exquisite touch of saffron to produce the ultimate taste. category: Classic Sweets (Classic sweets" encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations,) price: 1400 per kg taste: If you like rich and soft khoya with a touch of saffron and sugar, this sweet is for you.
    8 product name: Gulaab Jaman Products desc: Indulge in the sweet nostalgia of our traditional recipe for “Gulaab Jamun”, these golden brown dumplings are made up of pure khoya, fried to perfection and lovingly dipped in fragrant sugar syrup. category: Classic Sweets (Classic sweets" encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations,) price: 1200 per kg taste: If you like rich and soft khoya balls dipped in sugar syrup, this sweet is for you.
    9 product name: Egg Maisoo Products desc: Discover the timeless charm of "Egg Maisoo," our famous traditional mithai made from pure eggs, quality oil, and a touch of sugar. Crunchy, succulent, and perfect for celebrations or sharing with loved ones. Experience a legacy of flavors in every bite. category: Classic Sweets (Classic sweets" encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations,) price: 1500 per kg taste: If you like rich and crunchy texture sweets made with eggs, this sweet is for you.
    10 product name: Malai Khaja Products desc: Experience the essence of tradition in every bite of our premium Malai Khaja that combines crispy layers with a rich, creamy center of Rabri (Made with milk and sugar). This sweet treat is a perfect blend of textures and flavors to fulfill your sweet cravings. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 1400 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
    11 product name: Khoya Puff Products desc: Khoya Puff, also known as Khoya Mawa Puff or Khoya Patties, is a delicious and indulgent Indian sweet treat that features layers of flaky puff pastry filled with a rich and creamy khoya (milk solids) filling. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 1100 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
    12 product name: Verki Samosa Products desc: Khoya samosa, also known as verki samosa, is a unique and crispy variation of the traditional Indian samosa. Unlike the typical triangular-shaped samosa, verki samosa is prepared using thinly rolled layers of dough, similar to filo pastry, which are then filled with a savory mixture and folded into small parcels. category: Malai Khaja (Malai Khaja is a delectable and traditional Indian sweet originating from the eastern state of Odisha. It is known for its flaky layers, rich texture, and delightful taste.) price: 840 per kg taste: if you like deep fried cripsy sweet with creamy filling, this sweet is for you.
    13 product name: Barfi Products desc: Barfi, also known as burfi, is a popular Indian sweet delicacy that is enjoyed across various regions and festivities. It is characterized by its dense, fudge-like texture and its wide range of flavors, including traditional ones like plain, almond, pistachio, and coconut, as well as modern variations like chocolate and fruit-flavored barfis.. category: CLassic Sweets (Classic sweets encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations) price: 1300 per kg
    14 product name: Moti Choor Laddoo desc: Motichoor laddoo is a popular Indian sweet delicacy that is adored for its exquisite taste and texture. It is traditionally made from tiny, deep-fried balls of gram flour (besan) batter, which are then soaked in sugar syrup and shaped into round laddoos (sweet balls). category: CLassic Sweets (Classic sweets encompass a wide array of traditional confections enjoyed across various cultures and regions around the world. These sweets have stood the test of time, often passed down through generations) price: 1000 per kg
    
    Ft sweets offers packaging as well as a mixed mithai option where users can make a mithai box consiisting of multiple
    mithais Mix Mithai: All our products available in the inventory can be added in the mix mithai box, the mithai box can be of 0.5kgs or 1kgs.
        Mithai Boxes: 2 boxes are available for now. 0.5 kg box and 1kg box. Premium Packaging will be availabe for every box as per customers demand
    
    """,
    verbose=True,
    allow_delegation=False,
    # tools=[search_tool],
    # llm=ollama_llm # was defined above in the file
    llm=ollama_llm
    )

    # Define the Langchain agent for brand tone setting, customer service, and product recommendation
    tone_setter = Agent(
        role='Brand Tone Setter',
        goal='Craft compelling and brand-specific content to enhance marketing strategies, provide excellent customer service, and recommend products to customers',
        backstory="""As a versatile customer service representative, and product recommender, you are renowned 
        for your ability to create engaging replies, resolve customer queries effectively, and recommend 
        products tailored to customer needs. Your expertise lies in understanding the brand's tone, 
        addressing customer concerns with empathy, and suggesting suitable products to enhance their experience.""",
        verbose=True,
        allow_delegation=True,
        llm=ollama_llm # Assuming gpt35 is the language model you want to use
    )


    writer = Agent(
        role='Customer Service Representative',
        goal='Craft compelling and brand-specific content to enhance marketing strategies across diverse platforms',
        backstory="""As a versatile Content Strategist and writer, you are renowned for creating insightful and engaging marketing posts 
        tailored for various brands across multiple social media platforms. Your expertise lies in transforming complex concepts into compelling 
        narratives, ensuring maximum impact for each unique brand.""",
        verbose=True,
        allow_delegation=True,
        llm=ollama_llm
    )


    # Conduct a comprehensive analysis of FT sweets, brief description of the brand. Include its mission, values, Products and unique selling 
    #   points. The Brands Target Audience. Identify key competitors in the industry and how the brand differentiates itself from them. Define the key messages or 
    #   phrases associated with the brand. What does the brand want to communicate to its audience.Outline the brand's future goals and aspirations. 
    #   Where does the brand envision itself in the coming years?

    # Create tasks for your agents
    task1 = Task(
    description="""Conduct comprehensive analysis of FT sweets,and convert the details in bullet points so that
    when a user asks queries data can be retrieved faster. Make Data connections and answer the users questions
    precisely.""",
    agent=researcher
    )

    task2 = Task(
        description="""The personality and tone associated with the brand is a friendly, professional, 
        and helpful since you want to converse with the user for our FT sweets users that may need
        help with knowing about our brand and our product details as well as other details of our brand. """,
        agent=tone_setter
    )

    task3 = Task(
    description=f"""Using the insights provided, Answer the user prompt precisely: {PROMPT}, Make sure that your response is less than 200 words 
    and answers Your response should be a answer to the user query in a precide manner with just the 
    response as output donot include and make sure that you answer in a first person perspective.""",
    agent=writer
    )

    # Instantiate your crew with a sequential process
    crew = Crew(
    agents=[researcher,tone_setter,writer],
    tasks=[task1, task2,task3],
    verbose=2, # You can set it to 1 or 2 to different logging levels
    )

    # # Get your crew to work!
    result = crew.kickoff()

    # print("######################")
    # print(result)
    return result

app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['GET'])
def query():
    # data = request.json
    # prompt = data['prompt']
    
    prompt= request.args.get('prompt')
    result = run_chatbot(prompt)
    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)