import streamlit as st
import pandas as pd
import pickle
with open('Laptop_price_predictor_model.pkl','rb') as file:
    laptop_price_predictor=pickle.load(file)
with open("D:\Machine Learning\ML Projects\Mobile Phone Price estimator\Mobile_price_estimator_model.pkl",'rb') as mobile_model:
    Mobile_price_estimator_model=pickle.load(mobile_model)
with open("D:\Machine Learning\ML Projects\House Price Estimator\House price estimator model.pkl",'rb') as house_model:
    House_price_estimator_model=pickle.load(house_model)
with open("D:\Machine Learning\ML Projects\Car Price Estimator\Car_price_estimator_model.pkl",'rb') as car_model:
    car_price_estimator_model=pickle.load(car_model)
with open('label_encoders.pkl', 'rb') as f:
    loaded_encoders = pickle.load(f)

company_encoder = loaded_encoders['Company Name']
model_encoder = loaded_encoders['Model Name']
color_encoder = loaded_encoders['Color']

class firstPage:
    def __init__(self):
        self.mobile_stock=None
        self.laptop_stock=None
        self.house_stock=None
        self.car_stock=None
    def title(self):
        # Designing title

        st.markdown(
            """
            <style>
            .title {
                color: blue;
                font-size: 50px;
                background-color: yellow;
                text-align:center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<h1 class="title">Multiple Domain price Estimator</h1>', unsafe_allow_html=True)
    def images(self):
        # Designing images
        ##create columns
        
        col1,col2,col3,col4=st.columns(4)
        # Display images in each column
        with col1:
            self.mobile_stock=st.image('images of mobile.png', caption='Mobile Stock')

        with col2:
            self.house_stock=st.image('image of house.jpeg', caption='House Stock')

        with col3:
            self.car_stock=st.image('image of cars.png', caption='Car Stock')
        with col4:
            self.laptop_stock=st.image('laptops image.jpg', caption='Laptop Stock')
    def options(self):
        st.markdown(
            """
            <style>
            .stButton>button {
                background-color: yellow;
                color: blue;
                font-size: 20px;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 16px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        #st.markdown('<h1 class="title">Multiple Domain Price Estimator</h1>', unsafe_allow_html=True)
        st.markdown("Click the product whose price you want to get predicted")

        # Add buttons with custom CSS class
        if st.button('Laptop', key='laptop'):
            st.session_state.page = 'laptop'
        if st.button('Mobile', key='mobile'):
            st.session_state.page = 'mobile'
        if st.button('Car', key='car'):
            st.session_state.page='car'
        if st.button('House', key='house'):
            st.session_state.page='house'
    def Laptop_page(self):
        #st.markdown('<h1 class="title">Laptop Price Estimator</h1>', unsafe_allow_html=True)
        Company=st.text_input("Enter the name of Laptop Company*",key='company')
        if Company==None:
            st.error("Don't leave me empty") 
        product=st.text_input(f"Enter the product of {Company}",key='product')
        type=st.text_input(f"Enter the type of {product}",key='product type')
        inches=st.number_input(f"Enter the scree size of {type} in inches",10,25,key='screen-size')
        screen_resolution=st.text_input(f"Enter the screen resolution of your {product}",key='Screen-resolution')
        cpu_company=st.text_input(f"Enter the Company whose cpu is used in your {product}",key='cpu-company')
        cpu_type=st.text_input(f"Enter the cpu type of {cpu_company} used in your {product}",key='cpu-type')
        cpu_frequency=st.number_input(f"How much is the cpu frequency of your {cpu_type} in Giga Hertz",key="cpu_frequency")
        Ram=st.number_input(f"Enter the size of ram installed in your {product}",key='ram')
        memory=st.text_input(f"Enter the storage of your {product}",key='storage')
        gpu_company=st.text_input(f"Enter the Company whose gpu is used in your {product}",key='gpu-company')
        st.info("If there is not any gpu in your laptop then write N/A")
        gpu_type=st.text_input(f"Enter the gpu type of {gpu_company} used in your {product}",key='gpu-type')
        st.info("If there is not any gpu in your laptop then write N/A")
        operating=st.text_input("Enter the operating system of your laptop",key='Operating System')
        weight=st.number_input("Enter the weight of your laptop in kg",key='weight')
        # Create a DataFrame with the input data
        if st.button("Predict Price"):
            if not Company or not product or not type or not screen_resolution or not cpu_company or not cpu_type or not memory or not gpu_company or not gpu_type or not operating:
                st.error("Please fill in all the required fields.")
                pass
            else:
                input_data = pd.DataFrame({
                'Company': [Company],
                'Product': [product],
                'TypeName': [type],
                'Inches': [inches],
                'ScreenResolution': [screen_resolution],
                'CPU_Company': [cpu_company],
                'CPU_Type': [cpu_type],
                'CPU_Frequency': [cpu_frequency],
                'Ram': [Ram],
                'Memory': [memory],
                'GPU_Company': [gpu_company],
                'GPU_Type': [gpu_type],
                'OpSys': [operating],
                'Weight': [weight]
                })
                prediction = laptop_price_predictor.predict(input_data)
                st.success(f"Price in euro is {prediction[0]:,.2f}")
    def Mobile_page(self):
        st.markdown('<h1 class="title">Mobile Phone Price Estimator</h1>', unsafe_allow_html=True)
        Name=st.text_input("Enter the name of Mobile Phone",key='name')
        rating=st.number_input(f"Enter the rating of {Name} out of 5",key='rating')
        just_sim_number=st.selectbox("Enter the type of sim",['No Sim Supported ','Dual Sim ','Single Sim '],key='just_sim_number')
        if just_sim_number!="No Sim Supported ":
            generations_of_sim=str(st.multiselect("Select The generation supported by mobile phone",("3G ","4G ","5G ")))
            technologies_of_sim=str(st.multiselect("Select the technology supported by your sim",['VoLTE','Vo5G']))
            No_of_Sim=just_sim_number+str(generations_of_sim)+str(technologies_of_sim)
            st.text(No_of_Sim)
        else:
            No_of_Sim=just_sim_number
        Ram=st.text_input("Enter the size of ram(in GB) installed in your mobile",key='ram')
        Battery=st.text_input("Enter the Battery power(in mAh) of your mobile",key='storage')
        display=st.number_input(f"Enter the scree size of your mobile in inches",key='screen-size')
        external_memory_support=st.selectbox("Enter any one option regarding external memory in your mobile",['Memory Card Not Supported','Memory Card Supported','Memory Card Supported(Hybrid)'])
        if external_memory_support!="Memory Card Not Supported":
            memory_size=st.text_input(f"{external_memory_support} upto 'enter storage'").upper()
            external_memory=external_memory_support+memory_size
        else:
            external_memory=external_memory_support
        android_version=st.text_input("Enter the android version of your mobile")
        company=st.text_input("Enter the company of your mobile")
        inbuilt_memory=st.text_input("Enter the inbuilt memory size(in gb) of your mobile")
        fast_charging=st.text_input("Enter the charging speed of mobile in watt")
        
        #Create a DataFrame with the input data
        if st.button("Predict Price"):
            if not company or not fast_charging or not inbuilt_memory or not android_version or not external_memory_support or not display or not Ram or not just_sim_number or not rating or not Name:
                st.error("Please fill in all the required fields.")
            else:
                #input_data = pd.DataFrame(
                #'Company': [Company],
                #'Product': [product],
                #'TypeName': [type],
                #'Inches': [inches],
                #'ScreenResolution': [screen_resolution],
                #'CPU_Company': [cpu_company],
                #'CPU_Type': [cpu_type],
                #'CPU_Frequency': [cpu_frequency],
                #'Ram': [Ram],
                #'Memory': [memory],
                #'GPU_Company': [gpu_company],
                #'GPU_Type': [gpu_type],
                #'OpSys': [operating],
                #'Weight': [weight]
                #)
                prediction = Mobile_price_estimator_model.predict([[Name,rating,No_of_Sim,Ram,Battery,display,external_memory,android_version,company,inbuilt_memory,fast_charging]])
                st.success(f"Price of mobile in pkr is {prediction[0]:,.2f}")
    def House_page(self):
        st.markdown('<h1 class="title">House Price Estimator</h1>', unsafe_allow_html=True)
        n_bedrooms=st.number_input("Enter the number of bedrooms in the house",1,20,key='bedrooms')
        n_bathrooms=st.number_input("Enter the number of bathrooms in the house",1,20,key='bathrooms')
        sqft_lot=st.number_input("Enter the total area size of the house in sqft",min_value=100,max_value=60000,key='sqft_lot')
        sqft_living=st.number_input("Enter the living area size of the house in sqft",min_value=100,max_value=sqft_lot,key='sqft_living')
        n_floors=st.number_input("Enter the number of floors in the house(Considering ground floor as 0 floor)",0,30,key='floors')
        water_front=st.selectbox('Does the house have water view in front?',options=[0,1])
        st.info("O means not waterfront and 1 means have waterfront")
        view=st.select_slider("Select the number of stars for the view that can be seen from the house",[0,1,2,3,4],key="View")
        condition=st.select_slider("Select the number of stars for the condition of the house",[1,2,3,4,5],key="condition")
        sqft_above=st.number_input("Enter the area size of the house that is constructed above in sqft",min_value=0,max_value=sqft_living,key='sqft_above')
        year_built=st.number_input("Enter the year in which it was constructed",1900,2024,key='Year_built')
        year_renovted=st.number_input("Enter the year in which it was renovted(if not renovated then write 0)",max_value=2024,key="year_renovated")
        zip_code=st.number_input("Enter the zip code of the city where the house is located",key='zipcode')
        if st.button("Predict Price"):
            predicted_price=House_price_estimator_model.predict([[n_bedrooms,n_bathrooms,sqft_living,sqft_lot,n_floors,water_front,view,condition,sqft_above,year_built,year_renovted,zip_code]])
            st.success(f"Estimated price:${predicted_price[0]:,.2f}")

    def Car_page(self):
        import pandas as pd
        from sklearn.preprocessing import LabelEncoder
        st.markdown('<h1 class="title">Car Price Estimator</h1>', unsafe_allow_html=True)
        company=st.text_input("Enter the company of the car",key='company')
        model=st.text_input("Enter the model of the car",key='model')
        year=st.number_input("Enter the model year of the car",key='year')
        location=st.selectbox("Enter the location of the car where it is available to purchase",options=['Islamabad','Kashmir','Balochistan','Sindh','KPK','Punjab'],key='location')
        if location=='Islamabad':
            location=1
        elif location=='KPK':
            location=2
        elif location=='Punjab':
            location=4
        elif location=='Sindh':
            location=5
        elif location=='Kashmir':
            location=3
        else:
            location=0
        mileage=st.number_input("Enter the approx number of miles the car can travel on a gallon of fuel",key='mileage')
        engine_type=st.selectbox("Enter the engine type of your car",options=['Petrol','Diesel','Hybrid'],key='engine_type')
        if engine_type=='Petrol':
            engine_type=2
        elif engine_type=='Diesel':
            engine_type=0
        else:
            engine_type=1
        engine_capacity=st.number_input("Enter the engine capacity of car",key='engineCapacity')
        color=st.text_input("Enter the color of your car",key='color')
        assembly=st.selectbox("Select the assembly type of your car",options=['Imported','Local'],key='assembly')
        if assembly=='Imported':
            assembly=1
        else:
            assembly=0
        transmision_type=st.selectbox("Select the transmision type for your car",options=['Automatic','Manual'],key='Transmission')
        if transmision_type=='Automatic':
            transmision_type=0
        else:
            transmision_type=1
        registration_status=st.selectbox("Select the registration status of your car",options=['Registered','UnRegistered'],key='Registration')
        if registration_status=='Registered':
            registration_status=0
        else:
            registration_status=1

        # Encode categorical variables
        
        encoded_company = company_encoder.fit_transform([company])
        encoded_model = model_encoder.transform([model])
        encoded_color = color_encoder.transform([color])
        if st.button("Predict Price"):
            predicted_price=car_price_estimator_model.predict([[encoded_company,encoded_model,year,location,mileage,engine_type,engine_capacity,encoded_color,assembly,transmision_type,registration_status]])
            st.success(f"Estimated price:${predicted_price[0]:,.2f}")   
    
        

if 'page' not in st.session_state:
    st.session_state.page = 'home'
# Create an instance of the class and call the methods
frontend = firstPage()
# Check the session state to determine which page to display
if st.session_state.page == 'laptop':
    frontend.Laptop_page()
if st.session_state.page=='mobile':
    frontend.Mobile_page()
if st.session_state.page=='house':
    frontend.House_page()
if st.session_state.page=='car':
    frontend.Car_page()
else:
    frontend.title()
    frontend.images()
    frontend.options()

'''In this code:

The session state st.session_state.page is used to manage the current page.
When the "Laptop" button is clicked, the session state is updated to 'laptop'.
The appropriate page is displayed based on the session state.'''