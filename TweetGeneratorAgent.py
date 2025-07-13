import google.generativeai as genai
import ipywidgets as widgets
from IPython.display import display, Markdown
API_KEY = "AIzaSyBhX6YBDGq4juMaCKNBEYvNXxZvPM-ADz8"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
topic_input = widgets.Text(
    description="Topic",
    layout=widgets.Layout(width="400px")
)
tone_input = widgets.Dropdown(
    description="Tone",
    options=['Professional','Casual','Motivational','Informative'],
    layout=widgets.Layout(width="400px")
)
audience_input = widgets.Text(
    description="Audience",
    layout=widgets.Layout(width="400px")
)
hashtag_input = widgets.Text(
    description="Hashtags",
    layout=widgets.Layout(width="400px")
)
submit_button = widgets.Button(
    description="Generate Tweet",
    button_style="Success",
    tooltip="Click to generate tweet",
    layout=widgets.Layout(width="400px")
)
output=widgets.Output()
def generate_tweet(b):
  output.clear_output()
  prompt= f"""
  You are an expert content writer.
  Generate a tweet about the topic "{topic_input.value}",
  use a "{tone_input.value}" tone,
  generate tweet for "{audience_input.value}" audience,
  and keep it under 280 characters.
  """
  with output:
    try:
      response = model.generate_content(prompt)
      tweet=response.text.strip()
      display(Markdown(f"### Generated Tweet : \n\n {tweet} "))
    except Exception as e:
      print("Error",e)
submit_button.on_click(generate_tweet)
form=widgets.VBox([
    widgets.HTML(value="<h3> Tweet Generator Agent </h3>"),
    topic_input,
    tone_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])
display(form)