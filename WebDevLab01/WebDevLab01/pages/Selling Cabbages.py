import streamlit as st
import info2
import pandas as pd
import altair as alt
import time
import random
import json

# HEADER FOR PAGE
def header_main():
    st.title("🥬 Purchase Cabbages Here!!! 🥬")
    st.write('---')
    st.write(info2.text)
    st.write(info2.more_text)
    st.write('---')
header_main()

# BADGES
st.header("🥬 Cabbage Qualifications! 🥬")
st.write("My qualifications to sell Cabbage! You can trust me!")
st.image("https://static1.srcdn.com/wordpress/wp-content/uploads/2020/06/Cabbage-merchant-in-Avatar-The-Last-Airbender.png", width=200)
st.badge("Verified Vendor", color="orange")  # NEW
st.badge("No More Cabbage Slugs", color="green")
st.badge("9/10 Satisfied Customers", color="blue")
st.write('---')

# TUNE
st.header("Enjoy a Tune While You Shop!")
st.markdown(
    """
    <iframe width="560" height="315" 
        src="https://www.youtube.com/embed/b7vfDSJjKiI?autoplay=1&mute=1"
        frameborder="0"
        allow="autoplay; encrypted-media"
        allowfullscreen>
    </iframe>
    """,
    unsafe_allow_html=True
)
st.write('---')

# BACKGROUND COLOR PICKING WITH SESSION STATE
color_options = {
    "Light Green": "#CDEBC5",
    "Light Grey": "#F5F5F5",
    "Yellowish-Green": "#E4F78F",
    "White": "#FFFFFF"
}

if "selected_color_name" not in st.session_state:
    st.session_state.selected_color_name = "Light Green"

st.header("Please choose a background color:")
selected_color_name = st.selectbox(" ", list(color_options.keys()), index=list(color_options.keys()).index(st.session_state.selected_color_name))
st.session_state.selected_color_name = selected_color_name
selected_color_hex = color_options[selected_color_name]

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {selected_color_hex};
    }}
    </style>
