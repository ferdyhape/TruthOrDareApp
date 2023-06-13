import streamlit as st
import random
import json

# set page config
st.set_page_config(
    page_title="TOD Game App | FERDYHAPE", 
    page_icon=":gear:",
    layout="centered", 
    initial_sidebar_state="auto", menu_items=None
    )

# sidebar for author introduction
st.sidebar.markdown("""

<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
        integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>

<body>
    <div class="profile_picture">
        <img src="https://github.com/ferdyhape.png" alt="Profile_Picture" srcset="">
    </div>
    <p class ="html" style='text-align: center;'>Connect with me!</p>
    <div class="group-icon">
        <a href="https://github.com/ferdyhape" target="_blank"><i class="fa-brands fa-github"></i></a>
        <a href="https://instagram.com/ferdyhape" target="_blank"><i class="fa-brands fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/ferdy-hahan-pradana/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
    </div> 
    <footer>
        <p class="copyright">©2023<br> Copyright By <a href="https://github.com/ferdyhape">FERDYHAPE</a></p>
    </footer>
    <style>
    .profile_picture {
        text-align:center;
    }
    .profile_picture img{
      border-radius: 50%;
      width: 65%;
    }
    .group-icon {
        margin: 10px 20px;
        padding: 0;
        border-radius: 25px;
        background-color: #F6F6F6;
        text-align: center;
        font-size: 25px;
    } 
    .group-icon:hover {
        background-color: #F9F9F9;
        cursor: pointer;
    }
    .fa-github {
        color: #333;
    }
    .fa-instagram {
        color: #833AB4;
    }
    .fa-linkedin {
        color: #0e76a8;
    }
    .author {
        margin: 0px 10px;;
        font-size: 20px;
        font-weight: bold;
    }
    .html {
        margin: 10px 10px;
        padding: 0;
    }
    footer {
        position: static;
        height: 280px;
        width: 100%;
    }
    .copyright{
        position: absolute;
        width: 100%;
        color: #fff;
        line-height: 20px;
        font-size: 1em;
        text-align: center;
        bottom:0;
    }
    .copyright a {
        margin: 0;
        text-decoration: none;
    }
    footer p {
        margin: 0;
    }
    a {
        font-weight: bolder;
        margin: 0 10px;
    }
    </style>
</body>

""", unsafe_allow_html=True)



# set the title of page
def title_template(title):
    st.title(f"""
    {title}
    """)

def read_json_file(path_file):
    try:
        with open(path_file) as file:
            data = file.read()
            data_json = json.loads(data)
            
        return data_json
    except FileNotFoundError:
        print(f"File {path_file} not found.")
    except json.JSONDecodeError:
        print(f"Error!!!")

def main():
    st.title("Truth or Dare App")
    st.write("Click the button below to get a random Truth and Dare question.")
    # Ask random truth or dare questions
    columns = st.columns(8)
    asked_questions = []
    asked_actions = []
    json_data = read_json_file("../data/data.json")
    truth_questions = json_data["truth_questions"]
    dare_actions = json_data["dare_actions"]

    if columns[0].button("Truth"):
        if len(asked_questions) == len(truth_questions):
            st.warning("Congratulations! You have completed all the truth questions.")
        else:
            question = random.choice(list(set(truth_questions) - set(asked_questions)))
            asked_questions.append(question)
            st.success(f"Truth: {question}")

    if columns[1].button("Dare"):
        if len(asked_actions) == len(dare_actions):
            st.warning("Congratulations! You have completed all the dare actions.")
        else:
            action = random.choice(list(set(dare_actions) - set(asked_actions)))
            asked_actions.append(action)
            st.success(f"Dare: {action}")

if __name__ == "__main__":
    main()
