import plotly.express as px

df = px.data.gapminder()

# --- Chart 1: Basic scatter ---
fig = px.scatter(
    df[df["year"] == 2007],
    x="gdpPercap",
    y="lifeExp",
    title="GDP vs. Life Expectancy (2007)"
)
fig.write_html("scatter_basic.html")
print("✓ scatter_basic.html")

# --- Chart 2: Layered bubble chart ---
fig = px.scatter(
    df[df["year"] == 2007],
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name="country",
    log_x=True,
    title="GDP vs. Life Expectancy (2007)",
    labels={
        "gdpPercap": "GDP per Capita (USD)",
        "lifeExp": "Life Expectancy (years)"
    }
)
fig.write_html("scatter_layered.html")
print("✓ scatter_layered.html")

# --- Chart 3: Animated scatter ---
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name="country",
    animation_frame="year",
    animation_group="country",
    log_x=True,
    range_x=[200, 100000],
    range_y=[25, 90],
    title="GDP vs. Life Expectancy Over Time"
)
fig.write_html("scatter_animated.html")
print("✓ scatter_animated.html")

# --- Chart 4: Line chart ---
countries = ["United States", "China", "India", "Brazil", "Nigeria"]
fig = px.line(
    df[df["country"].isin(countries)],
    x="year",
    y="lifeExp",
    color="country",
    markers=True,
    title="Life Expectancy Over Time (Selected Countries)",
    labels={"lifeExp": "Life Expectancy (years)", "year": "Year"}
)
fig.write_html("line_chart.html")
print("✓ line_chart.html")
