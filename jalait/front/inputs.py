class Input:
    """Contains all the labels and options for the front-end"""

    text = {
        "label": "📄 Please enter your text here",
        "placeholder": "I have wrotten a veri bad text in english due to the fact that i am not very good at english.",
    }

    lang_level = {
        "label": "📢 Language Level",
        "options": [
            "slang or casual",
            "normal or usual",
            "sustained or formal",
        ],
    }

    lang_country = {
        "label": "🌏 Country",
        "options": [
            "-",
            "American",
            "British",
            "*beta* - Ireland",
            "*beta* - Australia",
            "*beta* - Canada",
            "*beta* - New Zeeland",
            "*beta* - India",
            "*beta* - South Africa",
        ],
    }

    fix_text = {
        "label": "🔧 Fix Text",
        "value": True,
    }

    grammar = {
        "label": "👩‍🏫 Give grammar, vocal and pronunciation feedback",
        "value": True,
    }

    audio = {
        "label": "🔉 Provide Audio Output",
        "value": False,
    }

    idioms = {
        "label": "📸 Heavy hand on idioms",
        "value": False,
    }
