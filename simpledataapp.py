import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from phone_sales;', ttl=600)
# Initialize database when app starts
init_database()

# App Setup
st.markdown("<h1 style='text-align:center;'>Streamlit Data Entry App with Azure Postgres Database</h1>", unsafe_allow_html=True)
st.markdown('''<center><h2>A sample data entry application created for business purpose.</center></h2>''', unsafe_allow_html=True)
st.markdown('''<center><h3>How to use the app: Make an entry on the left and watch the table and charts change.😊
            </center></h3>''', unsafe_allow_html=True)


# Split the page into two column
col1, col2 = st.columns([2, 8], gap='large')

# Creating Phone Brands and model
brand = {
    'Apple':[
        'iPhone 7', 'iPhone 8', 'iPhone X', 'iPhone 11', 'iPhone 12', 'iPhone 13', 'iPhone 14'
    ],
    'Oppo':[
        'Oppo Reno8', 'Oppo Reno7', 'Oppo Reno5', 'Oppo A96', 'Oppo A77', 'Oppo A57', 'Oppo A16'
    ],
    'Samsung': [
        'Galaxy F14', 'Galaxy S23', 'Galaxy Z Flip', 'Samsung S8', 'Samsung S9', 'Galaxy M14', 'Galaxy A54' 
    ],
    'Xiaomi': [
        'Xiaomi 13', 'Xiaomi 12T', 'Xiaomi 11', 'Xiaomi Mix 4', 'Redmi Note 12S', 'Redmi K60', 'Redmi Note 10'
    ]
}

# Sales Entry 
with col1.expander(label='', expanded=True):
    st.header('Sales Entry')
    phone_brand = st.selectbox('Select Brand', brand.keys())
    phone_model =  st.selectbox('Select Model', brand[phone_brand])
    purchase_date = st.date_input('Enter purchase date')
    sold_date = st.date_input('Enter sold date')
    cost_price = st.number_input('Enter cost price')
    sold_price = st.number_input('Enter sold price')

    # Saving the entry to the database.
    if st.button('Save Details'):
       
        try:
            df2 = conn.query(f"INSERT INTO phone_sales (phone_brand, phone_model, purchase_date, sold_date, sold_price, cost_price)
            VALUES ('{phone_brand}', :'{phone_model}', '{purchase_date}', '{sold_date}', '{sold_price}', '{cost_price}');", ttl=600)
            st.success("Data saved successfully!")
            st.write(df2)
        except Exception as e:
            logger.error(f"Failed to save data: {e}")
            st.error("Failed to save data. Please try again.")
