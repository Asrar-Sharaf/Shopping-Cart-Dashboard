
import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('Shopping Cart Data.csv')
    
# Descriptive Analysis
def describtive_Analysis(df):
    st.title("Descriptive Analysis")

    num = df.describe()
    cat = df.describe(include='O')

    col1, col2, col3 = st.columns([5, 0.5 , 5])
    with col1:
        st.subheader('Numerical Descriptive Statistics')
        st.dataframe(num.T,height=800, width=10000)
    with col3:
        st.subheader('Categorical Descriptive Statistics')
        st.dataframe(cat, height=180, width=10000)
    
# Univariate Analysis
def univariate_analysis(df):
    st.title("Univariate Analysis")

    gender = st.sidebar.selectbox('Select gender', ["All"] + df['gender'].unique().tolist())
    product_type = st.sidebar.selectbox('Select Product Type', ["All"] + df['product_type'].unique().tolist())
    state = st.sidebar.selectbox('Select State', ["All"] + df['state'].unique().tolist())
    show_data = st.sidebar.checkbox('Show Data', False)

    if show_data:
        st.header('Dataset Sample')
        st.dataframe(df.head(8))

    if gender != "All":
        df = df[df['gender'] == gender]
    if product_type != "All":
        df = df[df['product_type'] == product_type]
    if state != "All":
        df = df[df['state'] == state]

    # Gender Frequency
    gender_fig = px.bar(df, x='gender', title='Gender Frequency', color_discrete_sequence=['#2E8B57'])
    st.plotly_chart(gender_fig)

    # Proportion of Product Types
    product_type_fig = px.pie(df, names='product_type', title='Proportion of Product Types', color_discrete_sequence=['orange', '#2E8B57'])
    st.plotly_chart(product_type_fig)

    # Distribution of Customer Ages
    age_dist_fig = px.histogram(df, x='age', nbins=130, title='Distribution of Customer Ages', color_discrete_sequence=['#2E8B57'], marginal='box')
    st.plotly_chart(age_dist_fig)

    # Price Distribution
    price_fig = px.histogram(df, x="total_price", title="Price Distribution", color_discrete_sequence=['#2E8B57'], nbins=30, marginal='violin')
    st.plotly_chart(price_fig)

    # State-Wise Distribution
    state_dist_fig = px.histogram(df, x='state', nbins=300, title='State-Wise Distribution', color_discrete_sequence=['#2E8B57'], marginal='rug')
    st.plotly_chart(state_dist_fig)

# Bivariate Analysis
def bivariate_analysis(df):
    st.title("Bivariate Analysis")

    state = st.sidebar.selectbox('Select State for Bivariate', ["All"] + df['state'].unique().tolist())
    city = st.sidebar.selectbox('Select City for Bivariate', ["All"] + df['city'].unique().tolist())
    product_type = st.sidebar.selectbox('Select Product Type for Bivariate', ["All"] + df['product_type'].unique().tolist())
    day_name = st.sidebar.selectbox('Select Day for Bivariate', ["All"] + df['order_Day_Name'].unique().tolist())
    quarter = st.sidebar.selectbox('Select Quarter for Bivariate', ["All"] + df['quarter'].unique().tolist())
    gender = st.sidebar.selectbox('Select gender', ["All"] + df['gender'].unique().tolist())
    show_data = st.sidebar.checkbox('Show Data', False)

    if show_data:
        st.header('Dataset Sample')
        st.dataframe(df.head(8))
        
    if state != "All":
        df = df[df['state'] == state]
    if city != "All":
        df = df[df['city'] == city]
    if product_type != "All":
        df = df[df['product_type'] == product_type]
    if day_name != "All":
        df = df[df['order_Day_Name'] == day_name]
    if quarter != "All":
        df = df[df['quarter'] == quarter]
    if gender != "All":
        df = df[df['gender'] == gender]

    # Total Price for Each State
    state_price_fig = px.histogram(df, x="state", y="total_price", title="Total Price for Each State", color_discrete_sequence=["#2E8B57"], marginal='box')
    st.plotly_chart(state_price_fig)

    # Total Price Distribution Across Cities
    city_price_fig = px.bar(df, x='city', y='total_price', title='Total Price Distribution Across Cities', color_discrete_sequence=['#2E8B57'])
    st.plotly_chart(city_price_fig)

    # Quantity Ordered by Product Type
    quantity_product_fig = px.pie(df, names="product_type", values="quantity_x", title="Quantity Ordered by Product Type", color_discrete_sequence=['orange', '#2E8B57'])
    st.plotly_chart(quantity_product_fig)

    # Total Price for Each Gender
    gender_price_fig = px.histogram(df, x="gender", y="total_price", title="Total Price for Each Gender", color_discrete_sequence=["#2E8B57"], marginal='box')
    st.plotly_chart(gender_price_fig)

    # Number of Orders per Day
    order_counts_by_day = df.groupby('order_Day_Name')['order_id'].count().reset_index()
    order_counts_fig = px.bar(order_counts_by_day, x='order_Day_Name', y='order_id', title='Number of Orders per Day', color='order_Day_Name', color_discrete_sequence=px.colors.sequential.Greens)
    st.plotly_chart(order_counts_fig)

    # Number of Orders per Quarter
    order_counts_by_quarter = df.groupby('quarter')['order_id'].count().reset_index()
    order_counts_quarter_fig = px.scatter(order_counts_by_quarter, x='quarter', y='order_id', title='Number of Orders per Quarter', color='quarter', color_discrete_sequence=px.colors.sequential.Greens, marginal_y='rug')
    st.plotly_chart(order_counts_quarter_fig)

st.sidebar.title("Shopping Cart Dashboard")
page = st.sidebar.radio("Choose an Analysis",("Describtive Analysis", "Univariate Analysis", "Bivariate Analysis"))

# Display the selected analysis
if page == "Describtive Analysis":
    describtive_Analysis(df)
elif page == "Univariate Analysis":
    univariate_analysis(df)
elif page == "Bivariate Analysis":
    bivariate_analysis(df)