""", unsafe_allow_html=True)

st.write(f"You Selected a Background Color of: `{selected_color_name}`")
st.write(f"With a Hex Code of: ({selected_color_hex})")
st.write('---')

# PREDICTED CABBAGE INTAKE SLIDER WITH SESSION STATE
if "predicted_intake" not in st.session_state:
    st.session_state.predicted_intake = 0

st.header("🥬 Predicted Cabbage Intake! 🥬")
st.write("How much cabbage do you want to buy?!")
value = st.slider("Select how much cabbage: ", min_value=0, max_value=40, value=st.session_state.predicted_intake)
st.session_state.predicted_intake = value

if value == 0:
    st.warning("Zero? That's none.")
elif value <= 20:
    st.info("Not Quite Enough Cabbages!")
elif 20 < value < 40:
    st.info("Almost there!!")
elif value == 40:
    st.success("🥬 YES!!! MAX CABBAGES!!! 🥬")
st.write(f" 🥬 You selected {value} heads of cabbage! 🥬")
st.write('---')

# RANK YOUR FAVORITE CABBAGES (already uses session state)
st.header("🥬 Rank Your Favorite Cabbages 🥬")
st.write("Rank the cabbages with how much you like them! Your favorite cabbage should be ranked 1!")

cabbages = ["Savoy Cabbage", "Napa Cabbage", "Red Cabbage", "Green Cabbage"]
for cabbage in cabbages:
    key = f"rank_{cabbage}"
    if key not in st.session_state:
        st.session_state[key] = 1

scores = {}
for cabbage in cabbages:
    key = f"rank_{cabbage}"
    scores[cabbage] = st.slider(f"Rank for {cabbage}", 1, 4, st.session_state[key], key=key)

df = pd.DataFrame({"Cabbage": list(scores.keys()), "Ranking": list(scores.values())})
df = df.sort_values("Ranking", ascending=True)

st.subheader("Your Cabbage Rankings")
st.dataframe(df)

chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Cabbage', sort='-y'),
    y='Ranking',
    color='Cabbage',
    tooltip=['Cabbage', 'Ranking']
).properties(width=400, height=200)
st.altair_chart(chart)
st.write("---")

# CABBAGE BREAK
st.header("🥬 A Cabbage Break! 🥬")
st.image("https://static.vecteezy.com/system/resources/previews/006/562/329/non_2x/cabbage-illustration-in-cartoon-style-vector.jpg", width=100)
st.write("Please enjoy this lovely picture of a beautiful cabbage!")
st.write('---')

# CHART FOR PRICES
categories = ["Savoy Cabbage", "Napa Cabbage", "Red Cabbage", "Green Cabbage"]
values = [5, 3, 5, 2]
numbers = pd.DataFrame({"Prices": values}, index=categories)
st.header("🥬 Cabbage Prices by Type 🥬")
st.write("Please refer to the chart below to see the price of each type of cabbage.")
st.bar_chart(numbers)
st.write("---")

# CABBAGE SPINNER WITH SESSION STATE
outcomes = ["a free cabbage!", "nothing.", "2% off a cabbage!", "0 free cabbages.", "5% off your whole order!"]

if "spin_result" not in st.session_state:
    st.session_state.spin_result = None

st.header("🥬 Cabbage Spinner! 🥬")
st.write("Spin for a chance to win free cabbage!")

if st.button("Spin the Wheel!"):
    with st.spinner("The Wheel is Spinning!! Cabbage is coming your way!!!"):
        time.sleep(5)
        st.session_state.spin_result = random.choice(outcomes)

if st.session_state.spin_result:
    st.success(f" 🥬 You received **{st.session_state.spin_result}** 🥬")
st.write('---')

# INPUT FOR TYPE OF CABBAGE WANTED (already uses session state keys as number_input keys)
st.header("🥬 Cabbage Wanted 🥬")
st.write("Please enter the quantity of each type of cabbage you want.")

items = {
    "Savoy Cabbage": 5,
    "Napa Cabbage": 3,
    "Red Cabbage": 5,
    "Green Cabbage": 2
}
selected_items = []
total = 0.0

st.subheader("Select the Quantity of Cabbage:")
for item, price in items.items():
    if item not in st.session_state:
        st.session_state[item] = 0
    qty = st.number_input(
        f"{item} (${price:.2f} each)", 
        min_value=0, max_value=10, step=1, value=st.session_state[item], key=item
    )
    # <-- Remove this assignment: st.session_state[item] = qty

    if qty > 0:
        total_price = qty * price
        selected_items.append((item, total_price))
        total += total_price

if selected_items:
    filtered_data = pd.DataFrame(selected_items, columns=["Cabbage", "Total Price"])
    st.bar_chart(filtered_data.set_index("Cabbage"))
    st.success(f"Total Amount Due: ${total:.2f}")
else:
    st.warning("Please enter a quantity of cabbages.")

st.write("The **y-axis** shows the total cost, and the **x-axis** shows the selected cabbage types.")


# SAVE DATA ON ENTER BUTTON CLICK
if st.button("ENTER"):
    detailed_items = []
    for item, price in items.items():
        qty = st.session_state.get(item, 0)
        if qty > 0:
            detailed_items.append({
                "Cabbage": item,
                "Quantity": qty,
                "Unit Price": price,
                "Total Price": qty * price
            })

    cabbage_rankings = {cabbage: st.session_state.get(f"rank_{cabbage}", 1) for cabbage in cabbages}
    prices = {cat: val for cat, val in zip(categories, values)}

    cabbage_data = {
        "background_color": {
            "name": st.session_state.selected_color_name,
            "hex": color_options[st.session_state.selected_color_name]
        },
        "predicted_cabbage_intake": st.session_state.predicted_intake,
        "cabbage_rankings": cabbage_rankings,
        "cabbage_prices": prices,
        "selected_cabbage_orders": detailed_items,
        "total_amount_due": total,
        "spin_result": st.session_state.spin_result
    }

    with open("cabbage_data.json", "w") as f:
        json.dump(cabbage_data, f, indent=4)

    st.success("All your cabbage data has been saved!")
st.write("Once you hit the enter button, your data will be saved and sent! Please wait 24 hours to come to the stand to collect and pay for your products!")
